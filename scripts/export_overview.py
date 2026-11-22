"""Export a real matched FlowBatt example for the local project-page schematic.

Run from any directory with the repository's existing ML Python environment:
    PYTHONDONTWRITEBYTECODE=1 python webpage/scripts/export_overview.py

This is inference only. It neither trains nor modifies the source dataset/checkpoint.
The exported animation contains actual dopri5 solution outputs at requested times;
the website must not describe these output frames as adaptive solver steps.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.dont_write_bytecode = True
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "webpage/.cache/matplotlib"))

import numpy as np
from PIL import Image
import torch
from matplotlib import colormaps
from prepare_paper_schematic import save_paper_capacity
from select_overview_example import CACHE, MINIMUM_EOL_EXCLUSIVE, cached_shortlist, forecast_metrics

sys.path.insert(0, str(ROOT / "github"))

from flow_matching.solver import ODESolver
from flowbatt.data import get_dataset
from flowbatt.inference import load_flowbatt
from flowbatt.sampling import CachedConditionFlowModel, encode_condition


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numbers(array: np.ndarray, decimals: int = 6) -> list:
    """Round only the compact JSON presentation copy, never the model input."""
    return np.round(np.asarray(array, dtype=np.float64), decimals).tolist()


@torch.inference_mode()
def main() -> None:
    torch.set_num_threads(2)
    source = ROOT / "github/datasets/MATR-1.npz"
    checkpoint = ROOT / "github/checkpoints/flowbatt/MATR-1.pth"
    dataset = get_dataset("MATR-1")
    candidates, cache_settings = cached_shortlist()
    test_index = candidates[0]["testIndex"]
    draw_count, seed, frame_count = 10, 2026, 101
    reference = dataset.label_transformation.inverse_transform(
        dataset.test_data.label[test_index:test_index + 1]
    )
    capacity = dataset.test_data.feature[test_index].numpy().copy()
    model, initializer, _, config = load_flowbatt(
        (1, 100, 100), mask_size=10, device="cpu", battery_dataset="MATR-1"
    )
    condition = dataset.test_data.feature[test_index:test_index + 1]
    encoded = encode_condition(model, condition)
    model_wrapper = CachedConditionFlowModel(model)
    condition_batch = encoded.repeat(draw_count, 1)
    # Set the draw seed after constructing/loading the model, independently of
    # any random numbers consumed during architecture initialization.
    torch.manual_seed(seed)
    initial = torch.randn((draw_count, config.sequence_length), dtype=torch.float32)
    observed = dataset.test_data.label[test_index:test_index + 1, :10]
    initial = initializer(initial, observed.repeat(draw_count, 1), condition_batch)
    times = torch.linspace(0, 1, frame_count, dtype=torch.float32)
    solution = ODESolver(velocity_model=model_wrapper).sample(
        x_init=initial, step_size=None, method="dopri5", atol=1e-5, rtol=1e-5,
        time_grid=times, return_intermediates=True, model_extras=condition_batch,
    )
    physical = dataset.label_transformation.inverse_transform(solution) * 100
    samples = physical[-1].numpy()
    reference_percent = reference.numpy()[0] * 100
    fresh_metrics = forecast_metrics(reference_percent, samples)
    # This is a deliberately good illustration requested for Figure 1. The cell
    # is ranked by all ten cached draws; the displayed fresh draw is selected by
    # forecast RMSE, and both stages are disclosed in the downloadable metadata.
    eligible_draws = [
        index for index, crossing in enumerate(fresh_metrics["perDrawEolCycles"])
        if crossing is not None and crossing > MINIMUM_EOL_EXCLUSIVE
    ]
    if not eligible_draws:
        raise ValueError("No fresh draw meets the requested >1000-cycle 80% crossing criterion.")
    sample_index = min(eligible_draws, key=lambda index: fresh_metrics["perDrawRmse"][index])
    states = physical[:, sample_index].numpy()
    cycles = np.arange(config.sequence_length) * 10 + 1
    reference_crossing = int(np.flatnonzero(reference_percent <= 80)[0])
    sample_lengths = [
        int(np.flatnonzero(row <= 80)[0]) + 1 if np.any(row <= 80) else len(row)
        for row in samples
    ]

    assert solution.shape == (frame_count, draw_count, 256)
    assert np.isfinite(physical.numpy()).all()
    assert np.array_equal(states[-1], samples[sample_index])
    # The learned vector field is zero over the known 10-point prefix.
    expected_prefix = observed.repeat(draw_count, 1).unsqueeze(0)
    prefix_error = float((solution[:, :, :10] - expected_prefix).abs().max())
    # Dense-output interpolation can introduce float32 roundoff even with an
    # exactly zero vector field; keep those solver outputs unmodified.
    assert prefix_error < 5e-6, prefix_error
    with np.load(source, allow_pickle=False) as archive:
        assert np.array_equal(capacity, archive["x_test"][test_index])
        assert np.array_equal(reference.numpy()[0], archive["y_test_physical"][test_index])
    with np.load(ROOT / "results/generative_uq/matr_1_Q/flowbatt_10_samples.npz", allow_pickle=False) as cached:
        assert np.array_equal(reference.numpy()[0], cached["reference"][test_index])

    # Original columns run from high voltage to low voltage. PNG image rows
    # therefore use capacity.T directly: highest voltage at the top. Numeric
    # JSON rows use low-to-high voltage for an ordinary upward-increasing axis.
    minimum, maximum = float(capacity.min()), float(capacity.max())
    lookup = colormaps["cividis"](np.linspace(0, 1, 256), bytes=True)[:, :3]
    indices = np.clip(np.round((capacity.T - minimum) / (maximum - minimum) * 255), 0, 255).astype(np.uint8)
    image_path = ROOT / "webpage/public/data/capacity-matr1-example.png"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(lookup[indices]).save(image_path, optimize=True)
    paper_image = save_paper_capacity(capacity, minimum, maximum)
    colors = ["#" + "".join(f"{int(channel):02x}" for channel in rgb) for rgb in lookup]

    result = {
        "metadata": {
            "dataset": "MATR-1", "testIndex": test_index, "displayName": f"MATR-1 · test cell {test_index + 1}",
            "cellId": None, "earlyCycles": 100, "sequenceLength": 256,
            "selection": "Post-hoc good-prediction illustration: among alternative test rows whose reference first crosses 80% SOH after cycle 1000, choose the lowest mean per-draw forecast RMSE in the existing ten-draw cache. Display the lowest-RMSE fresh draw whose own 80% crossing is also after cycle 1000. This is not an unbiased or aggregate performance estimate.",
            "identityNote": "The numeric archive has no serialized cell IDs. The display cell number is the one-based test-array row, not a source battery identifier.",
            "selectionMetrics": {
                "metricDefinition": "SOH RMSE in percentage points, excluding the ten known prefix coordinates and including the first reference 80% crossing. No clipping or smoothing; ranking uses the mean of all ten individual draw RMSEs, not the best cached draw.",
                "excludedTestIndices": [0], "candidateCount": len(candidates),
                "eligibility": {
                    "minimumReferenceEolCycleExclusive": MINIMUM_EOL_EXCLUSIVE,
                    "minimumSelectedPredictionEolCycleExclusive": MINIMUM_EOL_EXCLUSIVE,
                    "eligibleFreshDrawIndices": eligible_draws,
                    "rule": "Both the reference and displayed prediction must first reach 80% SOH after cycle 1000; the previous test row 0 is excluded.",
                },
                "sourcePredictionCache": str(CACHE.relative_to(ROOT)),
                "sourcePredictionCacheSha256": sha256(CACHE),
                "cacheSettings": cache_settings, "cachedTopFive": candidates[:5],
                "freshInference": fresh_metrics,
                "selectedDrawIndex": sample_index,
                "selectedDrawRmse": fresh_metrics["perDrawRmse"][sample_index],
                "selectedDrawEolCycle": fresh_metrics["perDrawEolCycles"][sample_index],
                "freshInferenceNote": "Ten fresh CPU draws use a seed reset after model loading. Their noise draws need not match the cached multi-cell batch, so fresh metrics are reported separately.",
            },
            "sourceDataset": str(source.relative_to(ROOT)), "sourceDatasetSha256": sha256(source),
            "sourceCheckpoint": str(checkpoint.relative_to(ROOT)), "sourceCheckpointSha256": sha256(checkpoint),
            "referenceType": "Preprocessed, causally smoothed reference SOH; not raw cycle measurements.",
            "referenceRawMeasuredLength": None,
            "recommendedInferenceView": {
                "cycleLimits": [0, int(np.ceil(max(int(cycles[reference_crossing]), fresh_metrics["perDrawEolCycles"][sample_index]) / 200) * 200)],
                "sohLimits": [80, 110],
                "note": "Display window only. Exported states and predictions retain all 256 coordinates through cycle 2551; out-of-window noise is not clipped in the data.",
            },
            "exportScript": "webpage/scripts/export_overview.py",
            "exportScriptSha256": sha256(Path(__file__)),
            "selectionScript": "webpage/scripts/select_overview_example.py",
            "selectionScriptSha256": sha256(Path(__file__).with_name("select_overview_example.py")),
        },
        "capacity": {
            "cycles": list(range(1, 101)), "voltageIndices": list(range(1, 101)),
            "values": numbers(capacity[:, ::-1].T, 9), "unit": "Ah",
            "minimum": minimum, "maximum": maximum,
            "axisLabel": "Voltage-grid index", "orientation": "Rows low-to-high voltage; columns early battery cycles. PNG top is highest voltage.",
            "colormap": "cividis", "colormapStops": [
                {"offset": i / 255, "color": color} for i, color in enumerate(colors)
            ],
            "image": "data/capacity-matr1-example.png",
            "paperColormap": "cool", "paperImage": paper_image,
            "paperColormapSource": "Original Figure 1 capacity contours in manuscript/figs/drawing_artwork.svg use the Matplotlib cool palette.",
            "definition": "Discharge capacity at each cycle minus the cycle-10 capacity curve, in Ah.",
            "preprocessing": "Exact prepared 100×100 matrix. The original pipeline sets cycle 11 to zero, retains zero baseline cycle 10, and replaces non-finite values by zero. No display smoothing or downsampling.",
        },
        "trajectories": {
            "cycles": cycles.tolist(), "reference": numbers(reference_percent),
            "observedCount": 10, "samples": numbers(samples), "eolPercent": 80,
            "referenceEolCycle": int(cycles[reference_crossing]),
            "referenceDisplayLength": reference_crossing + 1,
            "sampleDisplayLengths": sample_lengths,
            "referenceDisplayRule": "Reference shown through its first 80% SOH crossing, excluding the later 70% padding floor. Exact raw measured length is unavailable.",
            "sampleDisplayRule": "Final predicted trajectories may be shown through their individual first 80% crossings. No values are clipped or smoothed in this export.",
        },
        "generation": {
            "times": numbers(times.numpy()), "states": numbers(states), "sampleIndex": sample_index,
            "seed": seed, "drawCount": draw_count, "solver": "dopri5", "atol": 1e-5, "rtol": 1e-5,
            "functionEvaluations": model_wrapper.function_evaluations,
            "observedPrefixMaxNormalizedRoundoff": prefix_error,
            "stateMeaning": "Actual ODE solution outputs at 101 requested times; not adaptive solver steps or linear morphs.",
            "initialRange": [float(states[0].min()), float(states[0].max())],
            "range": [float(states.min()), float(states.max())],
            "finalMatchesSample": sample_index,
        },
        "model": {
            "blocks": config.num_blocks, "channels": config.channels,
            "guidanceScale": config.guidance_scale, "conditionDropout": config.class_dropout_prob,
            "conditionEmbedding": numbers(encoded.numpy()[0]),
            "device": "cpu", "torchVersion": torch.__version__,
        },
    }
    output = ROOT / "webpage/src/data/overview-example.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, separators=(",", ":"), allow_nan=False) + "\n")
    # Serve an identical downloadable provenance/data copy without requiring
    # the front end to serialize the full numeric capacity matrix into HTML.
    download = ROOT / "webpage/public/data/overview-example.json"
    download.write_bytes(output.read_bytes())
    print(json.dumps({
        "output": str(output.relative_to(ROOT)), "bytes": output.stat().st_size,
        "imageBytes": image_path.stat().st_size, "statesShape": list(states.shape),
        "samplesShape": list(samples.shape), "initialRange": result["generation"]["initialRange"],
        "functionEvaluations": model_wrapper.function_evaluations,
        "referenceEolCycle": result["trajectories"]["referenceEolCycle"],
        "testIndex": test_index, "selectedDrawIndex": sample_index,
        "freshMetrics": fresh_metrics,
    }, indent=2))


if __name__ == "__main__":
    main()
