"""Exact symbolic audit: Dirac numerator -> d-dimensional angular average -> B kernels.
Requires sympy. This checks algebraic reductions, not the overall Minkowski diagram sign.
"""
import sympy as sp

x1,x2,x3,x4,d=sp.symbols('x1 x2 x3 x4 d')
Q1,Q2,Q3,Q4,Q5,Q6=sp.symbols('Q1:7')
A=x2+x3
# Coefficients of q1,q2,q3 in t_i, using the fixed labeled routing.
t=[
    sp.Matrix([-x4, A, x3]),
    sp.Matrix([-x4, A-1, x3]),
    sp.Matrix([-x4, A-1, x3-1]),
    sp.Matrix([1-x4, A, x3]),
]
# Gram matrix in basis Q=(q1^2,q2^2,q3^2,q1.q2,q1.q3,q2.q3)
Gm=sp.Matrix([[Q1,Q4,Q5],[Q4,Q2,Q6],[Q5,Q6,Q3]])
def dot(u,v):
    return sp.expand((u.T*Gm*v)[0])
def coeffs(expr):
    return tuple(sp.factor(sp.diff(sp.expand(expr), Q)) for Q in (Q1,Q2,Q3,Q4,Q5,Q6))

f={}
for i in range(4):
    for j in range(i+1,4):
        f[(i+1,j+1)]=coeffs(dot(t[i],t[j]))
Aexpr=sp.expand(x2+x3)
f_expected={
(1,2):(x4**2,Aexpr*(Aexpr-1),x3**2,-x4*(2*Aexpr-1),-2*x3*x4,x3*(2*Aexpr-1)),
(1,3):(x4**2,Aexpr*(Aexpr-1),x3*(x3-1),-x4*(2*Aexpr-1),-x4*(2*x3-1),2*x2*x3-x2+2*x3**2-2*x3),
(1,4):(x4*(x4-1),Aexpr**2,x3**2,-Aexpr*(2*x4-1),-x3*(2*x4-1),2*x3*Aexpr),
(2,3):(x4**2,(Aexpr-1)**2,x3*(x3-1),-2*x4*(Aexpr-1),-x4*(2*x3-1),(2*x3-1)*(Aexpr-1)),
(2,4):(x4*(x4-1),Aexpr*(Aexpr-1),x3**2,-2*x4*Aexpr+Aexpr+x4-1,-x3*(2*x4-1),x3*(2*Aexpr-1)),
(3,4):(x4*(x4-1),Aexpr*(Aexpr-1),x3*(x3-1),-2*x4*Aexpr+Aexpr+x4-1,-2*x3*x4+x3+x4-1,2*x2*x3-x2+2*x3**2-2*x3),
}
for pair in f:
    assert all(sp.simplify(a-b)==0 for a,b in zip(f[pair],f_expected[pair])), f'point-dot mismatch {pair}'
print('PASS: all six f_ij vectors reconstructed from t_i dot t_j')

# Derive g by expanding G(K+t1,...,K+t4) with formal loop contractions.
# D_ij = K^2 + K.t_i + K.t_j + t_i.t_j. Odd K terms vanish;
# K.t_i K.t_j is replaced by K^2/d * (t_i.t_j).
Z = sp.symbols('K2')
L = sp.symbols('L1:5')
T = {}
for i in range(1,5):
    for j in range(i+1,5):
        T[(i,j)] = sp.symbols(f'T{i}{j}')
def D(i,j):
    return Z + L[i-1] + L[j-1] + T[(min(i,j),max(i,j))]
