#!/usr/bin/env python3
"""Independent VLL fermion effective-potential audit of UV tadpoles and masses.

For each charged-lepton/VLL sector, the divergent one-loop fermion potential
is proportional to Tr[(M^dagger M)^2]. This script derives its first and
second derivatives analytically, checks the invariant against an independent
SVD spectrum, and compares the second derivatives with the exact-basis
fermion self-energy UV-local coefficients already archived in this PR.
It does not choose a tadpole or VEV renormalization scheme.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

ME = 20_000.0
VH = 246.22
THETA_L = 1.0e-2
M_LEPTON = {"mu": 0.1056583755, "tau": 1.77686}
BENCHMARKS = {
    "A_open_AA": {"vs_GeV": 70.886458, "mA_GeV": 10.0},
    "B_closed_AA": {"vs_GeV": 315.0, "mA_GeV": 63.0},
}


def yukawas(vs: float, ml: float) -> tuple[float, float]:
    y = math.sqrt(2.0) * ME * THETA_L / VH
    lam = math.sqrt(2.0) * ml / (THETA_L * vs)
    return y, lam


def trace_m4_closed_form(h: float, s: float, y: float, lam: float) -> float:
    """Tr[(M^dagger M)^2] for M=[[0,y h/sqrt(2)],[lam s/sqrt(2),ME]]."""
    return (
        ME**4
        + ME**2 * y**2 * h**2
        + 0.25 * y**4 * h**4
        + ME**2 * lam**2 * s**2
        + 0.25 * lam**4 * s**4
    )


def trace_m4_from_svd(h: float, s: float, y: float, lam: float) -> float:
    matrix = np.array([
        [0.0, y * h / math.sqrt(2.0)],
        [lam * s / math.sqrt(2.0), ME],
    ])
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    return float(np.sum(singular_values**4))


def derivatives(vs: float) -> dict:
    total = {"F": 0.0, "F_h": 0.0, "F_s": 0.0,
             "F_hh": 0.0, "F_hs": 0.0, "F_ss": 0.0}
    by_flavour = {}
    for flavour, ml in M_LEPTON.items():
        y, lam = yukawas(vs, ml)
        f = trace_m4_closed_form(VH, vs, y, lam)
        fh = 2.0 * ME**2 * y**2 * VH + y**4 * VH**3
        fs = 2.0 * ME**2 * lam**2 * vs + lam**4 * vs**3
        fhh = 2.0 * ME**2 * y**2 + 3.0 * y**4 * VH**2
        fss = 2.0 * ME**2 * lam**2 + 3.0 * lam**4 * vs**2
        item = {
            "ml_GeV": ml, "y": y, "lambda": lam,
            "Tr_MdagM_squared_GeV4": f,
            "dF_dh_GeV3": fh,
            "dF_ds_GeV3": fs,
            "d2F_dh2_GeV2": fhh,
            "d2F_dhds_GeV2": 0.0,
            "d2F_ds2_GeV2": fss,
            "svd_trace_relative_difference": abs(
                trace_m4_from_svd(VH, vs, y, lam) - f
            ) / max(abs(f), 1.0),
        }
        by_flavour[flavour] = item
        for key in total:
            total[key] += item[{
                "F": "Tr_MdagM_squared_GeV4",
                "F_h": "dF_dh_GeV3",
                "F_s": "dF_ds_GeV3",
                "F_hh": "d2F_dh2_GeV2",
                "F_hs": "d2F_dhds_GeV2",
                "F_ss": "d2F_ds2_GeV2",
            }[key]]
    return {"sum": total, "by_flavour": by_flavour}


def verify_symbolic_derivatives(vs: float) -> dict:
    with mp.workdps(50):
        me = mp.mpf(str(ME))
        vh = mp.mpf(str(VH))
        vs_mp = mp.mpf(str(vs))
        theta_l = mp.mpf(str(THETA_L))
        errors = []
        for ml_float in M_LEPTON.values():
            ml = mp.mpf(str(ml_float))
            y = mp.sqrt(2) * me * theta_l / vh
            lam = mp.sqrt(2) * ml / (theta_l * vs_mp)

            def f(h, singlet):
                return (
                    me**4 + me**2*y**2*h**2 + y**4*h**4/4
                    + me**2*lam**2*singlet**2 + lam**4*singlet**4/4
                )

            fh = 2*me**2*y**2*vh + y**4*vh**3
            fs = 2*me**2*lam**2*vs_mp + lam**4*vs_mp**3
            fhh = 2*me**2*y**2 + 3*y**4*vh**2
            fss = 2*me**2*lam**2 + 3*lam**4*vs_mp**2
            got = (
                mp.diff(lambda h: f(h, vs_mp), vh),
                mp.diff(lambda x: f(vh, x), vs_mp),
                mp.diff(lambda h: f(h, vs_mp), vh, 2),
                mp.diff(lambda x: f(vh, x), vs_mp, 2),
                mp.diff(lambda x: mp.diff(lambda h: f(h, x), vh), vs_mp),
            )
            expected = (fh, fs, fhh, fss, mp.mpf("0"))
            errors.extend(float(abs(a-b)/max(1, abs(b))) for a,b in zip(got,expected))
    return {"mpmath_dps": 50, "derivative_components_checked": len(errors),
            "max_relative_difference": max(errors)}


def run_audit(reference_json: Path) -> dict:
    reference = json.loads(reference_json.read_text(encoding="utf-8"))
    out = {}
    max_local_rel = 0.0
    max_svd_rel = 0.0
    max_symbolic_rel = 0.0
    for label, benchmark in BENCHMARKS.items():
        vs = benchmark["vs_GeV"]
        calc = derivatives(vs)
        ref = reference["benchmarks"][label]
        fhh = calc["sum"]["F_hh"]
        fhs = calc["sum"]["F_hs"]
        fss = calc["sum"]["F_ss"]
        ref_hh = float(ref["hh"]["UV_local_coefficient_sum"][0])
        ref_hs = float(ref["hs"]["UV_local_coefficient_sum"][0])
        ref_ss = float(ref["ss"]["UV_local_coefficient_sum"][0])
        errors = {
            "hh_relative": abs(fhh-ref_hh)/max(abs(ref_hh),1.0),
            "hs_absolute_GeV2": abs(fhs-ref_hs),
            "ss_relative": abs(fss-ref_ss)/max(abs(ref_ss),1.0),
        }
        if errors["hh_relative"] > 2e-10 or errors["ss_relative"] > 2e-10:
            raise AssertionError(f"{label}: effective-potential diagonal UV pole mismatch {errors}")
        if errors["hs_absolute_GeV2"] > 2e-7:
            raise AssertionError(f"{label}: nonzero mixed local pole {errors['hs_absolute_GeV2']}")
        pole_factor = -1.0/(16.0*math.pi**2)
        tadpole_poles = {
            "T_h_loop_pole_coefficient_GeV3": pole_factor*calc["sum"]["F_h"],
            "T_s_loop_pole_coefficient_GeV3": pole_factor*calc["sum"]["F_s"],
        }
        mass_poles = {
            "hh_loop_local_pole_coefficient_GeV2": pole_factor*fhh,
            "hs_loop_local_pole_coefficient_GeV2": pole_factor*fhs,
            "ss_loop_local_pole_coefficient_GeV2": pole_factor*fss,
        }
        max_local_rel = max(max_local_rel, errors["hh_relative"], errors["ss_relative"])
        max_svd_rel = max(
            max_svd_rel,
            max(x["svd_trace_relative_difference"] for x in calc["by_flavour"].values()),
        )
        symbolic = verify_symbolic_derivatives(vs)
        max_symbolic_rel = max(max_symbolic_rel, symbolic["max_relative_difference"])
        out[label] = {
            "vs_GeV": vs,
            "couplings_and_invariants": calc,
            "comparison_to_exact_mass_eigenstate_uv_local_sums": {
                "independent_effective_potential_derivatives_GeV2": {
                    "hh": fhh, "hs": fhs, "ss": fss,
                },
                "exact_mass_eigenstate_uv_local_coefficients_GeV2": {
                    "hh": ref_hh, "hs": ref_hs, "ss": ref_ss,
                },
                "errors": errors,
            },
            "fermion_loop_tadpole_pole_coefficients": tadpole_poles,
            "fermion_loop_local_mass_pole_coefficients": mass_poles,
            "symbolic_derivative_check": symbolic,
        }
    return {
        "status": "PASS",
        "method": (
            "closed-form Tr[(Mdagger M)^2] and its derivatives, checked against "
            "independent SVD singular values and 50-digit mpmath differentiation"
        ),
        "divergent_potential_convention": (
            "V_1^div = +(Delta_UV/(16 pi^2)) sum_flavours Tr[(Mdagger M)^2]; "
            "the listed one-point 1PI pole is -dV_1^div/dphi and the listed "
            "mass-matrix counterterm pole is -d2V_1^div/dphi_a dphi_b"
        ),
        "benchmarks": out,
        "global_checks": {
            "max_relative_difference_effective_potential_vs_self_energy_local_uv": max_local_rel,
            "max_relative_difference_closed_form_vs_svd": max_svd_rel,
            "max_relative_difference_analytic_vs_mpmath_derivatives": max_symbolic_rel,
        },
        "interpretation_limits": [
            "The listed first-derivative coefficients are VLL-sector one-point 1PI UV poles, -dV_1^div/dphi, only.",
            "They do not by themselves select a tadpole or VEV-renormalization prescription.",
            "The second derivatives reproduce the VLL-sector local mass UV poles; they are not finite pole-mass shifts.",
            "No gauge, Goldstone, ghost, scalar, top-quark, or non-VLL contributions are included.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_audit(args.reference_json)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "global_checks": result["global_checks"],
        "benchmarks": {
            k: {
                "tadpoles": v["fermion_loop_tadpole_pole_coefficients"],
                "local_mass_poles": v["fermion_loop_local_mass_pole_coefficients"],
                "UV_comparison": v["comparison_to_exact_mass_eigenstate_uv_local_sums"],
            } for k,v in result["benchmarks"].items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()
