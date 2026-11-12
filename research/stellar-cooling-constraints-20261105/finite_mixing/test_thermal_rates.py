import math
import unittest
import numpy as np
from numpy.polynomial.legendre import leggauss

import rates
from finite_mixing.moving_muon_compton import (
    moving_muon_compton_rates,
    moving_muon_point_kernel,
    thermal_compton_emissivity,
)
from finite_mixing.thermal_dimuon import thermal_dimuon_emissivity


def _fermi(x):
    return np.exp(-np.logaddexp(0.0,x))


def _cold_dilute_density(T,mu,order=160):
    z,w=leggauss(order)
    xmax=max(36.0,max(abs(mu)-rates.M_MU,0.0)/T+36.0)
    t=.5*math.sqrt(xmax)*(z+1.0)
    w=.5*math.sqrt(xmax)*w
    x=t*t
    E=rates.M_MU+T*x
    p=np.sqrt(T*x*(2*rates.M_MU+T*x))
    total=0.0
    for muq in (mu,-mu):
        f=_fermi((E-muq)/T)
        total += np.sum(w*2*T*E*p*t*f)/math.pi**2
    return total


def _stationary_vsigma(mass,energy,current,order=128):
    z,w=leggauss(order)
    eg,msq=rates.compton_matrix_elements(mass,[energy],z,current=current)
    K=math.sqrt(energy*energy-mass*mass)
    den=rates.M_MU+energy-K*z
    factor=eg[0]/(64*math.pi**2*rates.M_MU*energy*den)*(2*math.pi*w)
    return np.sum(factor[:,None]*msq[0],axis=0)


class MovingMuonComptonKernelTests(unittest.TestCase):
    def test_stationary_muon_point_matches_existing_rate_kernel(self):
        mass,energy,cosine=10.0,30.0,0.3
        for current,gv,ga in (("vector",1.0,0.0),("axial",0.0,-1.0)):
            with self.subTest(current=current):
                point=moving_muon_point_kernel(
                    mass,energy,0.0,0.4,cosine,0.7,gv,ga,1.0
                )
                _,reference=rates.compton_matrix_elements(
                    mass,[energy],[cosine],current=current
                )
                np.testing.assert_allclose(
                    point["matrix_element_squared_by_mode"],
                    reference[0,0],rtol=3e-12,atol=1e-13
                )

    def test_photon_ward_identity_for_moving_muon_and_both_charges(self):
        for charge in (+1.0,-1.0):
            point=moving_muon_point_kernel(
                10.0,30.0,80.0,0.4,-0.3,1.2,0.2,-0.9,charge
            )
            self.assertLess(point["final_muon_shell_relative_error"],1e-10)
            self.assertLess(max(point["photon_ward_relative_residual_by_mode"]),1e-9)

    def test_moving_muon_rates_obey_mode_by_mode_detailed_balance(self):
        mass,energy,T,mu=10.0,15.0,25.0,46.674
        result=moving_muon_compton_rates(
            mass,energy,T,mu,0.0,-1.0,orders=(8,8,8,8)
        )
        np.testing.assert_allclose(
            result["production"],
            math.exp(-energy/T)*result["absorption"],
            rtol=3e-12,atol=1e-15
        )
        self.assertLess(result["diagnostics"]["final_muon_shell_relative_error"],1e-10)

    def test_muon_charge_conjugation_cancels_interference_at_zero_chemical_potential(self):
        theta=1e-2
        gv,ga=math.sin(theta)**2,-math.cos(theta)**2
        v=moving_muon_compton_rates(10,15,25,0,1,0,orders=(8,8,8,8))
        a=moving_muon_compton_rates(10,15,25,0,0,-1,orders=(8,8,8,8))
        mixed=moving_muon_compton_rates(10,15,25,0,gv,ga,orders=(8,8,8,8))
        incoherent=gv*gv*v["production"]+ga*ga*a["production"]
        np.testing.assert_allclose(mixed["production"],incoherent,rtol=3e-12,atol=1e-14)

    def test_nonzero_muon_chemical_potential_keeps_charge_resolved_interference(self):
        theta=1e-2
        result=moving_muon_compton_rates(
            10,15,25,46.674,math.sin(theta)**2,-math.cos(theta)**2,
            orders=(10,8,8,8)
        )
        minus=result["charge_resolved"]["mu_minus"]["production"]
        plus=result["charge_resolved"]["mu_plus"]["production"]
        self.assertGreater(float(np.sum(minus)),float(np.sum(plus)))
        self.assertTrue(np.all(result["production"]>0.0))

    def test_cold_dilute_limit_recovers_stationary_target_vsigma(self):
        T=1e-3
        mu=rates.M_MU-5*T
        mass,energy=10.0,15.0
        density=_cold_dilute_density(T,mu)
        result=moving_muon_compton_rates(
            mass,energy,T,mu,0.0,-1.0,orders=(12,8,8,8)
        )
        sigma=_stationary_vsigma(mass,energy,"axial")
        np.testing.assert_allclose(
            result["absorption"]/density,sigma,rtol=5e-4,atol=1e-13
        )

    def test_unpolarized_inverse_rate_matches_eq_5_12(self):
        result=moving_muon_compton_rates(
            10.0,15.0,25.0,46.674,0.0,-1.0,orders=(8,8,8,8)
        )
        normalization=result["unpolarized_normalization"]
        self.assertEqual(result["mode_order"],["L","+","-"])
        self.assertEqual(normalization["initial_photon_polarization_average"],2)
        self.assertEqual(normalization["initial_vector_polarization_average"],3)
        self.assertLess(normalization["Eq_5_12_relative_residual"],3e-10)

    def test_full_compton_emissivity_has_finite_balance_and_shell_errors(self):
        result=thermal_compton_emissivity(
            10.0,19.26522111,46.67432845,0.0,-1.0,
            energy_order=8,orders=(8,8,8,8)
        )
        self.assertGreater(result["emissivity_total_MeV5"],0.0)
        self.assertLess(result["max_detailed_balance_relative_error"],1e-11)
        self.assertLess(result["max_final_muon_shell_relative_error"],1e-10)
        self.assertLess(result["max_Eq_5_12_relative_residual"],3e-10)
        self.assertAlmostEqual(
            sum(result["emissivity_by_mode_MeV5"]),
            result["emissivity_total_MeV5"],places=11
        )


