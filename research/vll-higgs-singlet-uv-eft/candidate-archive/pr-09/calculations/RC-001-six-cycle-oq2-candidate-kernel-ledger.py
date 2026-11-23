#!/usr/bin/env python3
"""RC-001 symbolic O(p^2) candidate-kernel ledger for six labeled cycles.

The generic Dirac trace identity is derived with explicit (+---) 4x4 matrices
and symbolic u_i,v_i,m_i,k_i. Model-specific Yukawa matrices are then inserted
for every one of 6 labeled cycles x 16 internal-state paths. For each path the
script constructs its route in a common p-invariant basis, derives f_ij,g,d,
Delta_0 and the conditional Wick-kernel coefficients B1/B2/B3, and checks the
three reverse-cycle pairings after the exact Feynman-simplex constraint.

This is an O(p^2) candidate-integrand ledger, not a complete UV-EFT match.
The B-kernel formulas are conditional on the stated Minkowski/Wick convention;
the script does not integrate the 4-parameter simplex, establish the complete
diagrammatic common i/sign, or close all EFT soft graphs and counterterms.
Requires Python 3 and SymPy.
"""
from itertools import permutations, product, combinations
from pathlib import Path
import csv, hashlib, time
import sympy as sp

# ---------- A. Independent generic trace identity, symbolic in all inputs ----------
zero = sp.zeros(2)
sigmas = [
    sp.Matrix([[0,1],[1,0]]),
    sp.Matrix([[0,-1],[1,0]])*sp.I,
    sp.Matrix([[1,0],[0,-1]]),
]
gamma = [sp.diag(1,1,-1,-1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(zero,sigma),sp.Matrix.hstack(-sigma,zero)))
gamma5 = sp.I*gamma[0]*gamma[1]*gamma[2]*gamma[3]
PR = (sp.eye(4)+gamma5)/2
PL = (sp.eye(4)-gamma5)/2
u = sp.symbols("u1:5")
v = sp.symbols("v1:5")
m = sp.symbols("m1:5")
k = [[sp.symbols(f"k{i}{mu}") for mu in range(4)] for i in range(1,5)]

def slash(vec):
    return gamma[0]*vec[0]-gamma[1]*vec[1]-gamma[2]*vec[2]-gamma[3]*vec[3]
def dot4(a,b):
    return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
def simp(z):
    # Keep exact expanded polynomials; avoid costly repeated factorization across 576 rows.
    return sp.expand(z)

vertices = [u[i]*PR+v[i]*PL for i in range(4)]
Ns = [slash(k[i])+m[i]*sp.eye(4) for i in range(4)]
raw = sp.eye(4)
for i in range(4):
    raw = raw*vertices[i]*Ns[i]
raw_trace = sp.expand(sp.trace(raw))
Hgen = u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3]
Hoddgen = u[0]*v[1]*u[2]*v[3]-v[0]*u[1]*v[2]*u[3]
Mgen = sp.prod(m)*(sp.prod(u)+sp.prod(v))
Cgen = {ij:sp.Integer(0) for ij in combinations(range(4),2)}
for chirality in product((0,1),repeat=4):
    trans=tuple(i for i in range(4) if chirality[i]!=chirality[(i+1)%4])
    if len(trans)!=2:
        continue
    ij=trans
    coup=sp.prod(u[i] if chirality[i]==0 else v[i] for i in range(4))
    Cgen[ij] += coup*sp.prod(m[i] for i in range(4) if i not in ij)
Ggen=(dot4(k[0],k[1])*dot4(k[2],k[3])
      -dot4(k[0],k[2])*dot4(k[1],k[3])
      +dot4(k[0],k[3])*dot4(k[1],k[2]))
Egen=sp.det(sp.Matrix.hstack(*[sp.Matrix(ki) for ki in k]))
decomp = sp.expand(2*Hgen*Ggen
    +2*sum(Cgen[ij]*dot4(k[ij[0]],k[ij[1]]) for ij in Cgen)
    +2*Mgen+2*sp.I*Egen*Hoddgen)
assert sp.simplify(raw_trace-decomp)==0
print("PASS: generic Dirac trace identity verified symbolically for arbitrary u_i,v_i,m_i,k_i.")

