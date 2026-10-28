#!/usr/bin/env python3
"""Exact tree-level muon semi-Compton amplitudes for vector/axial A' currents.

Process: gamma(k) + mu(p) -> mu(p') + A'(q), in the initial-muon rest frame.

The code:
* evaluates both s- and u-channel diagrams using explicit Dirac matrices/spinors;
* checks the electromagnetic Ward identity k_mu M^{mu nu}=0 for vector,
  axial and mixed A' currents;
* integrates exact 2->2 phase space over the lab scattering angle;
* resolves final A' transverse and longitudinal polarizations separately.

Units: masses and energies are in MeV; cross sections are in MeV^{-2}.
The couplings gV and gA are the A' muon-current couplings. This is a
tree-level vacuum scattering calculation, not a supernova emissivity or
transport calculation: no thermal distributions, Pauli blocking, in-medium
effects, or stellar profiles are included.
"""
from __future__ import annotations

import argparse
import math

import numpy as np

M_MU_MEV = 105.6583755
ALPHA_EM = 1.0 / 137.035999084
E_CHARGE = math.sqrt(4.0 * math.pi * ALPHA_EM)

I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
SIGMA = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
GAMMA = [np.block([[I2, Z2], [Z2, -I2]])]
for _sigma in SIGMA:
    GAMMA.append(np.block([[Z2, _sigma], [-_sigma, Z2]]))
GAMMA5 = 1j * GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3]
ID4 = np.eye(4, dtype=complex)


def slash(v: np.ndarray) -> np.ndarray:
    """Slash a contravariant four-vector with metric (+---)."""
    return GAMMA[0] * v[0] - sum(GAMMA[i] * v[i] for i in range(1, 4))


def u_spinor(p: np.ndarray, mass: float, spin: int) -> np.ndarray:
    """Dirac u spinor normalized to ubar u = 2m."""
    energy = float(p[0])
    spatial = np.asarray(p[1:], dtype=float)
    chi = np.zeros(2, dtype=complex)
    chi[spin] = 1.0
    sigma_p = sum(SIGMA[i] * spatial[i] for i in range(3))
    return math.sqrt(energy + mass) * np.concatenate(
        (chi, sigma_p @ chi / (energy + mass))
    )


def lab_kinematics(
    photon_energy: float,
    vector_mass: float,
    cos_theta: float,
    muon_mass: float = M_MU_MEV,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Exact kinematics in the initial-muon rest frame.

    Returns p, k, p', q for gamma(k)+mu(p)->mu(p')+A'(q).
    The physical root is chosen continuously to the Klein-Nishina solution
    as vector_mass -> 0.
    """
    eg, ma, m, c = photon_energy, vector_mass, muon_mass, cos_theta
    threshold = ma + ma * ma / (2.0 * m)
    if eg < threshold:
        raise ValueError(
            f"Below threshold: E_gamma={eg:g} MeV < {threshold:g} MeV"
        )
    p = np.array([m, 0.0, 0.0, 0.0])
    k = np.array([eg, 0.0, 0.0, eg])
    a = m + eg
    b = eg * c
    d = m * eg + ma * ma / 2.0
    discriminant = d * d - (a * a - b * b) * ma * ma
    if discriminant < -1e-10 * max(d * d, 1.0):
        raise ValueError("No real physical final-state solution")
    discriminant = max(discriminant, 0.0)
    q_energy = (a * d + b * math.sqrt(discriminant)) / (a * a - b * b)
    energy_tolerance = 1e-10 * max(ma, abs(q_energy), 1.0)
    if q_energy < ma - energy_tolerance:
        raise ValueError("No physical outgoing A' energy at this lab angle")
    q_momentum = math.sqrt(max(q_energy * q_energy - ma * ma, 0.0))
    sin_theta = math.sqrt(max(1.0 - c * c, 0.0))
    q = np.array(
        [q_energy, q_momentum * sin_theta, 0.0, q_momentum * c]
    )
    p_prime = p + k - q
    p_prime_mass_sq = p_prime[0]**2 - float(np.dot(p_prime[1:], p_prime[1:]))
    if abs(p_prime_mass_sq - muon_mass**2) > 1e-7 * max(muon_mass**2, 1.0):
        raise ValueError("No on-shell final muon at this lab angle")
    return p, k, p_prime, q


def photon_polarizations() -> tuple[np.ndarray, np.ndarray]:
    """Two real physical photon polarizations for k along +z."""
    return (
        np.array([0.0, 1.0, 0.0, 0.0]),
        np.array([0.0, 0.0, 1.0, 0.0]),
    )


def vector_polarizations(
    q: np.ndarray, vector_mass: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Two transverse and one longitudinal physical polarization vectors."""
    q3 = np.asarray(q[1:], dtype=float)
    q_abs = float(np.linalg.norm(q3))
    if q_abs == 0.0:
        direction = np.array([0.0, 0.0, 1.0])
    else:
        direction = q3 / q_abs

    # Construct a transverse orthonormal basis for an arbitrary q direction.
    # The previous fixed e2=(0,1,0) was only orthogonal to q when q_y=0.
    reference = (
        np.array([0.0, 1.0, 0.0])
        if abs(direction[1]) < 0.9
        else np.array([1.0, 0.0, 0.0])
    )
    e1 = np.cross(reference, direction)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(direction, e1)
    e2 /= np.linalg.norm(e2)
    transverse_1 = np.concatenate(([0.0], e1))
    transverse_2 = np.concatenate(([0.0], e2))
    longitudinal = np.concatenate(
        ([q_abs / vector_mass], q[0] * direction / vector_mass)
    )
    return transverse_1, transverse_2, longitudinal


