"""Reproduce the numerical estimates used in the Major 2 reply.

Run from any directory with Python and mpmath:
    python check_parameter_window.py

This is a benchmark check, not a new experimental recast or a UV scan.
The exact one-loop F_A integral is the one in the archived main-v6.tex,
eq:gminus2-FV-FA, with g_mu^V=0 and |g_mu^A|=g_X.
"""

import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp


def evaluate(dps):
    mp.mp.dps = dps
    m_mu = mp.mpf("0.1056583755")  # GeV; same value throughout this check
    delta_mean = mp.mpf("38e-11")
    delta_sigma = mp.mpf("63e-11")
    allowed_negative = 2 * delta_sigma - delta_mean
    coupling_floor = mp.mpf("1e-6")
    coefficient = 2 * mp.pi * mp.sqrt(allowed_negative) / m_mu

    def f_a(mass_GeV):
        r = (m_mu / mass_GeV) ** 2
        return mp.quad(
            lambda x: (x * (1 - x) * (4 - x) + 2 * r * x**3)
            / (1 - x + r * x**2),
            [0, 1],
        )

    def exact_g_limit(mass_GeV):
        return coefficient * mass_GeV / mp.sqrt(f_a(mass_GeV))

    crossing = mp.findroot(
        lambda mass: exact_g_limit(mass) - coupling_floor,
        (mp.mpf("0.0005"), mp.mpf("0.0006")),
    )
    values = {
        "negative_delta_a_limit_abs": allowed_negative,
        "g_limit_per_GeV_light_limit": coefficient,
        "g_limit_at_1MeV_light_limit": coefficient / 1000,
        "g_limit_at_1MeV_exact_integral": exact_g_limit(mp.mpf("0.001")),
        "F_A_at_1MeV": f_a(mp.mpf("0.001")),
        "coupling_floor_crossing_MeV_light_limit": coupling_floor / coefficient * 1000,
        "coupling_floor_crossing_MeV_exact_integral": crossing * 1000,
        "v_s_min_GeV_ms10_lambda4pi": 10 / mp.sqrt(8 * mp.pi),
        "mA_over_g_min_GeV_ms10_lambda4pi": 20 / mp.sqrt(8 * mp.pi),
        "g_max_unit_charge_sqrt4pi_convention": mp.sqrt(4 * mp.pi),
        "g_max_charge2_sqrt4pi_convention": mp.sqrt(4 * mp.pi) / 2,
    }
    return {key: mp.nstr(value, 25) for key, value in values.items()}


def main():
    low_precision = evaluate(40)
    high_precision = evaluate(60)
    relative_changes = {
        key: abs(mp.mpf(value) / mp.mpf(low_precision[key]) - 1)
        for key, value in high_precision.items()
    }
    largest_change = max(relative_changes.values())
    if largest_change > mp.mpf("1e-22"):
        raise RuntimeError("40/60 decimal-digit numerical cross-check failed")
    script = Path(__file__).resolve()
    repository = script.parents[2]
    source_paths = [
        "Replies_to_Referee_3_referee_facing_2026-11-04.tex",
        "overleaf-source/axial-vector-model-building-v6/main-v6.tex",
        "overleaf-source/axial-vector-model-building-v6/plots/axial_vector_constraint.pdf",
    ]
    result = {
        "scope": "Pure axial, heavy-scalar, no-cancellation reference benchmark; no astrophysical ranking or exclusion recast.",
        "inputs": {
            "m_mu_GeV": "0.1056583755",
            "delta_a_mean": "38e-11",
            "delta_a_sigma": "63e-11",
            "sigma_multiplier": 2,
            "g_display_min": "1e-6",
            "g_display_max": "1",
            "mass_display_GeV": ["1e-3", "1e2"],
            "m_s_reference_GeV": "10",
            "lambda_max": "4*pi",
        },
        "outputs": high_precision,
        "verification": {
            "working_precision_decimal_digits": [40, 60],
            "max_relative_change": mp.nstr(largest_change, 8),
        },
        "runtime": {"python": platform.python_version(), "mpmath": mp.__version__},
        "sha256": {
            **{p: hashlib.sha256((repository / p).read_bytes()).hexdigest() for p in source_paths},
            "check_parameter_window.py": hashlib.sha256(script.read_bytes()).hexdigest(),
        },
    }
    output = script.parent / "outputs" / "parameter_window_2026-11-04.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
