#!/usr/bin/env python3
"""Reproduce the illustrative Plan-B low-energy mu/tau h-s mixing estimate.

This is NOT a full UV prediction. It keeps only the light, flavor-diagonal
Dirac-fermion bubble and the EFT hs lbar-l contact tadpole. The real part of
the mixed self-energy depends on the local portal/matching conditions.
"""
from math import log, pi, sqrt

MH = 125.25       # GeV; reference Higgs pole mass used for this estimate
VH = 246.22       # GeV
M_LEPTON = {"mu": 0.1056583755, "tau": 1.77686}  # GeV
LAMBDA_S_MAX = 4.0 * pi
MU_SUB = MH


def beta(s, m):
    return sqrt(max(0.0, 1.0 - 4.0 * m * m / s))


def b0_difference(s, m):
    """B0(s;m,m)-B0(0;m,m), for s > 4 m^2 and the stated +i0 convention."""
    b = beta(s, m)
    return complex(2.0 - b * log((1.0 + b) / (1.0 - b)), pi * b)


def a0_finite(m, mu=MU_SUB):
    """A0 finite part in the convention A0=m^2(Delta+1-ln(m^2/mu^2))."""
    return m * m * (1.0 - log(m * m / (mu * mu)))


def b0_finite(s, m, mu=MU_SUB):
    """B0 finite part for s > 4 m^2 with the +i0 convention."""
    b = beta(s, m)
    return complex(
        -log(m * m / (mu * mu)) + 2.0 - b * log((1.0 + b) / (1.0 - b)),
        pi * b,
    )


def vs_min_from_scalar_perturbativity(ms, lambda_s_max=LAMBDA_S_MAX):
    # m_s^2 = 2 lambda_S v_s^2, hence v_s >= m_s/sqrt(2 lambda_S^max).
    return ms / sqrt(2.0 * lambda_s_max)


def pi_mom_light_bubble(s, vs):
    """MOM benchmark: Pi(0)=Pi'(0)=0; removes local mass and kinetic mixing."""
    total = 0j
    pieces = {}
    for name, m in M_LEPTON.items():
        # F(s)-F(0)-s F'(0) = (8 m^2 - 2 s) [B0(s)-B0(0)] - 4s/3.
        residual = (8.0 * m * m - 2.0 * s) * b0_difference(s, m) - 4.0 * s / 3.0
        value = (m * m / (VH * vs)) * residual / (16.0 * pi * pi)
        pieces[name] = value
        total += value
    return total, pieces


def pi_ms_light_bubble_plus_contact(s, vs, mu=MU_SUB):
    """MS-bar-like EFT benchmark, with local portal and derivative coefficients
    set to zero at mu. Includes the hs lbar-l contact tadpole from the dim-5
    operator. The finite real part is conditional on this matching choice.
    """
    total = 0j
    bubble_pieces = {}
    contact_pieces = {}
    for name, m in M_LEPTON.items():
        yprod = m * m / (VH * vs)
        f_bubble = 4.0 * a0_finite(m, mu) + 2.0 * (4.0 * m * m - s) * b0_finite(s, m, mu)
        bubble = yprod * f_bubble / (16.0 * pi * pi)
        # L_EFT contains -[m/(v_h v_s)] h s lbar-l, yielding this tadpole.
        contact = 4.0 * m**4 / (VH * vs) * (1.0 - log(m * m / (mu * mu))) / (16.0 * pi * pi)
        bubble_pieces[name] = bubble
        contact_pieces[name] = complex(contact, 0.0)
        total += bubble + contact
    return total, bubble_pieces, contact_pieces


def gamma_s_to_AA(ms, vs, mA):
    if 2.0 * mA >= ms:
        return 0.0
    x = (mA / ms) ** 2
    return ms**3 / (32.0 * pi * vs**2) * (1.0 - 4.0*x + 12.0*x*x) * sqrt(1.0 - 4.0*x)


def gamma_s_to_ll(ms, vs, ml):
    if 2.0 * ml >= ms:
        return 0.0
    return ml**2 * ms / (8.0 * pi * vs**2) * (1.0 - 4.0*ml**2/ms**2)**1.5