def x_vertex(epsilon_x: np.ndarray, g_v: float, g_a: float) -> np.ndarray:
    """Contract gamma^nu (gV - gA gamma5) with the outgoing A' polarization."""
    return slash(epsilon_x) @ (g_v * ID4 - g_a * GAMMA5)


def amplitude_matrix(
    p: np.ndarray,
    k: np.ndarray,
    p_prime: np.ndarray,
    q: np.ndarray,
    muon_mass: float,
    epsilon_gamma: np.ndarray,
    epsilon_x: np.ndarray,
    g_v: float,
    g_a: float,
) -> np.ndarray:
    """Spinor-space matrix for the sum of the s- and u-channel diagrams.

    Overall phase is omitted. The electromagnetic coupling e is multiplied
    in the cross-section routine, so this matrix carries gV/gA only.
    """
    s_invariant = (p[0] + k[0]) ** 2 - np.dot(p[1:] + k[1:], p[1:] + k[1:])
    r = p - q
    u_invariant = r[0] ** 2 - np.dot(r[1:], r[1:])
    denom_s = s_invariant - muon_mass**2
    denom_u = u_invariant - muon_mass**2
    vertex_x = x_vertex(epsilon_x, g_v, g_a)
    vertex_gamma = slash(epsilon_gamma)
    prop_s = (slash(p + k) + muon_mass * ID4) / denom_s
    prop_u = (slash(r) + muon_mass * ID4) / denom_u
    return vertex_x @ prop_s @ vertex_gamma + vertex_gamma @ prop_u @ vertex_x


def ward_identity_residual(
    photon_energy: float,
    vector_mass: float,
    cos_theta: float,
    g_v: float,
    g_a: float,
    muon_mass: float = M_MU_MEV,
) -> float:
    """Largest |M(epsilon_gamma -> k)| over spins and A' polarizations."""
    p, k, p_prime, q = lab_kinematics(
        photon_energy, vector_mass, cos_theta, muon_mass
    )
    residual = 0.0
    for initial_spin in range(2):
        u_in = u_spinor(p, muon_mass, initial_spin)
        for final_spin in range(2):
            u_out = u_spinor(p_prime, muon_mass, final_spin)
            ubar_out = u_out.conj().T @ GAMMA[0]
            for epsilon_x in vector_polarizations(q, vector_mass):
                mat = amplitude_matrix(
                    p, k, p_prime, q, muon_mass, k, epsilon_x, g_v, g_a
                )
                residual = max(residual, abs(ubar_out @ mat @ u_in))
    return float(residual)