# ---------- B. Model-specific path weights and routed O(p^2) geometry ----------
cL,sL,cR,sR,a,b,m1,m2 = sp.symbols("c_L s_L c_R s_R a b m_1 m_2", nonzero=True)
x1,x2,x3,x4 = sp.symbols("x_1 x_2 x_3 x_4")
xs=(x1,x2,x3,x4)
Q=sp.symbols("Q1:7")
Q1,Q2,Q3,Q4,Q5,Q6=Q
Gp=sp.Matrix([[Q1,Q4,Q5],[Q4,Q2,Q6],[Q5,Q6,Q3]])
pvec={1:sp.Matrix([[1,0,0]]),2:sp.Matrix([[0,1,0]]),3:sp.Matrix([[0,0,1]]),4:sp.Matrix([[-1,-1,-1]])}
label_num={"h1":1,"h2":2,"s1":3,"s2":4}
labels=("h1","h2","s1","s2")
type_of={"h1":"h","h2":"h","s1":"s","s2":"s"}
cycles=[("h1",)+tail for tail in permutations(("h2","s1","s2"))]
paths=list(product((0,1),repeat=4))
Ckeys=list(combinations(range(4),2))
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])

def dotc(u,v):
    return sp.expand((u*Gp*v.T)[0])
def coeffs(expr):
    P=sp.Poly(sp.expand(expr),*Q)
    return tuple(sp.factor(P.coeff_monomial(q)) for q in Q)
def g_from_f(ff):
    # Four-dimensional angular average after the finite O(p^2) coefficients are formed.
    return tuple(sp.factor(ff[(0,1)][k]+ff[(2,3)][k]-ff[(0,2)][k]-ff[(1,3)][k]
        +ff[(0,3)][k]+ff[(1,2)][k]+sp.Rational(1,2)*(ff[(0,2)][k]+ff[(1,3)][k]))
        for k in range(6))
def weights(cycle,path):
    seq=tuple(Yh if type_of[label]=="h" else Ys for label in cycle)
    nxt=path[1:]+path[:1]
    uu=[seq[i][path[i],nxt[i]] for i in range(4)]
    vv=[seq[i][nxt[i],path[i]] for i in range(4)]
    mus=tuple(m1 if nxt[i]==0 else m2 for i in range(4))
    H=simp(uu[0]*vv[1]*uu[2]*vv[3]+vv[0]*uu[1]*vv[2]*uu[3])
    Hodd=simp(uu[0]*vv[1]*uu[2]*vv[3]-vv[0]*uu[1]*vv[2]*uu[3])
    M=simp(sp.prod(mus)*(sp.prod(uu)+sp.prod(vv)))
    C={ij:sp.Integer(0) for ij in Ckeys}
    for chirality in product((0,1),repeat=4):
        trans=tuple(i for i in range(4) if chirality[i]!=chirality[(i+1)%4])
        if len(trans)!=2: continue
        ij=trans
        coup=sp.prod(uu[i] if chirality[i]==0 else vv[i] for i in range(4))
        C[ij]+=coup*sp.prod(mus[i] for i in range(4) if i not in ij)
    C={ij:simp(value) for ij,value in C.items()}
    return H,Hodd,M,C,mus

# Build all six route geometries directly in the common p-basis.
geometry={}
for cycle in cycles:
    qvs=[pvec[label_num[label]] for label in cycle[:3]]
    r=[sp.zeros(1,3),-qvs[1],-qvs[1]-qvs[2],qvs[0]]
    R=sum((xs[i]*r[i] for i in range(4)),sp.zeros(1,3))
    t=[ri-R for ri in r]
    ff={ij:coeffs(dotc(t[ij[0]],t[ij[1]])) for ij in Ckeys}
    gg=g_from_f(ff)
    dd=coeffs(sp.expand(sum(xs[i]*dotc(r[i],r[i]) for i in range(4))-dotc(R,R)))
    T=sp.Matrix([coeffs(expr) for expr in [
        dotc(qvs[0],qvs[0]),dotc(qvs[1],qvs[1]),dotc(qvs[2],qvs[2]),
        dotc(qvs[0],qvs[1]),dotc(qvs[0],qvs[2]),dotc(qvs[1],qvs[2])
    ]])
    assert sp.simplify(T.det()) in (1,-1)
    geometry[cycle]=(ff,gg,dd)

