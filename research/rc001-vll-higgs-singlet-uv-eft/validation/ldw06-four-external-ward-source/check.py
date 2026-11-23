"""Fixed-k LD-W-06 source identity for all four original external emissions."""
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

I=s.I
G=tuple(mgamma(a) for a in range(4))
eta=s.diag(1,-1,-1,-1)
U=s.eye(4)
P_L=(U-mgamma(5))/2
P_R=U-P_L
t=tuple(x/2 for x in (s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)))
dual=tuple(-x.T for x in t)
R=(dual,t,dual,t)
ix=list(product(range(2),repeat=4))
N=range(4)
g=s.symbols("g2")
assert I*I*g==-g # every extra vertex and intermediate matter propagator

def dot(a,b):
    return (a.T*eta*b)[0]

def sq(a):
    return dot(a,a)

def slash(a):
    return sum((eta[u,u]*a[u]*G[u] for u in N),s.zeros(4))

def S(a):
    assert sq(a)
    return slash(a)/sq(a)

def diff(A,B):
    return sum(s.expand(a-b)!=0 for a,b in zip(A,B,strict=True))

def linear(ws,ms):
    return sum((w*m for w,m in zip(ws,ms,strict=True)),s.zeros(4))

def seed_raw(i,j,k,l):
    return sum(t[b][j,i]*dual[b][k,l] for b in range(3))

def seed_fierz(i,j,k,l):
    return -(2*int(i==l and k==j)-int(i==j and k==l))*s.Rational(1,4)

def act(j,a,n,fun):
    return sum(R[j][a][n[j],m]*fun(*n[:j],m,*n[j+1:]) for m in range(2))

def box_physical(k,ps):
    p1,p2,p3,p4=ps
    assert p1+p2+p3+p4==s.zeros(4,1)
    rA=k-p2
    rB=k+p3
    h=p4+rB
    assert h==rA-p1
    A=p2-rA
    B=-p3-rB
    d=(sq(k),sq(rA),sq(rB),sq(h)-400)
    assert all(d)
    return dot(A,B)*slash(h)*P_L/s.prod(d),d

def bare_legs(k,p,q):
    out=[]; poles=[]
    for i in N:
        ps=list(p); P=p[i]+q; ps[i]=P
        F,d=box_physical(k,ps); poles.append(d)
        # Whole W vertex and intermediate matter propagator in exact flow;
        # common g2 P4 removed. Remaining i*i is the minus on all four.
        if i==0:
            A=[I*G[m]*P_L*I*S(P)*F for m in N]
        elif i==3:
            A=[F*I*S(P)*I*G[m]*P_L for m in N]
        else:
            current=p[i]+P
            A=[I*current[m]*I*F/sq(P) for m in N]
        out.append(linear([eta[m,m]*q[m] for m in N],A))
    return out,poles

def source(k,p,q):
    # Independent fixed-k Fourier source variation. Insertion exp(-iqx)
    # sends p_j to p_j+q in this convention. Keep the four finite shifts.
    h=k-p[0]-p[1]
    a=2*p[1]-k
    b=-2*p[2]-k
    a0=k-p[1]
    b0=k+p[2]
    data=((a,b,a0,b0,h-q),(a+2*q,b,a0-q,b0,h-q),
          (a,b-2*q,a0,b0+q,h),(a,b,a0,b0,h))
    fs=[]
    for a,b,rA,rB,H in data:
        d=(sq(k),sq(rA),sq(rB),sq(H)-400)
        assert all(d)
        fs.append(dot(a,b)*slash(H)*P_L/s.prod(d))
    inv=(slash(p[0])*S(p[0]+q)*fs[0],
         sq(p[1])/sq(p[1]+q)*fs[1],
         sq(p[2])/sq(p[2]+q)*fs[2],
         fs[3]*S(p[3]+q)*slash(p[3]))
    return fs,inv

