"""Independent Compton cross-section and detailed-balance audit.

This module evaluates the tree-level muon Compton amplitude with one photon and
one massive vector, retaining exact two-body recoil. It is independent of
reference.py and production rates.py / transport.py.

It checks:
  * the exact phase-space/spin-degeneracy relation for forward and reverse
    unpolarized cross sections;
  * the Blinov Eq. (34) forward/reverse ratio (3/2) v_V^2;
  * the equivalence of the Eqs. (31) and (32) algebraic rate coefficients;
  * Eq. (35) from Fermi/Bose occupation factors;
  * the Thomson/Klein-Nishina normalization of the underlying QED amplitude.

The exact-rest-muon cross section is a vacuum two-body diagnostic. It is NOT a
thermal supernova rate: thermal muon momentum averaging and Pauli blocking must
still be included for a full rate calculation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy.special import expit

M_MU_DEFAULT = 105.6583755
ALPHA_DEFAULT = 1.0 / 137.035999084

_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)
_SIGMA = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
_GAMMA = np.zeros((4, 4, 4), dtype=complex)
_GAMMA[0] = np.block([[_I2, _Z2], [_Z2, -_I2]])
for _i, _sigma in enumerate(_SIGMA, start=1):
    _GAMMA[_i] = np.block([[_Z2, _sigma], [-_sigma, _Z2]])
_GAMMA0 = _GAMMA[0]
_METRIC = np.array([1.0, -1.0, -1.0, -1.0])


def slash(four_vector):
    """Dirac slash for contravariant four-vector, metric (+---)."""
    p = np.asarray(four_vector, dtype=complex)
    return sum(_GAMMA[mu] * _METRIC[mu] * p[mu] for mu in range(4))


def dirac_adjoint(matrix):
    return _GAMMA0 @ matrix.conjugate().T @ _GAMMA0


def kallen(x, y, z):
    """Numerically stable factored Källén function for squared masses."""
    a = math.sqrt(max(y, 0.0))
    b = math.sqrt(max(z, 0.0))
    return (x - (a + b)*(a + b)) * (x - (a - b)*(a - b))


def two_body_momentum(s, mass_a, mass_b):
    """Magnitude of either CM momentum in a two-body state."""
    if s <= 0:
        raise ValueError("s must be positive")
    value = kallen(s, mass_a*mass_a, mass_b*mass_b)
    if value < -1e-10 * s*s:
        return 0.0
    return math.sqrt(max(value, 0.0)) / (2.0 * math.sqrt(s))


def _polarizations(mass, energy, momentum, direction, massless=False):
    """Physical polarization four-vectors for a boson moving along direction."""
    n = np.asarray(direction, dtype=float)
    n = n / np.linalg.norm(n)
    # Scattering plane is x-z. These two vectors are orthonormal to n.
    e1 = np.array([n[2], 0.0, -n[0]])
    e1_norm = np.linalg.norm(e1)
    if e1_norm < 1e-14:
        e1 = np.array([1.0, 0.0, 0.0])
    else:
        e1 /= e1_norm
    e2 = np.cross(n, e1)
    e2 /= np.linalg.norm(e2)
    result = [
        np.array([0.0, *e1], dtype=complex),
        np.array([0.0, *e2], dtype=complex),
    ]
    if not massless:
        if mass <= 0:
            raise ValueError("A massive polarization sum requires mass>0")
        p_abs = float(np.linalg.norm(momentum))
        result.append(np.array([p_abs / mass, *(energy / mass * n)], dtype=complex))
    return result


def matrix_element_squared_cm(
    m_mu, m_in, m_out, omega_in_lab, cos_theta,
    coupling_in, coupling_out,
):
    """Unpolarized |M|^2 for muon + boson(in) -> muon + boson(out).

    The muon is initially at rest in the lab frame. The calculation is performed
    in the CM frame. Initial muon spin and initial-boson polarizations are
    averaged; final muon spin and final-boson polarizations are summed.
    """
    if m_mu <= 0 or m_in < 0 or m_out < 0 or omega_in_lab <= m_in:
        raise ValueError("Invalid masses or incoming boson energy")
    s = m_mu*m_mu + m_in*m_in + 2.0*m_mu*omega_in_lab
    root_s = math.sqrt(s)
    p_in = two_body_momentum(s, m_mu, m_in)
    p_out = two_body_momentum(s, m_mu, m_out)
    if p_in <= 0 or p_out <= 0:
        return 0.0

    e_mu_in = (s + m_mu*m_mu - m_in*m_in) / (2.0*root_s)
    e_b_in = (s - m_mu*m_mu + m_in*m_in) / (2.0*root_s)
    e_mu_out = (s + m_mu*m_mu - m_out*m_out) / (2.0*root_s)
    e_b_out = (s - m_mu*m_mu + m_out*m_out) / (2.0*root_s)

    sin_theta = math.sqrt(max(1.0 - cos_theta*cos_theta, 0.0))
    p = np.array([e_mu_in, 0.0, 0.0, -p_in])
    k_in = np.array([e_b_in, 0.0, 0.0, p_in])
    n_out = np.array([sin_theta, 0.0, cos_theta])
    k_out = np.array([e_b_out, p_out*sin_theta, 0.0, p_out*cos_theta])
    p_out_mu = np.array([e_mu_out, -p_out*sin_theta, 0.0, -p_out*cos_theta])

    den_s = s - m_mu*m_mu
    p_dot_kout = (
        p[0]*k_out[0] - np.dot(p[1:], k_out[1:])
    )
    den_u = m_out*m_out - 2.0*p_dot_kout
    if abs(den_s) < 1e-30 or abs(den_u) < 1e-30:
        raise FloatingPointError("Singular Compton propagator in sampled kinematics")

    pol_in = _polarizations(
        m_in, e_b_in, k_in[1:], np.array([0.0, 0.0, 1.0]),
        massless=(m_in == 0.0),
    )
    pol_out = _polarizations(
        m_out, e_b_out, k_out[1:], n_out, massless=(m_out == 0.0)
    )
    spin_out = slash(p_out_mu) + m_mu*np.eye(4)
    spin_in = slash(p) + m_mu*np.eye(4)

    summed = 0.0
    for eps_in in pol_in:
        for eps_out in pol_out:
            vertex = (
                slash(eps_out.conjugate())
                @ (slash(p + k_in) + m_mu*np.eye(4))
                @ slash(eps_in) / den_s
                + slash(eps_in)
                @ (slash(p - k_out) + m_mu*np.eye(4))
                @ slash(eps_out.conjugate()) / den_u
            )
            trace = np.trace(
                spin_out @ vertex @ spin_in @ dirac_adjoint(vertex)
            )
            summed += float(trace.real)

    # Average over two initial muon spins and initial boson polarizations.
    average = 2.0 * len(pol_in)
    return (coupling_in*coupling_out)**2 * summed / average


def exact_cross_section(
    m_mu, m_in, m_out, omega_in_lab, coupling_in, coupling_out,
    alpha_angle_order=96,
):
    """Exact tree-level vacuum cross section in the initial-muon rest frame.

    Returns MeV^-2. Couplings are the dimensionless vertex couplings e and g_V.
    """
    s = m_mu*m_mu + m_in*m_in + 2.0*m_mu*omega_in_lab
    p_in = two_body_momentum(s, m_mu, m_in)
    p_out = two_body_momentum(s, m_mu, m_out)
    if p_in <= 0 or p_out <= 0:
        return 0.0
    nodes, weights = np.polynomial.legendre.leggauss(alpha_angle_order)
    angular_integral = 0.0
    for c, w in zip(nodes, weights):
        angular_integral += w * matrix_element_squared_cm(
            m_mu, m_in, m_out, omega_in_lab, float(c),
            coupling_in, coupling_out,
        )
    angular_integral *= 2.0*math.pi
    return angular_integral * (p_out/p_in) / (64.0*math.pi**2*s)


def sigma_forward_B14(m_mu, m_v, omega, alpha=ALPHA_DEFAULT, g_v=1.0):
    """Blinov Eq. (30) forward cross section in the no-recoil approximation."""
    if omega <= m_v:
        return 0.0
    alpha_v = g_v*g_v/(4.0*math.pi)
    velocity = math.sqrt(1.0 - (m_v/omega)**2)
    return (
        8.0*math.pi*alpha*alpha_v/(3.0*m_mu*m_mu)
        * (1.0 + m_v*m_v/(2.0*omega*omega)) * velocity
    )


def exact_momentum_ratio(m_mu, m_v, omega_gamma):
    """p_f/p_i for mu+gamma -> mu+V with exact muon recoil."""
    s = m_mu*m_mu + 2.0*m_mu*omega_gamma
    p_i = two_body_momentum(s, m_mu, 0.0)
    p_f = two_body_momentum(s, m_mu, m_v)
    return p_f/p_i if p_i > 0 else 0.0


def no_recoil_velocity(m_v, omega):
    if omega <= m_v:
        return 0.0
    return math.sqrt(1.0 - (m_v/omega)**2)


def inverse_vector_energy_same_s(m_mu, m_v, omega_gamma):
    """Incoming V energy in muon rest frame giving the same s as incoming gamma."""
    return omega_gamma - m_v*m_v/(2.0*m_mu)


def phase_space_cross_section_ratio(m_mu, m_v, omega_gamma):
    """Exact detailed-balance ratio from spin degeneracies and CM phase space."""
    r = exact_momentum_ratio(m_mu, m_v, omega_gamma)
    return 1.5*r*r


def no_recoil_B18_ratio(m_v, omega):
    v = no_recoil_velocity(m_v, omega)
    return 1.5*v*v


def occupation_detailed_balance_ratio(
    e_mu_initial, e_gamma, e_mu_final, chemical_potential, temperature,
):
    """Return inverse/forward occupation-factor ratio for a Compton pair.

    Forward: f_mu(E1) f_gamma(Egamma) [1-f_mu(E2)]
    Inverse: f_mu(E2) [1-f_mu(E1)] [1+f_gamma(Egamma)]
    Energy conservation fixes omega_V = E1 + Egamma - E2.
    """
    if temperature <= 0 or e_gamma <= 0:
        raise ValueError("Require T>0 and positive photon energy")
    omega_v = e_mu_initial + e_gamma - e_mu_final
    if omega_v <= 0:
        raise ValueError("Energy conservation gives non-positive vector energy")
    f1 = float(expit((chemical_potential - e_mu_initial)/temperature))
    f2 = float(expit((chemical_potential - e_mu_final)/temperature))
    nb = 1.0/math.expm1(e_gamma/temperature)
    forward = f1*nb*(1.0-f2)
    inverse = f2*(1.0-f1)*(1.0+nb)
    return inverse/forward, math.exp(omega_v/temperature), omega_v


def klein_nishina_total(omega, m_mu, alpha=ALPHA_DEFAULT):
    """Unpolarized QED Klein-Nishina total cross section in MeV^-2."""
    x = omega/m_mu
    if x <= 0:
        raise ValueError("omega must be positive")
    term = (
        (1.0+x)/x**3
        * (2.0*x*(1.0+x)/(1.0+2.0*x) - math.log1p(2.0*x))
        + math.log1p(2.0*x)/(2.0*x)
        - (1.0+3.0*x)/(1.0+2.0*x)**2
    )
    return 2.0*math.pi*alpha*alpha/(m_mu*m_mu)*term


def audit_point(m_mu, m_v, omega, alpha=ALPHA_DEFAULT, g_v=1.0,
                angle_order=96):
    """Compare exact forward/reverse cross sections with Eqs. (30)/(34)."""
    e = math.sqrt(4.0*math.pi*alpha)
    e_v = inverse_vector_energy_same_s(m_mu, m_v, omega)
    s_forward = exact_cross_section(
        m_mu, 0.0, m_v, omega, e, g_v, angle_order
    )
    if e_v > m_v:
        s_reverse = exact_cross_section(
            m_mu, m_v, 0.0, e_v, g_v, e, angle_order
        )
    else:
        s_reverse = 0.0
    r = exact_momentum_ratio(m_mu, m_v, omega)
    exact_ratio = s_forward/s_reverse if s_reverse > 0 else None
    phase_ratio = 1.5*r*r
    sigma_b14 = sigma_forward_B14(m_mu, m_v, omega, alpha, g_v)
    v = no_recoil_velocity(m_v, omega)
    no_recoil_rate_coeff = 2.0*sigma_b14/v if v > 0 else None
    exact_rate_coeff = 2.0*s_forward/r if r > 0 else None
    return {
        "m_mu_MeV": m_mu,
        "mV_MeV": m_v,
        "omega_gamma_lab_MeV": omega,
        "omega_V_inverse_lab_MeV": e_v,
        "exact_threshold_open": bool(e_v > m_v),
        "v_no_recoil": v,
        "p_ratio_exact": r,
        "p_ratio_over_v": r/v if v > 0 else None,
        "sigma_forward_exact_MeV-2": s_forward,
        "sigma_reverse_exact_MeV-2": s_reverse,
        "sigma_forward_B14_MeV-2": sigma_b14,
        "sigma_exact_over_B14": s_forward/sigma_b14 if sigma_b14 > 0 else None,
        "cross_section_ratio_direct": exact_ratio,
        "cross_section_ratio_phase_space": phase_ratio,
        "B18_no_recoil_ratio": 1.5*v*v,
        "direct_ratio_relative_residual": (
            exact_ratio/phase_ratio - 1.0 if exact_ratio is not None else None
        ),
        "B15_B16_exact_kinematic_coefficient_residual": (
            (3.0*r*s_reverse)/(2.0*s_forward/r) - 1.0
            if r > 0 and s_reverse > 0 else None
        ),
        "exact_rate_coefficient_over_B16_no_recoil": (
            exact_rate_coeff/no_recoil_rate_coeff
            if exact_rate_coeff is not None and no_recoil_rate_coeff else None
        ),
    }


def run_audit(
    masses=(0.1, 1.0, 10.0),
    energies=(12.0, 15.0, 20.0, 30.0, 50.0, 100.0),
    m_mu=M_MU_DEFAULT, alpha=ALPHA_DEFAULT, g_v=1.0,
    angle_order=96,
):
    rows = []
    for m_v in masses:
        for omega in energies:
            if omega > m_v:
                rows.append(audit_point(
                    m_mu, m_v, omega, alpha, g_v, angle_order
                ))
    return {
        "source": "Independent tree-level QED x vector-current Compton amplitude; comparison with Blinov et al. arXiv:2511.09619v2 Eqs. (30)--(35)",
        "interpretation": (
            "Exact two-body vacuum cross sections with a stationary initial muon. "
            "The Eq. (34) ratio is checked directly; the no-recoil formula is not "
            "replaced in the supernova calculation. Thermal muon averaging and "
            "Pauli blocking are outside this audit."
        ),
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "reference_code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "m_mu_MeV": m_mu,
        "alpha": alpha,
        "gV": g_v,
        "angle_order": angle_order,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--masses", default="0.1,1,10")
    parser.add_argument("--energies", default="12,15,20,30,50,100")
    parser.add_argument("--angle-order", type=int, default=96)
    args = parser.parse_args()
    masses = tuple(float(x) for x in args.masses.split(","))
    energies = tuple(float(x) for x in args.energies.split(","))
    result = run_audit(masses=masses, energies=energies,
                       angle_order=args.angle_order)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in result["rows"]:
        print(
            f"mV={row['mV_MeV']:g} MeV, omega={row['omega_gamma_lab_MeV']:g} MeV: "
            f"sigma_exact/B14={row['sigma_exact_over_B14']:.5g}, "
            f"r/v={row['p_ratio_over_v']:.5g}, "
            f"exact_rate/B16={row['exact_rate_coefficient_over_B16_no_recoil']:.5g}, "
            f"B18 residual={row['direct_ratio_relative_residual']:.3e}"
        )


if __name__ == "__main__":
    main()
