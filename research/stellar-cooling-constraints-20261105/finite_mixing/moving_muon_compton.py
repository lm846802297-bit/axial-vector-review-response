"""Exact-recoil semi-Compton kernels with moving thermal muons.

Rates are per g_X^2 and per A' polarization at fixed A' energy. Both muon
charges, Fermi blocking, photon Bose enhancement, and exact 2->2 recoil are
retained. The A' momentum is along +z in the local medium rest frame; mode
order is (L,+,-), with physical epsilon_L=(|k|/m,0,0,omega/m) for the axial
current and a Ward-equivalent epsilon_L-q/m for the conserved vector current.
The +/- modes are circular transverse polarizations in that same frame.
This is a local collision kernel, not stellar transport.
"""
from __future__ import annotations
import math
import sys
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import rates


def _fermi(x):
    return np.exp(-np.logaddexp(0.0, x))


def _polarization_trace(prop_s, prop_u, spin_out, spin_in, gamma_vertex):
    """Photon-summed |M_h|^2; initial muon spin is averaged."""
    total = None
    for nu in range(4):
        amplitude = (
            gamma_vertex @ prop_s @ rates._GAMMA[nu]
            + rates._GAMMA[nu] @ prop_u @ gamma_vertex
        )
        conjugate = rates._GAMMA[0] @ rates._dagger(amplitude) @ rates._GAMMA[0]
        trace = np.trace(spin_out @ amplitude @ spin_in @ conjugate,
                         axis1=-2, axis2=-1)
        term = -rates._METRIC[nu] * trace.real / 2.0
        total = term.copy() if total is None else total + term
    return total * rates.E2


