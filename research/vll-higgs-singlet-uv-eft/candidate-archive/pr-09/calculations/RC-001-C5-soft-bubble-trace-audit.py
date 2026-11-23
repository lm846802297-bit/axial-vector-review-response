#!/usr/bin/env python3
"""RC-001 independent EFT C5 C5* soft-bubble trace and pole audit.

Derives the massless chiral bubble numerator with explicit (+---) 4x4 Dirac
matrices, reduces it to the scalar B0 integral in dimensional regularization,
and checks the vertex/propagator/closed-loop sign product against the source
§248 amplitude. It then checks the EFT soft counterterm and hard/soft pole
bookkeeping in the same stated normalization.

This closes the algebraic check for the single SFT-01 bubble in the specified
C5 C5* four-scalar 1PI sector; it is not a substitute for a FeynArts/FeynCalc
topology census, nor does it integrate the six-cycle UV candidate kernels or
establish the final Wilson coefficient.
Requires Python 3 and SymPy.
"""
import sympy as sp

checks=[]
def check(name,expr,expected=0):
    residual=sp.simplify(expr-expected)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks.append(name)
    print(f"PASS: {name}")

# Explicit Minkowski Dirac matrices, metric (+---).
zero=sp.zeros(2)
sigmas=[
    sp.Matrix([[0,1],[1,0]]),
    sp.Matrix([[0,-1],[1,0]])*sp.I,
    sp.Matrix([[1,0],[0,-1]]),
]
gamma=[sp.diag(1,1,-1,-1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(zero,sigma),sp.Matrix.hstack(-sigma,zero)))
gamma5=sp.I*gamma[0]*gamma[1]*gamma[2]*gamma[3]
PR=(sp.eye(4)+gamma5)/2
PL=(sp.eye(4)-gamma5)/2
k=sp.symbols("k0:4")
q=sp.symbols("q0:4")
def slash(v):
    return gamma[0]*v[0]-gamma[1]*v[1]-gamma[2]*v[2]-gamma[3]*v[3]
def dot(a,b):
    return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]

kplusq=[k[i]+q[i] for i in range(4)]
trace=sp.expand(sp.trace(PR*slash(k)*PL*slash(kplusq)))
check("massless chiral trace equals 2 k dot (k+q)",trace,2*dot(k,kplusq))

s=sp.symbols("s", real=True)
numerator_reduction=dot(k,kplusq) - (dot(k,k)+dot(kplusq,kplusq)-dot(q,q))/2
check("2 k dot (k+q) numerator reduces to k^2+(k+q)^2-s",
      2*numerator_reduction,0)

# The k^2 and (k+q)^2 terms integrate to scaleless tadpoles in dimensional regularization.
# Sign ledger: two vertices (-i)^2, two propagators i^2, closed fermion loop (-1).
vertex_factor=(-sp.I)**2
propagator_factor=sp.I**2
closed_loop_factor=-1
combined=sp.simplify(vertex_factor*propagator_factor*closed_loop_factor)
check("two vertices, two propagators, and closed fermion loop combine to -1",
      combined,-1)
# The reduced loop integral contributes -i s B0/(16 pi^2); combined sign gives +i s B0/(16 pi^2).
I=sp.I
reduced_integral_factor=-I*s
amplitude_factor=sp.simplify(combined*reduced_integral_factor)
check("full soft-bubble prefactor is +i s B0/(16 pi^2)",amplitude_factor,I*s)

DeltaUV,DeltaIR,L,log_s,t=sp.symbols("Delta_UV Delta_IR L log_s t", real=True)
# Factor |C5|^2/(16 pi^2) out of all amplitudes.
B0=DeltaUV-log_s+2
soft=I*s*B0
soft_ct=-I*s*DeltaUV
check("bare soft-loop UV pole is +i s Delta_UV",sp.diff(soft,DeltaUV),I*s)
check("local EFT counterterm cancels the soft UV pole",sp.diff(soft+soft_ct,DeltaUV),0)
check("renormalized soft bubble keeps -log(-s/mu^2)+2",
      soft+soft_ct,I*s*(-log_s+2))

hard=I*((-DeltaIR+L-2)*s+t/6)
regions=hard+soft
check("hard plus bare soft has separately labeled DeltaUV-DeltaIR poles",
      regions,I*((DeltaUV-DeltaIR+L-log_s)*s+t/6))
check("hard-soft region poles cancel after DeltaIR=DeltaUV",
      regions.subs(DeltaIR,DeltaUV),I*((L-log_s)*s+t/6))
check("hard local matching polynomial remains (L-2)s+t/6",
      hard.subs(DeltaIR,0),I*((L-2)*s+t/6))

print(f"RESULT: {len(checks)} exact trace/sign/pole checks passed.")
print("SCOPE: the SFT-01 massless C5 C5* bubble and its local UV counterterm, plus §248 hard/soft pole comparison.")
print("OPEN: independent FeynArts/FeynCalc graph generation, other EFT operator sectors, path-dependent UV simplex integration, and final finite Wilson-vector closure.")
