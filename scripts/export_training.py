"""Export a real FlowBatt training-objective example, without training a model.

    PYTHONDONTWRITEBYTECODE=1 python webpage/scripts/export_training.py

The 101 frames evaluate the conditional flow-matching training path for one
real prepared training cell and one Gaussian draw. They are neither inference
ODE states nor optimizer history. All writes are confined to webpage/.
"""
from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
WEBPAGE = ROOT / "webpage"
os.environ["MPLCONFIGDIR"] = str(WEBPAGE / ".cache/matplotlib")
sys.path.insert(0, str(ROOT / "github"))

import numpy as np
from PIL import Image
import torch
from matplotlib import colormaps
from flow_matching.path import AffineProbPath
from flow_matching.path.scheduler import CondOTScheduler
from flowbatt.data import get_dataset
from flowbatt.inference import load_flowbatt
from flowbatt.sampling import encode_condition


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numbers(array: np.ndarray | torch.Tensor, decimals: int = 6) -> list:
    if torch.is_tensor(array):
        array = array.cpu().numpy()
    return np.round(np.asarray(array, dtype=np.float64), decimals).tolist()


def save_capacity(matrix: np.ndarray, name: str, minimum: float, maximum: float) -> str:
    lookup = colormaps[name](np.linspace(0, 1, 256), bytes=True)[:, :3]
    # Original rows are cycles; columns run from high to low voltage.
    # Transpose only for PNG: cycle x, highest-voltage row at the top.
    indices = np.clip(np.round((matrix.T - minimum) / (maximum - minimum) * 255), 0, 255).astype(np.uint8)
    relative = f"data/capacity-matr1-training-{name}.png"
    target = WEBPAGE / "public" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(lookup[indices]).save(target, optimize=True)
    return relative


