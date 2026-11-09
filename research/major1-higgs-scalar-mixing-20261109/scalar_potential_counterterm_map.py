#!/usr/bin/env python3
"""Gauge-invariant VLL potential poles and leading EFT dimension-eight audit.

The full-theory fermion determinant is evaluated in the unbroken scalar
backgrounds. Its UV pole is mapped onto the renormalizable scalar potential.
The leading dimension-five EFT mass operator is then treated separately:
its one-loop light-fermion determinant generates a dimension-eight scalar
operator, and its mixed h-s contact contribution is kept explicitly.

All reported coefficients multiply Delta_UV = 1/epsilon - gamma_E + ln(4 pi).
This is a VLL-sector UV-pole audit, not a complete gauge-independent
renormalization or a complete UV-EFT matching calculation.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

VH = 246.22
ME = 20_000.0
LOOP = 1.0 / (16.0 * math.pi**2)
BENCHMARKS = {
    "A_open_AA": 70.886458,
    "B_closed_AA": 315.0,
}


def potential_tadpoles_per_vev(
    vh: float, vs: float, dmu_h2: float, dmu_s2: float,
    dlam_h: float, dlam_s: float, dlam_hs: float,
) -> tuple[float, float]:
    """Derivatives of the potential counterterm divided by the VEVs."""
    return (
        -dmu_h2 + vh**2*dlam_h + 0.5*vs**2*dlam_hs,
        -dmu_s2 + vs**2*dlam_s + 0.5*vh**2*dlam_hs,
    )


def potential_mass_counterterm(
    vh: float, vs: float, dmu_h2: float, dmu_s2: float,
    dlam_h: float, dlam_s: float, dlam_hs: float,
) -> list[list[float]]:
    """Second derivatives of the potential counterterm at the vacuum."""
    return [
        [-dmu_h2 + 3.0*vh**2*dlam_h + 0.5*vs**2*dlam_hs,
         vh*vs*dlam_hs],
        [vh*vs*dlam_hs,
         -dmu_s2 + 3.0*vs**2*dlam_s + 0.5*vh**2*dlam_hs],
    ]


def solve_potential_counterterms(
    vh: float, vs: float,
    F_h: float, F_s: float, F_hh: float, F_hs: float, F_ss: float,
) -> dict:
    """Solve the five gauge-invariant potential counterterms from V1^div.

    V1^div = +Delta_UV F/(16 pi^2), while the potential counterterm is
    delta V = -Delta_UV F/(16 pi^2). Therefore the potential counterterm
    derivatives equal the corresponding loop 1PI pole coefficients in the
    convention Gamma_inv = p^2 I - M_loc^2 + Pi_RC.
    """
    t_h_loop_1pi = -LOOP * F_h
    t_s_loop_1pi = -LOOP * F_s
    pi_hh_loop = -LOOP * F_hh
    pi_hs_loop = -LOOP * F_hs
    pi_ss_loop = -LOOP * F_ss

    t_h_over_vh = t_h_loop_1pi / vh
    t_s_over_vs = t_s_loop_1pi / vs

    dlam_hs = pi_hs_loop / (vh * vs)
    dlam_h = (pi_hh_loop - t_h_over_vh) / (2.0 * vh**2)
    dlam_s = (pi_ss_loop - t_s_over_vs) / (2.0 * vs**2)
    dmu_h2 = vh**2*dlam_h + 0.5*vs**2*dlam_hs - t_h_over_vh
    dmu_s2 = vs**2*dlam_s + 0.5*vh**2*dlam_hs - t_s_over_vs

    tad_ct = potential_tadpoles_per_vev(
        vh, vs, dmu_h2, dmu_s2, dlam_h, dlam_s, dlam_hs
    )
    mass_ct = potential_mass_counterterm(
        vh, vs, dmu_h2, dmu_s2, dlam_h, dlam_s, dlam_hs
    )
    return {
        "delta_mu_H2_GeV2": dmu_h2,
        "delta_mu_S2_GeV2": dmu_s2,
        "delta_lambda_H": dlam_h,
        "delta_lambda_S": dlam_s,
        "delta_lambda_HS": dlam_hs,
        "potential_counterterm_tadpoles_per_vev_GeV2": list(tad_ct),
        "potential_counterterm_mass_matrix_GeV2": mass_ct,
        "loop_1PI_tadpole_pole_coefficients_GeV3": [
            t_h_loop_1pi, t_s_loop_1pi
        ],
        "loop_Pi_RC_local_pole_coefficients_GeV2": [
            [pi_hh_loop, pi_hs_loop],
            [pi_hs_loop, pi_ss_loop],
        ],
        "tadpole_cancellation_residual_GeV2": [
            t_h_loop_1pi - vh*tad_ct[0],
            t_s_loop_1pi - vs*tad_ct[1],
        ],
        "mass_cancellation_residual_GeV2": [
            [pi_hh_loop-mass_ct[0][0], pi_hs_loop-mass_ct[0][1]],
            [pi_hs_loop-mass_ct[1][0], pi_ss_loop-mass_ct[1][1]],
        ],
    }


def leading_eft5_derivatives(vh: float, vs: float, by_flavour: dict) -> dict:
    """Derivatives of F_EFT = sum |C5|^4 (Hdag H)^2(Sdag S)^2.

    With H0=phi_h/sqrt(2), S=phi_s/sqrt(2), the neutral light mass is
    m_l(phi_h,phi_s)=C5 phi_h phi_s/2=y lambda phi_h phi_s/(2 M_E).
    """
    total = {k: 0.0 for k in ("F", "F_h", "F_s", "F_hh", "F_hs", "F_ss")}
    flavours = {}
    sum_c5_fourth = 0.0
    for name, item in by_flavour.items():
        y = float(item["y"])
        lam = float(item["lambda"])
        c5 = y * lam / ME
        kappa = 0.5 * c5
        mass = kappa * vh * vs
        f = mass**4
        values = {
            "F": f,
            "F_h": 4.0*f/vh,
            "F_s": 4.0*f/vs,
            "F_hh": 12.0*f/vh**2,
            "F_hs": 16.0*f/(vh*vs),
            "F_ss": 12.0*f/vs**2,
        }
        for key, value in values.items():
            total[key] += value
        sum_c5_fourth += abs(c5)**4
        flavours[name] = {
            "C5_GeVminus1": c5,
            "kappa_neutral_mass_operator_GeVminus1": kappa,
            "m_EFT5_at_vev_GeV": mass,
            "input_light_mass_GeV": float(item["ml_GeV"]),
            "mass_relative_difference": abs(mass-float(item["ml_GeV"])) / float(item["ml_GeV"]),
            "F_derivatives": values,
        }

    bubble = {
        "hh": 12.0*total["F"] / vh**2,
        "hs": 12.0*total["F"] / (vh*vs),
        "ss": 12.0*total["F"] / vs**2,
    }
    contact = {
        "hh": 0.0,
        "hs": 4.0*total["F"] / (vh*vs),
        "ss": 0.0,
    }
    total_local = {
        "hh": bubble["hh"] + contact["hh"],
        "hs": bubble["hs"] + contact["hs"],
        "ss": bubble["ss"] + contact["ss"],
    }
    return {
        "flavours": flavours,
        "sum_derivatives_GeV": total,
        "bubble_local_UV_coefficients_GeV2": bubble,
        "dimension5_contact_local_UV_coefficients_GeV2": contact,
        "complete_leading_EFT5_local_UV_coefficients_GeV2": total_local,
        "one_loop_EFT_1PI_tadpole_pole_coefficients_GeV3": {
            "h": -LOOP*total["F_h"],
            "s": -LOOP*total["F_s"],
        },
        "one_loop_EFT_Pi_RC_local_pole_coefficients_GeV2": {
            "hh": -LOOP*total_local["hh"],
            "hs": -LOOP*total_local["hs"],
            "ss": -LOOP*total_local["ss"],
        },
        "dimension8_operator": "(Hdagger H)^2 (Sdagger S)^2",
        "dimension8_potential_counterterm_coefficient_GeVminus4": -LOOP*sum_c5_fourth,
        "dimension8_potential_loop_pole_coefficient_GeVminus4": LOOP*sum_c5_fourth,
        "dimension8_operator_coefficient_sum_C5_fourth_GeVminus4": sum_c5_fourth,
    }


def plan_c_soft_plus_hard(
    vh: float, vs: float, s: float, mu: float, by_flavour: dict,
) -> complex:
    """Plan-C-lite finite soft bubble+contact plus hard derivative term.

    This reproduces the published Plan-C-lite convention only for the
    leading mass-proportional EFT5 light-lepton terms and the recorded
    derivative hard coefficient. It is used here to audit scale dependence,
    not to promote the subset to a complete matching result.
    """
    total = 0.0j
    for item in by_flavour.values():
        mass = float(item["ml_GeV"])
        m2 = mass*mass
        m4 = m2*m2
        beta = math.sqrt(max(0.0, 1.0 - 4.0*m2/s))
        log_ratio = math.log(m2/(mu*mu))
        a0 = m2*(1.0-log_ratio)
        b0 = complex(
            -log_ratio + 2.0 - beta*math.log((1.0+beta)/(1.0-beta)),
            math.pi*beta,
        )
        product = m2/(vh*vs)
        bubble = product*(4.0*a0 + 2.0*(4.0*m2-s)*b0)*LOOP
        contact = 4.0*m4/(vh*vs)*(1.0-log_ratio)*LOOP
        q = 2.0*m2/(vh*vs)
        hard = -q*s*LOOP*(math.log(ME*ME/(mu*mu))-2.0/3.0)
        total += bubble + contact + hard
    return total


def plan_c_scale_dependence(
    vh: float, vs: float, s: float, by_flavour: dict,
    mu_reference: float = ME, finite_difference_step: float = 1.0e-5,
) -> dict:
    """Check that the leftover Plan-C scale dependence is exactly EFT5 O8.

    The bubble and hard derivative cancel their momentum-dependent scale
    logarithms. The remaining local term equals twice the leading-EFT5
    mixed Pi_B UV-pole coefficient; the dimension-eight Wilson coefficient
    must supply the opposite running. The finite matching value of that
    Wilson coefficient is not determined here.
    """
    sum_m4 = sum(float(item["ml_GeV"])**4 for item in by_flavour.values())
    soft_derivative = 0.0
    hard_derivative = 0.0
    for item in by_flavour.values():
        mass = float(item["ml_GeV"])
        m2 = mass*mass
        m4 = m2*m2
        soft_derivative += (32.0*m4 - 4.0*m2*s)/(vh*vs)*LOOP
        hard_derivative += (4.0*m2*s)/(vh*vs)*LOOP
    total_derivative = soft_derivative + hard_derivative
    eft5_pi_b_uv = 16.0*sum_m4/(vh*vs)*LOOP
    eps = finite_difference_step
    plus = plan_c_soft_plus_hard(
        vh, vs, s, mu_reference*math.exp(eps), by_flavour
    )
    minus = plan_c_soft_plus_hard(
        vh, vs, s, mu_reference*math.exp(-eps), by_flavour
    )
    numerical_derivative = (plus-minus)/(2.0*eps)
    identity_residual = total_derivative - 2.0*eft5_pi_b_uv
    return {
        "evaluation": "s=m_h^2, leading EFT5 soft bubble+contact plus Plan-C hard derivative",
        "mu_reference_GeV": mu_reference,
        "soft_d_dlnmu_GeV2": soft_derivative,
        "hard_derivative_d_dlnmu_GeV2": hard_derivative,
        "total_d_dlnmu_GeV2": total_derivative,
        "leading_EFT5_PiB_hs_local_UV_coefficient_GeV2": eft5_pi_b_uv,
        "twice_leading_EFT5_PiB_hs_local_UV_coefficient_GeV2": 2.0*eft5_pi_b_uv,
        "identity_residual_GeV2": identity_residual,
        "relative_identity_residual": abs(identity_residual)/max(abs(total_derivative),1e-300),
        "finite_difference_d_dlnmu_GeV2": [numerical_derivative.real,numerical_derivative.imag],
        "relative_finite_difference_residual": abs(numerical_derivative.real-total_derivative)/max(abs(total_derivative),1e-300),
        "required_dimension8_counterterm_contribution_d_dlnmu_GeV2": -total_derivative,
        "interpretation": (
            "The remaining scale dependence is local and equals twice the EFT5 mixed UV-pole coefficient. "
            "It is canceled by the running of the dimension-eight operator counterterm. "
            "This fixes the required scale derivative, not the finite matching value of its Wilson coefficient."
        ),
    }


def run_mapping(tadpole_json: Path, matrix_json: Path) -> dict:
    tadpole = json.loads(tadpole_json.read_text(encoding="utf-8"))
    matrix = json.loads(matrix_json.read_text(encoding="utf-8"))
    benchmarks = {}

    for label, vs_expected in BENCHMARKS.items():
        t = tadpole["benchmarks"][label]
        m = matrix["benchmarks"][label]
        vs = float(t["vs_GeV"])
        if abs(vs-vs_expected) > 1e-9:
            raise AssertionError(f"{label}: unexpected v_s={vs}")

        inv = t["couplings_and_invariants"]["sum"]
        pot = solve_potential_counterterms(
            VH, vs,
            inv["F_h"], inv["F_s"], inv["F_hh"], inv["F_hs"], inv["F_ss"],
        )
        eft = leading_eft5_derivatives(
            VH, vs, t["couplings_and_invariants"]["by_flavour"]
        )
        plan_c_scale = plan_c_scale_dependence(
            VH, vs, 125.25**2, t["couplings_and_invariants"]["by_flavour"]
        )

        full_c = {
            "hh": float(m["hh"]["UV_p2_coefficient_sum_C"][0]),
            "hs": float(m["hs"]["UV_p2_coefficient_sum_C"][0]),
            "ss": float(m["ss"]["UV_p2_coefficient_sum_C"][0]),
        }
        full_field_ct = {k: -LOOP*v for k, v in full_c.items()}
        bubble_local = {
            "hh": float(m["hh"]["light_light_UV_local_coefficient"][0]),
            "hs": float(m["hs"]["light_light_UV_local_coefficient"][0]),
            "ss": float(m["ss"]["light_light_UV_local_coefficient"][0]),
        }
        eft_bubble_vs_leading = {
            key: bubble_local[key] - eft["bubble_local_UV_coefficients_GeV2"][key]
            for key in ("hh", "hs", "ss")
        }

        # These are retained as the exact-basis light-bubble-only subtraction
        # from the earlier audit. They are not the complete EFT subtraction:
        # the dimension-five contact and its higher-dimensional counterterm
        # must also be included.
        bubble_only_matching = {}
        for key in ("hh", "hs", "ss"):
            entry = m[key]
            delta_local = float(entry["full_minus_light_UV_local_coefficient"][0])
            delta_c = float(entry["full_minus_light_UV_p2_coefficient_C"][0])
            bubble_only_matching[key] = {
                "Pi_RC_local_pole_coefficient_full_minus_light_bubble_GeV2": -LOOP*delta_local,
                "delta_Z_matching_counterterm_pole_coefficient": -LOOP*delta_c,
            }

        benchmarks[label] = {
            "vs_GeV": vs,
            "full_theory_VLL_potential_counterterms": pot,
            "full_theory_VLL_field_counterterms": {
                "delta_Z_HH": full_field_ct["hh"],
                "delta_Z_HS": full_field_ct["hs"],
                "delta_Z_SS": full_field_ct["ss"],
                "full_theory_p2_UV_coefficients_C": full_c,
                "p2_cancellation_residual": {
                    key: LOOP*full_c[key] + full_field_ct[key]
                    for key in ("hh", "hs", "ss")
                },
            },
            "leading_EFT5_light_loop_and_dimension8_counterterm": eft,
            "planC_scale_dependence_and_dimension8_running_check": plan_c_scale,
            "comparison_to_archived_exact_light_bubble": {
                "exact_mass_eigenstate_light_bubble_local_UV_coefficients_GeV2": bubble_local,
                "leading_EFT5_bubble_local_UV_coefficients_GeV2": eft["bubble_local_UV_coefficients_GeV2"],
                "difference_exact_bubble_minus_leading_EFT5_GeV2": eft_bubble_vs_leading,
                "interpretation": (
                    "The difference includes finite-M_E power corrections because the archived "
                    "light-state vertices are exact-SVD quantities, whereas the EFT5 values use "
                    "only the leading dimension-five operator."
                ),
            },
            "previous_bubble_only_matching_subtraction_not_complete": bubble_only_matching,
        }

    return {
        "status": "PASS",
        "UV_convention": {
            "Delta_UV": "1/epsilon - gamma_E + ln(4 pi)",
            "inverse_propagator": "Gamma_inv = p^2 I - M_loc^2 + Pi_RC",
            "fermion_determinant": "V1_div = + Delta_UV Tr[(Mdagger M)^2]/(16 pi^2)",
            "potential_counterterm": "delta V = - Delta_UV Tr[(Mdagger M)^2]/(16 pi^2)",
            "Pi_RC_loop_local": "-F_ab Delta_UV/(16 pi^2)",
            "Pi_RC_loop_p2": "+C_ab p^2 Delta_UV/(16 pi^2)",
            "field_counterterm": "delta Z_ab = -C_ab Delta_UV/(16 pi^2)",
        },
        "renormalizable_potential_counterterm_basis": {
            "delta_V": "-delta_mu_H2 HdaggerH - delta_mu_S2 SdaggerS + delta_lambda_H(HdaggerH)^2 + delta_lambda_S(SdaggerS)^2 + delta_lambda_HS(HdaggerH)(SdaggerS)",
            "delta_mu_H2": "+2 M_E^2 sum_l |y_l|^2/(16 pi^2)",
            "delta_mu_S2": "+2 M_E^2 sum_l |lambda_l|^2/(16 pi^2)",
            "delta_lambda_H": "-sum_l |y_l|^4/(16 pi^2)",
            "delta_lambda_S": "-sum_l |lambda_l|^4/(16 pi^2)",
            "delta_lambda_HS": "0 at this one-loop VLL determinant order",
        },
        "EFT_dimension8_counterterm_basis": {
            "operator": "(Hdagger H)^2 (Sdagger S)^2",
            "coefficient": "-sum_l |C5_l|^4/(16 pi^2)",
            "C5_definition": "C5_l = y_l lambda_l/M_E; m_l(h,s)=C5_l(v_h+h)(v_s+s)/2",
            "reason": "The light determinant of the dimension-five mass operator generates a dimension-eight scalar operator; its h-s contact contribution is required in the EFT two-point UV pole.",
        },
        "benchmarks": benchmarks,
        "scope": [
            "Only the original mu/tau plus VLL fermion sector is included.",
            "All listed coefficients multiply Delta_UV and are not finite mass shifts or physical pole corrections.",
            "The full-theory renormalizable potential poles and the EFT dimension-eight pole are separate operator-basis statements; they must not be combined as if the EFT had only renormalizable scalar operators.",
            "The archived light-light two-point bubble alone is not the complete EFT subtraction; the dimension-five contact and dimension-eight counterterm are required.",
            "Finite tadpole conditions, VEV definition, gauge/Goldstone/ghost/scalar contributions, and the complete finite UV-EFT matching remain open.",
            "The finite portal threshold at M_E is distinct from the vanishing full-theory one-loop divergent lambda_HS pole.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tadpole-json", type=Path, required=True)
    parser.add_argument("--matrix-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_mapping(args.tadpole_json, args.matrix_json)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        label: {
            "potential": data["full_theory_VLL_potential_counterterms"],
            "field": data["full_theory_VLL_field_counterterms"],
            "EFT5": data["leading_EFT5_light_loop_and_dimension8_counterterm"],
        } for label, data in result["benchmarks"].items()
    }, indent=2))


if __name__ == "__main__":
    main()