class ThermalDimuonTests(unittest.TestCase):
    def test_threshold_is_closed_and_immediately_above_is_open(self):
        threshold=2*rates.M_MU
        closed=thermal_dimuon_emissivity(threshold,19.265,46.674,0,-1)
        opened=thermal_dimuon_emissivity(
            threshold*(1+1e-4),19.265,46.674,0,-1,
            energy_order=16,angular_order=48
        )
        self.assertFalse(closed["open"])
        self.assertEqual(closed["emissivity_total_MeV5"],0.0)
        self.assertTrue(opened["open"])
        self.assertGreater(opened["emissivity_total_MeV5"],0.0)
        self.assertLess(opened["max_detailed_balance_relative_error"],1e-11)

    def test_integrated_axial_vector_ratio_matches_analytic_width_ratio(self):
        threshold=2*rates.M_MU
        mass=1.2*threshold
        T,mu=19.26522111,46.67432845
        vector=thermal_dimuon_emissivity(
            mass,T,mu,1,0,energy_order=24,angular_order=64
        )
        axial=thermal_dimuon_emissivity(
            mass,T,mu,0,-1,energy_order=24,angular_order=64
        )
        beta2=1-threshold**2/mass**2
        expected=beta2/(1+2*rates.M_MU**2/mass**2)
        self.assertAlmostEqual(
            axial["emissivity_total_MeV5"]/vector["emissivity_total_MeV5"],
            expected,places=12
        )

    def test_dimuon_energy_quadrature_converges(self):
        mass=1.05*2*rates.M_MU
        coarse=thermal_dimuon_emissivity(
            mass,19.265,46.674,0,-1,energy_order=16,angular_order=48
        )
        fine=thermal_dimuon_emissivity(
            mass,19.265,46.674,0,-1,energy_order=32,angular_order=64
        )
        self.assertLess(
            abs(coarse["emissivity_total_MeV5"]/fine["emissivity_total_MeV5"]-1),
            2e-6
        )


if __name__=="__main__":
    unittest.main(verbosity=2)
