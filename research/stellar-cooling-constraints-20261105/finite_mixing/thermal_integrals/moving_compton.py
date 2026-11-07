"""Full moving-muon semi-Compton thermal rates at fixed mediator energy.

Process: A'(k) + mu^Q(p) <-> gamma(q) + mu^Q(p').
All energies and momenta are in MeV. The rates are normalized to the
couplings g_vector and g_axial supplied by the caller (usually divided by gX).
"""
from __future__ import annotations

import numpy as np

from rates import (
    ALPHA, E2, M_MU, _G5, _GAMMA, _I4, _METRIC, _dagger, _fermion, _slash,
)


def _bose(energy, temperature):
    """Stable Bose occupation for positive energy."""
    x = np.asarray(energy, float) / float(temperature)
    ex = np.exp(-np.minimum(x, 700.0))
    return ex / (-np.expm1(-np.minimum(x, 700.0)))


def _mapped_interval(order, lower, upper):
    if order < 4 or upper <= lower:
        raise ValueError("Invalid Gauss-Legendre interval")
    z, w = np.polynomial.legendre.leggauss(order)
    return (lower + upper)/2 + (upper-lower)*z/2, (upper-lower)*w/2


def _muon_radial_rule(temperature, chemical_potential, omega, order):
    """Composite final-muon p rule covering thermal and recoil-shifted support."""
    if temperature <= 0 or omega <= 0 or order < 8:
        raise ValueError("Require T>0, omega>0 and radial order>=8")
    # A Fermi surface exists only for a positive chemical potential above
    # the rest mass. A large negative mu_Q describes a dilute antiparticle
    # population and must not be converted into a fictitious p_F.
    p_fermi = (np.sqrt(chemical_potential**2 - M_MU**2)
               if chemical_potential > M_MU else 0.0)
    if p_fermi > 0.0:
        edge_lo = max(0.0, p_fermi - 10.0*temperature)
        edge_hi = p_fermi + 2.0*omega + 20.0*temperature
        if edge_lo > 0.0:
            p1, w1 = _mapped_interval(max(4, order//2), 0.0, edge_lo)
        else:
            p1, w1 = np.zeros(0), np.zeros(0)
        p2, w2 = _mapped_interval(order, edge_lo, edge_hi)
        return np.concatenate((p1, p2)), np.concatenate((w1, w2))
    p_max = max(20.0*temperature, 12.0*np.sqrt(M_MU*temperature)) + 2.0*omega
    return _mapped_interval(order, 0.0, p_max)


def moving_compton_matrix_elements(
    mass,
    omega,
    momentum,
    cos_theta_p,
    cos_theta_gamma,
    phi_gamma,
    g_vector,
    g_axial,
    *,
    charge="mu_minus",
    photon_ward=False,
    vector_mediator_ward=False,
):
    """Return q*, E_mu' and spin-averaged |M_h|^2 for moving muons.

    The momentum argument p is the final-muon momentum in the production
    process gamma+mu(p') -> A'+mu(p); p' = p+k-q is the initial muon.
    The inverse absorption rate uses the same squared amplitude. The
    incoming A' momentum is along +z. The final-muon azimuth is set to zero
    using axial symmetry. Photon polarizations are e_theta/e_phi.
    The trace sums photon polarizations and final muon spin, and averages
    the initial muon spin. Multiply by the explicit two-spin degeneracy
    only in the phase-space integral.

    charge='mu_plus' implements the charge-conjugate current: the relative
    vector--axial interference sign is reversed. Pure-current endpoints
    are unchanged.
    """
    if charge not in ("mu_minus", "mu_plus"):
        raise ValueError("charge must be 'mu_minus' or 'mu_plus'")
    vals = (mass, omega, g_vector, g_axial)
    if not all(np.isfinite(x) for x in vals) or mass <= 0 or omega < mass:
        raise ValueError("Require finite couplings, mass>0 and omega>=mass")
    if not np.isfinite(g_vector) or not np.isfinite(g_axial):
        raise ValueError("Couplings must be finite")

    p, cp, cg, phi = np.broadcast_arrays(
        np.asarray(momentum, float),
        np.asarray(cos_theta_p, float),
        np.asarray(cos_theta_gamma, float),
        np.asarray(phi_gamma, float),
    )
    if np.any(p < 0) or np.any(np.abs(cp) > 1) or np.any(np.abs(cg) > 1):
        raise ValueError("Require p>=0 and angular cosines in [-1,1]")

    k_mag = np.sqrt(max(omega*omega - mass*mass, 0.0))
    ep = np.sqrt(p*p + M_MU*M_MU)
    sp = np.sqrt(np.maximum(1.0-cp*cp, 0.0))
    sg = np.sqrt(np.maximum(1.0-cg*cg, 0.0))
    pvec = np.stack((p*sp, np.zeros_like(p), p*cp), axis=-1)
    nhat = np.stack((sg*np.cos(phi), sg*np.sin(phi), cg), axis=-1)
    kvec = np.array([0.0, 0.0, k_mag])
    avec = ep + omega
    Pvec = pvec + kvec
    D = avec - np.einsum("...i,...i->...", Pvec, nhat)
    numerator = mass*mass + 2.0*(ep*omega - k_mag*p*cp)
    if np.any(D <= 0.0):
        raise ArithmeticError("Nonpositive photon-energy Jacobian denominator")
    q = numerator/(2.0*D)
    if np.any(q <= 0.0) or np.any(q >= avec):
        raise ArithmeticError("The on-shell photon root is outside its physical range")
    eprime = avec-q
    pprime_vec = Pvec-q[..., None]*nhat
    p4 = np.concatenate((ep[..., None], pvec), axis=-1)
    pprime4 = np.concatenate((eprime[..., None], pprime_vec), axis=-1)
    k4 = np.broadcast_to(np.array([omega, 0.0, 0.0, k_mag]), p4.shape)
    q4 = np.concatenate((q[..., None], q[..., None]*nhat), axis=-1)

    # Verify the mass shell after solving the energy delta function.
    pprime_shell = np.sum(pprime_vec*pprime_vec, axis=-1) + M_MU*M_MU
    shell_error = np.max(np.abs(eprime*eprime-pprime_shell)/np.maximum(eprime*eprime, 1.0))
    if shell_error > 2e-10:
        raise ArithmeticError(f"Final-muon mass-shell residual is {shell_error:g}")

    prop_s_den = mass*mass + 2.0*(ep*omega - k_mag*p*cp)
    prop_u_den = -2.0*(ep*q - np.einsum("...i,...i->...", pvec, q[..., None]*nhat))
    if np.any(prop_s_den <= 0.0) or np.any(prop_u_den >= 0.0):
        raise ArithmeticError("Unexpected Compton propagator denominator sign")
    prop_s = (_slash(p4+k4)+M_MU*_I4)/prop_s_den[..., None, None]
    prop_u = (_slash(p4-q4)+M_MU*_I4)/prop_u_den[..., None, None]
    # Reverse-production convention: p is the final muon and pprime the
    # initial muon. This ordering is essential for the photon Ward identity.
    spin_out = _slash(p4)+M_MU*_I4
    spin_in = _slash(pprime4)+M_MU*_I4

    zeros = np.zeros_like(p)
    eps_l_physical = np.stack((np.full_like(p, k_mag/mass), zeros, zeros,
                               np.full_like(p, omega/mass)), axis=-1)
    small = mass/(omega+k_mag) if omega+k_mag > 0 else 0.0
    eps_l_vector = np.stack((np.full_like(p, -small), zeros, zeros,
                             np.full_like(p, small)), axis=-1)
    eps_plus = np.broadcast_to(
        np.array([0.0, 1.0, 1.0j, 0.0])/np.sqrt(2.0), p4.shape
    )
    eps_minus = np.broadcast_to(
        np.array([0.0, 1.0, -1.0j, 0.0])/np.sqrt(2.0), p4.shape
    )
    if vector_mediator_ward:
        eps_l_vector = k4

    eps_mediator = (
        (eps_l_vector, eps_l_physical),
        (eps_plus, eps_plus),
        (eps_minus, eps_minus),
    )
    if photon_ward:
        eps_photon = (q4,)
    else:
        e_theta = np.stack((zeros, cg*np.cos(phi), cg*np.sin(phi), -sg), axis=-1)
        e_phi = np.stack((zeros, -np.sin(phi), np.cos(phi), zeros), axis=-1)
        eps_photon = (e_theta, e_phi)

    axial_charge_sign = 1.0 if charge == "mu_minus" else -1.0
    answer = []
    gamma0 = _GAMMA[0]
    for eps_vector, eps_axial in eps_mediator:
        vx_vector = _slash(eps_vector)
        vx_axial = _slash(eps_axial)@(-_G5)
        total = np.zeros_like(p, dtype=float)
        for photon_polarization in eps_photon:
            vg = _slash(photon_polarization)
            amp_vector = vx_vector@prop_s@vg + vg@prop_u@vx_vector
            amp_axial = vx_axial@prop_s@vg + vg@prop_u@vx_axial
            amplitude = g_vector*amp_vector - axial_charge_sign*g_axial*amp_axial
            conjugate = gamma0@_dagger(amplitude)@gamma0
            trace = np.trace(
                spin_out@amplitude@spin_in@conjugate, axis1=-2, axis2=-1
            )
            total += trace.real/2.0
        answer.append(total*E2)
    msq = np.stack(answer, axis=-1)
    return q, eprime, msq


def moving_muon_compton_rates(
    mass,
    omega,
    temperature,
    mu_mu,
    g_vector,
    g_axial,
    *,
    radial_order=24,
    angular_order=8,
    azimuth_order=12,
    chunk_size=4096,
):
    """Direct moving-muon production and absorption rates at fixed omega.

    Returns per-mode rates for the two charge species separately and summed.
    The initial-muon radial rule is composite near a degenerate Fermi surface;
    angular variables use Gauss-Legendre and periodic trapezoidal quadrature.
    """
    vals = (mass, omega, temperature, mu_mu, g_vector, g_axial)
    if not all(np.isfinite(x) for x in vals):
        raise ValueError("All inputs must be finite")
    if mass <= 0 or omega < mass or temperature <= 0:
        raise ValueError("Require mass>0, omega>=mass and T>0")
    if radial_order < 8 or angular_order < 4 or azimuth_order < 4 or chunk_size < 64:
        raise ValueError("Quadrature orders/chunk size are too small")

    c, wc = np.polynomial.legendre.leggauss(angular_order)
    phi = 2.0*np.pi*np.arange(azimuth_order)/azimuth_order
    wphi = np.full(azimuth_order, 2.0*np.pi/azimuth_order)
    prefactor = 2.0/(8.0*omega*(2.0*np.pi)**4)  # two initial-muon spins

    charge_results = {}
    for charge, chemical in (("mu_minus", +mu_mu), ("mu_plus", -mu_mu)):
        p_nodes, wp = _muon_radial_rule(temperature, chemical, omega, radial_order)
        # Flatten the tensor-product quadrature without storing 4D matrices.
        P, CP, CG, PHI = np.meshgrid(p_nodes, c, c, phi, indexing="ij")
        WP, WCP, WCG, WPHI = np.meshgrid(wp, wc, wc, wphi, indexing="ij")
        flat = [x.reshape(-1) for x in (P, CP, CG, PHI, WP*WCP*WCG*WPHI)]
        total_abs = np.zeros(3)
        total_prod = np.zeros(3)
        n_points = flat[0].size

        for start in range(0, n_points, chunk_size):
            stop = min(start+chunk_size, n_points)
            p, cp, cg, ph, qw = (x[start:stop] for x in flat)
            q, ep_out, msq = moving_compton_matrix_elements(
                mass, omega, p, cp, cg, ph, g_vector, g_axial, charge=charge
            )
            ep_final = np.sqrt(p*p+M_MU*M_MU)
            f_initial = _fermion((ep_out-chemical)/temperature)
            f_final = _fermion((ep_final-chemical)/temperature)
            fb = _bose(q, temperature)
            stat_abs = f_final*(1.0-f_initial)*(1.0+fb)
            stat_prod = f_initial*fb*(1.0-f_final)
            k_mag = np.sqrt(max(omega*omega-mass*mass, 0.0))
            sp = np.sqrt(np.maximum(1.0-cp*cp, 0.0))
            pvec = np.stack((p*sp, np.zeros_like(p), p*cp), axis=-1)
            nhat = np.stack((np.sqrt(np.maximum(1.0-cg*cg, 0.0))*np.cos(ph),
                             np.sqrt(np.maximum(1.0-cg*cg, 0.0))*np.sin(ph), cg), axis=-1)
            D = ep_in+omega-np.einsum("...i,...i->...", pvec+np.array([0.0,0.0,k_mag]), nhat)
            phase = prefactor*qw*(p*p/ep_final)*(q/D)
            total_abs += np.einsum("i,ih,i->h", phase, msq, stat_abs)
            total_prod += np.einsum("i,ih,i->h", phase, msq, stat_prod)

        charge_results[charge] = {
            "Gamma_prod_by_mode": total_prod,
            "Gamma_abs_by_mode": total_abs,
            "quadrature_points": int(n_points),
            "radial_nodes": int(len(p_nodes)),
        }

    prod_total = charge_results["mu_minus"]["Gamma_prod_by_mode"] + charge_results["mu_plus"]["Gamma_prod_by_mode"]
    abs_total = charge_results["mu_minus"]["Gamma_abs_by_mode"] + charge_results["mu_plus"]["Gamma_abs_by_mode"]
    expected_prod = np.exp(-omega/temperature)*abs_total
    balance = np.max(np.abs(prod_total-expected_prod)/np.maximum(np.abs(prod_total), 1e-300))
    return {
        "Gamma_prod_by_mode": prod_total,
        "Gamma_abs_by_mode": abs_total,
        "charge_contributions": charge_results,
        "max_detailed_balance_relative_residual": float(balance),
        "total_quadrature_points_per_charge": int(sum(
            item["quadrature_points"] for item in charge_results.values()
        )),
    }
