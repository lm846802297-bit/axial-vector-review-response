"""External formulas and analytic transport checks, independent of scan outputs."""
import unittest
import numpy as np
from numpy.testing import assert_allclose
from scipy.integrate import quad
from scipy.special import expit
from numpy.polynomial.legendre import leggauss
import rates
import transport
import vector_reference as ref


class LiteratureRates(unittest.TestCase):
    def test_fermi_closed_form_against_adaptive_integral(self):
        for mass,energy,temp,mu in [(1,30,30,50),(10,10,30,50),
                (100,150,30,0),(300,350,25,100),(1,200,10,-60)]:
            v=np.sqrt(1-(mass/energy)**2)
            expected=quad(lambda z:expit((mu-energy*(1+v*z)/2)/temp)
                           *expit((-mu-energy*(1-v*z)/2)/temp),-1,1,
                           epsabs=1e-18,epsrel=1e-12)[0]/2
            assert_allclose(ref.fermi_pair_average(mu,energy,temp,v),expected,rtol=1e-10)

    def test_spin_sums_against_blinov_closed_form(self):
        for mass in [1.,10.,100.,212.,250.,300.]:
            e=mass+np.array([.1,30.,100.,300.])
            nu,mm=ref.summed_decay_production(mass,e,30.,45.,100.)
            ours,_=rates.neutrino_rates(mass,e,30.,45.,order=96)
            assert_allclose(ours.sum(-1),nu,rtol=2e-10)
            ours,_=rates.charged_muon_decay_rates(mass,e,30.,100.,current='vector',order=96)
            assert_allclose(ours.sum(-1),mm,rtol=2e-10,atol=1e-100)

    def test_finite_mass_thomson_limit_each_mode(self):
        # E/m_mu -> 0 at fixed M/E, including near threshold.
        # E/m_mu ~ 1e-5: recoil is bounded at O(1e-5), while avoiding
        # cancellation of O(E^2) terms far below double-precision resolution.
        e=np.array([1e-3])
        for ratio in [.01,.3,.9]:
            mass=ratio*e[0]
            _,weights=rates.compton_kernels(mass,e,order=64,current='vector')
            expected=2*rates.ALPHA/(3*rates.M_MU**2)*np.array([ratio**2,1,1])
            assert_allclose(weights[0].sum(0),expected,rtol=4e-5)

    def test_photon_factor_two_and_velocity(self):
        m,e,t,n=3.,np.array([10.,30.]),25.,12.
        modes=ref.thomson_absorption_modes(m,e,t,n)
        v=np.sqrt(1-(m/e)**2)
        sigma=2*ref.ALPHA/(3*ref.M_MU**2)*(1+m*m/(2*e*e))*v
        expected=2*n*sigma/v/np.expm1(e/t)  # B.16
        assert_allclose((modes*np.exp(-e[:,None]/t)).sum(-1),expected,rtol=1e-13)

    def test_polarization_sum_is_not_decay_probability(self):
        m,e=100.,150.
        _,a=rates.neutrino_rates(m,e,1e-4,0.)
        gamma=m*m/(12*np.pi*e)  # two left-handed flavors, one V particle
        assert_allclose(a,[gamma]*3,rtol=1e-13)
        assert_allclose(a.sum(),3*gamma,rtol=1e-13)
        # At one lifetime the survival is e^-1 for every incident polarization.
        assert_allclose(np.exp(-a/gamma),np.exp(-1),rtol=1e-13)
        self.assertGreater(abs(np.exp(-a.sum()/gamma)-np.exp(-1)),.3)

    def test_wang_printed_transverse_formula_fails_positivity(self):
        # Eq. B.6a is proportional to M^2+2 E_gamma^2 cos(theta).
        # This assertion records a primary-source problem, NOT a target kernel.
        mass_over_energy=.1
        self.assertLess(mass_over_energy**2+2*(-.5),0.)
        _,squared=rates.compton_matrix_elements(.1,[1.],[-.5],current='vector')
        self.assertTrue(np.all(squared>=0.))


class AnalyticTransport(unittest.TestCase):
    def test_uniform_sphere_escape_including_inward_rays(self):
        radius=10.
        x,w=leggauss(100)
        r=radius*(x+1)/2
        volume_weights=3*r*r/radius**3*radius*w/2
        grid=np.array([0.,radius])
        mass,energy=1.,np.array([2.])
        velocity=np.sqrt(1-(mass/energy[0])**2)
        for tau in [.1,1.,10.]:
            rate=tau/radius/transport.KM_IN_MEV_INV*velocity
            columns,angles=transport.angular_columns(r,grid,np.full((2,1,1),rate),
                                                     mass,energy,radius,120,8)
            numerical=np.dot(volume_weights,np.exp(-columns[:,:,0,0])@angles)
            assert_allclose(numerical,ref.uniform_sphere_escape(tau),rtol=1e-5)

    def test_optical_depth_equals_lab_decay_rate_times_flight_time(self):
        mass,energy,radius=100.,np.array([150.]),25.
        gamma=mass**2/(12*np.pi*energy[0])
        v=np.sqrt(1-(mass/energy[0])**2)
        column,_=transport.angular_columns(np.array([0.]),np.array([0.,radius]),
            np.full((2,1,3),gamma),mass,energy,radius,8,8)
        assert_allclose(column,gamma*radius*transport.KM_IN_MEV_INV/v,rtol=1e-13)

if __name__=='__main__':unittest.main(verbosity=2)
