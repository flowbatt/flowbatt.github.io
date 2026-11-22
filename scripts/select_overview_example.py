"""Rank existing held-out predictions for a disclosed Figure 1 illustration.

Run with the repository's ML environment:
    PYTHONDONTWRITEBYTECODE=1 python webpage/scripts/select_overview_example.py

This reads the existing ten-draw MATR-1 prediction cache and requires a reference
80% crossing after cycle 1000. It performs no new inference and does not modify
the cache, source data, or checkpoint.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "results/generative_uq/matr_1_Q/flowbatt_10_samples.npz"
OBSERVED_COUNT = 10
EOL_PERCENT = 80
MINIMUM_EOL_EXCLUSIVE = 1000


def forecast_metrics(reference_percent: np.ndarray, samples_percent: np.ndarray) -> dict:
    """RMSE on the forecast only, including the first reference 80% crossing.

    The inputs are SOH percentage points, not fractions. No curve values are
    clipped, smoothed, or resampled. EOL is a sampled crossing, without linear
    interpolation between the archived ten-cycle coordinates.
    """
    reference = np.asarray(reference_percent, dtype=np.float64)
    samples = np.asarray(samples_percent, dtype=np.float64)
    crossings = np.flatnonzero(reference <= EOL_PERCENT)
    if not len(crossings):
        raise ValueError("The reference must cross 80% within its exported horizon.")
    stop = int(crossings[0]) + 1
    if stop <= OBSERVED_COUNT:
        raise ValueError("The forecast interval is empty.")
    difference = samples[:, OBSERVED_COUNT:stop] - reference[OBSERVED_COUNT:stop]
    rmse = np.sqrt(np.mean(difference ** 2, axis=1))
    cycles = np.arange(len(reference)) * 10 + 1
    eol = [
        int(cycles[np.flatnonzero(sample <= EOL_PERCENT)[0]])
        if np.any(sample <= EOL_PERCENT) else None for sample in samples
    ]
    reference_eol = int(cycles[stop - 1])
    return {
        "forecastStartIndex": OBSERVED_COUNT,
        "forecastEndIndexInclusive": stop - 1,
        "forecastPointCount": stop - OBSERVED_COUNT,
        "forecastStartCycle": int(cycles[OBSERVED_COUNT]),
        "forecastEndCycle": reference_eol,
        "rmseUnit": "SOH percentage points",
        "perDrawRmse": rmse.tolist(),
        "meanDrawRmse": float(rmse.mean()),
        "medianDrawRmse": float(np.median(rmse)),
        "maximumDrawRmse": float(rmse.max()),
        "ensembleMeanCurveRmse": float(np.sqrt(np.mean(difference.mean(axis=0) ** 2))),
        "lowestRmseDrawIndex": int(np.argmin(rmse)),
        "referenceEolCycle": reference_eol,
        "perDrawEolCycles": eol,
        "perDrawEolCycleErrors": [value - reference_eol if value is not None else None for value in eol],
        "eolRule": "First exported SOH value at or below 80%; ten-cycle grid, without interpolation.",
    }


def cached_shortlist() -> tuple[list[dict], dict]:
    """Rank eligible cells by mean draw RMSE; exclude the previous row 0."""
    with np.load(CACHE, allow_pickle=False) as archive:
        reference = archive["reference"].astype(np.float64) * 100
        samples = archive["samples"].astype(np.float64) * 100
        cache_settings = {
            "seed": int(archive["seed"]),
            "inferenceStepsMetadata": int(archive["inference_steps"]),
            "drawCount": samples.shape[0],
            "testRowCount": reference.shape[0],
        }
    candidates = [
        {"testIndex": index, **forecast_metrics(reference[index], samples[:, index])}
        for index in range(len(reference)) if index != 0
    ]
    candidates = [
        entry for entry in candidates
        if entry["referenceEolCycle"] > MINIMUM_EOL_EXCLUSIVE
    ]
    candidates.sort(key=lambda entry: (entry["meanDrawRmse"], entry["testIndex"]))
    return candidates, cache_settings


if __name__ == "__main__":
    candidates, settings = cached_shortlist()
    print(json.dumps({"cacheSettings": settings, "topFive": candidates[:5]}, indent=2))
