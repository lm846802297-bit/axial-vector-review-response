import math
import unittest

import numpy as np

try:
    from .compton_detailed_balance_audit import (
        ALPHA_DEFAULT, M_MU_DEFAULT, exact_cross_section,
        exact_momentum_ratio, inverse_vector_energy_same_s,
        klein_nishina_total, no_recoil_velocity, occupation_detailed_balance_ratio,
        phase_space_cross_section_ratio, sigma_forward_B14, audit_point,
    )
except ImportError:
    from compton_detailed_balance_audit import (
        ALPHA_DEFAULT, M_MU_DEFAULT, exact_cross_section,
        exact_momentum_ratio, inverse_vector_energy_same_s,
        klein_nishina_total, no_recoil_velocity, occupation_detailed_balance_ratio,
        phase_space_cross_section_ratio, sigma_forward_B14, audit_point,
    )


class ComptonDetailedBalanceAuditTests(unittest.TestCase):
    def test_direct_forward_reverse_cross_sections_reproduce_exact_phase_space_ratio(self):
        e = math.sqrt(4.0 * math.pi * ALPHA_DEFAULT)
        for m_v, omega in ((1.0, 10.0), (10.0, 20.0), (10.0, 50.0)):
            e_v = inverse_vector_energy_same_s(M_MU_DEFAULT, m_v, omega)
            forward = exact_cross_section(
                M_MU_DEFAULT, 0.0, m_v, omega, e, 1.0, 64)
            reverse = exact_cross_section(
                M_MU_DEFAULT, m_v, 0.0, e_v, 1.0, e, 64)
            direct = forward / reverse
            expected = phase_space_cross_section_ratio(
                M_MU_DEFAULT, m_v, omega)
            self.assertAlmostEqual(direct / expected, 1.0, places=10)

    def test_b15_and_b16_exact_kinematic_coefficients_agree(self):
        for m_v, omega in ((1.0, 10.0), (10.0, 20.0), (10.0, 50.0)):
            row = audit_point(M_MU_DEFAULT, m_v, omega, angle_order=48)
            self.assertAlmostEqual(
                row["B15_B16_exact_kinematic_coefficient_residual"], 0.0,
                delta=2e-10)

    def test_no_recoil_limit_reduces_to_b18(self):
        m_v, omega = 10.0, 20.0
        v = no_recoil_velocity(m_v, omega)
        r = exact_momentum_ratio(1.0e9, m_v, omega)
        self.assertAlmostEqual(r / v, 1.0, delta=2e-7)

    def test_b19_from_fermi_bose_occupation_factors(self):
        ratio, expected, omega_v = occupation_detailed_balance_ratio(
            e_mu_initial=M_MU_DEFAULT + 22.0,
            e_gamma=31.0,
            e_mu_final=M_MU_DEFAULT + 14.0,
            chemical_potential=74.0,
            temperature=28.0,
        )
        self.assertAlmostEqual(omega_v, 39.0, places=12)
        self.assertAlmostEqual(ratio / expected, 1.0, places=12)

    def test_exact_qed_amplitude_reproduces_klein_nishina(self):
        omega = 20.0
        e = math.sqrt(4.0 * math.pi * ALPHA_DEFAULT)
        exact = exact_cross_section(
            M_MU_DEFAULT, 0.0, 0.0, omega, e, e, 96)
        expected = klein_nishina_total(omega, M_MU_DEFAULT)
        self.assertAlmostEqual(exact / expected, 1.0, delta=2e-10)

    def test_b14_is_recovered_in_the_thomson_no_recoil_limit(self):
        omega, m_v = 0.5, 0.01
        e = math.sqrt(4.0 * math.pi * ALPHA_DEFAULT)
        exact = exact_cross_section(
            M_MU_DEFAULT, 0.0, m_v, omega, e, 1.0, 96)
        b14 = sigma_forward_B14(M_MU_DEFAULT, m_v, omega)
        self.assertAlmostEqual(exact / b14, 1.0, delta=0.02)

    def test_exact_recoil_threshold_exceeds_no_recoil_threshold(self):
        m_v = 10.0
        threshold = m_v + m_v*m_v/(2.0*M_MU_DEFAULT)
        omega = threshold - 1e-4
        e_v = inverse_vector_energy_same_s(M_MU_DEFAULT, m_v, omega)
        self.assertLess(e_v, m_v)
        e = math.sqrt(4.0*math.pi*ALPHA_DEFAULT)
        self.assertEqual(exact_cross_section(
            M_MU_DEFAULT, 0.0, m_v, omega, e, 1.0, 64), 0.0)

    def test_massive_vector_threshold_is_not_the_no_recoil_threshold(self):
        m_v = 10.0
        omega = 10.1
        self.assertGreater(no_recoil_velocity(m_v, omega), 0.0)
        self.assertLess(
            inverse_vector_energy_same_s(M_MU_DEFAULT, m_v, omega), m_v)


if __name__ == "__main__":
    unittest.main()
