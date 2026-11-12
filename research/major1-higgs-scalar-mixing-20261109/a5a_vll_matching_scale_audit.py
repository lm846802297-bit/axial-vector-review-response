#!/usr/bin/env python3
"""A5a provenance and scale audit for the 20 TeV VLL benchmark.

Checks:
  * conditional lower bound from m_tau ~= theta_tauL theta_tauR M_E;
  * exact heavy singular values of the benchmark 2x2 charged-lepton/VLL matrix;
  * logarithms between the input M_E and physical heavy singular values;
  * hard derivative logarithm at mu_R=M_E and mu_R=m_h;
  * archived Plan-C-lite partial hard+soft scale comparison.

The archived total-scale comparison is a diagnostic only: the complete same-order
EFT soft/counterterm closure is not yet established. No matching-scale uncertainty
is inferred from this script.
"""
from math import log, pi, sqrt
import numpy as np

ME = 20_000.0  # GeV, benchmark Dirac mass parameter
THETA_L = 1.0e-2
M_MU = 0.1056583755
M_TAU = 1.77686
V_H = 246.22
M_H = 125.25

BENCHMARKS = {
    "A": {
        "vS": 70.886458,
        "Pi_total_muR_ME": -0.413263168,
        "Pi_total_muR_mh": -0.413850308,
    },
    "B": {
        "vS": 315.0,
        "Pi_total_muR_ME": -0.092999245,
        "Pi_total_muR_mh": -0.093131373,
    },
}

def mass_matrix_and_singular_values(m_lepton):
    theta_R = m_lepton / (ME * THETA_L)
    # The leading-seesaw benchmark fixes the off-diagonal entries:
    # y v_H/sqrt(2)=M_E theta_L; lambda v_S/sqrt(2)=m_l/theta_L.
    matrix = np.array([
        [0.0, ME * THETA_L],
        [m_lepton / THETA_L, ME],
    ], dtype=float)
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    heavy, light = float(singular_values[0]), float(singular_values[1])
    return theta_R, light, heavy

def q_coefficient(vS):
    return 2.0 * (M_MU**2 + M_TAU**2) / (V_H * vS)

def hard_derivative_times_mh2(vS, muR):
    q = q_coefficient(vS)
    log_term = log(ME**2 / muR**2)
    # Plan-C / Pi_B convention: Pi'_B = -q/(16 pi^2) [log(M_E^2/mu_R^2)-2/3].
    derivative = -q / (16.0 * pi**2) * (log_term - 2.0/3.0)
    return M_H**2 * derivative

def main():
    print("A5a VLL matching-scale provenance audit")
    print(f"Input M_E = {ME:.6f} GeV; theta_L = {THETA_L:.8g}")
    print(f"Conditional theta_tauL,theta_tauR <= 1e-2 lower bound: "
          f"M_E >= {M_TAU/THETA_L**2/1000.0:.7f} TeV")
    theta_tau_R = M_TAU / (ME * THETA_L)
    print(f"At M_E=20 TeV: theta_tauR = {theta_tau_R:.10f}")
    assert theta_tau_R <= THETA_L
    assert ME/1000.0 > M_TAU/THETA_L**2/1000.0

    print("\nExact SVD heavy thresholds")
    for flavor, ml in (("mu", M_MU), ("tau", M_TAU)):
        theta_R, light, heavy = mass_matrix_and_singular_values(ml)
        threshold_log = log(heavy**2 / ME**2)
        print(
            f"{flavor}: theta_R={theta_R:.10g}, m_light={light:.9f} GeV, "
            f"m_heavy={heavy:.9f} GeV, "
            f"(m_heavy-M_E)/M_E={(heavy/ME-1.0):.9e}, "
            f"ln(m_heavy^2/M_E^2)={threshold_log:.9e}"
        )
        assert abs(heavy - (ME + (1.00276550555 if flavor == "mu" else 1.78914892189))) < 2e-6
        assert abs(threshold_log) < 2e-4

    L_h = log(ME**2 / M_H**2)
    print("\nHard derivative logarithm")
    print(f"ln(M_E^2/m_h^2) = {L_h:.12f}")
    print(f"ln(M_E^2/mu_R^2) at mu_R=M_E = 0")
    print("ln(M_E^2/mu_R^2) at mu_R=m_h is large; evaluate hard matching at the threshold")
    print("\nBenchmark hard derivative contribution s*Pi'_B(s=0)")
    for name, pars in BENCHMARKS.items():
        vs = pars["vS"]
        at_threshold = hard_derivative_times_mh2(vs, ME)
        at_higgs = hard_derivative_times_mh2(vs, M_H)
        print(
            f"{name}: mu_R=M_E -> {at_threshold:+.12e} GeV^2; "
            f"mu_R=m_h -> {at_higgs:+.12e} GeV^2; "
            f"hard shift = {at_higgs-at_threshold:+.12e} GeV^2"
        )

    print("\nArchived Plan-C-lite partial hard+soft scale comparison")
    for name, pars in BENCHMARKS.items():
        p_me = pars["Pi_total_muR_ME"]
        p_mh = pars["Pi_total_muR_mh"]
        diff = p_mh - p_me
        rel = abs(diff / p_me)
        print(
            f"{name}: Pi_total(mu_R=M_E)={p_me:+.9f} GeV^2; "
            f"Pi_total(mu_R=m_h)={p_mh:+.9f} GeV^2; "
            f"delta={diff:+.9e} GeV^2 ({100*rel:.6f}%)"
        )
        assert abs(rel - 0.00142074) < 2e-6

    print("\nMatching-scale variation bookkeeping")
    for muM in (ME/2.0, ME, 2.0*ME):
        print(
            f"mu_M={muM/1000.0:5.1f} TeV: "
            f"ln(M_E^2/mu_M^2)={log(ME**2/muM**2):+.9f}"
        )
    print("These logarithms are diagnostics only; the mu_M scan is not a physical uncertainty")
    print("until all EFT beta functions, threshold matching, and RG evolution are included.")

    print("\nPASS: 20 TeV is consistent with the conditional tau-mixing bound.")
    print("PASS: the physical heavy singular values lie within 1.8 GeV of the 20 TeV input.")
    print("PASS: mu_R=M_E removes the large heavy-threshold logarithm in the hard coefficient.")
    print("LIMIT: the archived 0.14% total-scale residual is not a complete RG/matching-scale test.")

if __name__ == "__main__":
    main()
