"""Independent physics limits for the mode-resolved SN rate kernels."""
import importlib.util
import unittest
from pathlib import Path

import numpy as np
from numpy.testing import assert_allclose

import rates


def reference_module():
    path = Path(__file__).resolve().parents[1] / "stellar-cooling-original-uv-model-20261105" / "stellar_semi_compton_axial_matrix_element.py"
    spec = importlib.util.spec_from_file_location("reference", path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class ComptonTests(unittest.TestCase):
    def test_crossed_published_full_polarization_sum(self):
        """Liu--Miller Eq20, with the independent absorption average factor."""
        m = rates.M_MU
        for mass, energy in [(0.01, 1), (1, 30), (10, 40), (50, 100), (250, 350)]:
            cosines = np.array([-0.8, 0, 0.8])
            eg, squared = rates.compton_matrix_elements(mass, [energy], cosines)
            s = mass**2 + 2*m*energy
            u = -2*m*eg[0]
            t = mass**2-s-u
            ratio = (s+u)**2/(s*u)
            bracket = m*m*((s+u)/(s*u))**2-t/(s*u)
            axial = 4-(2+4*m*m/mass**2)*ratio+4*(mass**2-4*m*m)*bracket
            assert_allclose(squared[0].sum(axis=-1), 2*rates.E2*axial, rtol=2e-9)
            _, vector_squared = rates.compton_matrix_elements(mass, [energy], cosines, current="vector")
            vector = 4-2*ratio+4*(mass**2+2*m*m)*bracket
            assert_allclose(vector_squared[0].sum(axis=-1), 2*rates.E2*vector, rtol=2e-9)

    def test_explicit_spinors_per_mode(self):
        """Compare the batched trace with the independently coded Dirac spinors."""
        ref = reference_module()
        mass, energy, cosine = 7.0, 41.0, 0.32
        eg, result = rates.compton_matrix_elements(mass, [energy], [cosine])
        eg = float(eg[0, 0])
        k = np.sqrt(energy**2-mass**2)
        sine = np.sqrt(1-cosine**2)
        p = np.array([rates.M_MU, 0, 0, 0])
        q = np.array([energy, 0, 0, k])
        photon = np.array([eg, eg*sine, 0, eg*cosine])
        pp = p+q-photon
        eps_photon = [np.array([0, cosine, 0, -sine]), np.array([0, 0, 1, 0])]
        eps_mediator = [np.array([k/mass, 0, 0, energy/mass]),
                        np.array([0, 1, 1j, 0])/np.sqrt(2),
                        np.array([0, 1, -1j, 0])/np.sqrt(2)]
        direct = []
        for eps in eps_mediator:
            total = 0.
            for initial in range(2):
                for final in range(2):
                    ui = ref.u_spinor(pp, rates.M_MU, initial)
                    uf = ref.u_spinor(p, rates.M_MU, final)
                    for egamma in eps_photon:
                        matrix = ref.amplitude_matrix(pp, photon, p, q, rates.M_MU, egamma, eps, 0, 1)
                        total += abs(uf.conj() @ ref.GAMMA[0] @ matrix @ ui)**2
            direct.append(total*rates.E2/2)
        assert_allclose(result[0, 0], direct, rtol=2e-12)

    def test_vector_thomson_limit(self):
        _, weights = rates.compton_kernels(1e-8, [1e-4], order=64, current="vector")
        sigma_transverse = weights[0, :, 1].sum()
        expected = 2*rates.ALPHA/(3*rates.M_MU**2)
        self.assertAlmostEqual(sigma_transverse/expected, 1, delta=3e-6)
        self.assertLess(weights[0, :, 0].sum()/sigma_transverse, 1e-7)

    def test_axial_longitudinal_scaling(self):
        _, small = rates.compton_kernels(0.001, [30], order=64)
        _, large = rates.compton_kernels(0.002, [30], order=64)
        self.assertAlmostEqual(small[0, :, 0].sum()/large[0, :, 0].sum(), 4, delta=1e-5)

    def test_mediator_rest_limit_isotropic_and_finite(self):
        for current in ["axial", "vector"]:
            for mass in [1., 50., 250.]:
                _, weights = rates.compton_kernels(mass, [mass], order=64, current=current)
                integrated = weights[0].sum(axis=0)
                self.assertTrue(np.all(np.isfinite(integrated)))
                # Vector Ward subtraction in the small-M rest limit gives
                # ~1e-12 relative floating-point cancellation in the trace.
                assert_allclose(integrated, integrated[0], rtol=5e-11)

    def test_compton_broadcast_and_stimulation(self):
        kernels = rates.compton_kernels(1, [10, 50], order=32)
        base = rates.compton_absorption(kernels, np.array([1e-5, 30]), np.array([10., 20.]))
        self.assertEqual(base.shape, (2, 2, 3))
        assert_allclose(base[0], 10*kernels[1].sum(axis=1), rtol=1e-12)
        self.assertTrue(np.all(base[1] >= 20*kernels[1].sum(axis=1)))

    def test_photon_ward_identity(self):
        for current in ["axial", "vector"]:
            eg, physical = rates.compton_matrix_elements(7., [41.], [-0.7, 0.2, 0.8], current)
            _, ward = rates.compton_matrix_elements(7., [41.], [-0.7, 0.2, 0.8], current, photon_ward=True)
            residual = np.max(abs(ward)/(eg[..., None]**2*physical))
            self.assertLess(residual, 2e-12)

    def test_compton_angle_quadrature_convergence(self):
        for mass in [0.01, 10., 250.]:
            energies = mass+np.array([0.1, 30., 200., 1000.])
            coarse = rates.compton_absorption(rates.compton_kernels(mass, energies, order=32), 35., 1.)
            fine = rates.compton_absorption(rates.compton_kernels(mass, energies, order=64), 35., 1.)
            assert_allclose(coarse, fine, rtol=3e-6)


class DecayTests(unittest.TestCase):
    def test_neutrino_vacuum_limit_and_rest_isotropy(self):
        mass = 10.
        energies = np.array([10., 30.])
        prod, absorp = rates.neutrino_rates(mass, energies, 1e-4, 0.)
        assert_allclose(prod, 0., atol=1e-100)
        expected = mass**2/(energies*12*np.pi)
        assert_allclose(absorp, np.repeat(expected[:, None], 3, axis=1), rtol=2e-13)

    def test_neutrino_detailed_balance_and_circular_modes(self):
        energy = np.array([12., 40., 100.])
        prod, absorp = rates.neutrino_rates(10, energy, 30, 45)
        assert_allclose(prod, np.exp(-energy[:, None]/30)*absorp, rtol=3e-13)
        self.assertTrue(np.any(abs(prod[:, 1]-prod[:, 2]) > 1e-5))
        reversed_prod, _ = rates.neutrino_rates(10, energy, 30, -45)
        assert_allclose(prod[:, [0, 2, 1]], reversed_prod, rtol=3e-13)

    def test_neutrino_total_matches_scalar_phase_integral(self):
        """Blinov Eq23: total spin sum = 3 times averaged decay width."""
        mass, energy, temp, chemical = 10., 40., 30., 24.
        z, w = np.polynomial.legendre.leggauss(120)
        k = np.sqrt(energy**2-mass**2)
        integral = 0.
        for mu in [chemical, 0.]:
            integral += np.dot(w, 1/(np.exp(((energy+k*z)/2-mu)/temp)+1)
                               /(np.exp(((energy-k*z)/2+mu)/temp)+1))/2
        expected = 3*mass/energy*mass/(24*np.pi)*integral
        prod, _ = rates.neutrino_rates(mass, energy, temp, chemical)
        self.assertAlmostEqual(prod.sum()/expected, 1, delta=2e-13)

    def test_charged_muon_decay_width_and_balance(self):
        for current in ["axial", "vector"]:
            for mass in [200., 212., 300., 500.]:
                energy = mass*1.2
                prod, absorp = rates.charged_muon_decay_rates(mass, energy, 1e-4, 0., current=current)
                if mass <= 2*rates.M_MU:
                    assert_allclose(absorp, 0)
                    continue
                beta = np.sqrt(1-4*rates.M_MU**2/mass**2)
                width = mass/(12*np.pi)*(beta**3 if current=="axial" else beta*(1+2*rates.M_MU**2/mass**2))
                assert_allclose(absorp, mass/energy*width, rtol=3e-13)
                prod, absorp = rates.charged_muon_decay_rates(mass, energy, 30, 100, current=current)
                assert_allclose(prod, np.exp(-energy/30)*absorp, rtol=3e-13)

    def test_decay_broadcast_grid(self):
        prod, absorp = rates.neutrino_rates(10, np.array([11., 30., 70.])[None, :],
                                           np.array([10., 30.])[:, None], np.array([0., 25.])[:, None])
        self.assertEqual(prod.shape, (2, 3, 3))
        self.assertTrue(np.all(absorp >= prod))

    def test_dimuon_angular_weights_from_dirac_trace(self):
        """Verify longitudinal/transverse angular shapes directly, not via widths."""
        mass = 300.
        beta = np.sqrt(1-4*rates.M_MU**2/mass**2)
        z = np.array([-0.8, 0., 0.6])
        momentum = mass*beta/2
        p1 = np.stack([np.full_like(z, mass/2), momentum*np.sqrt(1-z*z), np.zeros_like(z), momentum*z], axis=-1)
        p2 = p1.copy()
        p2[:, 1:] *= -1
        for current in ["axial", "vector"]:
            traced = []
            for eps in [np.array([0, 0, 0, 1]), np.array([0, 1, 1j, 0])/np.sqrt(2)]:
                vertex = rates._slash(eps)
                if current == "axial":
                    vertex = vertex@rates._G5
                conjugate = rates._GAMMA[0]@vertex.conj().T@rates._GAMMA[0]
                traced.append(np.trace((rates._slash(p1)+rates.M_MU*np.eye(4))@vertex
                                       @(rates._slash(p2)-rates.M_MU*np.eye(4))@conjugate,
                                       axis1=-2, axis2=-1).real)
            if current == "axial":
                expected = [2*mass**2*beta**2*(1-z*z), mass**2*beta**2*(1+z*z)]
            else:
                expected = [2*mass**2*(1-beta**2*z*z), 2*mass**2*(1-beta**2*(1-z*z)/2)]
            assert_allclose(traced, expected, rtol=2e-13)


if __name__ == "__main__":
    unittest.main(verbosity=2)