def moving_muon_compton_rates(
    mass, energy, temperature, mu_mu,
    g_vector=0.0, g_axial=-1.0, orders=(12, 8, 8, 8)
):
    """Return medium-rest-frame production/absorption rates in (L,+,-) order.

    The incoming A' momentum is q=(energy,0,0,sqrt(energy^2-mass^2)) in the
    medium rest frame. L is the physical longitudinal polarization for the
    axial current; +/- are circular transverse polarizations. Rates are per
    g_X^2. mu_mu is the mu- chemical potential; mu+ has chemical potential -mu_mu.
    Couplings are normalized to g_X in gamma^mu(g_vector+g_axial gamma5);
    the physical UV axial endpoint is g_axial=-1.
    orders are (kinetic-energy, cos(mu), cos(gamma), relative photon azimuth).
    """
    mass, energy, temperature, mu_mu = map(float, (mass, energy, temperature, mu_mu))
    g_vector, g_axial = float(g_vector), float(g_axial)
    if not all(math.isfinite(x) for x in
               (mass, energy, temperature, mu_mu, g_vector, g_axial)):
        raise ValueError("All inputs must be finite")
    if mass <= 0 or energy < mass or temperature <= 0:
        raise ValueError("Require mass>0, energy>=mass, temperature>0")
    if g_vector == 0 and g_axial == 0:
        raise ValueError("At least one muon-current coupling must be nonzero")
    if len(orders) != 4 or min(orders) < 4:
        raise ValueError("Four quadrature orders >=4 are required")
    n_p, n_mu, n_gamma, n_phi = map(int, orders)

    # x=(E_mu-m_mu)/T; t=sqrt(x) smooths the p=0 endpoint.
    x_max = max(36.0, max(abs(mu_mu)-rates.M_MU, 0.0)/temperature + 36.0)
    z_t, w_t = leggauss(n_p)
    t_max = math.sqrt(x_max)
    t = 0.5*t_max*(z_t+1.0)
    w_t = 0.5*t_max*w_t
    x = t*t
    p = np.sqrt(temperature*x*(2*rates.M_MU+temperature*x))
    e_mu = rates.M_MU + temperature*x
    # p^2 dp = 2 T p E_mu t dt.
    radial_measure = 2.0*temperature*p*t*w_t

    z_mu, w_mu = leggauss(n_mu)
    z_gamma, w_gamma = leggauss(n_gamma)
    z_phi, w_phi = leggauss(n_phi)
    phi = math.pi*(z_phi+1.0)
    w_phi = math.pi*w_phi

    p_b = p[:, None, None, None]
    e_b = e_mu[:, None, None, None]
    c_mu = z_mu[None, :, None, None]
    c_gamma = z_gamma[None, None, :, None]
    phi_b = phi[None, None, None, :]
    sin_mu = np.sqrt(np.maximum(1.0-c_mu*c_mu, 0.0))
    sin_gamma = np.sqrt(np.maximum(1.0-c_gamma*c_gamma, 0.0))
    p_x, p_z = p_b*sin_mu, p_b*c_mu
    n_x, n_y = sin_gamma*np.cos(phi_b), sin_gamma*np.sin(phi_b)
    n_z = c_gamma

    k_a = math.sqrt(max(energy*energy-mass*mass, 0.0))
    p_dot_q = e_b*energy-p_z*k_a
    c_den = e_b+energy-p_x*n_x-p_z*n_z-k_a*c_gamma
    k_num = mass*mass+2.0*p_dot_q
    photon_energy = k_num/(2.0*c_den)

    p_four = np.stack(
        np.broadcast_arrays(e_b, p_x, np.zeros_like(p_x), p_z), axis=-1
    )
    q_four = np.array([energy, 0.0, 0.0, k_a])
    photon_four = np.stack(
        np.broadcast_arrays(
            photon_energy, photon_energy*n_x,
            photon_energy*n_y, photon_energy*n_z
        ), axis=-1
    )
    p_final = p_four+q_four-photon_four
    e_final = p_final[..., 0]
    p2_final = np.sum(p_final[..., 1:]**2, axis=-1)
    shell_error = np.max(
        np.abs(e_final*e_final-p2_final-rates.M_MU**2)/rates.M_MU**2
    )
    if shell_error > 2e-10:
        raise ArithmeticError(f"Final muon is off shell: {shell_error:.3e}")

    # Time-reversed production convention of rates.py: p_four is the
    # final muon and p_final is the initial muon. Keep this ordering.
    den_s = k_num
    den_u = -2.0*(
        e_b*photon_energy-p_x*photon_energy*n_x-p_z*photon_energy*n_z
    )
    prop_s = (
        rates._slash(p_four+q_four)+rates.M_MU*rates._I4
    )/den_s[..., None, None]
    prop_u = (
        rates._slash(p_four-photon_four)+rates.M_MU*rates._I4
    )/den_u[..., None, None]
    spin_out = rates._slash(p_four)+rates.M_MU*rates._I4
    spin_in = rates._slash(p_final)+rates.M_MU*rates._I4

    eps_l_ax = np.array([k_a/mass, 0, 0, energy/mass], dtype=complex)
    eps_l_v = np.array(
        [-mass/(energy+k_a), 0, 0, mass/(energy+k_a)], dtype=complex
    )
    eps_plus = np.array([0, 1, 1j, 0], dtype=complex)/math.sqrt(2.0)
    eps_minus = np.array([0, 1, -1j, 0], dtype=complex)/math.sqrt(2.0)
    mode_eps = (
        (eps_l_v, eps_l_ax),
        (eps_plus, eps_plus),
        (eps_minus, eps_minus),
    )

    bose_x = photon_energy/temperature
    exp_minus_bose = np.exp(-bose_x)
    one_plus_bose = 1.0/(-np.expm1(-bose_x))
    bose = exp_minus_bose*one_plus_bose
    phase_measure = (
        radial_measure[:, None, None, None]
        *w_mu[None, :, None, None]
        *w_gamma[None, None, :, None]
        *w_phi[None, None, None, :]
        *(photon_energy/c_den)
    )
    # Includes two muon spin states and the integrated initial-muon azimuth.
    prefactor = 1.0/(128.0*math.pi**4*energy)

    charge_results = {}
    for charge_name, charge_sign in (("mu_minus", 1.0), ("mu_plus", -1.0)):
        mu_charge = charge_sign*mu_mu
        f_initial = _fermi((e_b-mu_charge)/temperature)
        f_final = _fermi((e_final-mu_charge)/temperature)
        abs_stat = f_initial*(1.0-f_final)*one_plus_bose
        prod_stat = f_final*(1.0-f_initial)*bose
        # Charge conjugation reverses the relative axial term for mu+ targets.
        ga_charge = charge_sign*g_axial
        production, absorption = np.zeros(3), np.zeros(3)
        min_m2, max_m2 = math.inf, 0.0
        for ih, (eps_v, eps_a) in enumerate(mode_eps):
            gamma_vertex = (
                g_vector*rates._slash(eps_v)
                +ga_charge*rates._slash(eps_a)@rates._G5
            )
            m2 = _polarization_trace(
                prop_s, prop_u, spin_out, spin_in, gamma_vertex
            )
            scale = max(float(np.max(np.abs(m2))), 1.0)
            minimum = float(np.min(m2))
            min_m2 = min(min_m2, minimum)
            if minimum < -2e-10*scale:
                raise ArithmeticError(f"Negative |M|^2 beyond roundoff: {minimum:.3e}")
            m2 = np.maximum(m2, 0.0)
            max_m2 = max(max_m2, float(np.max(m2)))
            production[ih] = prefactor*np.sum(phase_measure*m2*prod_stat)
            absorption[ih] = prefactor*np.sum(phase_measure*m2*abs_stat)
        charge_results[charge_name] = {
            "production": production, "absorption": absorption,
            "minimum_matrix_element_before_roundoff_clip": min_m2,
            "maximum_matrix_element": max_m2,
        }

    production = charge_results["mu_minus"]["production"]+charge_results["mu_plus"]["production"]
    absorption = charge_results["mu_minus"]["absorption"]+charge_results["mu_plus"]["absorption"]
    return {
        "production": production, "absorption": absorption,
        "mode_order": ["L", "+", "-"],
        "polarization_basis": "medium rest frame; A' momentum along +z",
        "charge_resolved": charge_results,
        "diagnostics": {
            "final_muon_shell_relative_error": float(shell_error),
            "x_max": float(x_max), "orders": list(orders),
            "couplings_normalized_to_gX": {
                "g_vector": g_vector, "g_axial": g_axial
            },
        },
    }


