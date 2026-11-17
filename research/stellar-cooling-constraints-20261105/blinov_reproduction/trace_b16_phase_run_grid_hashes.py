"""Call the production B.16 run() and trace each grid hash call."""
from __future__ import annotations

import numpy as np

import audit_b16_escape_phase_space as phase


_original = phase.float_array_sha256


def traced_float_array_sha256(values):
    array = np.asarray(values)
    digest = _original(values)
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


phase.float_array_sha256 = traced_float_array_sha256


if __name__ == "__main__":
    phase.run(
        phase.DEFAULT_PROFILE,
        phase.DEFAULT_FIG7,
        phase.DEFAULT_BASELINE,
        10.0,
        200,
        640,
        200,
        32,
        64,
        1000.0,
    )
