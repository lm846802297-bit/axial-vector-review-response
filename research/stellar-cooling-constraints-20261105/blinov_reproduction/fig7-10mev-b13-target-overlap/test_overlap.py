import unittest
import numpy as np
from overlap import chord_rectangle, gap_certificate, limits, rectangle, scalar_optical_depths

class DomainTests(unittest.TestCase):
    def test_limits_reject_duplicate_keys(self):
        point={'r_km':1.,'x':0.05,'omega_local_MeV':11.,'final_payload':{'temperature_MeV':20.}}
        self.assertEqual(limits([point],10.)['omega_max'],11.)
        with self.assertRaises(ValueError):
            limits([point,point],10.)
        with self.assertRaises(ValueError):
            limits([point],9.)

    def test_rectangle_applies_local_temperature_and_energy_cap(self):
        r=np.array([2.,3.,4.,5.])
        T=np.array([20.,10.,40.,30.])
        f={'r_min':1.,'r_max':4.,'x_min':0.,'x_max':.06,'omega_max':12.}
        np.testing.assert_array_equal(rectangle(r,T,11.,10.,f),[True,False,True,False])
        np.testing.assert_array_equal(rectangle(r,T,12.1,10.,f),[False]*4)

    def test_gap_uses_separate_extrema_even_with_misaligned_endpoints(self):
        p={'r_km':np.array([0.,1.,2.]),'T_MeV':np.array([10.,20.,25.]),
           'lapse':np.array([.7,.9,.8])}
        f={'r_min':.5,'r_max':1.2,'x_max':.05}
        cert=gap_certificate(p,10.,f)
        self.assertEqual(cert['intervals'],2)
        self.assertAlmostEqual(cert['min_gap_lower_bound_mev'],10/.9-10-1.05)
        self.assertEqual(cert['controlling_interval_km'],[1.,1.2])

    def test_chord_with_full_acceptance_matches_independent_native_rule(self):
        r=np.array([.35,.9]); ro=np.array([0.,.5,1.]); m=10.
        e=np.array([11.,17.,42.])
        y=np.array([[1.,2.,3.],[.5,2.,1.],[.6,1.,5.]])
        pn={'r_km':ro,'T_MeV':np.full_like(ro,20.)}
        q={'radius_km':1.,'angular_order':4,'path_order':7}
        f={'r_min':0.,'r_max':1.,'x_min':0.,'x_max':9.,'omega_max':43.}
        a=chord_rectangle(r,ro,pn,y,m,e,q,f)
        native,_=scalar_optical_depths(r,ro,y,m,e,1.,4,7)
        np.testing.assert_allclose(a,native,rtol=2e-15)
        # Cap masks hits on valid chords, no change to in-domain weights.
        f['omega_max']=16.
        again=chord_rectangle(r,ro,pn,y,m,e,q,f)
        np.testing.assert_array_equal(again[:,:,0],a[:,:,0])
        np.testing.assert_array_equal(again[:,:,1:],0.)

if __name__=='__main__':
    unittest.main()
