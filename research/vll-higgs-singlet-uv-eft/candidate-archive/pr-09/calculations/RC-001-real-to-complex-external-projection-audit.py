#!/usr/bin/env python3
"""Combinatoric audit of the real h,h,s,s to complex H,H†,S,S† projection.

Uses h=(H+H†)/sqrt(2) and s=(S+S†)/sqrt(2) for labeled external legs
h1,h2,s1,s2. Charge-neutral assignments have one H and one H†, and one S and
one S†. This script records the 1/4 field-decomposition weight per assignment
and pairs the six labeled real-field cycles under reversal. It does not assign
loop integrals or decide which oriented UV diagrams vanish.
Requires Python 3.
"""
from itertools import product, permutations
from pathlib import Path
import csv, hashlib

hlegs=("h1","h2")
slegs=("s1","s2")
choices={leg:("H","Hdag") for leg in hlegs}
choices.update({leg:("S","Sdag") for leg in slegs})
assignments=[]
for bits in product((0,1),repeat=4):
    mapping={leg:choices[leg][bits[i]] for i,leg in enumerate((*hlegs,*slegs))}
    if mapping["h1"]==mapping["h2"]: continue
    if mapping["s1"]==mapping["s2"]: continue
    assignments.append(mapping)
assert len(assignments)==4
weight=1/4
assert abs(sum(weight for _ in assignments)-1.0)<1e-15

cycles=[("h1",)+tail for tail in permutations(("h2","s1","s2"))]
assert len(cycles)==6
reverse_pairs=[]
for cycle in cycles:
    reverse=(cycle[0],cycle[3],cycle[2],cycle[1])
    if cycles.index(cycle)<cycles.index(reverse):
        reverse_pairs.append((cycle,reverse))
assert len(reverse_pairs)==3
pair_id={}
for idx,(forward,reverse) in enumerate(reverse_pairs,1):
    pair_id[forward]=idx
    pair_id[reverse]=idx

rows=[]
for ai,mapping in enumerate(assignments,1):
    orientation=";".join(f"{leg}:{mapping[leg]}" for leg in (*hlegs,*slegs))
    for cycle in cycles:
        reverse=(cycle[0],cycle[3],cycle[2],cycle[1])
        rows.append({
            "assignment_id":ai,
            "orientation_assignment":orientation,
            "field_decomposition_weight":weight,
            "cycle":"-".join(cycle),
            "reverse_cycle":"-".join(reverse),
            "reverse_pair_id":pair_id[cycle],
            "status":"combinatoric map only; momentum routing and amplitude projection open",
        })
assert len(rows)==24
assert all(sum(r["cycle"]=="-".join(c) for r in rows)==4 for c in cycles)
assert all(sum(r["assignment_id"]==a for r in rows)==6 for a in range(1,5))
assert all(abs(r["field_decomposition_weight"]-0.25)<1e-15 for r in rows)
assert {r["reverse_pair_id"] for r in rows}=={1,2,3}

out=Path("./rc001_real_to_complex_external_projection.csv")
with out.open("w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    writer.writeheader(); writer.writerows(rows)
digest=hashlib.sha256(out.read_bytes()).hexdigest()
print("PASS: 16 raw real-to-complex field assignments reduce to 4 charge-neutral assignments.")
print("PASS: each allowed assignment carries weight (1/sqrt(2))^4=1/4; total field-decomposition weight is 1.")
print("PASS: 6 labeled cycles = 4!/4, with 3 reverse pairs already included.")
print("PASS: projection ledger contains 24 assignment-cycle rows = 4 orientations x 6 cycles.")
print("LIMIT: this does not assign momentum invariants, evaluate diagrams, or determine which interaction-basis orientation/cycle terms vanish.")
print(f"CSV: {out} ({out.stat().st_size} bytes)")
print(f"SHA256: {digest}")
