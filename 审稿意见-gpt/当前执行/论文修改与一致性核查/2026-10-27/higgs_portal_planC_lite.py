#!/usr/bin/env python3
"""Plan C-lite: conditional portal matching and complex h-s pole diagnostics.

This script implements a deliberately scoped benchmark:
- degenerate vector-like lepton mass M_E;
- leading seesaw relations for Yukawas and mixing angles;
- the recorded one-loop zero-momentum portal threshold;
- the source-recorded finite derivative coefficient, with its sign converted
  from the RC-001 inverse-propagator convention to the Plan-B convention;
- the Plan-B low-energy mu/tau bubble plus EFT contact tadpole;
- complex poles from a 2x2 inverse propagator, retaining the p^2 dependence
  of the off-diagonal light-lepton self-energy on the second sheet.

It is NOT a full UV model prediction or an experimental recast. In particular,
the finite derivative coefficient is an existing source-aligned matching
result whose complete independent diagram-level validation remains open.
The diagonal real self-energies are absorbed into the benchmark masses and the
diagonal widths are held constant over each pole pair. The results are therefore
first-pass complex-pole diagnostics, not final HiggsSignals/lineshape limits.
Requires Python 3 only.
"""
from math import log, pi, sqrt, atan
import cmath

MH = 125.25
VH = 246.22
GAMMA_H_SM = 0.00407  # GeV; reference SM Higgs total width
M_LEPTON = {"mu": 0.1056583755, "tau": 1.77686}  # GeV
M_E = 20_000.0  # GeV; illustrative degenerate VLL benchmark
THETA_L = 1.0e-2
LAMBDA_MAX = sqrt(4.0 * pi)
MU_MATCH = M_E


def beta_real(s, m):
    return sqrt(max(0.0, 1.0 - 4.0 * m * m / s))


def a0_finite(m, mu):
    return m * m * (1.0 - log(m * m / (mu * mu)))


def b0_finite_real(s, m, mu):
    """B0 finite part for real s > 4 m^2, with Im B0 = +pi beta."""
    b = beta_real(s, m)
    return complex(
        -log(m * m / (mu * mu)) + 2.0 - b * log((1.0 + b) / (1.0 - b)),
        pi * b,
    )


def b0_finite_second_sheet(s, m, mu):
    """Analytic continuation to the resonance sheet near the positive real axis."""
    b = cmath.sqrt(1.0 - 4.0 * m * m / s)
    return (
        -log(m * m / (mu * mu))
        + 2.0
        - b * cmath.log((1.0 + b) / (1.0 - b))
        + 1j * pi * b
    )


def coupling_inputs(vs):
    """Leading seesaw benchmark satisfying theta_L,R <= 1e-2."""
    theta_r = {name: mass / (M_E * THETA_L) for name, mass in M_LEPTON.items()}
    yukawa_y = {name: sqrt(2.0) * M_E * THETA_L / VH for name in M_LEPTON}
    yukawa_lam = {
        name: sqrt(2.0) * M_E * theta_r[name] / vs for name in M_LEPTON
    }
    products = {
        name: yukawa_y[name] * yukawa_lam[name] for name in M_LEPTON
    }
    delta_lambda = -sum(abs(value) ** 2 for value in products.values()) / (8.0 * pi**2)
    return theta_r, yukawa_y, yukawa_lam, products, delta_lambda


def q_sum(vs):
    """Leading source coefficient q_l ~= 2 m_l^2/(v_h v_s)."""
    return sum(2.0 * mass**2 / (VH * vs) for mass in M_LEPTON.values())


