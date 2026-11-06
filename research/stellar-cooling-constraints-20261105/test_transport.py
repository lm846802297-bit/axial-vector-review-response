import unittest
import numpy as np
from transport import angular_columns, luminosities, radial_rule, KM_IN_MEV_INV

class TransportTests(unittest.TestCase):
    def test_uniform_sphere_escape(self):
        r,w=radial_rule(1.0,80)
        grid=np.r_[0,r,1]
        energy=np.array([2.])
        for a in (.1,1.,10.):
            rate=np.full((len(grid),1,1),a/KM_IN_MEV_INV)
            col,wa=angular_columns(r,grid,rate,0.,energy,1.,48,64)
            measured=np.sum(w*r*r*(np.exp(-col[:,:,0,0])@wa))*3
            exact=3/(4*a)*(1-1/(2*a*a)+(1/a+1/(2*a*a))*np.exp(-2*a))
            self.assertAlmostEqual(measured/exact,1.,delta=2e-4)
    def test_zero_opacity_and_coupling_scaling(self):
        source=np.ones((3,4,3))
        cols=np.zeros((3,2,4,3))
        wangle=np.array([.5,.5])
        out=luminosities(source,cols,wangle,np.array([1e-10,2e-10]))
        np.testing.assert_allclose(out[1]/out[0],4.)
    def test_polarization_before_exponent(self):
        source=np.array([[[1.,1.,1.]]])
        cols=np.array([[[[0.,10.,10.]]]])
        out=luminosities(source,cols,np.array([1.]),np.array([1.]))
        self.assertAlmostEqual(out[0],1+2*np.exp(-10),places=12)
    def test_chord_direction(self):
        r=np.array([.5])
        rate=np.ones((2,1,1))/KM_IN_MEV_INV
        cols,wa=angular_columns(r,np.array([0.,1.]),rate,0.,np.array([1.]),1.,16,24)
        self.assertGreater(cols[0,0,0,0],cols[0,-1,0,0])
if __name__=='__main__': unittest.main()
