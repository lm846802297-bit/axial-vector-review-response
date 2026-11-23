#!/usr/bin/env python3
"""Derive the conditional O(p^2) B1/B2/B3 kernel signs from the generic trace.

Conventions: metric (+---), propagator denominators D_i=(k+r_i)^2-m_i^2,
shift K=k+R, and combined Minkowski denominator K_M^2-Delta_0+d.
After Wick rotation K_M^2=-K_E^2, so the four-denominator scalar factor is
(K_E^2+Delta_0-d)^(-4). The common diagrammatic i/sign and model-specific
six-cycle amplitude normalization are intentionally kept outside this kernel.
Requires Python 3 + SymPy.
"""
import sympy as sp

checks=[]
def check(name, expr, expected=0):
    residual=sp.simplify(sp.expand(expr-expected))
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks.append(name)
    print(f"PASS: {name}")

H,g,F,S,M,d,Delta=sp.symbols("H g F S M d Delta", real=True, nonzero=True)
# Euclidean scalar integrals with the common 1/(16 pi^2) removed:
# I_r^(n) = Delta^(2+r-n) Gamma(r+2) Gamma(n-r-2)/(Gamma(2) Gamma(n)).
def I(r,n):
    return sp.simplify(Delta**(2+r-n)*sp.gamma(r+2)*sp.gamma(n-r-2)/(sp.gamma(2)*sp.gamma(n)))
check("I_2^(5)=1/(4 Delta)", I(2,5), 1/(4*Delta))
check("I_1^(4)=1/(3 Delta)", I(1,4), 1/(3*Delta))
check("I_0^(4)=1/(6 Delta^2)", I(0,4), 1/(6*Delta**2))
check("I_1^(5)=1/(12 Delta^2)", I(1,5), 1/(12*Delta**2))
check("I_0^(5)=1/(12 Delta^3)", I(0,5), 1/(12*Delta**3))

# Minkowski numerator decomposition from the explicitly checked chiral trace:
# N = 2 H G + 2 sum_ij C_ij k_i.k_j + 2 M + 2 i E H_odd.
# After k_i=K+t_i and angular averaging through O(p^2):
# G -> K_M^4 + g K_M^2 + O(p^4); sum C k_i.k_j -> S K_M^2+F+odd terms.
# Wick rotation gives K_M^4 -> K_E^4, K_M^2 -> -K_E^2 in the tensor term.
# The shifted denominator is (K_E^2+Delta-d)^(-4).
# Its linear expansion is base + 4 d (K_E^2+Delta)^(-5).
z=sp.Symbol('z')
base_shift=sp.expand((1-z)**(-4))
check("denominator expansion coefficient of d is +4", sp.diff(base_shift,z).subs(z,0), 4)

# O(p^2) terms from each numerator sector. The common i/(16 pi^2) is stripped.
B1_g=sp.simplify((-2*H*g)*I(1,4))
B1_d=sp.simplify((2*H)*(4*d)*I(2,5))
B2_F=sp.simplify((2*F)*I(0,4))
B2_d=sp.simplify((-2*S)*(4*d)*I(1,5))
B3_d=sp.simplify((2*M)*(4*d)*I(0,5))
check("four-slash tensor term gives -2 H g/(3 Delta)",B1_g,-sp.Rational(2,3)*H*g/Delta)
check("four-slash denominator-shift term gives +2 H d/Delta",B1_d,2*H*d/Delta)
check("two-slash external-invariant term gives +F/(3 Delta^2)",B2_F,F/(3*Delta**2))
check("two-slash denominator-shift term gives -2 S d/(3 Delta^2)",B2_d,-sp.Rational(2,3)*S*d/Delta**2)
check("mass numerator denominator-shift term gives +2 M d/(3 Delta^3)",B3_d,sp.Rational(2,3)*M*d/Delta**3)

B1=sp.factor(B1_g+B1_d)
B2=sp.factor(B2_F+B2_d)
B3=sp.factor(B3_d)
check("assembled B1 equals H(-2g/3+2d)/Delta",B1,H*(-sp.Rational(2,3)*g+2*d)/Delta)
check("assembled B2 equals (F/3-2Sd/3)/Delta^2",B2,(F-2*S*d)/(3*Delta**2))
check("assembled B3 equals 2Md/(3 Delta^3)",B3,sp.Rational(2,3)*M*d/Delta**3)

# If the denominator were instead (K_E^2+Delta+d)^(-4), only d-insertion terms
# flip. The tensor K_M^2 -> -K_E^2 sign does not flip. This distinguishes a
# denominator-shift change from the legacy whole-B1 sign flip.
B1_alt=sp.simplify(B1_g-B1_d)
B2_alt=sp.simplify(B2_F-B2_d)
B3_alt=sp.simplify(-B3_d)
check("opposite denominator shift flips d terms but not the B1 tensor term",B1_alt,(-sp.Rational(2,3)*H*g-2*H*d)/Delta)
check("opposite denominator shift flips only the B2 d insertion",B2_alt,(F+2*S*d)/(3*Delta**2))
check("opposite denominator shift flips the B3 insertion",B3_alt,-sp.Rational(2,3)*M*d/Delta**3)

# Verify parity-odd epsilon structure by multilinearity of the determinant.
# E=det[K+t1,K+t2,K+t3,K+t4]: terms with two K columns vanish;
# one-K terms are odd in K and integrate to zero; the K-independent term is O(p^4).
Ksym=sp.symbols("K0:4")
tsym=[[sp.symbols(f"t{i}_{mu}") for mu in range(4)] for i in range(1,5)]
Eshift=sp.expand(sp.det(sp.Matrix.hstack(*[sp.Matrix([Ksym[mu]+tsym[i][mu] for mu in range(4)]) for i in range(4)])))
P=sp.Poly(Eshift,*Ksym)
max_K_degree=max(sum(monom) for monom,_ in P.terms())
check("epsilon determinant is at most linear in the shifted loop momentum",max_K_degree,1)
constant_term=sp.expand(Eshift.subs({Ksym[i]:0 for i in range(4)}))
check("epsilon determinant's loop-independent term is quartic in external shifts",sp.Poly(constant_term,*[x for row in tsym for x in row]).total_degree(),4)

print(f"RESULT: {len(checks)} exact symbolic kernel/sign checks passed.")
print("DERIVED: B1=H(-2 g/3+2 d)/Delta; B2=(F/3-2 S d/3)/Delta^2; B3=2 M d/(3 Delta^3).")
print("SCOPE: conditional kernel signs under the declared generic trace, metric, denominator routing, and Wick convention.")
print("OPEN: mapping all model-specific mass paths and external cycles to this trace, global i/closed-loop/symmetry factors, dimensionally regulated light-mass regions, complete EFT soft graphs/counterterms, and final UV-EFT finite Wilson coefficient.")
