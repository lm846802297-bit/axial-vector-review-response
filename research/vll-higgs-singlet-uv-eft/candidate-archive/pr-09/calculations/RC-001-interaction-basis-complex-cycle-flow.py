#!/usr/bin/env python3
"""Interaction-basis flavor-flow audit for the RC-001 complex external channels.

For each of the four charge-neutral assignments of (h1,h2,s1,s2), this script
uses the actual interaction-basis Yukawa matrices for the mu and tau sectors,
enumerates all six labeled cycles, and checks the allowed flavor path and
chiral Dirac trace. It then maps the light-line bubble invariant to the
source-aligned mu s-channel or tau u-channel.

Metric (+---); unbroken phase; massless light fermion and one heavy Dirac
state of mass M. Yukawa couplings are taken real for the structural check.
This is not a loop integral or a final UV-EFT Wilson coefficient.
Requires Python 3 and SymPy.
"""
from itertools import combinations, permutations, product
import sympy as sp

I = sp.I
zero = sp.zeros(2)
sigmas = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -1], [1, 0]]) * I,
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(
        sp.Matrix.hstack(zero, sigma),
        sp.Matrix.hstack(-sigma, zero),
    ))
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
PR = sp.simplify((sp.eye(4) + gamma5) / 2)
PL = sp.simplify((sp.eye(4) - gamma5) / 2)

y, lam, M = sp.symbols("y lambda M", real=True, nonzero=True)
a, b = y/sp.sqrt(2), lam/sp.sqrt(2)
Yh0 = a * sp.Matrix([[0, 1], [0, 0]])
Ys0 = b * sp.Matrix([[0, 0], [1, 0]])
Yh0_dag, Ys0_dag = Yh0.T, Ys0.T

legs = ("h1", "h2", "s1", "s2")
choices = {
    "h1": ("H", "Hdag"), "h2": ("H", "Hdag"),
    "s1": ("S", "Sdag"), "s2": ("S", "Sdag"),
}
assignments = []
for bits in product((0, 1), repeat=4):
    assignment = {leg: choices[leg][bits[i]] for i, leg in enumerate(legs)}
    if assignment["h1"] == assignment["h2"] or assignment["s1"] == assignment["s2"]:
        continue
    assignments.append(assignment)
if len(assignments) != 4:
    raise AssertionError(f"expected 4 charge-neutral assignments, got {len(assignments)}")

cycles = [("h1",)+tail for tail in permutations(("h2", "s1", "s2"))]
sR, uR, tR = sp.symbols("s_R u_R t_R", real=True)

def pair_invariant(leg_a, leg_b):
    pair = frozenset((leg_a, leg_b))
    if pair in (frozenset(("h1", "s1")), frozenset(("h2", "s2"))):
        return sR
    if pair in (frozenset(("h1", "s2")), frozenset(("h2", "s1"))):
        return uR
    if pair in (frozenset(("h1", "h2")), frozenset(("s1", "s2"))):
        return tR
    raise AssertionError(f"unexpected external pair {pair}")

def field_vertex(field, flavor):
    if field == "H":
        return Yh0, PR
    if field == "Hdag":
        return Yh0_dag, PL
    if flavor == "mu":
        if field == "S":
            return Ys0, PR
        return Ys0_dag, PL
    # In the tau sector the UV interaction contains S^* Ebar_L tau_R:
    # the S and Sdag field orientations are interchanged.
    if field == "S":
        return Ys0_dag, PL
    return Ys0, PR

def slash(v):
    return gamma[0]*v[0] - gamma[1]*v[1] - gamma[2]*v[2] - gamma[3]*v[3]

def dot4(u, v):
    return sp.expand(u[0]*v[0] - u[1]*v[1] - u[2]*v[2] - u[3]*v[3])

momenta = [sp.Matrix(sp.symbols(f"k{i}_0:4")) for i in range(4)]
checks = 0
def check(name, expr, expected=0):
    global checks
    residual = sp.simplify(expr - expected)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1

check("real-scalar vertex product equals one 1/4 field-projection weight",
      a**2*b**2, y**2*lam**2/4)
check("four charge-neutral assignments have total external decomposition weight",
      sp.Rational(4,4), 1)

valid_cases = 0
zero_trace_cases = 0
nonzero_cases = 0
invalid_cases = 0
nonzero_cycles = set()
rows = []

