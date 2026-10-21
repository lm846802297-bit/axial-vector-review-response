#!/usr/bin/env python3
"""Numerical-exact audit of model-specific Yukawa orientation -> chiral trace weights.

Checks both hshs and hhss for all 16 internal mass paths. Uses rational mixing
parameters and explicit Minkowski 4x4 Dirac matrices. It compares the direct
Dirac trace with a projector-pattern decomposition built from the actual model
matrix elements, and separately reports H, C_ij, M. This is a numerator audit
only: no loop integration, Wick rotation, external-leg multiplicity or EFT subtraction.
Requires SymPy.
"""
from itertools import product, combinations
import sympy as sp

# Explicit gamma matrices for metric (+---)
zero = sp.zeros(2)
sigmas = [sp.Matrix([[0,1],[1,0]]), sp.Matrix([[0,-sp.I],[sp.I,0]]), sp.Matrix([[1,0],[0,-1]])]
gamma = [sp.diag(1,1,-1,-1)]
for s in sigmas:
    gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(zero,s), sp.Matrix.hstack(-s,zero)))
gamma5 = sp.I*gamma[0]*gamma[1]*gamma[2]*gamma[3]
PR=(sp.eye(4)+gamma5)/2
PL=(sp.eye(4)-gamma5)/2

def slash(k):
    return gamma[0]*k[0]-gamma[1]*k[1]-gamma[2]*k[2]-gamma[3]*k[3]
def dot(a,b):
    return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
def simp(x): return sp.simplify(sp.expand_complex(x))

# Rational parameters satisfy c^2+s^2=1 exactly.
a,b=sp.Integer(2),sp.Integer(3)
cL,sL=sp.Rational(3,5),sp.Rational(4,5)
cR,sR=sp.Rational(5,13),sp.Rational(12,13)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
mass={1:sp.Integer(2),2:sp.Integer(5)}
# Deterministic generic non-collinear Minkowski vectors
ks=[sp.Matrix(v) for v in [(2,1,-1,3),(1,-2,2,1),(3,0,1,-2),(-1,2,3,1)]]


def trace_direct(u,v,mu):
    verts=[u[i]*PR+v[i]*PL for i in range(4)]
    Ns=[slash(ks[i])+mu[i]*sp.eye(4) for i in range(4)]
    z=sp.eye(4)
    for i in range(4): z=z*verts[i]*Ns[i]
    return simp(sp.trace(z))

def decomposition(u,v,mu):
    # Each chirality assignment sigma_i selects u_i (R) or v_i (L).
    # A slash numerator is nonzero iff neighboring projector labels differ.
    H=u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3]
    M=sp.prod(mu)*(sp.prod(u)+sp.prod(v))
    C={ij:sp.Integer(0) for ij in combinations(range(4),2)}
    for sig in product((0,1), repeat=4):
        trans=tuple(i for i in range(4) if sig[i]!=sig[(i+1)%4])
        if len(trans)!=2: continue
        ij=tuple(trans)
        coup=sp.prod(u[i] if sig[i]==0 else v[i] for i in range(4))
        mp=sp.prod(mu[i] for i in range(4) if i not in ij)
        C[ij]+=coup*mp
    G=dot(ks[0],ks[1])*dot(ks[2],ks[3])-dot(ks[0],ks[2])*dot(ks[1],ks[3])+dot(ks[0],ks[3])*dot(ks[1],ks[2])
    # The parity-odd four-slash trace is retained here rather than silently
    # discarded. E = epsilon_{mu nu rho sigma} k1^mu k2^nu k3^rho k4^sigma
    # represented by the determinant of the four contravariant vectors.
    E=sp.det(sp.Matrix.hstack(*ks))
    Hodd=u[0]*v[1]*u[2]*v[3]-v[0]*u[1]*v[2]*u[3]
    pred=2*H*G+2*sum(C[ij]*dot(ks[ij[0]],ks[ij[1]]) for ij in C)+2*M+2*sp.I*E*Hodd
    return simp(pred), H, C, M, simp(E*Hodd)

counts={"hshs":0,"hhss":0}
maxdiff=sp.Integer(0)
for name,seq in [("hshs",(Yh,Ys,Yh,Ys)),("hhss",(Yh,Yh,Ys,Ys))]:
    for path in product((1,2), repeat=4):
        # Vertices connect path[r] -> path[r+1]; close cycle.
        nxt=path[1:]+path[:1]
        u=[seq[r][path[r]-1,nxt[r]-1] for r in range(4)]
        # Real Yukawas: reverse matrix element is the coefficient of P_L.
        v=[seq[r][nxt[r]-1,path[r]-1] for r in range(4)]
        # Edge masses follow the established convention (m_b,m_c,m_d,m_a).
        mu=[mass[nxt[0]],mass[nxt[1]],mass[nxt[2]],mass[nxt[3]]]
        direct=trace_direct(u,v,mu)
        pred,H,C,M,odd=decomposition(u,v,mu)
        diff=simp(direct-pred)
        if diff!=0:
            raise AssertionError(f"{name} path={path}: direct={direct}, predicted={pred}, diff={diff}")
        counts[name]+=1
# Exact symbolic aggregate check: the parity-odd Hodd coupling weight cancels
# over all 16 internal mass paths for each fixed scalar-vertex ordering.
cL_s,sL_s,cR_s,sR_s,a_s,b_s=sp.symbols('cL sL cR sR a b')
Yh_s=a_s*sp.Matrix([[cL_s*sR_s,cL_s*cR_s],[sL_s*sR_s,sL_s*cR_s]])
Ys_s=b_s*sp.Matrix([[sL_s*cR_s,-sL_s*sR_s],[-cL_s*cR_s,cL_s*sR_s]])
for name,seq in [("hshs",(Yh_s,Ys_s,Yh_s,Ys_s)),("hhss",(Yh_s,Yh_s,Ys_s,Ys_s))]:
    odd_sum=sp.Integer(0)
    H_sum=sp.Integer(0)
    for path in product((1,2), repeat=4):
        nxt=path[1:]+path[:1]
        u=[seq[r][path[r]-1,nxt[r]-1] for r in range(4)]
        v=[seq[r][nxt[r]-1,path[r]-1] for r in range(4)]
        p1=u[0]*v[1]*u[2]*v[3]
        p2=v[0]*u[1]*v[2]*u[3]
        odd_sum += p1-p2
        H_sum += p1+p2
    assert sp.factor(odd_sum)==0, (name, odd_sum)
    assert sp.factor(H_sum)==0, (name, H_sum)
    print(f"PASS: symbolic sum over 16 paths gives sum(H_odd)=sum(H)=0 for {name}")

print("PASS: direct explicit Dirac trace equals the full projector decomposition, including the parity-odd epsilon term")
print(f"PASS: hshs paths checked = {counts['hshs']}")
print(f"PASS: hhss paths checked = {counts['hhss']}")
print("Convention: V_ij = Y_ij P_R + Y_ji P_L for real Yukawas; edge masses=(m_b,m_c,m_d,m_a).")
print("BOUNDARY: this validates the chosen vertex/path convention at the numerator level only; epsilon cancellation in the full labeled amplitude, Wick signs, graph multiplicities and EFT subtraction remain open.")
