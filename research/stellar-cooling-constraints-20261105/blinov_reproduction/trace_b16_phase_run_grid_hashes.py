"""Trace the exact production CLI call and every grid-hash invocation."""
from __future__ import annotations

import sys
import numpy as np

import audit_b16_escape_phase_space as phase


_original_hash = phase.float_array_sha256
_original_run = phase.run


def traced_float_array_sha256(values):
    array = np.asarray(values)
    digest = _original_hash(values)
    if array.ndim == 1 and array.size in (200, 642, 842):
        print({
            "trace": "float_array_sha256",
            "shape": array.shape,
            "dtype": str(array.dtype),
            "sha256": digest,
            "min": float(np.min(array)),
            "max": float(np.max(array)),
            "first_8": array[:8].tolist(),
            "last_8": array[-8:].tolist(),
        }, flush=True)
    return digest


def traced_run(*args, **kwargs):
    print({
        "trace": "run_arguments",
        "positional": [str(x) if hasattr(x, "__fspath__") else x for x in args],
        "keyword": kwargs,
    }, flush=True)
    return _original_run(*args, **kwargs)


phase.float_array_sha256 = traced_float_array_sha256
phase.run = traced_run

if __name__ == "__main__":
    sys.argv = [
        "audit_b16_escape_phase_space.py",
        "--mass", "10",
        "--nr", "200",
        "--opacity-order", "640",
        "--ne", "200",
        "--na", "32",
        "--ns", "64",
        "--energy-offset", "1000",
        "--output", "/tmp/b16_cli_trace_result.json",
    ]
    phase.main()