def moving_muon_point_kernel(
    mass, energy, p_magnitude, cos_theta_mu, cos_theta_gamma, phi_gamma,
    g_vector=0.0, g_axial=-1.0, charge_sign=1.0
):
    """Pointwise kernel plus photon-Ward residual for regression tests."""
    mass, energy, p_magnitude = map(float, (mass, energy, p_magnitude))
    cm, cg, phi = map(float, (cos_theta_mu, cos_theta_gamma, phi_gamma))
    gv, ga, charge_sign = map(float, (g_vector, g_axial, charge_sign))
    if mass <= 0 or energy < mass or p_magnitude < 0 or abs(cm) > 1 or abs(cg) > 1:
        raise ValueError("Invalid pointwise kinematics")
    if charge_sign not in (-1.0, 1.0):
        raise ValueError("charge_sign must be +/-1")
    k_a = math.sqrt(energy*energy-mass*mass)
    e = math.hypot(rates.M_MU, p_magnitude)
    p = np.array([
        e, p_magnitude*math.sqrt(max(0.0, 1-cm*cm)), 0.0, p_magnitude*cm
    ])
    n = np.array([
        math.sqrt(max(0.0, 1-cg*cg))*math.cos(phi),
        math.sqrt(max(0.0, 1-cg*cg))*math.sin(phi), cg
    ])
    q = np.array([energy, 0.0, 0.0, k_a])
    p_dot_q = e*energy-p[3]*k_a
    c_den = e+energy-np.dot(p[1:],n)-k_a*cg
    photon_energy = (mass*mass+2*p_dot_q)/(2*c_den)
    photon = np.r_[photon_energy, photon_energy*n]
    p_final = p+q-photon
    shell = abs(
        p_final[0]**2-np.dot(p_final[1:],p_final[1:])-rates.M_MU**2
    )/rates.M_MU**2
    den_s = mass*mass+2*p_dot_q
    den_u = -2*(e*photon_energy-np.dot(p[1:],photon_energy*n))
    prop_s = (rates._slash(p+q)+rates.M_MU*rates._I4)/den_s
    prop_u = (rates._slash(p-photon)+rates.M_MU*rates._I4)/den_u
    spin_out = rates._slash(p)+rates.M_MU*rates._I4
    spin_in = rates._slash(p_final)+rates.M_MU*rates._I4
    eps_l_ax = np.array([k_a/mass,0,0,energy/mass],complex)
    eps_l_v = np.array([-mass/(energy+k_a),0,0,mass/(energy+k_a)],complex)
    eps_plus = np.array([0,1,1j,0],complex)/math.sqrt(2)
    eps_minus = np.array([0,1,-1j,0],complex)/math.sqrt(2)
    modes = ((eps_l_v,eps_l_ax),(eps_plus,eps_plus),(eps_minus,eps_minus))
    m2_values, ward_values = [], []
    for eps_v, eps_a in modes:
        vertex = gv*rates._slash(eps_v)+charge_sign*ga*rates._slash(eps_a)@rates._G5
        m2 = _polarization_trace(prop_s,prop_u,spin_out,spin_in,vertex)
        ward_amp = (
            vertex@prop_s@rates._slash(photon)
            +rates._slash(photon)@prop_u@vertex
        )
        ward_bar = rates._GAMMA[0]@rates._dagger(ward_amp)@rates._GAMMA[0]
        ward_trace = np.trace(spin_out@ward_amp@spin_in@ward_bar).real/2
        scale = max(abs(float(m2))/rates.E2,1.0)
        m2_values.append(float(m2))
        ward_values.append(abs(float(ward_trace))/scale)
    return {
        "photon_energy_MeV": float(photon_energy),
        "final_muon_energy_MeV": float(p_final[0]),
        "final_muon_shell_relative_error": float(shell),
        "matrix_element_squared_by_mode": m2_values,
        "photon_ward_relative_residual_by_mode": ward_values,
    }