def pi_soft_planb(s, vs, mu):
    """Low-energy bubble plus dimension-five contact tadpole in Plan-B convention."""
    total = 0j
    pieces = {}
    for name, mass in M_LEPTON.items():
        yprod = mass * mass / (VH * vs)
        b0 = (
            b0_finite_real(s, mass, mu)
            if isinstance(s, (int, float))
            else b0_finite_second_sheet(s, mass, mu)
        )
        bubble = yprod * (
            4.0 * a0_finite(mass, mu)
            + 2.0 * (4.0 * mass * mass - s) * b0
        ) / (16.0 * pi**2)
        contact = (
            4.0 * mass**4 / (VH * vs)
            * (1.0 - log(mass * mass / (mu * mu)))
            / (16.0 * pi**2)
        )
        pieces[name] = bubble + contact
        total += pieces[name]
    return total, pieces


def pi_hard_derivative_planb(s, vs, mu):
    """Candidate finite derivative matching, sign-converted from RC-001.

    RC-001 uses Gamma_inv = s I - M_loc^2 + Pi_RC and
    Pi_RC'(0)=q/(16 pi^2)[ln(M_E^2/mu^2)-2/3].
    Plan B defines the 1PI amplitude as -i Pi_B, hence Pi_B=-Pi_RC.
    """
    log_ratio = log(M_E * M_E / (mu * mu))
    pi_prime = -q_sum(vs) / (16.0 * pi**2) * (log_ratio - 2.0 / 3.0)
    return pi_prime * s


def pi_matched_planb(s, vs, mu=MU_MATCH):
    """Matched off-diagonal self-energy under lambda_HS^EFT(M_E)=0."""
    soft, _ = pi_soft_planb(s, vs, mu)
    hard_derivative = pi_hard_derivative_planb(s, vs, mu)
    # The dimension-four threshold is already absorbed in lambda_HS^EFT=0.
    # Do not add its hard constant a second time.
    return soft + hard_derivative


def gamma_s_to_aa(ms, vs, m_a):
    if 2.0 * m_a >= ms:
        return 0.0
    x = (m_a / ms) ** 2
    return (
        ms**3 / (32.0 * pi * vs**2)
        * (1.0 - 4.0 * x + 12.0 * x * x)
        * sqrt(1.0 - 4.0 * x)
    )


def gamma_s_to_ll(ms, vs, mass):
    if 2.0 * mass >= ms:
        return 0.0
    return (
        mass**2 * ms / (8.0 * pi * vs**2)
        * (1.0 - 4.0 * mass**2 / ms**2) ** 1.5
    )


def gamma_s_total(ms, vs, m_a):
    return gamma_s_to_aa(ms, vs, m_a) + sum(
        gamma_s_to_ll(ms, vs, mass) for mass in M_LEPTON.values()
    )


def complex_poles(ms, vs, m_a):
    """Solve det D^{-1}(s)=0 with p^2-dependent off-diagonal Pi(s).

    The diagonal inverse kernels are approximated as s-m^2+i m Gamma with
    on-shell real masses and fixed widths. The off-diagonal self-energy is
    evaluated on the resonance sheet; Newton iteration starts from constant-Pi
    roots. This is a controlled first-pass diagnostic, not a full pole scheme.
    """
    gamma_s = gamma_s_total(ms, vs, m_a)
    a = MH**2 - 1j * MH * GAMMA_H_SM
    b = ms**2 - 1j * ms * gamma_s

    def determinant(s):
        pi_hs = pi_matched_planb(s, vs, MU_MATCH)
        return (s - a) * (s - b) - pi_hs * pi_hs

    s_ref = (MH**2 + ms**2) / 2.0
    pi0 = pi_matched_planb(s_ref, vs, MU_MATCH)
    half_difference = (a - b) / 2.0
    split = cmath.sqrt(half_difference * half_difference + pi0 * pi0)
    guesses = [(a + b) / 2.0 + split, (a + b) / 2.0 - split]

    results = []
    for guess in guesses:
        z = guess
        for _ in range(60):
            fz = determinant(z)
            step = 1.0e-4 + 1.0e-6j
            derivative = (determinant(z + step) - determinant(z - step)) / (2.0 * step)
            if abs(derivative) < 1.0e-20:
                break
            dz = fz / derivative
            z -= dz
            if abs(dz) < 1.0e-10:
                break
        pole_mass = cmath.sqrt(z)
        if pole_mass.real < 0:
            pole_mass = -pole_mass
        pi_at_pole = pi_matched_planb(z, vs, MU_MATCH)
        # For (s-a) h - Pi s = 0, the eigenvector ratio is s/h=(s_p-a)/Pi.
        s_over_h = (z - a) / pi_at_pole if abs(pi_at_pole) else complex(float("inf"))
        results.append({
            "mass": pole_mass.real,
            "width": -2.0 * pole_mass.imag,
            "s": z,
            "residual": abs(determinant(z)),
            "pi": pi_at_pole,
            "s_over_h": s_over_h,
        })
    return gamma_s, sorted(results, key=lambda item: item["width"])


