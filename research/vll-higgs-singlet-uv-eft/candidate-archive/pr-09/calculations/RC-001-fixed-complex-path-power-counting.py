#!/usr/bin/env python3
"""Small-mixing power-counting audit of the fixed complex RC-001 paths.

Uses the positive-light-mass mass-basis matrices for the fixed complex
orientations H,S,Sdag,Hdag (mu) and H,Sdag,S,Hdag (tau). For each of the 16
internal paths it counts powers of s_L and s_R in the four-vertex product and
in the two mass numerators selected by the P_R,P_R,P_L,P_L trace.

The triangular mass-matrix condition M_11=0 gives
m_1/m_2 = s_L*s_R/(c_L*c_R). Each light mass numerator therefore adds one
power of both mixing sines. This is numerator-level power counting only; it
does not replace the d=4-2epsilon hard/soft expansion or establish a Wilson
coefficient.
Requires Python 3 and SymPy.
"""
from itertools import product
import sympy as sp

cL,sL,cR,sR,y,lam,m1,m2=sp.symbols(
    "c_L s_L c_R s_R y lambda m_1 m_2", nonzero=True, real=True
)
Yh=y*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=lam*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
fixed_complex_sequences={
    "mu":("H","S","Sdag","Hdag"),
    "tau":("H","Sdag","S","Hdag"),
}
# In the positive-mass convention both fixed orientations have this ordered
# matrix sequence; the S/Sdag labels, not the matrix algebra, are interchanged.
matrix_sequence=(Yh,Ys,Ys.T,Yh.T)
zero_mix={cL:1,sL:0,cR:1,sR:0}
rows=[]
for flavor,labels in fixed_complex_sequences.items():
    leading=[]
    for path in product((0,1),repeat=4):
        nxt=path[1:]+path[:1]
        coupling=sp.factor(sp.prod(
            matrix_sequence[i][path[i],nxt[i]] for i in range(4)
        ))
        poly=sp.Poly(sp.expand(coupling),sL,sR)
        if len(poly.terms()) != 1:
            raise AssertionError(f"non-monomial coupling product {flavor}/{path}: {coupling}")
        (raw_sL,raw_sR),coefficient=poly.terms()[0]
        light_mass_numerators=sum(1 for i in (0,2) if nxt[i]==0)
        effective=(raw_sL+light_mass_numerators,raw_sR+light_mass_numerators)
        mass_factor=(m1 if nxt[0]==0 else m2)*(m1 if nxt[2]==0 else m2)
        C13=sp.factor(coupling*mass_factor)
        if effective==(0,0):
            leading.append(path)
        rows.append({
            "flavor":flavor,
            "cycle":"-".join(labels),
            "path":"".join(str(x+1) for x in path),
            "raw_sL_power":raw_sL,
            "raw_sR_power":raw_sR,
            "light_mass_numerators":light_mass_numerators,
            "effective_sL_power_after_M11":effective[0],
            "effective_sR_power_after_M11":effective[1],
            "coupling_product":str(coupling),
            "C13_mass_weight":str(C13),
            "total_effective_mixing_degree":sum(effective),
        })
    if leading != [(0,1,0,1)]:
        raise AssertionError(f"{flavor}: expected unique degree-zero path 0101, got {leading}")
    print(f"PASS: {flavor} has a unique degree-zero path 0101.")

# Check the exact coefficient of the leading path and its zero-mixing limit.
leading_path=(0,1,0,1)
leading_next=leading_path[1:]+leading_path[:1]
cp_leading=sp.factor(sp.prod(
    matrix_sequence[i][leading_path[i],leading_next[i]] for i in range(4)
))
check_expr=sp.simplify(cp_leading-y**2*lam**2*cL**4*cR**4)
if check_expr!=0:
    raise AssertionError(f"leading coupling product mismatch: {check_expr}")
if sp.simplify(cp_leading.subs(zero_mix)-y**2*lam**2)!=0:
    raise AssertionError("leading coupling product does not reduce to y^2 lambda^2")
if sp.simplify((cp_leading*m2**2).subs(zero_mix)-y**2*lam**2*m2**2)!=0:
    raise AssertionError("leading C13 mass weight does not reduce to y^2 lambda^2 M_E^2")

nonleading=[r for r in rows if r["path"]!="1212"]
if len(rows)!=32 or len(nonleading)!=30:
    raise AssertionError(f"expected 32 flavor/path rows, got {len(rows)}")
min_degree=min(r["total_effective_mixing_degree"] for r in nonleading)
if min_degree<2:
    raise AssertionError(f"non-leading path is not mixing-suppressed: degree {min_degree}")

print("PASS: leading C13 weight is y^2 lambda^2 c_L^4 c_R^4 m_2^2.")
print("PASS: all 30 non-leading flavor/path rows have at least quadratic mixing suppression after M11=0.")
print(f"MIN_NONLEADING_MIXING_DEGREE: {min_degree}")
print("PATH TABLE:")
for row in rows:
    print(f"{row['flavor']:>3} path={row['path']} raw=({row['raw_sL_power']},{row['raw_sR_power']}) "
          f"n_light_mass={row['light_mass_numerators']} effective="
          f"({row['effective_sL_power_after_M11']},{row['effective_sR_power_after_M11']})")
print("LIMIT: this is numerator-level power counting. The method-of-regions expansion must still show how the finite-mass d=4 integrals split into hard and EFT-soft parts before any coefficient is promoted.")
