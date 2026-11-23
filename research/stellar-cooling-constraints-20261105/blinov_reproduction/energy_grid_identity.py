"""Deterministic, tolerance-aware identity checks for the archived B.16 energy grid."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_ENERGY_GRID_REFERENCE = (
    HERE / "outputs" / "b16_energy_grid_reference_10mev_2026-11-09.json"
)
ENERGY_GRID_RTOL = 5.0e-14
ENERGY_GRID_ATOL_MEV = 1.0e-13


def float_array_sha256(values) -> str:
    array = np.asarray(values, dtype="<f8")
    return hashlib.sha256(array.tobytes()).hexdigest()


def load_energy_grid_reference(path=DEFAULT_ENERGY_GRID_REFERENCE,
                               expected_sha256: str | None = None) -> dict:
    path = Path(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    nodes = np.asarray(payload.get("energy_nodes_MeV"), dtype=float)
    count = payload.get("energy_node_count")
    if nodes.ndim != 1 or not np.all(np.isfinite(nodes)):
        raise ValueError("Archived B.16 energy-grid reference must be a finite 1D array")
    if not isinstance(count, int) or len(nodes) != count:
        raise ValueError("Archived B.16 energy-grid reference node count is inconsistent")
    if len(nodes) != 842 or np.any(np.diff(nodes) <= 0.0):
        raise ValueError("Archived B.16 energy-grid reference must contain 842 sorted unique nodes")
    declared_hash = payload.get("energy_grid_sha256")
    actual_hash = float_array_sha256(nodes)
    if declared_hash != actual_hash:
        raise ValueError("Archived B.16 energy-grid reference SHA-256 is internally inconsistent")
    if expected_sha256 is not None and declared_hash != expected_sha256:
        raise ValueError("Archived B.16 energy-grid reference does not match the original baseline SHA-256")
    payload["_path"] = str(path)
    payload["_file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    payload["_nodes"] = nodes
    return payload


def compare_energy_grid(values, reference: dict,
                        rtol: float = ENERGY_GRID_RTOL,
                        atol: float = ENERGY_GRID_ATOL_MEV) -> dict:
    actual = np.asarray(values, dtype=float)
    expected = np.asarray(reference["_nodes"], dtype=float)
    if actual.ndim != 1 or actual.shape != expected.shape:
        return {
            "matches": False,
            "actual_node_count": int(actual.size),
            "reference_node_count": int(expected.size),
            "max_absolute_difference_MeV": None,
            "max_relative_difference": None,
            "rtol": float(rtol),
            "atol_MeV": float(atol),
        }
    absolute = np.abs(actual - expected)
    relative = absolute / np.maximum(np.abs(expected), np.finfo(float).tiny)
    return {
        "matches": bool(np.allclose(actual, expected, rtol=rtol, atol=atol)),
        "actual_node_count": int(actual.size),
        "reference_node_count": int(expected.size),
        "max_absolute_difference_MeV": float(np.max(absolute)),
        "max_relative_difference": float(np.max(relative)),
        "max_ulp_difference": float(np.max(absolute / np.abs(np.spacing(expected)))),
        "rtol": float(rtol),
        "atol_MeV": float(atol),
    }