Gformal = sp.expand(D(1,2)*D(3,4) - D(1,3)*D(2,4) + D(1,4)*D(2,3))
# Keep the direct Z*T terms; remove odd terms and Z^2 (zero-external-momentum).
Gterms = sp.Poly(Gformal, Z, *L, *T.values()).terms()
avg_q2 = 0
for monom, coeff in Gterms:
    powers = dict(zip((Z, *L, *T.values()), monom))
    zpow = powers[Z]
    lpow = sum(powers[ell] for ell in L)
    tpow = sum(powers[tv] for tv in T.values())
    # q^2 terms: Z^1*T^1 direct term, or two L factors averaged to Z/d*T.
    if zpow == 1 and lpow == 0 and tpow == 1:
        avg_q2 += coeff * Z * sp.prod(tv**powers[tv] for tv in T.values())
    elif zpow == 0 and lpow == 2 and tpow == 0:
        # Each L_i L_j maps to Z/d times t_i.t_j; L_i^2 maps to Z/d*t_i^2.
        ls = [ell for ell in L for _ in range(powers[ell])]
        if len(ls) == 2:
            ii = int(str(ls[0])[1:]); jj = int(str(ls[1])[1:])
            if ii == jj:
                # t_i^2 is not needed explicitly in the pairwise coefficient formula;
                # retain as T_ii for a complete formal average.
                tv = sp.symbols(f'T{ii}{ii}')
            else:
                tv = T[(min(ii,jj),max(ii,jj))]
            avg_q2 += coeff * Z * tv / d
# Collect the K^2 coefficient and substitute each T_ij by its independently generated Q vector.
g_from_trace = sp.expand(avg_q2.coeff(Z))
subT = {}
for (i,j), tv in T.items():
    subT[tv] = sum(f[(i,j)][a]*q for a,q in enumerate((Q1,Q2,Q3,Q4,Q5,Q6)))
g_coeffs_from_trace = coeffs(g_from_trace.subs(subT))
g_formula=tuple(sp.factor(f[(1,2)][i]+f[(3,4)][i]-f[(1,3)][i]-f[(2,4)][i]+f[(1,4)][i]+f[(2,3)][i]+sp.Rational(2,1)/d*(f[(1,3)][i]+f[(2,4)][i])) for i in range(6))
assert all(sp.simplify(a-b)==0 for a,b in zip(g_coeffs_from_trace,g_formula)), (g_coeffs_from_trace,g_formula)
print('PASS: explicit expansion of G(K+t1,...,K+t4) and angular averaging reproduces g')

# Reproduce delta Delta from sum x_i r_i^2 - R^2 for r=(0,-q2,-q2-q3,q1).
r=[sp.Matrix([0,0,0]),sp.Matrix([0,-1,0]),sp.Matrix([0,-1,-1]),sp.Matrix([1,0,0])]
R=sum((xx*rr for xx,rr in zip((x1,x2,x3,x4),r)),sp.zeros(3,1))
delta=sp.expand(sum(xx*dot(rr,rr) for xx,rr in zip((x1,x2,x3,x4),r))-dot(R,R))
d_expected=(x4*(1-x4), A*(1-A), x3*(1-x3), 2*x4*A, 2*x3*x4, 2*x3*(1-A))
assert all(sp.simplify(a-b)==0 for a,b in zip(coeffs(delta),d_expected)), 'delta Delta mismatch'
print('PASS: delta Delta gives the six d_alpha polynomials')

# Exact conversion from the I-integral kernel to B_p/Delta^p.
# I0(4)=1/(16pi^2)*1/(6 Delta^2), I1(4)=1/(16pi^2)*1/(3 Delta),
# I2(5)=1/(16pi^2)*1/(4 Delta), I1(5)=1/(16pi^2)*1/(12 Delta^2),
# I0(5)=1/(16pi^2)*1/(12 Delta^3).
H,S,M,F,dalpha,galpha,Delta=sp.symbols('H S M F d_alpha g_alpha Delta', nonzero=True)
K_reduced=sp.expand(2*F/(6*Delta**2)+2*H*galpha/(3*Delta)-8*dalpha*(H/(4*Delta)+S/(12*Delta**2)+M/(12*Delta**3)))
B1=H*(sp.Rational(2,3)*galpha-2*dalpha)
B2=sp.Rational(1,3)*F-sp.Rational(2,3)*S*dalpha
B3=-sp.Rational(2,3)*M*dalpha
B_reduced=B1/Delta+B2/Delta**2+B3/Delta**3
assert sp.simplify(K_reduced-B_reduced)==0
print('PASS: I-integral kernel converts exactly to B1/Delta + B2/Delta^2 + B3/Delta^3')
print('BOUNDARY: this does not establish the overall Minkowski i/sign, graph multiplicity, or UV-EFT subtraction.')
