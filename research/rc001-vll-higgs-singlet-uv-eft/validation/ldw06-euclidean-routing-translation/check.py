"""Exact route, pole-center and Euclidean large-ray controls (no integration)."""
import itertools
import json
import sympy as s

v=lambda xs:s.Matrix(xs)
sq=lambda x:x.dot(x)
zero=s.zeros(4,1)
p1,p2,p3,q=[s.eye(4)[:,i] for i in range(4)]
p4=-p1-p2-p3-q
mass2=s.Integer(400)
t=s.Symbol("R", positive=True)
es=[s.eye(4)[:,i] for i in range(4)]
w=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
gamma=[s.kronecker_product(w[0],m) for m in w]+[s.kronecker_product(w[1],s.eye(2))]
PL=(s.eye(4)-gamma[0]*gamma[1]*gamma[2]*gamma[3])/2


def slash(x):
    return sum((g*y for g,y in zip(gamma,x)),s.zeros(4))


def direct_box(k, ps):
    p1x,p2x,p3x,p4x=ps
    assert p1x+p2x+p3x+p4x==zero
    rA=k-p2x
    h=rA-p1x
    rB=h-p4x
    assert rB==k+p3x
    a=p2x-rA
    b=-p3x-rB
    return (k,rA,rB,h),a,b


def routed_negative(k, side):
    K=k+q
    h=k-p1-p2
    a,b=2*p2-k,-2*p3-K
    if side=="A":
        return (K,K-p2,K+p3,h),a-q,b
    return (k,k-p2,k+p3,h),a,b+q


def factors(route):
    lines,a,b=route
    return (*map(sq,lines[:3]),sq(lines[3])+mass2)


def rational_vector(route):
    # Matrix coefficients of gamma_mu P_L are formed after taking exact
    # coefficient limits; this independently preserves the Dirac numerator.
    lines,a,b=route
    return lines[-1]*a.dot(b)/s.prod(factors(route))


def pole_centers(route):
    return tuple(tuple(map(int,-v0)) for v0 in route[0][:3])


def vector_checks(x,y):
    assert all(s.expand(i-j)==0 for i,j in zip(x,y))
    return len(x)


def symbolic_checks():
    global p1,p2,p3,q
    original=p1,p2,p3,q
    p1,p2,p3,q=[v(s.symbols(f"{x}_0:4")) for x in ("p1","p2","p3","q")]
    p4=-p1-p2-p3-q
    k=v(s.symbols("k_0:4"))
    lowerA=direct_box(k,(p1+q,p2,p3,p4))
    lowerB=direct_box(k+q,(p1,p2,p3,p4+q))
    count=0
    for L,X in ((routed_negative(k-q,"A"),lowerA),(routed_negative(k+q,"B"),lowerB)):
        for lhs,rhs in zip((*L[0],*L[1:]),(*X[0],*X[1:])):
            count+=vector_checks(lhs,rhs)
        count+=vector_checks(factors(L),factors(X))
        count+=vector_checks(L[0][-1]*L[1].dot(L[2]),X[0][-1]*X[1].dot(X[2]))
    # Mapping A-anchored to B-anchored is a common translation of all factors,
    # not a replacement of only the light denominator or the heavy argument.
    H,D,u,z=s.symbols("H D u z")
    assert s.cancel((u+z)/(H+D)-u/H-(H*z-D*u)/(H*(H+D)))==0
    p1,p2,p3,q=original
    return count,1


def prescribed(k):
    ps=[p1,p2,p3,p4]
    shifted=[direct_box(k,[p+q if i==j else p for i,p in enumerate(ps)]) for j in range(4)]
    return {"F1":shifted[0],"F2":shifted[1],"F3":shifted[2],"F4":shifted[3],
            "A_original":routed_negative(k,"A"),"B_original":routed_negative(k,"B"),
            "A_translated":routed_negative(k-q,"A"),"B_translated":routed_negative(k+q,"B")}


def radial_coeff(expr,p):
    vals=[]
    for y in expr:
        y=s.cancel(y)
        if y==0:
            vals.append(s.S.Zero)
            continue
        x,d=s.fraction(y)
        num,den=s.Poly(x,t),s.Poly(d,t)
        power=num.degree()-den.degree()+p
        assert power<=0,(y,p,power)
        vals.append(num.LC()/den.LC() if power==0 else s.S.Zero)
    return v(vals)


def strings(x):
    return list(map(str,list(x)))


def main():
    route_checks,heavy_identity=symbolic_checks()
    for i,j in itertools.product(range(4),repeat=2):
        assert gamma[i]*gamma[j]+gamma[j]*gamma[i]==2*int(i==j)*s.eye(4)
    assert PL**2==PL and s.trace(PL)==2
    points={}
    for label,k in {"parallel":es[3],"orthogonal":es[0],"oblique":v([1,2,-1,1])}.items():
        routes=prescribed(t*k)
        allF={name:rational_vector(R) for name,R in routes.items()}
        expected=k/sq(k)**3
        for key in allF:
            assert radial_coeff(allF[key],5)==expected
        assert slash(expected)*PL!=s.zeros(4)
        diffs={}
        for name in ["F1","F2","F3"]:
            diffs[name+"−F4"]=strings(radial_coeff(allF[name]-allF["F4"],6))
        # Fixed light route: vary heavy line only using F1 and F4, which
        # have exactly coincident light data, then check both heavy signs.
        L=routes["F4"]
        assert routes["F1"][0][:3]==L[0][:3] and routes["F1"][1:]==L[1:]
        for sign in (-1,1):
            moved=((*L[0][:3],L[0][-1]+sign*q),*L[1:])
            lead=radial_coeff(rational_vector(moved)-allF["F4"],6)
            target=sign*(q/sq(k)**3-2*k.dot(q)*k/sq(k)**4)
            assert lead==target and slash(lead)*PL!=s.zeros(4)
            diffs["fixed_light_"+str(sign)]=strings(lead)
        points[label]={"direction":strings(k),"all_routes_R5_leading":strings(expected),
                       "R6_difference_leading":diffs}
    centers={name:pole_centers(route) for name,route in prescribed(zero).items()}
    for c in centers.values():
        assert len(set(c))==3
        assert min(sq(v(x)-v(y)) for x,y in itertools.combinations(c,2))>=1
    # Set p2=0 separately in the unshifted light chart; at F4, W and A
    # centers coincide. This only falsifies the distinct-center premise.
    exceptional=direct_box(zero,(p1,zero,p3,-p1-p3))
    collision=pole_centers(exceptional)
    assert collision[0]==collision[1]!=collision[2]
    print(json.dumps({"route_components":route_checks,"heavy_identity":heavy_identity,
        "clifford_pairs":16,"matrix_slash_chirality_nonzero":True,"nominal_centers":centers,
        "exceptional_centers":collision,"ray_controls":points},indent=2,ensure_ascii=False))


if __name__=="__main__":
    main()