def connected_bare(k,p,q):
    # Restore every original external propagator in each diagram before
    # comparison to the endpoint. Scalar i factors are kept.
    ans=[]
    for i in N:
        P=p[i]+q; ps=list(p); ps[i]=P
        F,_=box_physical(k,ps)
        A=I*S(p[0]); B=I*S(p[3]); H=I/sq(p[1]); Hb=I/sq(p[2])
        if i==0:
            out=H*Hb*A*(I*slash(q)*P_L)*(I*S(P))*F*B
        elif i==3:
            out=H*Hb*A*F*(I*S(P))*(I*slash(q)*P_L)*B
        else:
            out=H*Hb*A*F*B*(I*dot(q,p[i]+P))*(I/sq(P))
        ans.append(out)
    return ans

def known_internal(k,p,q,a,n):
    # Exactly the archived common-k 2-line + 2-seagull + 3W subset,
    # without starting a second dummy-variable translation.
    kap=k+q
    rAY,rAW=k-p[1],kap-p[1]
    rBY,rBW=kap+p[2],k+p[2]
    h=k-p[0]-p[1]
    VA,VB=2*p[1]-k,-2*p[2]-kap
    K,V,A,AW,B,BW=map(sq,(k,kap,rAY,rAW,rBY,rBW))
    Hp=sq(h)-400
    assert all((K,V,A,AW,B,BW,Hp))
    def commute(slot1,slot2,ward_first):
        return sum(act(slot1,b if ward_first else a,n,
                       lambda *m: act(slot1,a if ward_first else b,m,
                         lambda *z: act(slot2,b,z,seed_identity))) for b in range(3))
    wa=commute(1,2,True); ta=commute(1,2,False)
    wb=commute(2,1,False); tb=commute(2,1,True)
    Gweak=sum(s.LeviCivita(a,b,c)*act(1,b,n,lambda *m:act(2,c,m,seed_identity))
              for b,c in product(range(3),repeat=2))
    # q Γ contraction with metric convention and archived A->B phase.
    scalar_a=-dot(q,rAY+rAW)*dot(VA-q,VB)/(A*AW*V*B)
    scalar_b=-dot(q,rBY+rBW)*dot(VA,VB+q)/(B*BW*K*A)
    sg_a=dot(q,VB)/(V*A*B)
    sg_b=dot(VA,q)/(K*A*B)
    ym=(V-K)*dot(VA,VB)+dot(VA,k)*dot(VB,k)-dot(VA,kap)*dot(VB,kap)
    val=scalar_a*wa+scalar_b*wb+sg_a*(wa+ta)+sg_b*(wb+tb)-I*ym*Gweak/(K*V*A*B)
    return val*slash(h)*P_L/Hp

def seed_identity(i,j,k,l):
    return int(i==j and k==l)

