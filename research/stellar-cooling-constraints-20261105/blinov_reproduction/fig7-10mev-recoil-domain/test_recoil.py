from math import sqrt
import unittest

import numpy as np

from recoil import support


class StationaryKinematics(unittest.TestCase):
    M=105.6583755
    m=10.

    def test_mass_shell_from_independent_four_vector(self):
        M,m=self.M,self.m
        for w,cos in ((40.,-1.),(140.,.9),(300.,.99)):
            k=sqrt(w*w-m*m)
            # Construct the incoming/outgoing photon in Cartesian coords and
            # check the muon's final on-shell energy in both reactions.
            for production in (False,True):
                energy = ((2*M*w-m*m)/(2*(M-w+k*cos)) if production else
                          (2*M*w+m*m)/(2*(M+w-k*cos)))
                sign=1 if production else -1
                initial_plus_transfer_e=M+sign*(energy-w)
                transfer_p=sign*np.array([energy*sqrt(1-cos*cos),0,energy*cos-k])
                self.assertAlmostEqual(initial_plus_transfer_e,
                    sqrt(M*M+np.dot(transfer_p,transfer_p)),places=10)

    def test_backward_domain_and_absorption_half_loss(self):
        M,m=self.M,self.m
        cut=(M*M+m*m)/(2*M)
        half=(M+sqrt(M*M+4*m*m))/2
        w=np.array([cut-1e-3,cut+1e-3,half-1e-3,half+1e-3])
        o=support(w,m,M)
        np.testing.assert_array_equal(o['stationary_production_backward_forbidden'],
                                      [False,True,True,True])
        np.testing.assert_array_equal(o['stationary_absorption_recoil_90_gt_50pct'],
                                      [False,False,False,True])
        self.assertEqual(o['stationary_production_cosine_support_fraction_geometric'][0],1.)

    def test_cm_ratio_against_two_body_momenta(self):
        M,m=self.M,self.m
        w=np.array([12.,32.,120.,550.])
        s=M*M+m*m+2*M*w
        # Same center-of-mass energy for both channels; use product form lambda.
        p_gamma_sq=(s-M*M)**2/(4*s)
        p_V_sq=(s-(M+m)**2)*(s-(M-m)**2)/(4*s)
        u=support(w,m,M)['matched_s_p2ratio_relative_to_printed_lab_beta2']
        np.testing.assert_allclose(p_V_sq/p_gamma_sq/(1-m*m/w**2),u,rtol=1e-14)

if __name__=='__main__':
    unittest.main()
