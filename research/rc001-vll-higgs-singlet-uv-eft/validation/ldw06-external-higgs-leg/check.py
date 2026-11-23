"""Exact single reducible LD-W-06 H(p2) emission on the four-point seed."""
from functools import lru_cache
from itertools import product
import json
import platform
import sympy as S
from sympy.physics.matrices import mgamma

I = S.I
g = S.diag(1, -1, -1, -1)
g2 = S.Symbol("g_2", real=True)
y2 = S.Symbol("abs_y_squared", positive=True)
phase4 = -g2**2 * y2
assert S.prod([-I, -I, I*g2, I*g2, I, I, I, -I])*y2 == phase4
PL = (S.eye(4) - mgamma(5))/2

def dot(a, b):
    return (a.T*g*b)[0]

def norm(a):
    return dot(a, a)

def slash(a):
    return sum((g[j,j]*a[j]*mgamma(j) for j in range(4)), S.zeros(4))

def V(*args):
    return S.Matrix(args)

t = (S.Matrix([[0, 1], [1, 0]])/2,
     S.Matrix([[0, -I], [I, 0]])/2, S.diag(1, -1)/2)
labels = range(2)
weak_indices = tuple(product(labels, repeat=4))

@lru_cache(None)
def weak(a):
    # Direct index sewing in the frozen external-slot representation basis.
    raw = tuple(sum(t[a][j,m]*t[b][m,i]*(-t[b].T)[k,l]
                    for m,b in product(labels, range(3)))
                for i,j,k,l in weak_indices)
    T = [2*int(i==l and k==j)-int(i==j and k==l)
         for i,j,k,l in weak_indices]
    expected = tuple(-sum(t[a][j,m]*T[weak_indices.index((i,m,k,l))]
                          for m in labels)/4 for i,j,k,l in weak_indices)
    bad = tuple(sum(t[b][j,m]*t[a][m,i]*(-t[b].T)[k,l]
                    for m,b in product(labels, range(3)))
                for i,j,k,l in weak_indices)
    assert raw == expected and raw != bad
    return raw, expected, bad

def direct_route(ell, q, p1, p2, p3):
    # Solve vertex conservation starting at the external (W,H) vertex,
    # then at each inner scalar and the right Yukawa endpoint.
    p4 = -p1-p2-p3-q
    outgoing_scalar_at_external_vertex = -p2-q
    P = -outgoing_scalar_at_external_vertex
    rA = ell-P
    rB = p3+ell
    H = p4+rB
    assert p1+H-rA == S.zeros(4,1)
    # All-incoming H minus H-dagger momentum at the three scalar vertices.
    return P, rA, rB, H, p2-(-P), P-rA, -rB-p3

def lower(ell, p1, P, p3, M2, omit_heavy_shift=None):
    h = ell-p1-P if omit_heavy_shift is None else omit_heavy_shift
    d = (norm(ell), norm(ell-P), norm(ell+p3), norm(h)-M2)
    assert all(d)
    return dot(2*P-ell,-2*p3-ell)*slash(h)*PL/S.prod(d)

def entries(m, n):
    return sum(S.expand(a-b)!=0 for a,b in zip(m,n,strict=True))

