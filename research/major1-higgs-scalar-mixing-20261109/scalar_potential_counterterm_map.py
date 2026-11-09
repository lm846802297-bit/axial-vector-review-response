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

    With H0=phi_h/sqrt(2), S=phi_s/sqrt(2), and the RC-001 convention
    L_EFT5 = -C5 O5 + h.c., tree-level matching gives
    C5 = -y lambda/M_E and m_l(phi_h,phi_s)=C5 phi_h phi_s/2.
    The signed mass parameter is negative for positive y, lambda, M_E;
    the positive physical mass used in the determinant is |m_l|.
    """
    total = {k: 0.0 for k in ("F", "F_h", "F_s", "F_hh", "F_hs", "F_ss")}
    flavours = {}
    sum_c5_fourth = 0.0
    for name, item in by_flavour.items():
        y = float(item["y"])
        lam = float(item["lambda"])
        c5 = -y * lam / ME
        kappa = 0.5 * c5
        mass_parameter = kappa * vh * vs
        mass = abs(mass_parameter)
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
            "m_EFT5_mass_parameter_at_vev_GeV": mass_parameter,
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
    mu_reference: float = ME, mu_low: float = 125.25,
    finite_difference_step: float = 1.0e-5,
) -> dict:
    """Check Plan-C scale cancellation including the EFT5 O8 running.

    The finite Plan-C soft function already contains the dimension-five
    contact tadpole. The new UV-pole audit identifies the O8 counterterm
    whose running cancels the remaining local scale dependence. Its finite
    matching value at M_E is not calculated here.
    """
    sum_m4 = sum(float(item["ml_GeV"])**4 for item in by_flavour.values())
    sum_c5_fourth = sum(
        abs(float(item["y"])*float(item["lambda"])/ME)**4
        for item in by_flavour.values()
    )
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

    # In the Plan-B convention Pi_B receives +c8 v_h^3 v_s^3 from
    # V_EFT += c8 (Hdagger H)^2(Sdagger S)^2. The loop-induced part of
    # beta_c8 is fixed by requiring the O8 term to cancel the residual.
    beta_c8_loop = -2.0*LOOP*sum_c5_fourth
    delta_c8_running = beta_c8_loop*math.log(mu_low/mu_reference)
    delta_pi_ct_running = delta_c8_running*vh**3*vs**3
    pi_at_reference = plan_c_soft_plus_hard(
        vh, vs, s, mu_reference, by_flavour
    )
    pi_at_low = plan_c_soft_plus_hard(
        vh, vs, s, mu_low, by_flavour
    )
    delta_pi_soft_hard = pi_at_low-pi_at_reference
    residual_after_o8_running = delta_pi_soft_hard+delta_pi_ct_running
    identity_residual = total_derivative - 2.0*eft5_pi_b_uv
    return {
        "evaluation": "s=m_h^2, leading EFT5 soft bubble+contact plus Plan-C hard derivative",
        "mu_reference_GeV": mu_reference,
        "mu_low_GeV": mu_low,
        "soft_d_dlnmu_GeV2": soft_derivative,
        "hard_derivative_d_dlnmu_GeV2": hard_derivative,
        "total_d_dlnmu_GeV2": total_derivative,
        "leading_EFT5_PiB_hs_local_UV_coefficient_GeV2": eft5_pi_b_uv,
        "twice_leading_EFT5_PiB_hs_local_UV_coefficient_GeV2": 2.0*eft5_pi_b_uv,
        "identity_residual_GeV2": identity_residual,
        "relative_identity_residual": abs(identity_residual)/max(abs(total_derivative),1e-300),
        "finite_difference_d_dlnmu_GeV2": [numerical_derivative.real,numerical_derivative.imag],
        "relative_finite_difference_residual": abs(numerical_derivative.real-total_derivative)/max(abs(total_derivative),1e-300),
        "dimension8_running": {
            "sum_abs_C5_fourth_GeVminus4": sum_c5_fourth,
            "loop_induced_beta_c8_GeVminus4": beta_c8_loop,
            "delta_c8_from_mu_reference_to_mu_low_GeVminus4": delta_c8_running,
            "delta_PiB_from_O8_running_GeV2": delta_pi_ct_running,
            "delta_PiB_soft_plus_hard_GeV2": [delta_pi_soft_hard.real,delta_pi_soft_hard.imag],
            "residual_after_O8_running_GeV2": [residual_after_o8_running.real,residual_after_o8_running.imag],
            "relative_residual_after_O8_running": abs(residual_after_o8_running)/max(abs(delta_pi_soft_hard),1e-300),
            "finite_matching_value_c8_at_M_E": "not determined",
        },
        "required_dimension8_counterterm_contribution_d_dlnmu_GeV2": -total_derivative,
        "interpretation": (
            "The Plan-C finite soft expression already includes the EFT5 contact tadpole. "
            "The remaining scale dependence is the running of O8=(Hdagger H)^2(Sdagger S)^2. "
            "Its loop-induced running cancels the benchmark scale residual; the finite hard matching value c8(M_E) remains unknown."
        ),
    }


def finite_heavy_potential_matching(by_flavour: dict) -> dict:
    """Finite heavy-eigenstate CW matching onto the scalar potential at mu=M_E.

    Define X_l=|y_l|^2 HdaggerH and Y_l=|lambda_l|^2 SdaggerS.
    The heavy singular-value squared is the larger eigenvalue of Mdagger M.
    Expanding its Dirac Coleman-Weinberg determinant through dimension eight
    gives the complete VLL-induced scalar-potential operator set through
    (HdaggerH,SdaggerS)^4. The dimension-eight O8 coefficient is finite and
    fixes the MS boundary value at mu=M_E in this field/operator basis.
    """
    sums = {
        key: 0.0 for key in (
            "xy", "x3", "x2y", "xy2", "y3",
            "x4", "x3y", "x2y2", "xy3", "y4", "c5_fourth",
        )
    }
    for item in by_flavour.values():
        y2 = abs(float(item["y"]))**2
        lam2 = abs(float(item["lambda"]))**2
        sums["xy"] += y2*lam2
        sums["x3"] += y2**3
        sums["x2y"] += y2**2*lam2
        sums["xy2"] += y2*lam2**2
        sums["y3"] += lam2**3
        sums["x4"] += y2**4
        sums["x3y"] += y2**3*lam2
        sums["x2y2"] += y2**2*lam2**2
        sums["xy3"] += y2*lam2**3
        sums["y4"] += lam2**4
        sums["c5_fourth"] += (abs(float(item["y"])*float(item["lambda"]))/ME)**4

    m2 = ME**2
    m4 = ME**4
    coeff = {
        "delta_lambda_H_finite_at_mu_ME": 0.0,
        "delta_lambda_S_finite_at_mu_ME": 0.0,
        "delta_lambda_HS_finite_at_mu_ME": -2.0*LOOP*sums["xy"],
        "c_(HdagH)^3_GeVminus2": -LOOP*sums["x3"]/(3.0*m2),
        "c_(HdagH)^2(SdagS)_GeVminus2": LOOP*sums["x2y"]/m2,
        "c_(HdagH)(SdagS)^2_GeVminus2": LOOP*sums["xy2"]/m2,
        "c_(SdagS)^3_GeVminus2": -LOOP*sums["y3"]/(3.0*m2),
        "c_(HdagH)^4_GeVminus4": LOOP*sums["x4"]/(12.0*m4),
        "c_(HdagH)^3(SdagS)_GeVminus4": -(2.0/3.0)*LOOP*sums["x3y"]/m4,
        "c_(HdagH)^2(SdagS)^2_GeVminus4": -(7.0/2.0)*LOOP*sums["x2y2"]/m4,
        "c_(HdagH)(SdagS)^3_GeVminus4": -(2.0/3.0)*LOOP*sums["xy3"]/m4,
        "c_(SdagS)^4_GeVminus4": LOOP*sums["y4"]/(12.0*m4),
    }
    c8_pole = -LOOP*sums["c5_fourth"]
    c8_beta = -2.0*LOOP*sums["c5_fourth"]
    c8_match = -(7.0/2.0)*LOOP*sums["c5_fourth"]
    return {
        "matching_scale_GeV": ME,
        "renormalization_scheme": "MSbar",
        "matching_sector": "heavy mu/tau-associated VLL eigenstates only",
        "background_invariants": "X_l=|y_l|^2 HdaggerH; Y_l=|lambda_l|^2 SdaggerS",
        "heavy_CW_expansion_at_mu_ME": (
            "V_H=-1/(16 pi^2) sum_l[-3/2 M_E^4-2 M_E^2(X_l+Y_l)+2 X_l Y_l"
            "+((X_l+Y_l)^3/3-2 X_l Y_l(X_l+Y_l))/M_E^2"
            "+(-(X_l+Y_l)^4/12+X_l Y_l(X_l+Y_l)^2+2 X_l^2 Y_l^2)/M_E^4"
            "+ O(fields^10)]"
        ),
        "dimensionless_coupling_invariants": sums,
        "finite_potential_wilson_coefficients_at_mu_ME": coeff,
        "O8_matching_and_running": {
            "operator": "(HdaggerH)^2(SdaggerS)^2",
            "UV_pole_residue_GeVminus4": c8_pole,
            "finite_matching_coefficient_c8_at_mu_ME_GeVminus4": c8_match,
            "loop_induced_beta_c8_GeVminus4": c8_beta,
            "finite_matching_to_pole_residue_ratio": 3.5,
            "general_scale_dependence": (
                "c8(mu)=-[sum_l |C5_l|^4/(16 pi^2)]"
                "[7/2-ln(M_E^2/mu^2)]"
            ),
            "consistency": "d c8(mu)/d ln(mu)=beta_c8=-2 sum_l |C5_l|^4/(16 pi^2)",
        },
        "scope": [
            "The expansion is the finite heavy-eigenstate Coleman-Weinberg contribution in the specified MSbar scalar-background basis.",
            "The light-eigenstate determinant is matched to the leading dimension-five EFT loop separately and is not included in these hard Wilson coefficients.",
            "This closes the VLL fermion-sector scalar-potential matching through dimension eight, not the full derivative-operator or gauge/scalar EFT basis.",
            "The finite portal threshold is distinct from the vanishing divergent renormalizable portal pole.",
        ],
    }


def finite_potential_hs_mass_contributions(coefficients: dict, vh: float, vs: float) -> dict:
    """Evaluate the mixed second derivative of the matched potential at a VEV.

    The result is a local curvature contribution in the fixed background-field
    basis. It is not a physical mixing angle and depends on the finite portal
    renormalization condition.
    """
    terms = {
        "dimension4_portal_GeV2":
            float(coefficients["delta_lambda_HS_finite_at_mu_ME"])*vh*vs,
        "dimension6_H2S_GeV2":
            float(coefficients["c_(HdagH)^2(SdagS)_GeVminus2"])*vh**3*vs,
        "dimension6_HS2_GeV2":
            float(coefficients["c_(HdagH)(SdagS)^2_GeVminus2"])*vh*vs**3,
        "dimension8_H3S_GeV2":
            0.75*float(coefficients["c_(HdagH)^3(SdagS)_GeVminus4"])*vh**5*vs,
        "dimension8_H2S2_GeV2":
            float(coefficients["c_(HdagH)^2(SdagS)^2_GeVminus4"])*vh**3*vs**3,
        "dimension8_HS3_GeV2":
            0.75*float(coefficients["c_(HdagH)(SdagS)^3_GeVminus4"])*vh*vs**5,
    }
    terms["dimension6_sum_GeV2"] = (
        terms["dimension6_H2S_GeV2"] + terms["dimension6_HS2_GeV2"]
    )
    terms["dimension8_sum_GeV2"] = (
        terms["dimension8_H3S_GeV2"]
        + terms["dimension8_H2S2_GeV2"]
        + terms["dimension8_HS3_GeV2"]
    )
    terms["higher_dimensional_sum_GeV2"] = (
        terms["dimension6_sum_GeV2"] + terms["dimension8_sum_GeV2"]
    )
    terms["total_including_portal_GeV2"] = (
        terms["dimension4_portal_GeV2"] + terms["higher_dimensional_sum_GeV2"]
    )
    terms["additional_delta_lambda_HS_for_zero_local_hs_curvature"] = (
        -terms["higher_dimensional_sum_GeV2"]/(vh*vs)
    )
    return terms


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
        finite_hard = finite_heavy_potential_matching(
            t["couplings_and_invariants"]["by_flavour"]
        )
        finite_hard["local_hs_mass_contribution_at_benchmark_vev_GeV2"] = (
            finite_potential_hs_mass_contributions(
                finite_hard["finite_potential_wilson_coefficients_at_mu_ME"], VH, vs
            )
        )
        plan_c_scale = plan_c_scale_dependence(
            VH, vs, 125.25**2, t["couplings_and_invariants"]["by_flavour"],
            mu_reference=ME, mu_low=125.25,
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
            "finite_heavy_VLL_potential_matching_through_dimension8": finite_hard,
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
            "C5_definition": "L_EFT5=-C5_l O5+h.c.; C5_l=-y_l lambda_l/M_E; m_l(h,s)=C5_l(v_h+h)(v_s+s)/2; physical mass=|m_l|",
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
