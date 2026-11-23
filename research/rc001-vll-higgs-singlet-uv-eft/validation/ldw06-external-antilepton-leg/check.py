"""Exact H–H† lower box with one reducible W on the barred L leg."""
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

I=s.I
G=tuple(mgamma(i) for i in range(4))
eta=s.diag(1,-1,-1,-1)
one=s.eye(4)
PL=(one-mgamma(5))/2
PR=one-PL
half=s.Rational(1,2)
t=(half*s.Matrix([[0,1],[1,0]]),half*s.Matrix([[0,-I],[I,0]]),half*s.diag(1,-1))
J=2*I*t[1]
g2,yy=s.symbols("g2 y_abs_squared")
p4_phase=(-I)*(-I*yy)*(I*g2)**2*I**3*(-I)
assert p4_phase == -g2**2*yy

def dot(x,y):
    return (x.T*eta*y)[0]

def sq(x):
    return dot(x,x)

def sl(x):
    return sum((eta[i,i]*x[i]*G[i] for i in range(4)),s.zeros(4))

def S(x):
    assert sq(x)!=0
    return sl(x)/sq(x)

def count(x,y):
    return sum(s.expand(a-b)!=0 for a,b in zip(x,y,strict=True))

def seed(i,j,z,l):
    return sum(t[b][j,i]*(-t[b].T)[z,l] for b in range(3))

def weak(a,i,j,z,l):
    # Solve (in components) from the bare fundamental vertex. Convert the
    # barred slot of the input seed to fundamental coordinates and the
    # output back to the frozen dual slot using the SU(2) intertwiner J.
    Ji=J.inv()
    literal=sum(J[i,m]*t[a][m,n]*Ji[n,r]*seed(r,j,z,l)
                for m,n,r in product(range(2),repeat=3))
    def t3(r):
        return 2*int(r==l and z==j)-int(r==j and z==l)
    expected=-sum((-t[a].T)[i,r]*t3(r)/4 for r in range(2))
    wrong=-sum(t[a][i,r]*t3(r)/4 for r in range(2))
    assert literal==expected
    return literal,expected,wrong

def direct_routes(k,q,p,p2,p3):
    # p is the incoming barred-field momentum. The L momentum at the
    # external gauge vertex is -P_out; the left arrow into the box is
    # physically +P_out in the open gamma chain.
    p4=-p-p2-p3-q
    L_at_radiation=-p-q
    P=-L_at_radiation
    rA=k-p2
    rB=p3+k
    h=p4+rB
    assert P+h-rA==s.zeros(4,1)
    assert p+q+L_at_radiation==s.zeros(4,1)
    return P,rA,rB,h,p2-rA,-rB-p3

def seed_box(k,P,p2,p3,M2):
    h=k-P-p2
    poles=(sq(k),sq(k-p2),sq(k+p3),sq(h)-M2)
    assert all(poles)
    return dot(2*p2-k,-2*p3-k)*sl(h)*PL/s.prod(poles)

points=(
 ((4,1,2,1),(1,2,0,1),(2,0,1,0),(0,1,0,2),(2,1,1,1)),
 ((6,1,0,1),(1,1,0,0),(2,0,1,0),(0,2,0,1),(2,0,1,0)),
 ((5,2,1,1),(1,2,0,1),(1,1,0,0),(0,1,1,0),(1,0,1,0)),
)