def main():
    print(f"inputs: m_h={MH:.2f} GeV, v_h={VH:.2f} GeV, lambda_S^max=4 pi")
    print("assumption: v_s is minimized point-by-point by scalar-quartic perturbativity")
    print("columns: ms, vs_min, |Pi_MOM|, rho_MOM, |Pi_MS+contact|, rho_MS+contact")
    for ms in (10, 50, 100, 120, 124, 125, 125.25, 126, 130, 150):
        vs = vs_min_from_scalar_perturbativity(ms)
        s = MH * MH
        pi_mom, _ = pi_mom_light_bubble(s, vs)
        pi_ms, _, _ = pi_ms_light_bubble_plus_contact(s, vs, MU_SUB)
        denom = abs(MH*MH - ms*ms)
        rho_mom = abs(pi_mom) / denom if denom else float("inf")
        rho_ms = abs(pi_ms) / denom if denom else float("inf")
        print(f"{ms:7.2f} {vs:9.3f} {abs(pi_mom):12.5g} {rho_mom:12.5g} "
              f"{abs(pi_ms):16.5g} {rho_ms:12.5g}")

    ms = MH
    vs = vs_min_from_scalar_perturbativity(ms)
    pi_mom, pieces_mom = pi_mom_light_bubble(MH*MH, vs)
    pi_ms, pieces_ms, contacts_ms = pi_ms_light_bubble_plus_contact(MH*MH, vs, MU_SUB)
    print("\nAt ms=mh and scalar-quartic-only v_s minimum:")
    print(f"  v_s_min = {vs:.5f} GeV")
    print(f"  Pi_MOM = {pi_mom.real:.6g} {pi_mom.imag:+.6g} i GeV^2")
    print(f"  Pi_MS+contact(mu=mh) = {pi_ms.real:.6g} {pi_ms.imag:+.6g} i GeV^2")
    print(f"  MOM |Pi| gives the small-angle diagnostic rho=0.1 at |ms-mh| ~ {5*abs(pi_mom)/MH*1000:.2f} MeV")
    print(f"  MS  |Pi| gives the small-angle diagnostic rho=0.1 at |ms-mh| ~ {5*abs(pi_ms)/MH*1000:.2f} MeV")
    print("  These bands are only diagnostics; widths and the full complex propagator are required near degeneracy.")

    print("\nAt ms=mh, v_s=v_s_min, singlet widths from the manuscript formulas:")
    for mA in (10.0, 63.0):
        gaa = gamma_s_to_AA(ms, vs, mA)
        gtau = gamma_s_to_ll(ms, vs, M_LEPTON["tau"])
        gmu = gamma_s_to_ll(ms, vs, M_LEPTON["mu"])
        print(f"  mA={mA:5.1f} GeV: Gamma_AA={gaa:.5g}, Gamma_tautau={gtau:.5g}, "
              f"Gamma_mumu={gmu:.5g}, sum={gaa+gtau+gmu:.5g} GeV")

    # Optional extra condition not imposed in the original manuscript:
    # |lambda_tau| <= sqrt(4pi), |theta_tauR| <= 1e-2.
    vs_yuk = sqrt(2.0) * M_LEPTON["tau"] / (1.0e-2 * sqrt(4.0*pi))
    pi_mom_yuk, _ = pi_mom_light_bubble(MH*MH, vs_yuk)
    pi_ms_yuk, _, _ = pi_ms_light_bubble_plus_contact(MH*MH, vs_yuk, MU_SUB)
    print("\nOptional extra Yukawa-perturbativity benchmark (not in original paper):")
    print(f"  v_s >= {vs_yuk:.3f} GeV from |lambda_tau|<=sqrt(4pi) and |theta_tauR|<=1e-2")
    print(f"  at ms=mh: |Pi_MOM|={abs(pi_mom_yuk):.5g}, |Pi_MS+contact|={abs(pi_ms_yuk):.5g} GeV^2")


if __name__ == "__main__":
    main()
