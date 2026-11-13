import unittest
import numpy as np
from gr_ray_transport import KM_TO_MEV_INV, StaticSphericalMetric, propagate_ray

class TestGRRayTransport(unittest.TestCase):
    def setUp(self):
        self.r=np.linspace(0,30,601)
        self.flat=StaticSphericalMetric(self.r,np.ones_like(self.r),np.ones_like(self.r))
        self.gamma=lambda r,w:1e-16
        self.mass=10.; self.omega=300.; self.rs=10.; self.rmax=25.
        self.v=np.sqrt(1-(self.mass/self.omega)**2)
    def test_flat_radial_outward(self):
        out=propagate_ray(self.flat,mass_MeV=self.mass,source_radius_km=self.rs,
            source_local_energy_MeV=self.omega,source_mu=1,gamma_abs_star=self.gamma,r_max_km=self.rmax)
        length=self.rmax-self.rs; tau=self.gamma(0,0)*length*KM_TO_MEV_INV/self.v
        self.assertTrue(out.escapes_to_rmax); self.assertAlmostEqual(out.proper_path_km,length,places=8)
        self.assertAlmostEqual(out.optical_depth/tau,1,places=7)
    def test_flat_chords_inward_and_outward(self):
        for mu in (-.8,-.2,.2,.8):
            out=propagate_ray(self.flat,mass_MeV=self.mass,source_radius_km=self.rs,
                source_local_energy_MeV=self.omega,source_mu=mu,gamma_abs_star=self.gamma,r_max_km=self.rmax)
            smax=-mu*self.rs+np.sqrt(self.rmax**2-self.rs**2+self.rs**2*mu**2)
            tau=self.gamma(0,0)*smax*KM_TO_MEV_INV/self.v
            self.assertTrue(out.escapes_to_rmax); self.assertAlmostEqual(out.proper_path_km,smax,places=7)
            self.assertAlmostEqual(out.optical_depth/tau,1,places=7)
    def test_flat_tangential_limit(self):
        out=propagate_ray(self.flat,mass_MeV=self.mass,source_radius_km=self.rs,
            source_local_energy_MeV=self.omega,source_mu=0,gamma_abs_star=self.gamma,r_max_km=self.rmax)
        self.assertTrue(out.escapes_to_rmax)
        self.assertAlmostEqual(out.proper_path_km,np.sqrt(self.rmax**2-self.rs**2),places=7)
    def test_killing_energy_redshift(self):
        lapse=.7+.3*self.r/self.r.max(); metric=StaticSphericalMetric(self.r,lapse,np.ones_like(self.r))
        rs,r2=10.,25.; E=metric.N(rs)*100.
        self.assertAlmostEqual(metric.local_energy(E,rs),100.,places=12)
        self.assertLess(metric.local_energy(E,r2),100.)
    def test_bound_energy_not_escaping(self):
        metric=StaticSphericalMetric(self.r,.8*np.ones_like(self.r),np.ones_like(self.r))
        out=propagate_ray(metric,mass_MeV=10,source_radius_km=10,source_local_energy_MeV=11,
            source_mu=1,gamma_abs_star=self.gamma,r_max_km=25)
        self.assertFalse(out.escapes_to_rmax); self.assertTrue(np.isinf(out.optical_depth))
    def test_schwarzschild_toy_radial_path(self):
        r=np.linspace(3.1,30,539); M=1.5; N=np.sqrt(1-2*M/r); B=1/N
        metric=StaticSphericalMetric(r,N,B)
        out=propagate_ray(metric,mass_MeV=10,source_radius_km=10,source_local_energy_MeV=300,
            source_mu=1,gamma_abs_star=self.gamma,r_max_km=25)
        self.assertTrue(out.escapes_to_rmax); self.assertGreater(out.proper_path_km,15)
        self.assertGreater(out.optical_depth,0)

if __name__=="__main__": unittest.main(verbosity=2)