def verify():
    k,q,p,p2,p3=(s.Matrix(s.symbols(n+"_0:4")) for n in ("k","q","p","p2","p3"))
    P,rA,rB,h,A,B=direct_routes(k,q,p,p2,p3)
    assert h==k-P-p2 and rA==k-p2 and rB==k+p3
    Q=sl(q)*PL
    # Polynomial connected identity, both light denominators cleared.
    assert count(sl(p)*Q*sl(P),sq(P)*sl(p)*PR-sq(p)*PL*sl(P))==0
    assert count(Q*sl(P),(sq(P)*one-sl(p)*sl(P))*PR)==0
    assert all(J*T*J.inv()==-T.T for T in t)
    results=[]
    for values in points:
        k,q,p,p2,p3=map(s.Matrix,values)
        P,rA,rB,h,A,B=direct_routes(k,q,p,p2,p3)
        poles=(sq(k),sq(rA),sq(rB),sq(h)-400)
        assert all(poles)
        C=dot(A,B)*sl(h)*PL/s.prod(poles)
        E=seed_box(k,p+q,p2,p3,400)
        assert count(C,E)==0 and PR*C==C
        contracted_left=(one-sl(p)*S(P))*E
        stats={name:0 for name in ("uncontracted","contracted","barred_external_propagator_restored",
            "barred_on_shell_projected","reversed_arrow","wrong_crossing","wrong_matrix_order",
            "wrong_chirality","wrong_dual_charge","missing_inverse_propagator_term")}
        for a,i,j,z,l in product(range(3),*([range(2)]*4)):
            w,z_ref,bad=weak(a,i,j,z,l)
            M=[p4_phase*(I*g2)*w*V*PL*I*S(P)*C for V in G]
            raw=sum((eta[u,u]*q[u]*M[u] for u in range(4)),s.zeros(4))
            for u,V in enumerate(G):
                assert count(M[u],-g2*p4_phase*z_ref*V*PL*S(P)*E)==0
                stats["uncontracted"]+=16
            expected=-g2*p4_phase*z_ref*contracted_left
            assert count(raw,expected)==0
            stats["contracted"]+=16
            if sq(p):
                restored=I*S(p)*raw
                endpoint=-I*g2*p4_phase*z_ref*(S(p)*PR-PL*S(P))*E
                assert count(restored,endpoint)==0
                stats["barred_external_propagator_restored"]+=16
            else:
                row_pool=sl(p)*PR
                assert row_pool*sl(p)==s.zeros(4) and row_pool*PR==row_pool and row_pool*E!=s.zeros(4)
                assert count(row_pool*raw,-g2*p4_phase*z_ref*row_pool*E)==0
                stats["barred_on_shell_projected"]+=16
            mult=-g2*p4_phase*z_ref
            stats["reversed_arrow"]+=count(raw,mult*sl(q)*PL*S(-P)*E)
            stats["wrong_crossing"]+=count(raw,mult*sl(q)*PL*S(p-q)*seed_box(k,p-q,p2,p3,400))
            stats["wrong_matrix_order"]+=count(raw,mult*E*S(P)*sl(q)*PL)
            stats["wrong_chirality"]+=count(raw,mult*sl(q)*PR*S(P)*E)
            stats["wrong_dual_charge"]+=count(raw,-g2*p4_phase*bad*contracted_left)
            compare=raw if sq(p) else row_pool*raw
            no_inverse=mult*E if sq(p) else mult*row_pool*E
            stats["missing_inverse_propagator_term"]+=count(compare,no_inverse)
        assert all(stats[x]>0 for x in ("reversed_arrow","wrong_crossing","wrong_matrix_order",
                                      "wrong_chirality","wrong_dual_charge"))
        assert bool(stats["missing_inverse_propagator_term"])==bool(sq(p))
        results.append({"p1_squared":str(sq(p)),"q_squared":str(sq(q)),
            "P_squared":str(sq(P)),"lower_box_poles":list(map(str,poles)),
            "heavy_pole_without_crossed_shift":str(sq(k-p-p2)-400),"entries":stats})
    return {"scope":"single reducible barred L(p1) emission of the LD-W-06 ordered box prior to integration",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),
                       "machine":platform.machine()},
            "symbolic":{"connected_ward_polynomial":16,"amputated_ward_polynomial":16,
                        "dual_representation_generators":3,"routing":"exact"},
            "points":results}

if __name__ == "__main__":
    print(json.dumps(verify(),indent=2))