def lambda_s(ms, vs):
    return ms * ms / (2.0 * vs * vs)


def lambda_h_sm():
    return MH * MH / (2.0 * VH * VH)


def stability_lower_bound(ms, vs):
    return -2.0 * sqrt(lambda_h_sm() * lambda_s(ms, vs))


def zero_uv_portal_comparator(ms, vs, delta_lambda):
    """Tree-level diagnostic if lambda_HS^UV=0, so lambda_HS^EFT=Delta lambda."""
    offdiag = delta_lambda * VH * vs
    denominator = MH * MH - ms * ms
    if abs(denominator) < 1.0e-12:
        theta_abs = pi / 4.0
        tan2 = float("inf")
    else:
        tan2 = 2.0 * offdiag / denominator
        theta_abs = 0.5 * abs(cmath.phase(complex(denominator, 2.0 * offdiag)))
    return offdiag, tan2, theta_abs


def main():
    vs_min = sqrt(2.0) * M_LEPTON["tau"] / (THETA_L * LAMBDA_MAX)
    benchmarks = [
        {"label": "open A-prime channel", "vs": vs_min, "mA": 10.0},
        {"label": "closed A-prime channel", "vs": 315.0, "mA": 63.0},
    ]

    print("Plan C-lite benchmark calculation")
    print(f"m_h={MH:.5f} GeV, v_h={VH:.5f} GeV, M_E={M_E:.1f} GeV")
    print(f"theta_L={THETA_L:.5g}, |lambda|_max=sqrt(4 pi)={LAMBDA_MAX:.6f}")
    print("Reference matching: lambda_HS^EFT(M_E)=0; lambda_HS^UV=-Delta lambda_HS.")
    print("The finite derivative coefficient is a source-aligned candidate, not final UV closure.")
    print()

    for bench in benchmarks:
        vs, m_a = bench["vs"], bench["mA"]
        theta_r, y, lam, products, delta_lambda = coupling_inputs(vs)
        gx = m_a / (2.0 * vs)
        print(f"BENCHMARK: {bench['label']}")
        print(f"  m_A={m_a:.6g} GeV, g_X={gx:.8g}, v_s={vs:.8g} GeV")
        print(f"  theta_R(mu)={theta_r['mu']:.8g}, theta_R(tau)={theta_r['tau']:.8g}")
        print(f"  y_mu=y_tau={y['tau']:.8g}")
        print(f"  lambda_mu={lam['mu']:.8g}, lambda_tau={lam['tau']:.8g}")
        print(f"  y_lambda products: mu={products['mu']:.8g}, tau={products['tau']:.8g}")
        print(f"  Delta lambda_HS^E={delta_lambda:.9g}")
        print(f"  lambda_HS^UV for lambda_HS^EFT=0: {-delta_lambda:.9g}")
        print(f"  q_sum={q_sum(vs):.9g}")
        print(f"  candidate c_partialHS (RC convention, mu=M_E)="
              f"{M_E**2 * (-q_sum(vs)/(16*pi**2)*(-2.0/3.0))/(VH*vs):.9g}")
        print(f"  lambda_S at m_s=m_h={lambda_s(MH, vs):.8g}")
        soft, _ = pi_soft_planb(MH**2, vs, M_E)
        hard = pi_hard_derivative_planb(MH**2, vs, M_E)
        total = soft + hard
        print(f"  Pi_soft(mu=M_E)={soft.real:.9g}{soft.imag:+.9g}i GeV^2")
        print(f"  Pi_hard_derivative(mu=M_E)={hard.real:.9g}{hard.imag:+.9g}i GeV^2")
        print(f"  Pi_total(mu=M_E)={total.real:.9g}{total.imag:+.9g}i GeV^2")
        soft_low, _ = pi_soft_planb(MH**2, vs, MH)
        hard_low = pi_hard_derivative_planb(MH**2, vs, MH)
        total_low = soft_low + hard_low
        print(f"  scale check total(mu=m_h)={total_low.real:.9g}{total_low.imag:+.9g}i")
        print(f"  scale residual |Re[Pi(mu=m_h)-Pi(mu=M_E)]|="
              f"{abs(total_low.real-total.real):.6g} GeV^2 (contact/higher-order matching remains open)")
        gamma_s, poles = complex_poles(MH, vs, m_a)
        a = MH**2 - 1j * MH * GAMMA_H_SM
        b = MH**2 - 1j * MH * gamma_s
        pi_at_ref = pi_matched_planb(MH**2, vs, M_E)
        complex_ratio = abs(pi_at_ref) / abs(a - b)
        print(f"  Gamma_s(m_h)={gamma_s:.9g} GeV")
        print(f"  complex mixing diagnostic |Pi/(a-b)|={complex_ratio:.9g}")
        print(f"  complex-pole proxy 2|Pi/(a-b)|={2.0*complex_ratio:.9g}")
        for pole in poles:
            print(f"    pole: m={pole['mass']:.9f} GeV, Gamma={pole['width']*1000.0:.6f} MeV, "
                  f"|F|={pole['residual']:.3g}, |s/h|={abs(pole['s_over_h']):.6g}")
        print("  near-degenerate pole rows (poles sorted by width):")
        for ms in (124.5, 125.0, 125.25, 125.5, 125.9):
            gs, row_poles = complex_poles(ms, vs, m_a)
            row = "; ".join(
                f"({p['mass']:.6f} GeV, {p['width']*1000.0:.4f} MeV)"
                for p in row_poles
            )
            print(f"    m_s={ms:.2f} GeV, Gamma_s={gs:.6g} GeV: {row}")
        band, tan2_exact, delta_im, target = near_degenerate_band(vs, m_a)
        if band is None:
            print(f"  |tan(2 theta_complex)|<0.1 throughout the width-regulated exact-degeneracy diagnostic "
                  f"(value at degeneracy={tan2_exact:.6g})")
        else:
            print(f"  |tan(2 theta_complex)|>=0.1 band estimate: |m_s-m_h|<={band:.4f} MeV")
        for ms in (10.0, MH):
            offdiag, tan2, theta_abs = zero_uv_portal_comparator(ms, vs, delta_lambda)
            stable = delta_lambda > stability_lower_bound(ms, vs)
            print(f"  zero-UV-portal comparator at m_s={ms:g} GeV: "
                  f"lambda_EFT={delta_lambda:.7g}, M_hs^2={offdiag:.7g} GeV^2, "
                  f"bounded-from-below={stable}, tan2theta={tan2}")
        print()


def near_degenerate_band(vs, m_a, threshold=0.1):
    pi_at_ref = pi_matched_planb(MH**2, vs, M_E)
    gs = gamma_s_total(MH, vs, m_a)
    delta_im = abs(MH * GAMMA_H_SM - MH * gs)
    target = 2.0 * abs(pi_at_ref) / threshold
    if target <= delta_im:
        return None, 2.0 * abs(pi_at_ref) / delta_im, delta_im, target
    delta_s = sqrt(target * target - delta_im * delta_im)
    delta_m_mev = delta_s / (2.0 * MH) * 1000.0
    return delta_m_mev, 2.0 * abs(pi_at_ref) / delta_im, delta_im, target


if __name__ == "__main__":
    main()
