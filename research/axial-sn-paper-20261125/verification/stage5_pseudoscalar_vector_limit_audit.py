import math
import platform
import hashlib
import json
import sys
import numpy as np

M = 105.6583755
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
SIGMA = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
GAMMA = np.array([np.block([[I2, Z2], [Z2, -I2]])] +
                 [np.block([[Z2, s], [-s, Z2]]) for s in SIGMA])
G5 = 1j * GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3]
I4 = np.eye(4, dtype=complex)
METRIC = np.array([1., -1., -1., -1.])


def slash(v):
    return np.einsum('a,aij->ij', np.asarray(v) * METRIC, GAMMA)


def spinor(p, spin):
    chi = np.zeros(2, dtype=complex)
    chi[spin] = 1.0
    sigma_p = sum(SIGMA[i] * p[i + 1] for i in range(3))
    return math.sqrt(p[0] + M) * np.r_[chi, sigma_p @ chi / (p[0] + M)]


def ubar(u):
    return u.conj().T @ GAMMA[0]


def kinematics(mass, photon_energy, cosine):
    p = np.array([M, 0., 0., 0.])
    k = np.array([photon_energy, 0., 0., photon_energy])
    a = M + photon_energy
    b = photon_energy * cosine
    d = M * photon_energy + mass * mass / 2.0
    disc = d * d - (a * a - b * b) * mass * mass
    if disc < -1e-11 * max(d * d, 1.0):
        raise ValueError('unphysical kinematics')
    q0 = (a * d + b * math.sqrt(max(disc, 0.0))) / (a * a - b * b)
    qabs = math.sqrt(max(q0 * q0 - mass * mass, 0.0))
    q = np.array([q0, qabs * math.sqrt(max(1.0 - cosine * cosine, 0.0)), 0., qabs * cosine])
    pp = p + k - q
    shell = abs(pp[0] ** 2 - np.dot(pp[1:], pp[1:]) - M * M) / (M * M)
    return p, k, q, pp, qabs, shell


def amplitude(p, k, q, eps_a, eps_gamma, current):
    s_mom = p + k
    u_mom = p - q
    ds = s_mom[0] ** 2 - np.dot(s_mom[1:], s_mom[1:]) - M * M
    du = u_mom[0] ** 2 - np.dot(u_mom[1:], u_mom[1:]) - M * M
    prop_s = (slash(s_mom) + M * I4) / ds
    prop_u = (slash(u_mom) + M * I4) / du
    vg = slash(eps_gamma)
    if current == 'axial':
        vx = slash(eps_a) @ G5
    elif current == 'vector':
        vx = slash(eps_a)
    elif current == 'pseudoscalar':
        vx = G5
    else:
        raise ValueError(current)
    return vx @ prop_s @ vg + vg @ prop_u @ vx


def spin_summed_mode(mass, photon_energy, cosine, eps_a, current):
    p, k, q, pp, qabs, shell = kinematics(mass, photon_energy, cosine)
    photon_modes = (np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.]))
    total = 0.0
    for eps_gamma in photon_modes:
        amp = amplitude(p, k, q, eps_a, eps_gamma, current)
        for si in range(2):
            ui = spinor(p, si)
            for sf in range(2):
                uf = spinor(pp, sf)
                total += abs(ubar(uf) @ amp @ ui) ** 2 / 2.0
    return total, shell, qabs