def thermal_compton_emissivity(
    mass, temperature, mu_mu, g_vector=0.0, g_axial=-1.0,
    energy_order=12, orders=(12,8,8,8), x_max=36.0
):
    """Complete local A' momentum integral; output emissivity per g_X^2."""
    mass, temperature, mu_mu = map(float,(mass,temperature,mu_mu))
    if mass <= 0 or temperature <= 0 or energy_order < 4 or x_max <= 0:
        raise ValueError("Invalid mass, temperature, energy order, or cutoff")
    z, w = leggauss(energy_order)
    y_max = math.sqrt(x_max)
    y = 0.5*y_max*(z+1.0)
    w_y = 0.5*y_max*w
    omega = mass+temperature*y*y
    q_momentum = np.sqrt(np.maximum((omega-mass)*(omega+mass),0.0))
    production, absorption = np.zeros((energy_order,3)), np.zeros((energy_order,3))
    charge_production = {
        "mu_minus": np.zeros((energy_order,3)),
        "mu_plus": np.zeros((energy_order,3)),
    }
    charge_absorption = {
        "mu_minus": np.zeros((energy_order,3)),
        "mu_plus": np.zeros((energy_order,3)),
    }
    shell_errors = []
    for i, omega_i in enumerate(omega):
        local = moving_muon_compton_rates(
            mass,float(omega_i),temperature,mu_mu,g_vector,g_axial,orders
        )
        production[i], absorption[i] = local["production"], local["absorption"]
        for charge in ("mu_minus","mu_plus"):
            charge_production[charge][i] = local["charge_resolved"][charge]["production"]
            charge_absorption[charge][i] = local["charge_resolved"][charge]["absorption"]
        shell_errors.append(local["diagnostics"]["final_muon_shell_relative_error"])
    weight = 2.0*temperature*y*w_y*omega**2*q_momentum/(2.0*math.pi**2)
    q_mode = np.einsum("i,ih->h",weight,production)
    q_charge = {
        charge: np.einsum("i,ih->h",weight,values)
        for charge,values in charge_production.items()
    }
    balance = np.exp(-omega/temperature)[:,None]*absorption
    rel = np.abs(production-balance)/np.maximum(np.abs(production),1e-300)
    return {
        "mass_MeV": mass, "temperature_MeV": temperature,
        "mode_order": ["L", "+", "-"],
        "polarization_basis": "medium rest frame; A' momentum along +z",
        "muon_chemical_potential_MeV": mu_mu,
        "couplings_normalized_to_gX": {
            "g_vector": float(g_vector), "g_axial": float(g_axial)
        },
        "energy_MeV": omega.tolist(),
        "mediator_momentum_MeV": q_momentum.tolist(),
        "production_MeV": production.tolist(),
        "absorption_MeV": absorption.tolist(),
        "production_by_charge_MeV": {
            k:v.tolist() for k,v in charge_production.items()
        },
        "absorption_by_charge_MeV": {
            k:v.tolist() for k,v in charge_absorption.items()
        },
        "emissivity_by_mode_MeV5": q_mode.tolist(),
        "emissivity_by_charge_and_mode_MeV5": {
            k:v.tolist() for k,v in q_charge.items()
        },
        "emissivity_total_MeV5": float(np.sum(q_mode)),
        "max_detailed_balance_relative_error": float(np.max(rel)),
        "max_final_muon_shell_relative_error": float(max(shell_errors)),
        "quadrature": {
            "energy_order": energy_order, "inner_orders": list(orders),
            "x_max": x_max
        },
    }