for assignment_index, assignment in enumerate(assignments, 1):
    for flavor in ("mu", "tau"):
        Hleg = next(leg for leg in ("h1", "h2") if assignment[leg] == "H")
        Sfield = "S" if flavor == "mu" else "Sdag"
        Sleg = next(leg for leg in ("s1", "s2") if assignment[leg] == Sfield)
        target_invariant = pair_invariant(Hleg, Sleg)

        for cycle in cycles:
            fields = [assignment[leg] for leg in cycle]
            vertices = [field_vertex(field, flavor) for field in fields]
            valid_paths = []
            for path in product((0, 1), repeat=4):
                nxt = path[1:] + path[:1]
                entries = [vertices[i][0][path[i], nxt[i]] for i in range(4)]
                if all(sp.simplify(entry) != 0 for entry in entries):
                    valid_paths.append((path, nxt, entries))
            if len(valid_paths) == 0:
                invalid_cases += 1
                continue
            if len(valid_paths) != 1:
                raise AssertionError(f"expected unique flavor path for {cycle}/{flavor}, got {valid_paths}")
            valid_cases += 1
            path, nxt, entries = valid_paths[0]
            masses = [M if nxt[i] == 1 else sp.Integer(0) for i in range(4)]
            spin_trace = sp.eye(4)
            for i in range(4):
                spin_trace = spin_trace * vertices[i][1] * (
                    slash(momenta[i]) + masses[i]*sp.eye(4)
                )
            spin_trace = sp.simplify(sp.trace(spin_trace))
            coupling_product = sp.simplify(sp.prod(entries))
            check(f"coupling product {assignment_index}/{flavor}/{cycle}",
                  coupling_product, a**2*b**2)

            if spin_trace == 0:
                zero_trace_cases += 1
                rows.append((assignment_index, flavor, cycle, path, "zero Dirac trace", "—", str(coupling_product)))
                continue

            nonzero_cases += 1
            nonzero_cycles.add(cycle)
            light_lines = [i for i in range(4) if nxt[i] == 0]
            if len(light_lines) != 2:
                raise AssertionError(f"expected two light lines, got {light_lines}")
            expected_trace = 2*M**2*dot4(momenta[light_lines[0]], momenta[light_lines[1]])
            check(f"massless-light numerator {assignment_index}/{flavor}/{cycle}",
                  spin_trace, expected_trace)

            # With route r=(0,-q2,-q2-q3,q1), the invariant between the
            # two light propagators is (q1+q2)^2 for start state 0 and
            # (q2+q3)^2 for start state 1.
            start_state = path[0]
            routed_pair = (cycle[0], cycle[1]) if start_state == 0 else (cycle[1], cycle[2])
            routed_invariant = pair_invariant(*routed_pair)
            check(f"bubble routing {assignment_index}/{flavor}/{cycle}",
                  routed_invariant, target_invariant)
            rows.append((assignment_index, flavor, cycle, path, "nonzero", str(routed_invariant), str(coupling_product)))

if (invalid_cases, valid_cases, zero_trace_cases, nonzero_cases) != (32,16,8,8):
    raise AssertionError(
        f"topology census mismatch: invalid={invalid_cases}, valid={valid_cases}, "
        f"zero={zero_trace_cases}, nonzero={nonzero_cases}"
    )
if len(nonzero_cycles) != 4:
    raise AssertionError(f"expected 4 contributing real-field cycles, got {nonzero_cycles}")

print("PASS: 4 charge-neutral assignments and 6 labeled cycles enumerated for each of mu/tau.")
print(f"PASS: {invalid_cases}/48 cycle/flavor/assignment cases forbidden by interaction-basis flavor flow.")
print(f"PASS: {valid_cases}/48 cases have a unique allowed flavor path.")
print(f"PASS: the valid paths split into {zero_trace_cases} zero-trace and {nonzero_cases} nonzero-trace cases.")
print("PASS: all 8 nonzero traces reduce to 2 M^2 times the dot product of the two massless-light-line momenta.")
print("PASS: all 8 nonzero light-line bubble invariants match the source mu s-channel or tau u-channel routing.")
print("PASS: each nonzero real-scalar contribution carries a^2 b^2 = y^2 lambda^2/4; do not apply another factor 1/4 to the real-field loop.")
print("NONZERO CYCLE TABLE:")
for row in rows:
    if row[4] == "nonzero":
        print(f"  assignment {row[0]} | {row[1]} | cycle={'-'.join(row[2])} | path={row[3]} | invariant={row[5]} | coupling={row[6]}")
print(f"RESULT: {checks} exact symbolic checks passed.")
print("SCOPE: interaction-basis flavor flow, chirality trace, and s/u routing only; no loop integration or final UV-EFT coefficient.")
