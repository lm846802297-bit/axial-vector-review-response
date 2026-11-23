"""Exact B-side external conjugate-Higgs leg on the LD-W-06 seed."""
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

I = s.I
eta = s.diag(1, -1, -1, -1)
t = (s.Matrix([[0, 1], [1, 0]])/2,
     s.Matrix([[0, -I], [I, 0]])/2, s.diag(1, -1)/2)
slots = tuple(product(range(2), repeat=4))
g2, yy = s.symbols("g2 yy")
PL = (s.eye(4)-mgamma(5))/2
P4 = s.prod((-I, -I*yy, I*g2, I*g2, I, I, I, -I))
assert P4 == -g2**2*yy

def dot(x, y):
    return (x.T*eta*y)[0]

def sq(x):
    return dot(x, x)

def sl(x):
    return sum((eta[j,j]*x[j]*mgamma(j) for j in range(4)), s.zeros(4))*PL

def different(a, b):
    return sum(s.expand(x-y)!=0 for x,y in zip(a,b,strict=True))

def tensor(a, i,j,k,l):
    # Frozen physical external slots: compare a literal conjugate-vertex
    # sewing with an R_{H†} action on the known four-point seed -T3/4.
    direct = sum(t[b][j,i]*(-t[b].T)[n,l]*t[a][n,k]
                 for b,n in product(range(3),range(2)))
    # At the external vertex the raw momentum factor is -(2p3+q).
    # Above the transpose is in components; put that momentum minus in R.
    direct = -direct
    expected = sum((-t[a].T)[k,n]*(-s.Rational(1,4))*
                   (2*int(i==l and n==j)-int(i==j and n==l)) for n in range(2))
    wrong_order = sum(t[b][j,i]*(-t[b].T)[k,n]*(-t[a].T)[n,l]
                      for b,n in product(range(3),range(2)))
    wrong_transpose = sum((-t[a])[k,n]*(-s.Rational(1,4))*
                          (2*int(i==l and n==j)-int(i==j and n==l)) for n in range(2))
    assert direct == expected
    return direct, expected, wrong_order, wrong_transpose

def solve_vertices(k, q, p1,p2,p3):
    # No Ward replacement used here. Start at the radiation vertex with
    # all-incoming original H† momentum p3 and H momentum -P.
    p4 = -p1-p2-p3-q
    P = p3+q
    raw_w = -P-p3
    rB = P+k
    h = p4+rB
    rA = p1+h
    assert p2+rA-k == s.zeros(4,1)
    return P,raw_w,rA,rB,h,p2-rA,-P-rB

POINTS = (
    ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
    ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
    ((5,2,1,1),(1,2,0,1),(1,0,1,0),(0,1,1,0),(1,0,1,0)),
)

def validate():
    k,q,p1,p2,p3 = (s.Matrix(s.symbols(n+"_0:4")) for n in ("k","q","p1","p2","p3"))
    P,w,rA,rB,h,A,B = solve_vertices(k,q,p1,p2,p3)
    assert rA==k-p2 and rB==k+p3+q and h==k-p1-p2
    assert A==2*p2-k and B==-2*p3-k-2*q
    assert s.expand(dot(q,w)+sq(P)-sq(p3))==0
    rows=[]
    for point in POINTS:
        k,q,p1,p2,p3=map(s.Matrix,point)
        M2=s.Integer(400)
        P,w,rA,rB,h,A,B = solve_vertices(k,q,p1,p2,p3)
        d=(sq(k),sq(rA),sq(rB),sq(h)-M2)
        assert all(d) and sq(P)
        C=dot(A,B)*sl(h)/s.prod(d)
        def reduce_four(p_B, p_correction=True):
            # Independent four-point formula as function of independent
            # right scalar argument (with p4 implied by conservation).
            h0=k-p1-p2
            current_B=-2*(p_B if p_correction else p3)-k
            d0=(sq(k),sq(k-p2),sq(k+p_B),sq(h0)-M2)
            assert all(d0)
            return dot(2*p2-k,current_B)*sl(h0)/s.prod(d0)
        expected_C=reduce_four(p3+q)
        assert different(C,expected_C)==0
        ratio=1-sq(p3)/sq(P)
        stats=dict(uncontracted=0, amputated=0, external_scalar_restored=0,
                   after_scalar_pole_projection=0, wrong_crossing=0,
                   wrong_transpose=0, wrong_order=0, missing_relative_minus=0,
                   copied_internal_current=0, discarded_inverse=0)
        for a,i,j,kB,l in product(range(3),*([range(2)]*4)):
            direct,ext,order,trans=tensor(a,i,j,kB,l)
            bare_t_transposed=-direct  # undo the absorbed momentum minus
            vector=[P4*bare_t_transposed*(I*g2)*w[mu]*I*C/sq(P) for mu in range(4)]
            ward=sum((eta[mu,mu]*q[mu]*vector[mu] for mu in range(4)),s.zeros(4))
            for mu,rhs in enumerate(vector):
                assert different(rhs,-P4*g2*ext*(2*p3+q)[mu]*expected_C/sq(P))==0
                stats["uncontracted"]+=16
            reference=-P4*g2*ext*ratio*expected_C
            assert different(ward,reference)==0
            stats["amputated"]+=16
            if sq(p3):
                assert different(ward*I/sq(p3),-I*P4*g2*ext*
                                 (1/sq(p3)-1/sq(P))*expected_C)==0
                stats["external_scalar_restored"]+=16
            else:
                assert ratio==1
                stats["after_scalar_pole_projection"]+=16
            P_bad=p3-q
            assert sq(P_bad)
            wrong_ratio=1-sq(p3)/sq(P_bad)
            stats["wrong_crossing"]+=different(ward,-P4*g2*ext*wrong_ratio*reduce_four(P_bad))
            stats["wrong_transpose"]+=different(ward,-P4*g2*trans*ratio*expected_C)
            stats["wrong_order"]+=different(ward,-P4*g2*order*ratio*expected_C)
            stats["missing_relative_minus"]+=different(ward,-reference)
            stats["copied_internal_current"]+=different(ward,-P4*g2*ext*ratio*reduce_four(P,False))
            stats["discarded_inverse"]+=different(ward,-P4*g2*ext*expected_C)
        assert all(stats[k] for k in ("wrong_crossing","wrong_transpose","wrong_order","missing_relative_minus","copied_internal_current"))
        assert bool(stats["discarded_inverse"])==bool(sq(p3))
        rows.append({"q_squared":str(sq(q)), "p3_squared":str(sq(p3)), "P_squared":str(sq(P)),
                     "reduced_four_point_poles":list(map(str,d)), "ward_scalar_factor":str(ratio),
                     "B_dot_A_shifted":str(dot(A,B)), "B_dot_A_internal_current":str(dot(A,-2*p3-k)),
                     "exact_entry_counts":stats})
    return {"check_scope":"one reducible external Hdagger(p3) LD-W-06 graph, before loop integration",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"os":platform.system(),"machine":platform.machine()},
            "symbolic":"vertex conservation, scalar Ward factor and B-side current shift exact",
            "points":rows}

if __name__ == "__main__":
    print(json.dumps(validate(),indent=2))