def sample(A):
    # Stable list of (Dirac row, column, exact scalar) for first nonzero element.
    for n,x in enumerate(A):
        value=s.expand(x)
        if value:
            return [n//4,n%4,str(value)]

POINTS=(
 ((4,1,2,1),(1,2,0,1),(2,0,1,0),(0,1,0,2),(2,1,1,1)),
 ((6,1,0,1),(1,1,0,0),(2,0,1,0),(0,2,0,1),(2,0,1,0)),
 # four original null momenta; q computed separately and need not be null
 ((7,1,2,2),None,(1,1,0,0),(2,0,2,0),(3,0,0,3),(4,-4,0,0)),
 ((4,1,2,1),(0,0,0,0),(2,0,1,0),(0,1,0,2),(2,1,1,1)),
)

def run():
    assert all(seed_raw(*n)==seed_fierz(*n) for n in ix)
    for a,n in product(range(3),ix):
        assert sum(act(i,a,n,seed_fierz) for i in N)==0
    rows=[]
    for data in POINTS:
        k=s.Matrix(data[0])
        p=list(map(s.Matrix,data[2:]))
        q=s.Matrix(data[1]) if data[1] is not None else -sum(p,s.zeros(4,1))
        if len(p)==3:
            p.append(-sum(p,s.zeros(4,1))-q)
        assert sum(p,s.zeros(4,1))+q==s.zeros(4,1)
        on=all(not sq(x) for x in p)
        off=all(sq(x) for x in p)
        assert all(sq(x+q) for x in p) and (on or off)
        raw,d=bare_legs(k,p,q)
        F,inv=source(k,p,q)
        conn=connected_bare(k,p,q) if off else None
        if on:
            left=slash(p[0])*P_R; right=P_L*slash(p[3])
            assert left*slash(p[0])==s.zeros(4) and slash(p[3])*right==s.zeros(4)
        stat={a:0 for a in ("amputated","connected","projected","wrong_fermion_order",
                            "omitted_inverse","wrong_heavy_rule","missing_one_leg",
                            "source_nonzero","projected_source_nonzero","selected_internal_remainder_nonzero")}
        r_example=None
        for a,n in product(range(3),ix):
            w=[act(i,a,n,seed_raw) for i in N]
            z=[act(i,a,n,seed_fierz) for i in N]
            bare=linear(w,raw)
            variation=linear(z,F)
            assert not diff(variation,linear(z,[f-F[3] for f in F]))
            Rinv=linear(z,inv)
            rhs=-variation+Rinv
            assert not diff(bare,rhs)
            stat["amputated"]+=16
            if off:
                restored=linear(w,conn)
                ended=(I/sq(p[1]))*(I/sq(p[2]))*(I*S(p[0]))*rhs*(I*S(p[3]))
                assert not diff(restored,ended)
                stat["connected"]+=16
            else:
                assert not diff(left*bare*right,-left*variation*right)
                stat["projected"]+=16
                stat["projected_source_nonzero"]+=diff(left*variation*right,s.zeros(4))
            check_data=bare if off else left*bare*right
            noinv=-variation if off else -left*variation*right
            stat["omitted_inverse"]+=diff(check_data,noinv)
            left_bad=F[0]*S(p[0]+q)*slash(p[0])
            right_bad=slash(p[3])*S(p[3]+q)*F[3]
            stat["wrong_fermion_order"]+=diff(bare,rhs+z[0]*(left_bad-inv[0])+z[3]*(right_bad-inv[3]))
            h0=k-p[0]-p[1]
            # Reusing the p4-shifted kernel for p1 would omit the heavy shift.
            assert d[0][0:3]==d[3][0:3] and d[0][3]==sq(h0-q)-400 and d[3][3]==sq(h0)-400
            err_h=F[3]-slash(p[0])*S(p[0]+q)*F[3]
            stat["wrong_heavy_rule"]+=diff(bare,rhs-z[0]*(err_h-(F[0]-inv[0])))
            stat["missing_one_leg"]+=diff(bare,bare-w[1]*raw[1])
            stat["source_nonzero"]+=diff(variation,s.zeros(4))
            if off and q!=s.zeros(4,1):
                combined=bare+known_internal(k,p,q,a,n)
                stat["selected_internal_remainder_nonzero"]+=diff(combined,s.zeros(4))
                if r_example is None and sample(combined):
                    r_example={"W_generator_index_zero_based":a,"weak_indices_zero_based":n,
                               "dirac_entry_zero_based_and_value":sample(combined)}
        if q==s.zeros(4,1):
            assert stat["source_nonzero"]==stat["omitted_inverse"]==0
        else:
            assert stat["source_nonzero"] and stat["missing_one_leg"] and stat["wrong_fermion_order"]
            assert bool(stat["omitted_inverse"])==off
            if on:
                assert stat["projected_source_nonzero"]
            if off:
                assert stat["wrong_heavy_rule"] and r_example
        rows.append({"q_squared":str(sq(q)),"q_zero":q==s.zeros(4,1),"all_original_legs_null":on,
            "original_virtualities":list(map(lambda x:str(sq(x)),p)),
            "shifted_virtualities":list(map(lambda x:str(sq(x+q)),p)),
            "heavy_denominators_for_four_shifts":[str(x[3]) for x in d],
            "counts":stat,"partial_internal_diagnostic_evaluated":bool(off and q!=s.zeros(4,1)),
            "pointwise_partial_remainder_example":r_example})
    return {"scope":"four bare reducible LD-W-06 external emissions at a fixed loop coordinate; selected internal diagnostic is not an integrated physics test",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),
                       "machine":platform.machine()},
            "symbolic":{"seed_tensor_entries":16,"global_covariance_entries":48},
            "points":rows}

if __name__ == "__main__":
    print(json.dumps(run(),indent=2))
