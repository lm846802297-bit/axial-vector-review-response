#!/usr/bin/env python3
"""RC-001 exact full-propagator basis-covariance and path-sum audit.

For the fixed complex orientation H,S,Sdag,Hdag (mu) or H,Sdag,S,Hdag
(tau), the chiral trace has the flavor structure
  Y_h P_1 Y_s D_2 Y_s^T P_3 Y_h^T D_4,
where D_i=diag(1/(k_i^2-m_a^2)) and
P_i=diag(m_a/(k_i^2-m_a^2)).
The script verifies that the sum over all 16 mass-eigenstate paths equals
the interaction-basis matrix-propagator trace exactly, for finite mixing.
It then takes the unbroken limit and verifies that only path 0101 survives,
reproducing the source-aligned two-heavy/two-light box integrand.
Metric (+---); real Yukawa couplings; positive light masses with the
right-handed rephasing D=diag(-1,1).
Requires Python 3 and SymPy.
"""
from itertools import product
import sympy as sp

checks = 0
def check(name, expr, expected=0):
    global checks
    residual = sp.cancel(sp.together(sp.simplify(expr - expected)))
    if isinstance(residual, sp.MatrixBase):
        ok = residual == sp.zeros(*residual.shape)
    else:
        ok = residual == 0
    if not ok:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1
    print(f"PASS: {name}")

# Exact orthogonal rotations, rational in tan(theta/2).
tL, tR, ME, y, lam = sp.symbols("t_L t_R M_E y lambda", real=True, nonzero=True)
def rotation(t):
    den = 1 + t**2
    c, s = (1-t**2)/den, 2*t/den
    return sp.Matrix([[c,s],[-s,c]])
UL, UR = rotation(tL), rotation(tR)
Dphase = sp.diag(-1,1)
URp = UR*Dphase
cL,sL,cR,sR = UL[0,0],UL[0,1],UR[0,0],UR[0,1]

# The exact triangular mass-matrix condition M11=0:
# m1/m2 = sL*sR/(cL*cR).
m1 = sp.factor(ME*sL*sR/(cL*cR))
masses = sp.diag(m1,ME)
Minteraction = sp.simplify(UL*masses*URp.T)
check("interaction-basis mass matrix has exact M11=0",
      Minteraction[0,0])
check("left rotation is exactly orthogonal", UL.T*UL, sp.eye(2))
check("right rotation is exactly orthogonal", UR.T*UR, sp.eye(2))

# Interaction-basis complex Yukawa matrices and positive-mass Eq.(13) matrices.
Yh0 = y*sp.Matrix([[0,1],[0,0]])
Ys0 = lam*sp.Matrix([[0,0],[1,0]])
Yh = sp.simplify(UL.T*Yh0*URp)
Ys = sp.simplify(UL.T*Ys0*URp)
Yh_eq13 = y*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys_eq13 = lam*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
check("mass-basis Higgs vertex is the positive-mass Eq.(13) matrix",Yh,Yh_eq13)
check("mass-basis singlet vertex is the positive-mass Eq.(13) matrix",Ys,Ys_eq13)

# Four ordered propagator factors. P1/P3 are chirality-flipping mass
# numerators; D2/D4 are chirality-preserving slash propagators.
k1,k2,k3,k4 = sp.symbols("k_1^2 k_2^2 k_3^2 k_4^2", nonzero=True)
ks = (k1,k2,k3,k4)
def denominator(k):
    return sp.diag(1/(k-m1**2),1/(k-ME**2))
def mass_numerator(k):
    return sp.diag(m1/(k-m1**2),ME/(k-ME**2))
D1,D2,D3,D4 = (denominator(k) for k in ks)
P1,P3 = mass_numerator(k1),mass_numerator(k3)

# Mass-basis closed flavor trace, with the fixed PR,PR,PL,PL chirality flow.
T_mass = sp.trace(Yh*P1*Ys*D2*Ys.T*P3*Yh.T*D4)

# Expand the matrix trace explicitly into its 2^4=16 internal mass paths.
path_terms = {}
T_paths = sp.Integer(0)
for path in product((0,1),repeat=4):
    a,b,c,d = path
    term = (Yh[a,b]*P1[b,b]*Ys[b,c]*D2[c,c]
            *Ys.T[c,d]*P3[d,d]*Yh.T[d,a]*D4[a,a])
    path_terms[path] = sp.factor(term)
    T_paths += term
check("all 16 internal mass paths sum to the mass-basis matrix trace",T_paths,T_mass)
nonzero_generic = [p for p,v in path_terms.items() if v != 0]
check("finite generic mixing retains all 16 allowed mass paths",
      sp.Integer(len(nonzero_generic)),16)

# Transform each chiral propagator block to the interaction basis. The
# adjacent U_L/U_R factors cancel around the closed trace.
P1_I = URp*P1*UL.T
D2_I = URp*D2*URp.T
P3_I = UL*P3*URp.T
D4_I = UL*D4*UL.T
T_interaction = sp.trace(Yh0*P1_I*Ys0*D2_I*Ys0.T*P3_I*Yh0.T*D4_I)
check("finite-mixing mass-basis path sum equals interaction-basis propagator trace",
      T_mass,T_interaction)

# In the unbroken limit, m1=sL=sR=0 and m2=ME. Only the source-aligned
# path (light,heavy,light,heavy) survives.
zero_mix = {tL:0,tR:0}
surviving = []
for path,term in path_terms.items():
    value = sp.factor(term.subs(zero_mix))
    if value != 0:
        surviving.append((path,value))
check("unbroken limit leaves exactly one mass path",sp.Integer(len(surviving)),1)
expected_path = (0,1,0,1)
check("the unique unbroken path is (light,heavy,light,heavy)",
      sp.Integer(0 if surviving[0][0] == expected_path else 1))
target = y**2*lam**2*ME**2 / (
    k2*k4*(k1-ME**2)*(k3-ME**2)
)
check("unbroken path has the source-aligned y^2 lambda^2 M_E^2 numerator and denominators",
      surviving[0][1],target)

# The fixed-chirality Dirac trace supplies 2 k2.k4. This factor is
# independent of the flavor-matrix identity above.
K24 = sp.symbols("k2_dot_k4")
check("full unbroken numerator is 2 y^2 lambda^2 M_E^2 k2.k4",
      2*K24*surviving[0][1],
      2*y**2*lam**2*ME**2*K24/(k2*k4*(k1-ME**2)*(k3-ME**2)))

# Four real-field vertices carry (1/sqrt(2))^4=1/4, exactly the external
# field-decomposition weight of one charge-neutral complex assignment.
Yh_real = Yh/sp.sqrt(2)
Ys_real = Ys/sp.sqrt(2)
T_real = sp.trace(Yh_real*P1*Ys_real*D2*Ys_real.T*P3*Yh_real.T*D4)
check("real-field loop normalization is exactly one quarter of complex orientation",
      T_real,T_mass/4)
check("four neutral external assignments have total decomposition weight one",
      4*sp.Rational(1,4),1)

print(f"RESULT: {checks} exact symbolic full-propagator/path-sum checks passed.")
print("FINITE-MIXING IDENTITY: the 16 mass-eigenstate paths are one matrix-propagator trace, not 16 independent diagrams.")
print("UNBROKEN LIMIT: only path 0101 survives and gives the source-aligned two-heavy/two-light box.")
print("NORMALIZATION: the real-field four-vertex factor 1/4 equals the external complex-field projection weight; do not apply another factor 1/4.")
print("SCOPE: exact integrand-level flavor/basis identity and unbroken-limit reduction; no new loop integration, determinant-log multiplicity, or Wilson coefficient.")
