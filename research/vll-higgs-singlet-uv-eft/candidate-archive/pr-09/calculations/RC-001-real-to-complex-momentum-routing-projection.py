#!/usr/bin/env python3
"""Project the source-aligned complex hard amplitudes onto labeled h1 h2 s1 s2.

Uses h=(H+H†)/sqrt(2), s=(S+S†)/sqrt(2), all external momenta incoming,
and the source §248 local amplitudes: mu channel (L_mu-2)*s_mu+t/6 and tau
channel (L_tau-2)*u_tau+t/6. It enumerates the four charge-neutral complex
assignments and maps their pair invariants to s_R, u_R, t_R using momentum
conservation. This is an external-state projection, not a calculation of the
mass-basis six-cycle UV loop.
Requires Python 3 + SymPy.
"""
from itertools import product
import sympy as sp

checks=[]
def check(name,expr,expected=0):
    residual=sp.simplify(sp.expand(expr-expected))
    if residual!=0: raise AssertionError(f"{name}: residual={residual}")
    checks.append(name); print(f"PASS: {name}")

legs=("h1","h2","s1","s2")
choices={"h1":("H","Hdag"),"h2":("H","Hdag"),"s1":("S","Sdag"),"s2":("S","Sdag")}
assignments=[]
for bits in product((0,1),repeat=4):
    m={leg:choices[leg][bits[i]] for i,leg in enumerate(legs)}
    if m["h1"]==m["h2"] or m["s1"]==m["s2"]: continue
    assignments.append(m)
assert len(assignments)==4

sR,uR,tR,Lmu,Ltau=sp.symbols("s_R u_R t_R L_mu L_tau", real=True)
# All momenta are incoming, p_h1+p_h2+p_s1+p_s2=0.
# Define s_R=(p_h1+p_s1)^2, u_R=(p_h1+p_s2)^2, t_R=(p_h1+p_h2)^2.
# The other pair invariants follow from momentum conservation.
def pair_invariant(leg_a,leg_b):
    pair=frozenset((leg_a,leg_b))
    if pair==frozenset(("h1","s1")) or pair==frozenset(("h2","s2")): return sR
    if pair==frozenset(("h1","s2")) or pair==frozenset(("h2","s1")): return uR
    if pair==frozenset(("h1","h2")) or pair==frozenset(("s1","s2")): return tR
    raise AssertionError(f"unexpected pair {pair}")

rows=[]; mu_s=[]; tau_u=[]
for idx,m in enumerate(assignments,1):
    h_leg=next(leg for leg in ("h1","h2") if m[leg]=="H")
    hbar_leg=next(leg for leg in ("h1","h2") if m[leg]=="Hdag")
    s_leg=next(leg for leg in ("s1","s2") if m[leg]=="S")
    sbar_leg=next(leg for leg in ("s1","s2") if m[leg]=="Sdag")
    smu=pair_invariant(h_leg,s_leg)
    utau=pair_invariant(h_leg,sbar_leg)
    t=pair_invariant(h_leg,hbar_leg)
    mu_s.append(smu); tau_u.append(utau)
    rows.append((idx,";".join(f"{leg}:{m[leg]}" for leg in legs),smu,utau,t,sp.Rational(1,4)))

check("four charge-neutral assignments each carry weight 1/4",sum(r[5] for r in rows),1)
check("mu-channel routing maps to s_R twice",sum(1 for x in mu_s if x==sR),2)
check("mu-channel routing maps to u_R twice",sum(1 for x in mu_s if x==uR),2)
check("tau-channel routing maps to s_R twice",sum(1 for x in tau_u if x==sR),2)
check("tau-channel routing maps to u_R twice",sum(1 for x in tau_u if x==uR),2)
check("every orientation preserves the h-h / s-s invariant t_R",sum(1 for r in rows if r[4]==tR),4)

# For each assignment, the mu local polynomial uses s_mu; tau uses u_tau.
mu_projected=sp.simplify(sum(r[5]*((Lmu-2)*r[2]+r[4]/6) for r in rows))
tau_projected=sp.simplify(sum(r[5]*((Ltau-2)*r[3]+r[4]/6) for r in rows))
check("projected mu local polynomial",mu_projected,(Lmu-2)*(sR+uR)/2+tR/6)
check("projected tau local polynomial",tau_projected,(Ltau-2)*(sR+uR)/2+tR/6)

print("PROJECTED LOCAL AMPLITUDE (common i/(16 pi^2) factored out):")
print("  |C5_mu|^2 * [(L_mu-2)(s_R+u_R)/2 + t_R/6]")
print("+ |C5_tau|^2 * [(L_tau-2)(s_R+u_R)/2 + t_R/6]")
print(f"RESULT: {len(checks)} exact symbolic projection checks passed.")
print("LIMIT: uses the source-aligned complex local amplitudes as inputs; does not evaluate or validate the mass-basis six-cycle UV loop or global graph factors.")
print("ASSIGNMENTS:")
for idx,orientation,smu,utau,t,w in rows:
    print(f"  {idx}: {orientation} | mu s-channel={smu}, tau u-channel={utau}, t={t}, weight={w}")
