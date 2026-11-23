"""Exact independent fixed-k comparison of selected commutators and Yang–Mills."""
import itertools
import json
import sympy as s

R=s.Rational
I=s.I
eta=s.diag(1,-1,-1,-1)
v=lambda items:s.Matrix(items)
dot=lambda x,y:(x.T*eta*y)[0]
sq=lambda x:dot(x,x)
perms=list(itertools.permutations(range(3)))


def action_vertex(momentum, polarization):
    # -g f^{abc}(∂_μ W_ν^a)W^{bμ}W^{cν}; iS and e^{-ipx}
    # give -g times the sum of all assignments of the three labelled legs.
    return -sum(s.LeviCivita(i,j,l)*dot(momentum[i],polarization[j])*
                dot(polarization[i],polarization[l]) for i,j,l in perms)


def weak():
    t=[s.Matrix([[0,1],[1,0]])/2,s.Matrix([[0,-I],[I,0]])/2,s.diag(1,-1)/2]
    A=[s.kronecker_product(x,s.eye(2)) for x in t]
    B=[s.kronecker_product(s.eye(2),-x.T) for x in t]
    for c in range(3):
        G=sum((s.LeviCivita(c,j,l)*A[j]*B[l] for j in range(3) for l in range(3)),s.zeros(4))
        wa=sum(((A[j]*A[c]-A[c]*A[j])*B[j] for j in range(3)),s.zeros(4))
        wb=sum((A[j]*(B[c]*B[j]-B[j]*B[c]) for j in range(3)),s.zeros(4))
        assert wa==wb==I*G
        assert G!=s.zeros(4)
    assert (-I)**2/(-I)==-I
    return 96


def symbolic():
    # Contract the action in a Gram algebra before using any null/shell condition.
    names=('q2','k2','qk','ab','aq','bq','ak','bk','qp2','kp2','qp3','kp3')
    q2,k2,qk,ab,aq,bq,ak,bk,qp2,kp2,qp3,kp3=s.symbols(' '.join(names))
    G=s.Matrix([[q2,qk,aq,bq],[qk,k2,ak,bk],[aq,ak,0,ab],[bq,bk,ab,0]])
    q,k,a,b=[s.eye(4)[:,j] for j in range(4)]
    def act(momentum, pol):
        return -sum(s.LeviCivita(i,j,l)*(momentum[i].T*G*pol[j])[0]*
                    (pol[i].T*G*pol[l])[0] for i,j,l in perms)
    raw=act((q,k,-k-q),(q,a,b))
    K2=k2+2*qk+q2
    metric=(K2-k2)*ab
    assert s.expand(raw-(metric-ak*bq-(bk+bq)*aq))==0
    total=k2*bq+K2*aq-raw
    frozen=total.subs({ak:2*kp2-k2,bk:-2*(kp3+qp3)-K2-bq}, simultaneous=True)
    assert s.expand(frozen-(2*kp2*bq-2*(kp3+qp3)*aq-metric))==0
    assert s.expand(total.subs(qk,-q2/2).subs(aq,0)-(k2+ak)*bq)==0
    assert s.expand(total.subs(qk,-q2/2).subs(bq,0)-(k2+bk)*aq)==0
    return 4


def point(label,p2,p3,kx,expect):
    q=v([0,2,0,0]); k=v([4,kx,1,0]); K=k+q
    p1=v([2,0,1,2]); p2=v(p2); p3=v(p3); p4=-p1-p2-p3-q
    rA,rB,h=k-p2,K+p3,k-p1-p2
    assert h==rA-p1==rB+p4
    a,b=2*p2-k,-2*p3-K
    aq,bq=dot(a,q),dot(b,q)
    Q,KQ=sq(k),sq(K)
    factors=[Q,KQ,sq(rA),sq(rB),sq(h)-400]
    assert all(factors) and sq(q)==-4 and all(map(sq,[p1,p2,p3,p4]))
    assert h != s.zeros(4,1)
    action=action_vertex((q,k,-K),(q,a,b))
    ac,bc=Q*bq,KQ*aq
    projected_yang_mills=-action
    subtotal=ac+bc+projected_yang_mills
    metric=(KQ-Q)*dot(a,b)
    new=2*dot(p2,k)*bq-2*dot(p3,K)*aq-metric
    assert subtotal==new
    assert subtotal==expect
    if label.startswith("A"):
        assert Q==KQ and aq==0 and bq!=0 and bool(subtotal)==bool(dot(p2,k))
    if label.startswith("B"):
        assert Q==KQ and bq==0 and aq!=0 and bool(subtotal)==bool(dot(p3,K))
    if label.endswith("exact"):
        assert ac+bc!=0 and projected_yang_mills!=0
    return {"label":label,"k":[str(x) for x in k],"p2":[str(x) for x in p2],
            "p3":[str(x) for x in p3],"p1":[str(x) for x in p1],"q":[str(x) for x in q],
            "p4":[str(x) for x in p4],"q_squared":str(sq(q)),
            "D3W_factors":[str(x) for x in factors],"a_dot_q":str(aq),"b_dot_q":str(bq),
            "p2_dot_k":str(dot(p2,k)),"p3_dot_K":str(dot(p3,K)),
            "A_numerator":str(ac),"B_numerator":str(bc),
            "three_W_numerator":str(projected_yang_mills),"metric_piece":str(-metric),
            "selected_sum_numerator":str(subtotal),"selected_sum_over_D3W":str(subtotal/s.prod(factors)),
            "mutation_delta":{"flipped_YM_phase":str(2*action),
                              "metric_only":str(action-metric),
                              "swap_single_W_weights":str((KQ-Q)*(bq-aq))}}


def main():
    A=[1,-R(1,2),R(7,2),1]; At=[1,-R(1,2),R(5,2),1]
    B=[1,-R(1,2),R(9,2),1]; Bt=[1,-R(1,2),R(7,2),1]
    C=[1,2,1,0]
    checks=weak(),symbolic()
    rows=[point("A exact",A,C,-1,0),point("A detuned",At,C,-1,20),
          point("B exact",[1,2,0,1],B,-1,0),point("B detuned",[1,2,0,1],Bt,-1,20),
          point("generic nonzero metric",At,C,0,112)]
    for r in rows[:4]:
        assert r["mutation_delta"]["flipped_YM_phase"]!="0"
        assert r["mutation_delta"]["metric_only"]!="0"
    assert rows[-1]["mutation_delta"]["swap_single_W_weights"]!="0"
    print(json.dumps({"normalization":"g2 P4 iG_AB slash(h) P_L",
                      "weak_entries":checks[0],"symbolic_identities":checks[1],
                      "points":rows},indent=2))


if __name__=="__main__":
    main()