def amplitude_level_ward_residual(mass, photon_energy, order=64):
    z, _ = np.polynomial.legendre.leggauss(order)
    y_goldstone = 2.0 * M / mass
    max_residual = 0.0
    max_vector_residual = 0.0
    for c in z:
        p, k, q, pp, qabs, shell = kinematics(mass, photon_energy, float(c))
        nhat = q[1:] / np.linalg.norm(q[1:])
        ref = np.array([0., 1., 0.]) if abs(nhat[1]) < 0.9 else np.array([1., 0., 0.])
        e1 = np.cross(ref, nhat)
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(nhat, e1)
        e2 /= np.linalg.norm(e2)
        eps_t1 = np.r_[0., e1]
        eps_t2 = np.r_[0., e2]
        for eps_gamma in (np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.])):
            amp_aq = amplitude(p, k, q, q / mass, eps_gamma, 'axial')
            amp_ps = amplitude(p, k, q, np.zeros(4), eps_gamma, 'pseudoscalar')
            amp_vq = amplitude(p, k, q, q / mass, eps_gamma, 'vector')
            amp_vt1 = amplitude(p, k, q, eps_t1, eps_gamma, 'vector')
            amp_vt2 = amplitude(p, k, q, eps_t2, eps_gamma, 'vector')
            for si in range(2):
                ui = spinor(p, si)
                for sf in range(2):
                    uf = spinor(pp, sf)
                    lhs = ubar(uf) @ amp_aq @ ui
                    rhs = -y_goldstone * (ubar(uf) @ amp_ps @ ui)
                    residual = abs(lhs-rhs) / max(abs(lhs), abs(rhs), 1e-300)
                    max_residual = max(max_residual, float(residual))
                    vq = abs(ubar(uf) @ amp_vq @ ui)
                    vt1 = abs(ubar(uf) @ amp_vt1 @ ui)
                    vt2 = abs(ubar(uf) @ amp_vt2 @ ui)
                    vt = math.sqrt(vt1*vt1 + vt2*vt2)
                    max_vector_residual = max(max_vector_residual, float(vq/max(vt,1e-300)))
    return max_residual, max_vector_residual


def integrated_cross_sections(mass, photon_energy, order=160):
    z, w = np.polynomial.legendre.leggauss(order)
    sig_a_l = sig_p = sig_v_l = sig_v_t = 0.0
    max_shell = 0.0
    ward_axial = []
    ward_vector = []
    for c, wc in zip(z, w):
        p, k, q, pp, qabs, shell = kinematics(mass, photon_energy, float(c))
        max_shell = max(max_shell, shell)
        phase = qabs / photon_energy * wc
        nhat = q[1:] / np.linalg.norm(q[1:])
        eps_l = np.r_[qabs / mass, q[0] * nhat / mass]
        eps_l_shift = eps_l - q / mass
        ref = np.array([0., 1., 0.]) if abs(nhat[1]) < 0.9 else np.array([1., 0., 0.])
        e1 = np.cross(ref, nhat)
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(nhat, e1)
        e2 /= np.linalg.norm(e2)
        eps_t1 = np.r_[0., e1]
        eps_t2 = np.r_[0., e2]
        a_l, _, _ = spin_summed_mode(mass, photon_energy, float(c), eps_l, 'axial')
        a_q, _, _ = spin_summed_mode(mass, photon_energy, float(c), q / mass, 'axial')
        p_s, _, _ = spin_summed_mode(mass, photon_energy, float(c), np.zeros(4), 'pseudoscalar')
        v_l, _, _ = spin_summed_mode(mass, photon_energy, float(c), eps_l_shift, 'vector')
        v_q, _, _ = spin_summed_mode(mass, photon_energy, float(c), q / mass, 'vector')
        v_t1, _, _ = spin_summed_mode(mass, photon_energy, float(c), eps_t1, 'vector')
        v_t2, _, _ = spin_summed_mode(mass, photon_energy, float(c), eps_t2, 'vector')
        sig_a_l += phase * a_l
        sig_p += phase * p_s
        sig_v_l += phase * v_l
        sig_v_t += phase * (v_t1 + v_t2)
        y_goldstone = 2.0 * M / mass
        ward_axial.append(abs(a_q - y_goldstone**2 * p_s) / max(a_q, y_goldstone**2 * p_s, 1e-300))
        ward_vector.append(v_q / max(v_t1 + v_t2, 1e-300))
    y_goldstone = 2.0 * M / mass
    pseudo_scaled = y_goldstone * y_goldstone * sig_p
    return {
        'mass_MeV': mass,
        'photon_energy_MeV': photon_energy,
        'mass_over_photon_energy': mass / photon_energy,
        'sigma_axial_longitudinal': sig_a_l,
        'sigma_pseudoscalar_unit_y': sig_p,
        'goldstone_yukawa_per_gA': y_goldstone,
        'sigma_goldstone_pseudoscalar': pseudo_scaled,
        'physical_L_vs_Goldstone_relative': abs(sig_a_l / pseudo_scaled - 1.0),
        'exact_qWard_relative_max': max(ward_axial),
        'vector_L_over_T': sig_v_l / sig_v_t,
        'vector_L_over_T_divided_by_m2_over_Egamma2': (sig_v_l / sig_v_t) / (mass / photon_energy)**2,
        'vector_qWard_over_T_max': max(ward_vector),
        'max_final_muon_shell_relative_error': max_shell,
        'angular_order': order,
    }