def polarization_resolved_matrix_element_squared(
    p: np.ndarray,
    k: np.ndarray,
    p_prime: np.ndarray,
    q: np.ndarray,
    vector_mass: float,
    g_v: float,
    g_a: float,
    mode: str,
    muon_mass: float = M_MU_MEV,
) -> float:
    """Spin-summed |M|^2, averaged over initial muon spin and photon polarization.

    The electromagnetic coupling e^2 is not included here.
    """
    gamma_pols = photon_polarizations()
    x_pols = vector_polarizations(q, vector_mass)
    if mode == "T":
        x_pols = x_pols[:2]
    elif mode == "L":
        x_pols = x_pols[2:]
    elif mode != "all":
        raise ValueError("mode must be 'T', 'L', or 'all'")
    total = 0.0
    for initial_spin in range(2):
        u_in = u_spinor(p, muon_mass, initial_spin)
        for final_spin in range(2):
            u_out = u_spinor(p_prime, muon_mass, final_spin)
            ubar_out = u_out.conj().T @ GAMMA[0]
            for epsilon_gamma in gamma_pols:
                for epsilon_x in x_pols:
                    mat = amplitude_matrix(
                        p, k, p_prime, q, muon_mass,
                        epsilon_gamma, epsilon_x, g_v, g_a
                    )
                    value = ubar_out @ mat @ u_in
                    total += abs(value) ** 2
    return float(total / 4.0)


def differential_cross_section_lab(
    photon_energy: float,
    vector_mass: float,
    cos_theta: float,
    g_v: float,
    g_a: float,
    mode: str = "all",
    muon_mass: float = M_MU_MEV,
    e_charge: float = E_CHARGE,
) -> float:
    """Exact tree-level d sigma/dOmega in the initial-muon rest frame, MeV^-2."""
    threshold = vector_mass + vector_mass**2 / (2.0 * muon_mass)
    if photon_energy <= threshold:
        return 0.0
    try:
        p, k, p_prime, q = lab_kinematics(
            photon_energy, vector_mass, float(cos_theta), muon_mass
        )
    except ValueError:
        # Some lab angles are kinematically inaccessible close to threshold.
        return 0.0
    msq = polarization_resolved_matrix_element_squared(
        p, k, p_prime, q, vector_mass, g_v, g_a, mode, muon_mass
    )
    q_abs = float(np.linalg.norm(q[1:]))
    jacobian_denominator = (
        q_abs * (muon_mass + photon_energy)
        - q[0] * photon_energy * float(cos_theta)
    )
    if jacobian_denominator <= 0.0:
        raise ArithmeticError(
            "Non-positive two-body phase-space Jacobian denominator"
        )
    return (
        e_charge**2 * msq * q_abs**2
        / (64.0 * math.pi**2 * muon_mass * photon_energy
           * jacobian_denominator)
    )


def total_cross_section_lab(
    photon_energy: float,
    vector_mass: float,
    g_v: float,
    g_a: float,
    mode: str = "all",
    n_angle: int = 120,
    muon_mass: float = M_MU_MEV,
    e_charge: float = E_CHARGE,
) -> float:
    """Integrate the exact lab-frame two-body cross section over solid angle."""
    nodes, weights = np.polynomial.legendre.leggauss(n_angle)
    integral = 0.0
    for cos_theta, weight in zip(nodes, weights):
        dsigma_domega = differential_cross_section_lab(
            photon_energy, vector_mass, float(cos_theta),
            g_v, g_a, mode, muon_mass, e_charge
        )
        integral += float(weight) * 2.0 * math.pi * dsigma_domega
    return integral