POINTS = (
    ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
    ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
    ((5,2,1,1),(1,2,0,1),(1,0,1,0),(1,0,1,0),(0,1,1,0)),
)
def run():
    ell,q,p1,p2,p3 = [S.Matrix(S.symbols(f"{n}_0:4")) for n in ("ell","q","p1","p2","p3")]
    P,rA,rB,h,w,V_A,V_B = direct_route(ell,q,p1,p2,p3)
    assert P == p2+q and w == 2*p2+q
    assert S.expand(dot(q,w)-norm(P)+norm(p2)) == 0
    k = ell-q
    assert rA == k-p2 and rB == k+q+p3 and h == k-p1-p2
    assert V_A == 2*p2-k+q and V_B == -2*p3-k-q
    report = []
    for point in POINTS:
        ell,q,p1,p2,p3 = map(S.Matrix,point)
        M2 = S.Integer(400)
        P,rA,rB,h,w,A,B = direct_route(ell,q,p1,p2,p3)
        d = (norm(ell), norm(rA), norm(rB), norm(h)-M2)
        assert all(d) and norm(P)
        C = dot(A,B)*slash(h)*PL/S.prod(d)
        predicted = lower(ell,p1,p2+q,p3,M2)
        assert entries(C,predicted) == 0
        proj = 1-norm(p2)/norm(P)
        qdot_raw = sum((q[mu]*g[mu,mu]*(I*g2)*w[mu]*I/norm(P)
                        for mu in range(4)),S.Integer(0))
        assert qdot_raw == -g2*proj
        if norm(p2):
            qdot_connected = qdot_raw*I/norm(p2)
            assert S.expand(qdot_connected+I*g2*(1/norm(p2)-1/norm(P))) == 0
        else:
            assert proj == 1  # evaluated only after scalar-pole amputation
        stats = dict(amputated=0, uncontracted=0, projected_scalar_mass_shell=0,
                     connected=0, omitted_heavy_shift=0, reversed_weak_order=0,
                     omitted_external_inverse_propagator_term=0,
                     wrong_current_rebase=0, omitted_external_relative_minus=0)
        wrong_h = lower(ell,p1,P,p3,M2,omit_heavy_shift=ell-p1-p2)
        wrong_V = dot(A-2*q,B)*slash(h)*PL/S.prod(d)
        for a in range(3):
            raw,expected,bad = weak(a)
            for w0,w1,wbad in zip(raw,expected,bad,strict=True):
                # Common P4 from frozen phase convention, retained explicitly.
                for mu in range(4):
                    ell_component = phase4*w0*(I*g2)*w[mu]*I*C/norm(P)
                    k_component = -g2*phase4*w1*(2*p2+q)[mu]*predicted/norm(P)
                    assert entries(ell_component,k_component) == 0
                    stats["uncontracted"] += 16
                lhs=phase4*w0*qdot_raw*C
                rhs=phase4*w1*(-g2)*proj*predicted
                assert entries(lhs,rhs) == 0
                stats["amputated"] += 16
                if norm(p2):
                    assert entries(phase4*w0*qdot_connected*C,
                                   phase4*w1*(-I*g2)*(1/norm(p2)-1/norm(P))*predicted) == 0
                    stats["connected"] += 16
                else:
                    stats["projected_scalar_mass_shell"] += 16
                stats["omitted_heavy_shift"] += entries(lhs,phase4*w1*(-g2)*proj*wrong_h)
                stats["reversed_weak_order"] += entries(lhs,phase4*wbad*(-g2)*proj*predicted)
                stats["omitted_external_inverse_propagator_term"] += entries(lhs,phase4*w1*(-g2)*predicted)
                stats["wrong_current_rebase"] += entries(lhs,phase4*w1*(-g2)*proj*wrong_V)
                stats["omitted_external_relative_minus"] += entries(lhs,-rhs)
        assert stats["omitted_heavy_shift"] and stats["reversed_weak_order"]
        assert stats["wrong_current_rebase"] and stats["omitted_external_relative_minus"]
        assert bool(stats["omitted_external_inverse_propagator_term"]) == bool(norm(p2))
        report.append({"p2_squared":str(norm(p2)),"q_squared":str(norm(q)),
                      "shifted_scalar_virtuality":str(norm(P)),
                      "four_point_denominators":list(map(str,d)),
                      "scalar_ward_factor":str(proj),"entry_counts":stats})
    return {"python":platform.python_version(),"sympy":S.__version__,
            "scope":"one LD-W-06 reducible H(p2) emission; no full LSZ, Ward/STI or matching",
            "symbolic": {"vertices_and_common_k_routes": "pass", "scalar_WTI":"pass"},
            "points":report}

if __name__ == "__main__":
    print(json.dumps(run(),indent=2))