if __name__ == '__main__':
    cases = []
    for energy in (0.05, 0.1, 0.5, 1.0):
        for ratio in (0.1, 0.01, 0.001):
            mass = energy * ratio
            cases.append(integrated_cross_sections(mass, energy))
    amplitude_ward = []
    for energy in (0.05, 0.1, 0.5, 1.0):
        for ratio in (0.1, 0.01, 0.001):
            amplitude_ward.append({
                'photon_energy_MeV': energy,
                'mass_over_photon_energy': ratio,
                'axial_goldstone_amplitude_relative_residual': amplitude_level_ward_residual(energy*ratio, energy)[0],
                'vector_ward_amplitude_over_transverse_max': amplitude_level_ward_residual(energy*ratio, energy)[1],
            })
    convergence = []
    for order in (80, 160, 240):
        row = integrated_cross_sections(1.0e-4, 0.1, order=order)
        convergence.append({
            'angular_order': order,
            'physical_L_vs_Goldstone_relative': row['physical_L_vs_Goldstone_relative'],
            'vector_L_over_T_divided_by_m2_over_Egamma2': row['vector_L_over_T_divided_by_m2_over_Egamma2'],
        })
    source = open(__file__, 'rb').read()
    max_goldstone = max(x['physical_L_vs_Goldstone_relative'] for x in cases)
    max_axial_ward = max(x['exact_qWard_relative_max'] for x in cases)
    max_vector_ward = max(x['vector_qWard_over_T_max'] for x in cases)
    max_shell = max(x['max_final_muon_shell_relative_error'] for x in cases)
    max_vector_coefficient_error = max(abs(x['vector_L_over_T_divided_by_m2_over_Egamma2'] - 0.5) for x in cases)
    max_amplitude_ward = max(x['axial_goldstone_amplitude_relative_residual'] for x in amplitude_ward)
    max_vector_amplitude_ward = max(x['vector_ward_amplitude_over_transverse_max'] for x in amplitude_ward)
    acceptance = {
        'axial_ward_identity': bool(max_axial_ward < 1.0e-5 and max_amplitude_ward < 1.0e-6),
        'goldstone_equivalence_all_points': bool(max_goldstone < 1.0e-4),
        'conserved_vector_ward_identity': bool(max_vector_ward < 1.0e-15 and max_vector_amplitude_ward < 1.0e-5),
        'vector_longitudinal_m2_suppression': bool(max_vector_coefficient_error < 5.0e-3),
        'final_muon_mass_shell': bool(max_shell < 1.0e-14),
        'quadrature_convergence': bool(abs(convergence[-1]['vector_L_over_T_divided_by_m2_over_Egamma2'] - convergence[0]['vector_L_over_T_divided_by_m2_over_Egamma2']) < 1.0e-9),
    }
    result = {
        'title': 'Independent low-mass axial-to-pseudoscalar and conserved-vector limit audit',
        'python': sys.version,
        'platform': platform.platform(),
        'numpy': np.__version__,
        'source_sha256': hashlib.sha256(source).hexdigest(),
        'method': 'Explicit Dirac spinors; exact two-diagram muon Compton amplitude; exact two-body recoil; 160-point Gauss-Legendre angular integration; common d sigma/d cos(theta) phase-space factor q_Aprime/E_gamma.',
        'inputs': {'muon_mass_MeV': M, 'photon_energy_MeV': [0.05, 0.1, 0.5, 1.0], 'mass_over_photon_energy': [0.1, 0.01, 0.001], 'angular_order': 160},
        'cases': cases,
        'convergence': convergence,
        'amplitude_level_ward_checks': amplitude_ward,
        'summary': {
            'max_axial_ward_relative_residual': max_axial_ward,
            'max_axial_goldstone_amplitude_relative_residual': max_amplitude_ward,
            'max_vector_ward_amplitude_over_transverse': max_vector_amplitude_ward,
            'max_physical_L_vs_Goldstone_relative_difference': max_goldstone,
            'max_conserved_vector_qWard_over_T': max_vector_ward,
            'max_vector_coefficient_deviation_from_half': max_vector_coefficient_error,
            'max_final_muon_shell_relative_error': max_shell,
        },
        'acceptance': acceptance,
        'all_checks_pass': all(acceptance.values()),
    }
    if not result['all_checks_pass']:
        raise SystemExit('low-mass limit audit failed acceptance')
    print(json.dumps(result, indent=2))