def cm_kinematics(
    photon_energy_muon_rest: float,
    vector_mass: float,
    cos_theta_cm: float,
    phi_cm: float = 0.0,
    muon_mass: float = M_MU_MEV,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Exact CM-frame kinematics at fixed invariant energy.

    The input photon energy is the invariantly equivalent energy in the
    initial-muon rest frame, E_star=(p_mu.k)/m_mu. The CM z axis is along
    the incoming photon. Returns p_mu, k, p'_mu, q in MeV.
    """
    eg_star, ma, m = photon_energy_muon_rest, vector_mass, muon_mass
    threshold = ma + ma * ma / (2.0 * m)
    if eg_star < threshold:
        raise ValueError("Below A' production threshold")
    s = m * m + 2.0 * m * eg_star
    root_s = math.sqrt(s)
    k_cm = (s - m * m) / (2.0 * root_s)
    e_mu_cm = (s + m * m) / (2.0 * root_s)
    e_q_cm = (s + ma * ma - m * m) / (2.0 * root_s)
    e_prime_cm = (s + m * m - ma * ma) / (2.0 * root_s)
    lambda_kallen = (
        s * s + m**4 + ma**4 - 2.0 * s * m * m
        - 2.0 * s * ma * ma - 2.0 * m * m * ma * ma
    )
    q_cm = math.sqrt(max(lambda_kallen, 0.0)) / (2.0 * root_s)
    c = max(-1.0, min(1.0, cos_theta_cm))
    sin_theta = math.sqrt(max(1.0 - c * c, 0.0))
    q_vec = np.array([
        q_cm * sin_theta * math.cos(phi_cm),
        q_cm * sin_theta * math.sin(phi_cm),
        q_cm * c,
    ])
    p_mu = np.array([e_mu_cm, 0.0, 0.0, -k_cm])
    k = np.array([k_cm, 0.0, 0.0, k_cm])
    q = np.concatenate(([e_q_cm], q_vec))
    p_prime = np.concatenate(([e_prime_cm], -q_vec))
    return p_mu, k, p_prime, q


def differential_cross_section_cm(
    photon_energy_muon_rest: float,
    vector_mass: float,
    cos_theta_cm: float,
    g_v: float,
    g_a: float,
    mode: str = "all",
    muon_mass: float = M_MU_MEV,
    e_charge: float = E_CHARGE,
) -> float:
    """Exact d sigma/dOmega_CM, in MeV^-2, with initial spin/polarization averages."""
    p, k, p_prime, q = cm_kinematics(
        photon_energy_muon_rest, vector_mass, cos_theta_cm, 0.0, muon_mass
    )
    s = muon_mass**2 + 2.0 * muon_mass * photon_energy_muon_rest
    q_abs = float(np.linalg.norm(q[1:]))
    k_abs = float(np.linalg.norm(k[1:]))
    if q_abs == 0.0 or k_abs == 0.0:
        return 0.0
    msq = polarization_resolved_matrix_element_squared(
        p, k, p_prime, q, vector_mass, g_v, g_a, mode, muon_mass
    )
    return e_charge**2 * msq * q_abs / (64.0 * math.pi**2 * s * k_abs)


def total_cross_section_cm(
    photon_energy_muon_rest: float,
    vector_mass: float,
    g_v: float,
    g_a: float,
    mode: str = "all",
    n_angle: int = 120,
    muon_mass: float = M_MU_MEV,
) -> float:
    """Integrate the exact CM-frame differential cross section over solid angle."""
    threshold = vector_mass + vector_mass**2 / (2.0 * muon_mass)
    if photon_energy_muon_rest <= threshold:
        return 0.0
    nodes, weights = np.polynomial.legendre.leggauss(n_angle)
    return sum(
        float(w) * 2.0 * math.pi * differential_cross_section_cm(
            photon_energy_muon_rest, vector_mass, float(c),
            g_v, g_a, mode, muon_mass
        )
        for c, w in zip(nodes, weights)
    )


def klein_nishina_reference(
    photon_energy: float, g_v: float = 1.0, muon_mass: float = M_MU_MEV
) -> float:
    """Massless-vector Klein-Nishina total cross section for a vector muon current."""
    x = photon_energy / muon_mass
    if x <= 0.0:
        raise ValueError("Photon energy must be positive")
    bracket = (
        (1.0 + x) / x**2
        * (2.0 * (1.0 + x) / (1.0 + 2.0 * x)
           - math.log1p(2.0 * x) / x)
        + math.log1p(2.0 * x) / (2.0 * x)
        - (1.0 + 3.0 * x) / (1.0 + 2.0 * x)**2
    )
    r0_sq = (E_CHARGE * g_v / (4.0 * math.pi * muon_mass))**2
    return 2.0 * math.pi * r0_sq * bracket

def low_energy_vector_reference(
    photon_energy: float, vector_mass: float, muon_mass: float = M_MU_MEV
) -> tuple[float, float]:
    """Printed (T,L) low-energy expressions in arXiv:2610.35379 Eqs. (58)/(106).

    Independent spinor checks find that the printed T/L labels appear
    inconsistent with the paper's polarization projectors and the conserved-
    current Thomson limit. Return the printed labels verbatim for comparison;
    do not silently swap them.
    """
    if photon_energy <= vector_mass:
        raise ValueError("Photon energy must exceed the vector mass")
    phase = math.sqrt(1.0 - vector_mass**2 / photon_energy**2)
    alpha_x = 1.0 / (4.0 * math.pi)  # normalized gV=1
    sigma_t_printed = (
        2.0 * math.pi * ALPHA_EM * alpha_x * vector_mass**2
        / (muon_mass**2 * photon_energy**2) * phase
    )
    sigma_l_printed = (
        8.0 * math.pi * ALPHA_EM * alpha_x
        / (3.0 * muon_mass**2) * phase
    )
    return sigma_t_printed, sigma_l_printed


def minkowski_dot(a: np.ndarray, b: np.ndarray) -> float:
    return float(a[0] * b[0] - np.dot(a[1:], b[1:]))


def run_checks() -> None:
    # On-shell kinematics and polarization orthonormality.
    p, k, p_prime, q = lab_kinematics(0.01, 0.001, 0.3)
    assert abs(minkowski_dot(p_prime, p_prime) - M_MU_MEV**2) < 1e-7
    assert abs(minkowski_dot(q, q) - 0.001**2) < 1e-10
    pols = vector_polarizations(q, 0.001)
    for eps in pols:
        assert abs(minkowski_dot(q, eps)) < 1e-10
        assert abs(minkowski_dot(eps, eps) + 1.0) < 1e-10
    for i in range(3):
        for j in range(i):
            assert abs(minkowski_dot(pols[i], pols[j])) < 1e-10

    # A general non-coplanar q direction must also have physical polarizations.
    ma_general = 0.5
    q_spatial = np.array([0.7, 0.2, 0.9])
    q_general = np.concatenate((
        [math.sqrt(ma_general**2 + float(np.dot(q_spatial, q_spatial)))],
        q_spatial,
    ))
    general_pols = vector_polarizations(q_general, ma_general)
    for eps in general_pols:
        assert abs(minkowski_dot(q_general, eps)) < 1e-10
        assert abs(minkowski_dot(eps, eps) + 1.0) < 1e-10
    for i in range(3):
        for j in range(i):
            assert abs(minkowski_dot(general_pols[i], general_pols[j])) < 1e-10

    # Electromagnetic Ward identity for vector, axial and mixed A' currents.
    for gv, ga in ((1.0, 0.0), (0.0, 1.0), (0.25, 0.75)):
        residual = ward_identity_residual(0.01, 0.001, 0.3, gv, ga)
        assert residual < 1e-7, (gv, ga, residual)

    # In the soft-photon, light-A' limit, a conserved vector current has
    # Thomson scattering in T and a suppressed longitudinal mode.
    eg, ma = 1e-4, 1e-7
    sigma_t = total_cross_section_lab(eg, ma, 1.0, 0.0, "T", n_angle=64)
    sigma_l = total_cross_section_lab(eg, ma, 1.0, 0.0, "L", n_angle=64)
    sigma_thomson = E_CHARGE**2 / (6.0 * math.pi * M_MU_MEV**2)
    assert abs(sigma_t / sigma_thomson - 1.0) < 0.02, (
        sigma_t, sigma_thomson
    )
    assert sigma_l / sigma_t < 1e-3, (sigma_l, sigma_t)

    # The lab-angle Jacobian and invariant CM phase space must give the same
    # total cross section at fixed s, away from threshold.
    sigma_lab = total_cross_section_lab(
        1.0, 0.01, 1.0, 0.0, "all", n_angle=96
    )
    sigma_cm = total_cross_section_cm(
        1.0, 0.01, 1.0, 0.0, "all", n_angle=96
    )
    assert abs(sigma_lab / sigma_cm - 1.0) < 5e-3, (
        sigma_lab, sigma_cm, sigma_lab / sigma_cm
    )
    sigma_kn_numeric = total_cross_section_cm(
        1.0, 1e-4, 1.0, 0.0, "all", n_angle=96
    )
    sigma_kn_exact = klein_nishina_reference(1.0, g_v=1.0)
    assert abs(sigma_kn_numeric / sigma_kn_exact - 1.0) < 1e-4, (
        sigma_kn_numeric, sigma_kn_exact
    )

    printed_t, printed_l = low_energy_vector_reference(eg, ma)
    assert abs(sigma_t / printed_l - 1.0) < 0.02, (sigma_t, printed_l)
    assert abs((sigma_t + sigma_l) / (printed_t + printed_l) - 1.0) < 0.02

    # For the axial current, the longitudinal cross section scales as 1/M^2
    # at fixed E_gamma in the small-M regime (Goldstone-equivalence behavior).
    sig_l_m1 = total_cross_section_lab(
        1e-3, 2e-4, 0.0, 1.0, "L", n_angle=64
    )
    sig_l_m2 = total_cross_section_lab(
        1e-3, 1e-4, 0.0, 1.0, "L", n_angle=64
    )
    assert 3.5 < sig_l_m2 / sig_l_m1 < 4.5, (
        sig_l_m1, sig_l_m2, sig_l_m2 / sig_l_m1
    )
    print("checks=PASS")
    print(f"vector Ward residual (gV=1): "
          f"{ward_identity_residual(0.01, 0.001, 0.3, 1.0, 0.0):.3e}")
    print(f"axial Ward residual (gA=1): "
          f"{ward_identity_residual(0.01, 0.001, 0.3, 0.0, 1.0):.3e}")
    print(f"vector soft-limit sigma_T / Thomson = "
          f"{sigma_t / sigma_thomson:.6f}")
    print(f"vector soft-limit sigma_L / sigma_T = {sigma_l / sigma_t:.3e}")
    print(f"axial sigma_L(M=0.1 MeV) / sigma_L(M=0.2 MeV) = "
          f"{sig_l_m2 / sig_l_m1:.6f}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run numerical checks")
    parser.add_argument("--energy", type=float, default=1.0,
                        help="incoming photon energy in MeV")
    parser.add_argument("--mass", type=float, default=0.1,
                        help="A' mass in MeV")
    parser.add_argument("--n-angle", type=int, default=120)
    args = parser.parse_args()
    if args.check:
        run_checks()
        return
    if args.energy < args.mass + args.mass**2 / (2 * M_MU_MEV):
        parser.error("photon energy is below production threshold")
    print("current,gV,gA,sigma_T_MeV^-2,sigma_L_MeV^-2,sigma_total_MeV^-2")
    for label, gv, ga in (
        ("vector", 1.0, 0.0),
        ("axial", 0.0, 1.0),
        ("mixed", 0.25, 0.75),
    ):
        st = total_cross_section_lab(
            args.energy, args.mass, gv, ga, "T", args.n_angle
        )
        sl = total_cross_section_lab(
            args.energy, args.mass, gv, ga, "L", args.n_angle
        )
        print(f"{label},{gv:g},{ga:g},{st:.8e},{sl:.8e},{st+sl:.8e}")


if __name__ == "__main__":
    main()
