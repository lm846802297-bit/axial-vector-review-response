"""Right external L(p4) emitted W on the frozen ordered LD-W-06 S–S box."""
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
t=tuple(T/2 for T in (s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)))
g2,yy=s.symbols("g2 y_abs_squared")
phase4=s.prod((-I,-I*yy,I*g2,I*g2,I,I,I,-I))
assert phase4==-g2**2*yy

def dot(x,y):
    return (x.T*eta*y)[0]

def norm(x):
    return dot(x,x)

def slash(x):
    return sum((eta[m,m]*x[m]*G[m] for m in range(4)),s.zeros(4))

def S(x):
    assert norm(x)
    return slash(x)/norm(x)

def unequal(x,y):
    return sum(s.expand(a-b)!=0 for a,b in zip(x,y,strict=True))

def weak(st,i,j,z,l):
    # Literal W weak matrix element <L_l| t^a | L_n> in the
    # archived *physical slot* basis. Dirac ordering does not transpose it.
    raw=sum(t[b][j,i]*(-t[b].T)[z,n]*t[st][l,n]
            for b,n in product(range(3),range(2)))
    exp=-sum(t[st][l,n]*(2*int(i==n and z==j)-int(i==j and z==n))/4
             for n in range(2))
    wrong_t=sum(t[b][j,i]*(-t[b].T)[z,n]*t[st][n,l]
                for b,n in product(range(3),range(2)))
    wrong_slot=sum(t[b][j,i]*(-t[st].T)[z,n]*(-t[b].T)[n,l]
                   for b,n in product(range(3),range(2)))
    assert raw==exp
    return raw,exp,wrong_t,wrong_slot

def find_routes(k,q,p1,p2,p):
    # The barred partner enters radiation as -P. Along the physical B
    # open fermion arrow to the amplitude's original right column it is +P.
    bar_at_radiation=-p-q
    P=-bar_at_radiation
    p3=-p1-p2-P
    rA=k-p2
    h=rA-p1
    rB=h-P
    assert rB==k+p3
    assert p+bar_at_radiation+q==s.zeros(4,1)
    return P,p3,rA,rB,h,p2-rA,-rB-p3

def four(k,p1,p2,p3,M2,extra_h=None):
    h=k-p1-p2
    if extra_h is not None:
        h+=extra_h
    d=(norm(k),norm(k-p2),norm(k+p3),norm(h)-M2)
    assert all(d)
    return dot(2*p2-k,-2*p3-k)*slash(h)*PL/s.prod(d)

cases=(
 ((4,1,2,1),(1,2,0,1),(2,0,1,0),(0,1,0,2),(-5,-4,-2,-4)),
 ((6,1,0,1),(1,1,0,0),(2,0,1,0),(0,2,0,1),(-5,-3,-2,-1)),
 ((5,2,1,1),(1,2,0,1),(1,0,1,0),(0,1,1,0),(1,1,0,0)),
)

def verify():
    k,q,p1,p2,p=(s.Matrix(s.symbols(n+"_0:4")) for n in ("k","q","p1","p2","p"))
    P,p3,rA,rB,h,A,B=find_routes(k,q,p1,p2,p)
    assert h==k-p1-p2 and rA==k-p2 and rB==k+p3
    assert P+p1+p2+p3==s.zeros(4,1)
    Q=slash(q)*PL
    assert not unequal(slash(P)*Q*slash(p),norm(P)*PL*slash(p)-norm(p)*slash(P)*PR)
    assert not unequal(slash(P)*Q,(norm(P)*one-slash(P)*slash(p))*PL)
    rows=[]
    for args in cases:
        k,q,p1,p2,p=map(s.Matrix,args)
        P,p3,rA,rB,h,A,B=find_routes(k,q,p1,p2,p)
        D=(norm(k),norm(rA),norm(rB),norm(h)-400)
        assert all(D)
        C=dot(A,B)*slash(h)*PL/s.prod(D)
        F=four(k,p1,p2,p3,400)
        assert not unequal(C,F) and F*PL==F
        K=F*(one-S(P)*slash(p))
        stats={n:0 for n in ("uncontracted","contracted","original_right_propagator_restored",
               "right_on_shell_projected","reversed_arrow","wrong_crossing","spurious_heavy_shift",
               "wrong_matrix_order","wrong_chirality","weak_transpose","wrong_weak_slot",
               "lost_right_inverse_term","wrong_phase")}
        for a,i,j,z,l in product(range(3),*([range(2)]*4)):
            wr,we,wt,ws=weak(a,i,j,z,l)
            raw=[phase4*wr*C*I*S(P)*(I*g2*X*PL) for X in G]
            qraw=sum((eta[m,m]*q[m]*raw[m] for m in range(4)),s.zeros(4))
            pref=-g2*phase4*we
            for m,X in enumerate(G):
                assert not unequal(raw[m],pref*F*S(P)*X*PL)
                stats["uncontracted"]+=16
            assert not unequal(qraw,pref*K)
            stats["contracted"]+=16
            if norm(p):
                assert not unequal(qraw*I*S(p),I*pref*F*(PL*S(p)-S(P)*PR))
                stats["original_right_propagator_restored"]+=16
            else:
                U=PL*slash(p) # nonzero chiral columns in kernel of slash(p)
                assert U!=s.zeros(4) and PL*U==U and slash(p)*U==s.zeros(4) and F*U!=s.zeros(4)
                assert not unequal(qraw*U,pref*F*U)
                stats["right_on_shell_projected"]+=16
            Q=slash(q)*PL
            stats["reversed_arrow"]+=unequal(qraw,pref*F*S(-P)*Q)
            stats["wrong_crossing"]+=unequal(qraw,pref*F*S(p-q)*Q)
            stats["spurious_heavy_shift"]+=unequal(qraw,pref*four(k,p1,p2,p3,400,-q)*S(P)*Q)
            stats["wrong_matrix_order"]+=unequal(qraw,pref*Q*S(P)*F)
            stats["wrong_chirality"]+=unequal(qraw,pref*F*S(P)*slash(q)*PR)
            stats["weak_transpose"]+=unequal(qraw,-g2*phase4*wt*K)
            stats["wrong_weak_slot"]+=unequal(qraw,-g2*phase4*ws*K)
            stats["wrong_phase"]+=unequal(qraw,-pref*K)
            stats["lost_right_inverse_term"]+=unequal(qraw,pref*F) if norm(p) else unequal(qraw*U,pref*F*U)
        assert all(stats[n]>0 for n in ("reversed_arrow","wrong_crossing","spurious_heavy_shift",
                    "wrong_matrix_order","wrong_chirality","weak_transpose","wrong_weak_slot","wrong_phase"))
        assert bool(stats["lost_right_inverse_term"])==bool(norm(p))
        rows.append({"p4_squared":str(norm(p)),"q_squared":str(norm(q)),"P_squared":str(norm(P)),
                     "lower_box_poles":list(map(str,D)),"spurious_shifted_heavy_pole":str(norm(h-q)-400),
                     "entries":stats})
    return {"scope":"single reducible right L(p4) W emission on the actual LD-W-06 ordered S–S box",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),"machine":platform.machine()},
            "symbolic":{"connected_ward_polynomial":16,"amputated_ward_polynomial":16,
                        "routing":"exact","fundamental_weak_components_in_each_point":48},
            "points":rows}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
