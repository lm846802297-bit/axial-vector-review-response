"""Independent coefficient-ledger tests; no full amplitude computed."""
from fractions import Fraction
from itertools import combinations
import ast
import unittest

import sympy as sp

from replay import DEFAULT_FROZEN, SOURCE, derivative, verify_archive


# Coefficients of (k,q,p1,p2) for independent component evaluation.
H0, HA, HB = (1,0,-1,-1), (1,1,-1,-1), (1,-1,-1,-1)
Q = (0,1,0,0)


def plus(a,b,direction=1):
    return tuple(x+direction*y for x,y in zip(a,b,strict=True))


def vec(weights,momenta):
    return tuple(sum(coef*component for coef,component in
                     zip(weights,column,strict=True))
                 for column in zip(*momenta,strict=True))


def denominator(p,m2):
    return p[0]**2-sum(x*x for x in p[1:])-m2


class SignedRouteTests(unittest.TestCase):
    def test_exact_componentwise_routing_and_wrong_sign_controls(self):
        momenta = tuple(sp.symbols(f'{k}_0:4') for k in ('k','q','p1','p2'))
        self.assertTrue(all(len(m)==4 for m in momenta))
        self.assertEqual(len(set(sum(momenta,()))),16)
        h0=vec(H0,momenta)
        for route in (plus(HA,Q,-1),plus(HB,Q,1)):
            self.assertEqual(vec(route,momenta),h0)
        for wrong in (plus(HA,Q,1),plus(HB,Q,-1)):
            self.assertTrue(all((a-b).expand()!=0 for a,b in
                                zip(vec(wrong,momenta),h0,strict=True)))

    def test_archive_rational_anchor_vs_common_endpoint(self):
        # Use independently listed input vectors, not archive add/sub/dot.
        momenta = ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1))
        m2 = Fraction(400)
        self.assertEqual(tuple(denominator(vec(p,momenta),m2) for p in
                               (H0,HB,HA)),(-377,-389,-365))
        self.assertEqual(tuple(denominator(vec(p,momenta),m2) for p in
                               (plus(HA,Q,-1),plus(HB,Q,1))),(-377,-377))

    def test_derivative_changes_only_two_vector_initializers(self):
        frozen=DEFAULT_FROZEN
        verify_archive(frozen)
        old=(frozen/SOURCE).read_bytes()
        fixed=derivative(old)
        a,b=old.splitlines(),fixed.splitlines()
        changed=[i for i,(x,y) in enumerate(zip(a,b,strict=True),start=1) if x!=y]
        self.assertEqual(changed,[57,58])
        self.assertIsNotNone(ast.parse(fixed))
        self.assertEqual(sp.symbols('p10:4'),())
        self.assertEqual(sp.symbols('p20:4'),())

if __name__=='__main__':
    unittest.main(verbosity=2)
