import sys
import unittest
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))

from blinov_reproduction.reference import fermi_pair_average, decay_production
from blinov_reproduction.audit_b16_neutrino_inverse_decay import direct_pair_integrals


class B16NeutrinoInverseDecayTests(unittest.TestCase):
    def test_direct_B6_angular_integral_matches_independent_antiderivative(self):
        mu=np.array([-58.0,-1.0,0.0,1.0,50.0])[:,None]
        omega=np.array([12.0,20.0,50.0])[None,:]
        temperature=np.array([10.0,3.5,20.0,3.4,18.0])[:,None]
        velocity=np.sqrt(1.0-(10.0/omega)**2)
        direct,_=direct_pair_integrals(mu,omega,temperature,velocity,order=192)
        analytic=fermi_pair_average(mu,omega,temperature,velocity)
        np.testing.assert_allclose(direct,analytic,rtol=2e-12,atol=1e-300)

    def test_direct_inverse_integral_obeys_B10_detailed_balance(self):
        mu=np.array([-58.0,0.0,1.0,50.0])[:,None]
        omega=np.array([12.0,20.0,50.0])[None,:]
        temperature=np.array([10.0,3.5,3.4,18.0])[:,None]
        velocity=np.sqrt(1.0-(10.0/omega)**2)
        prod,absorb=direct_pair_integrals(mu,omega,temperature,velocity,order=192)
        residual=np.log(absorb/prod)-omega/temperature
        self.assertLess(float(np.max(np.abs(residual))),2e-12)

    def test_B6_two_flavour_sum_matches_reference_rate(self):
        mass=10.0
        omega=np.array([[12.0,20.0,50.0],[12.0,20.0,50.0]])
        temperature=np.array([[3.5],[10.0]])
        mu_numu=np.array([[0.0],[-58.0]])
        v=np.sqrt(1.0-(mass/omega)**2)
        i_mu,_=direct_pair_integrals(mu_numu,omega,temperature,v,order=192)
        i_tau,_=direct_pair_integrals(np.zeros_like(mu_numu),omega,temperature,v,order=192)
        direct=mass**2/(8.0*np.pi*omega)*(i_mu+i_tau)
        _,reference=decay_production(
            mass,omega,temperature,mu_numu,np.zeros_like(mu_numu)
        )
        np.testing.assert_allclose(direct,reference,rtol=2e-12,atol=1e-300)

    def test_B4_reduced_absorption_has_two_equivalent_forms(self):
        mu=0.0
        omega=np.array([12.0,20.0,50.0])
        temperature=3.5
        velocity=np.sqrt(1.0-(10.0/omega)**2)
        prod,absorb=direct_pair_integrals(mu,omega,temperature,velocity,order=192)
        reduced_a=(1.0-np.exp(-omega/temperature))*absorb
        reduced_b=np.expm1(omega/temperature)*prod
        np.testing.assert_allclose(reduced_a,reduced_b,rtol=2e-12,atol=1e-300)


if __name__=="__main__":
    unittest.main(verbosity=2)