# Construct every path-specific O(p^2) kernel row, retaining Delta0.
rows=[]
W={}
for cycle in cycles:
    ff,gg,dd=geometry[cycle]
    for path in paths:
        H,Hodd,M,C,mus=weights(cycle,path)
        S=simp(sum(C.values()))
        Delta0=sp.expand(sum(xs[i]*mus[i]**2 for i in range(4)))
        W[(cycle,path)]={"H":H,"Hodd":Hodd,"M":M,"C":C,"S":S,"mus":mus,"Delta0":Delta0}
        for alpha in range(6):
            F=simp(sum(C[ij]*ff[ij][alpha] for ij in Ckeys))
            B1=simp(H*(-sp.Rational(2,3)*gg[alpha]+2*dd[alpha]))
            B2=simp(sp.Rational(1,3)*F-sp.Rational(2,3)*S*dd[alpha])
            B3=simp(sp.Rational(2,3)*M*dd[alpha])
            row={"cycle":"-".join(cycle),"path":"".join(str(z+1) for z in path),
                 "alpha":alpha+1,"invariant":str(Q[alpha]),
                 "edge_masses":"/".join("m1" if z==m1 else "m2" for z in mus),
                 "Delta0":str(Delta0),"H":str(H),"S":str(S),"M":str(M),
                 "F_alpha":str(F),"g_alpha":str(gg[alpha]),"d_alpha":str(dd[alpha]),
                 "B1":str(B1),"B2":str(B2),"B3":str(B3)}
            for ij in Ckeys: row[f"C{ij[0]+1}{ij[1]+1}"]=str(C[ij])
            rows.append(row)

# Reverse-cycle path/parameter/invariant coefficient equality.
reverse_checks=0
reverse_pairs=[]
xreverse={xs[i]:xs[3-i] for i in range(4)}
simplex_sub={x4:1-x1-x2-x3}
fields=("Delta0","B1","B2","B3")
coeff_data={}
for row in rows:
    cyc=tuple(row["cycle"].split("-"))
    path=tuple(int(z)-1 for z in row["path"])
    alpha=row["alpha"]-1
    coeff_data.setdefault((cyc,path),{})[alpha]={key:sp.sympify(row[key]) for key in fields}
for cycle in cycles:
    rev=(cycle[0],cycle[3],cycle[2],cycle[1])
    if cycles.index(cycle)>cycles.index(rev): continue
    reverse_pairs.append((cycle,rev))
    for path in paths:
        rpath=(path[1],path[0],path[3],path[2])
        for alpha in range(6):
            left=coeff_data[(cycle,path)][alpha]
            right=coeff_data[(rev,rpath)][alpha]
            for field in fields:
                diff=sp.expand(left[field].xreplace(xreverse).subs(simplex_sub)-right[field].subs(simplex_sub))
                if diff != 0:
                    raise AssertionError(f"reverse kernel mismatch {cycle=} {path=} {rpath=} {alpha=} {field=}: {diff}")
                reverse_checks+=1

out=Path("./rc001_six_cycle_oq2_candidate_kernel_ledger.csv")
with out.open("w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
sha=hashlib.sha256(out.read_bytes()).hexdigest()
print(f"PASS: built {len(rows)} O(p^2) candidate-kernel coefficient rows = 6 cycles x 16 paths x 6 invariants.")
print("PASS: all six cycle geometries have invertible exact invariant-basis transforms.")
print(f"PASS: reverse-cycle coefficient audit {reverse_checks}/{reverse_checks} = 3 pairs x 16 paths x 6 invariants x 4 objects.")
print("PASS: each row retains path-specific Delta0, all C_ij, H, S, M, F_alpha, g_alpha, d_alpha, and B1/B2/B3.")
print("CONVENTION: B1/B2/B3 use the corrected candidate Wick formulas; this checks the complete path/cycle bookkeeping under that convention, not the physical global loop sign.")
print("LIMIT: no path-dependent simplex integrations, no FeynArts/FeynCalc run, and no complete EFT soft/counterterm subtraction.")
print(f"CSV: {out} ({out.stat().st_size} bytes)")
print(f"SHA256: {sha}")