@torch.inference_mode()
def main() -> None:
    torch.set_num_threads(2)
    source = ROOT / "github/datasets/MATR-1.npz"
    checkpoint = ROOT / "github/checkpoints/flowbatt/MATR-1.pth"
    source_hash, checkpoint_hash = sha256(source), sha256(checkpoint)
    dataset = get_dataset("MATR-1")
    train_index, seed, frame_count, observed_count = 0, 2026, 101, 10
    x1 = dataset.train_data.label[train_index:train_index + 1].clone()
    condition = dataset.train_data.feature[train_index:train_index + 1].clone()
    matrix = condition.numpy()[0]
    model, initializer, _, config = load_flowbatt(
        (1, 100, 100), mask_size=observed_count, device="cpu", battery_dataset="MATR-1"
    )
    model.eval()
    torch.manual_seed(seed)
    noise = torch.randn_like(x1)
    x0 = initializer(noise, x1[:, :observed_count], condition)
    # Match the inference export's 101 saved time positions for a shared slider.
    times = torch.linspace(0, 1, frame_count, dtype=torch.float32)
    path = AffineProbPath(scheduler=CondOTScheduler())
    sample = path.sample(
        x_0=x0.expand(frame_count, -1), x_1=x1.expand(frame_count, -1), t=times
    )
    predicted_chunks = []
    for start in range(0, frame_count, 16):
        end = min(start + 16, frame_count)
        predicted_chunks.append(model(
            sample.x_t[start:end], sample.t[start:end], condition.expand(end - start, -1, -1)
        ))
    predicted = torch.cat(predicted_chunks)
    # Same squared-error expression as train_step, here one cell per time.
    per_time_loss = torch.pow(predicted - sample.dx_t, 2).mean(dim=1)
    target = x1[0] - x0[0]
    encoded = encode_condition(model, condition)[0]
    cycles = np.arange(config.sequence_length) * 10 + 1
    physical_target = dataset.label_transformation.inverse_transform(x1)[0] * 100
    physical_states = dataset.label_transformation.inverse_transform(sample.x_t) * 100
    minimum, maximum = float(matrix.min()), float(matrix.max())
    transform = dataset.label_transformation
    velocity_scale = float((transform.max - transform.min + 1e-8) / 2 * 100)
    known_prefix_error = float((sample.x_t[:, :observed_count] - x1[:, :observed_count]).abs().max())
    formula_error = float((sample.x_t - ((1 - times[:, None]) * x0 + times[:, None] * x1)).abs().max())

    assert sample.x_t.shape == predicted.shape == (frame_count, config.sequence_length)
    assert torch.isfinite(sample.x_t).all() and torch.isfinite(predicted).all()
    assert torch.equal(sample.x_t[0], x0[0]) and torch.equal(sample.x_t[-1], x1[0])
    assert torch.equal(sample.dx_t, target.expand(frame_count, -1))
    assert formula_error == 0
    assert known_prefix_error < 2e-7
    assert torch.count_nonzero(target[:observed_count]) == 0
    assert torch.count_nonzero(predicted[:, :observed_count]) == 0
    assert torch.allclose(per_time_loss.mean(), torch.pow(predicted - sample.dx_t, 2).mean())
    with np.load(source, allow_pickle=False) as archive:
        assert np.array_equal(x1.numpy()[0], archive["y_train_scaled"][train_index])
        assert np.array_equal(matrix, archive["x_train"][train_index])
        assert np.array_equal(physical_target.numpy(), archive["y_train_physical"][train_index] * 100)
    # The exporter must never modify the dataset/checkpoint it reads.
    assert sha256(source) == source_hash and sha256(checkpoint) == checkpoint_hash

    capacity_image = save_capacity(matrix, "cividis", minimum, maximum)
    paper_image = save_capacity(matrix, "cool", minimum, maximum)
    source_paths = [
        "github/flowbatt/flow_matching.py", "github/flowbatt/train.py",
        "github/flowbatt/models/dit.py", "github/flowbatt/data.py",
    ]
    result = {
        "metadata": {
            "dataset": "MATR-1", "split": "train", "trainIndex": train_index,
            "displayName": "MATR-1 · training cell 1", "cellId": None,
            "selection": "First train-array row, chosen before evaluating this checkpoint; not selected by loss or prediction accuracy.",
            "sourceDataset": str(source.relative_to(ROOT)), "sourceDatasetSha256": source_hash,
            "sourceCheckpoint": str(checkpoint.relative_to(ROOT)), "sourceCheckpointSha256": checkpoint_hash,
            "sourceCode": [{"path": name, "sha256": sha256(ROOT / name)} for name in source_paths],
            "seed": seed, "sequenceLength": config.sequence_length, "earlyCycles": 100,
            "interpretation": "Training-objective illustration for one real prepared training cell and one noise draw, evaluated at a fixed pretrained checkpoint. No parameter updates, optimization history, or inference ODE solve.",
            "referenceType": "Prepared, normalized and causally smoothed training trajectory, including the model's 70% padding floor.",
            "identityNote": "The archive contains no original cell IDs or raw measured lengths. No original identity or raw endpoint is inferred.",
        },
        "capacity": {
            "image": capacity_image, "paperImage": paper_image,
            "colormap": "cividis", "paperColormap": "cool",
            "minimum": minimum, "maximum": maximum, "unit": "Ah",
            "cycles": list(range(1, 101)), "voltageIndices": list(range(1, 101)),
            "values": numbers(matrix[:, ::-1].T, 9),
            "orientation": "JSON rows low-to-high voltage, cycle columns; PNG highest-voltage row at top, cycles left-to-right.",
            "definition": "Actual unnormalized cycle-by-voltage discharge-capacity differences relative to cycle 10. Original cycle-11 zeroing and nonfinite treatment retained.",
        },
        "training": {
            "times": numbers(times, 9), "cycles": cycles.tolist(),
            "statesNormalized": numbers(sample.x_t),
            "x0Normalized": numbers(x0[0]), "x1Normalized": numbers(x1[0]),
            "targetVelocityNormalized": numbers(target),
            "predictedVelocityNormalized": numbers(predicted),
            "loss": numbers(per_time_loss, 9), "observedCount": observed_count,
            "stateRange": [float(sample.x_t.min()), float(sample.x_t.max())],
            "velocityRange": [min(float(target.min()), float(predicted.min())), max(float(target.max()), float(predicted.max()))],
            "stateSohPercentRange": [float(physical_states.min()), float(physical_states.max())],
            "targetSohPercentRange": [float(physical_target.min()), float(physical_target.max())],
            "path": "x_t = (1-t) x_0 + t x_1",
            "target": "u_t = x_1 - x_0",
            "lossDefinition": "Per-time mean squared error over all 256 normalized coordinates: mean((v_theta(x_t,t,Q)-u_t)^2). This is not optimizer history or an average test error.",
            "timeSampling": "Actual training samples t uniformly on [0,1]. This explanatory animation sweeps one pair at 101 requested positions t=i/100, aligned with the inference export; no training updates occur.",
            "scheduler": "CondOTScheduler", "alpha": "t", "sigma": "1-t", "terminalNoiseCoefficient": 0,
            "prefixHandling": "The first ten x0 coordinates equal the corresponding x1 values; their target and predicted velocities are zero. Full-trajectory loss still averages over 256 coordinates.",
            "knownPrefixMaxNormalizedRoundoff": known_prefix_error,
        },
        "normalization": {
            "minimum": float(transform.min), "maximum": float(transform.max), "epsilon": 1e-8,
            "sohPercentPerNormalizedUnit": velocity_scale,
            "stateToSohPercent": "100 * ((x_normalized+1)/2 * (maximum-minimum+epsilon) + minimum)",
            "velocityToSohPercentagePointsPerUnitT": "v_normalized * sohPercentPerNormalizedUnit; no affine offset is added to velocities.",
        },
        "model": {
            "blocks": config.num_blocks, "channels": config.channels,
            "conditionDropout": config.class_dropout_prob, "conditionEmbedding": numbers(encoded),
            "device": "cpu", "mode": "eval; fixed weights, no optimizer",
            "torchVersion": torch.__version__, "flowMatchingVersion": importlib.metadata.version("flow_matching"),
        },
    }
    output = WEBPAGE / "src/data/training-example.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, separators=(",", ":"), allow_nan=False) + "\n")
    download = WEBPAGE / "public/data/training-example.json"
    download.write_bytes(output.read_bytes())
    print(json.dumps({
        "output": str(output.relative_to(ROOT)), "bytes": output.stat().st_size,
        "frames": frame_count, "stateRange": result["training"]["stateRange"],
        "velocityRange": result["training"]["velocityRange"],
        "sohPercentRange": result["training"]["stateSohPercentRange"],
        "lossRange": [float(per_time_loss.min()), float(per_time_loss.max())],
        "images": [capacity_image, paper_image],
    }, indent=2))


if __name__ == "__main__":
    main()
