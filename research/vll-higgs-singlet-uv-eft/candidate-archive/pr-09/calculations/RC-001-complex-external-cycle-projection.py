#!/usr/bin/env python3
"""Project the six real-scalar cycle orderings onto fixed complex external fields.

Zero-mixing/unbroken limit; external legs are all incoming H,S,H^dagger,S^dagger.
The mass-basis vertex matrices are sparse, so the script exhausts all 6 labeled
cycle orderings x 16 internal-state paths for mu and tau, evaluates the exact
Dirac trace for every path with nonzero vertex entries, and identifies the
source-aligned s (mu) and u (tau) boxes.

This is an external-field/orientation projection check, not the full finite-
mixing Wilson coefficient. The 576 real-scalar candidate-kernel rows remain
useful diagnostics but cannot all be summed as one fixed complex amplitude.
Requires Python 3 and SymPy.
"""
from itertools import permutations, product
import sympy as sp

I = sp.I
z2 = sp.zeros(2)
sigmas = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -1], [1, 0]]) * I,
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(
        sp.Matrix.hstack(z2, sigma),
        sp.Matrix.hstack(-sigma, z2),
    ))
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
PR = sp.simplify((sp.eye(4) + gamma5) / 2)
PL = sp.simplify((sp.eye(4) - gamma5) / 2)

def slash(v):
    return gamma[0]*v[0] - gamma[1]*v[1] - gamma[2]*v[2] - gamma[3]*v[3]

checks = 0

def check(name, expr):
    global checks
    residual = sp.simplify(expr)
    if isinstance(residual, sp.MatrixBase):
        ok = residual == sp.zeros(*residual.shape)
    else:
        ok = residual == 0
    if not ok:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1
    print(f"PASS: {name}")

a, b, M = sp.symbols("y lambda M_E", nonzero=True)
Yh = a * sp.Matrix([[0, 1], [0, 0]])
Ys = b * sp.Matrix([[0, 0], [-1, 0]])
mass = {0: sp.Integer(0), 1: M}

# Complex-field vertices: H and S use Y P_R; their conjugates use Y^T P_L.
# For tau, S_tau=S^*, so the S/S^dagger assignments are interchanged.
verts_mu = {
    "H": (Yh, PR), "Hdag": (Yh.T, PL),
    "S": (Ys, PR), "Sdag": (Ys.T, PL),
}
verts_tau = {
    "H": (Yh, PR), "Hdag": (Yh.T, PL),
    "S": (Ys.T, PL), "Sdag": (Ys, PR),
}
cycles = [("H",) + tail for tail in permutations(("Hdag", "S", "Sdag"))]

# Generic external four-vectors, all incoming, with p_Hdag=-(p_H+p_S+p_Sdag).
pH = sp.Matrix([sp.Symbol(f"H_{i}") for i in range(4)])
pS = sp.Matrix([sp.Symbol(f"S_{i}") for i in range(4)])
pSd = sp.Matrix([sp.Symbol(f"Sd_{i}") for i in range(4)])
pHd = -pH-pS-pSd
mom4 = {"H": pH, "Hdag": pHd, "S": pS, "Sdag": pSd}
K = sp.Matrix([sp.Symbol(f"K_{i}") for i in range(4)])
C = a**2*b**2*M**2

# Exact generic trace for the fixed complex-field chirality sequence
# P_R, P_R, P_L, P_L. The two same-chirality edges require mass numerators;
# the other two edges carry slashed momenta.
m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")
kgeneric = [sp.Matrix([sp.Symbol(f"kg{i}_{mu}") for mu in range(4)])
            for i in range(1, 5)]
Ngeneric = [slash(kgeneric[i]) + (m1,m2,m3,m4)[i]*sp.eye(4)
            for i in range(4)]
trace_generic = sp.simplify(sp.expand(sp.trace(
    PR*Ngeneric[0]*PR*Ngeneric[1]*PL*Ngeneric[2]*PL*Ngeneric[3]
)))
dot24 = (kgeneric[1][0]*kgeneric[3][0]
         - kgeneric[1][1]*kgeneric[3][1]
         - kgeneric[1][2]*kgeneric[3][2]
         - kgeneric[1][3]*kgeneric[3][3])
check("generic P_R,P_R,P_L,P_L trace reduces to 2 m1 m3 k2.k4",
      trace_generic - 2*m1*m3*dot24)

# Coefficient vectors for the channel invariant. The Gram products are formal;
# only the coefficient-vector pairing is needed to label s/u/t.
mom3 = {
    "H": sp.Matrix([[1, 0, 0]]),
    "S": sp.Matrix([[0, 1, 0]]),
    "Sdag": sp.Matrix([[0, 0, 1]]),
    "Hdag": sp.Matrix([[-1, -1, -1]]),
}
targets = {"s": (1, 1, 0), "u": (1, 0, 1), "t": (0, 1, 1)}

def route(cycle):
    qv4 = [mom4[label] for label in cycle]
    r4 = [sp.zeros(4, 1), -qv4[1], -qv4[1]-qv4[2], qv4[0]]
    kline = [K+ri for ri in r4]
    qv3 = [mom3[label] for label in cycle]
    r3 = [sp.zeros(1, 3), -qv3[1], -qv3[1]-qv3[2], qv3[0]]
    return r4, kline, r3

def channel(cycle, path, r3):
    nxt = path[1:] + path[:1]
    line_masses = tuple(mass[nxt[i]] for i in range(4))
    light = [i for i,m in enumerate(line_masses) if m == 0]
    if len(light) != 2:
        return "not-two-light-lines", line_masses
    delta = r3[light[0]]-r3[light[1]]
    coeff = tuple(int(v) for v in list(delta))
    for name, target in targets.items():
        if coeff == target or coeff == tuple(-v for v in target):
            return name, line_masses
    return f"other:{coeff}", line_masses

def enumerate_complex(verts):
    surviving = []
    tested = 0
    for cycle in cycles:
        r4, kline, r3 = route(cycle)
        for path in product((0,1), repeat=4):
            tested += 1
            nxt = path[1:] + path[:1]
            coeff, projectors = [], []
            for i,label in enumerate(cycle):
                W,P = verts[label]
                coeff.append(W[path[i],nxt[i]])
                projectors.append(P)
            if any(value == 0 for value in coeff):
                continue
            trace_matrix = sp.eye(4)
            for i in range(4):
                trace_matrix = trace_matrix * (coeff[i]*projectors[i]) * (
                    slash(kline[i]) + mass[nxt[i]]*sp.eye(4)
                )
            tr = sp.factor(sp.expand(sp.trace(trace_matrix)))
            if sp.simplify(tr) != 0:
                ch, masses = channel(cycle,path,r3)
                surviving.append((cycle,path,ch,masses,tr,kline))
    if tested != 96:
        raise AssertionError(f"expected 96 cycle/path cases, got {tested}")
    return surviving

mu = enumerate_complex(verts_mu)
tau = enumerate_complex(verts_tau)
expected_mu_cycle = ("H","S","Sdag","Hdag")
expected_tau_cycle = ("H","Sdag","S","Hdag")
if len(mu) != 1 or mu[0][0] != expected_mu_cycle or mu[0][1] != (0,1,0,1) or mu[0][2] != "s":
    raise AssertionError(f"unexpected mu complex projection: {[(x[0],x[1],x[2]) for x in mu]}")
if len(tau) != 1 or tau[0][0] != expected_tau_cycle or tau[0][1] != (0,1,0,1) or tau[0][2] != "u":
    raise AssertionError(f"unexpected tau complex projection: {[(x[0],x[1],x[2]) for x in tau]}")
check("mu complex projection selects only H-S-Sdag-Hdag path 0101 in the s channel",
      sp.Integer(len(mu)-1))
check("tau complex projection selects only H-Sdag-S-Hdag path 0101 in the u channel",
      sp.Integer(len(tau)-1))

for flavor, item in (("mu",mu[0]),("tau",tau[0])):
    cycle,path,ch,masses,tr,kline = item
    check(f"{flavor} projected trace is +2 y^2 lambda^2 M_E^2 k_2.k_4",
          tr - 2*C*(kline[1][0]*kline[3][0] - kline[1][1]*kline[3][1]
                    - kline[1][2]*kline[3][2] - kline[1][3]*kline[3][3]))
    check(f"{flavor} projected path has mass pattern (M_E,0,M_E,0)",
          sp.Integer(sum(1 for m in masses if m == M)-2))
    check(f"{flavor} projected channel label is {ch}",
          sp.Integer(0) if ch in ("s","u") else sp.Integer(1))

# Check the fixed source denominator routing in each flavor.
r4_mu, kl_mu, _ = route(expected_mu_cycle)
q_s = -(pH+pS)
k_mu = kl_mu[1]
check("mu routing: light lines are k and k-q_s",
      (k_mu-(K-pS)) + (kl_mu[3]-(k_mu-q_s)))
check("mu routing: heavy lines are k+S and k-Sdag",
      (kl_mu[0]-(k_mu+pS)) + (kl_mu[2]-(k_mu-pSd)))

r4_tau, kl_tau, _ = route(expected_tau_cycle)
q_u = -(pH+pSd)
k_tau = kl_tau[1]
check("tau routing: light lines are k and k-q_u",
      (k_tau-(K-pSd)) + (kl_tau[3]-(k_tau-q_u)))
check("tau routing: heavy lines are k+Sdag and k-S",
      (kl_tau[0]-(k_tau+pSd)) + (kl_tau[2]-(k_tau-pS)))

# The real-scalar vertex V=Y P_R+Y^T P_L loses the S/Sdag orientation.
# Count its zero-mixing nonzero cycle/path rows as a diagnostic only.
real_survivors = []
for cycle in cycles:
    _, kline, _ = route(cycle)
    for path in product((0,1), repeat=4):
        nxt=path[1:]+path[:1]
        Vs=[]
        for i,label in enumerate(cycle):
            W = Yh if label in ("H","Hdag") else Ys
            Vs.append(W[path[i],nxt[i]]*PR + W[nxt[i],path[i]]*PL)
        if any(V == sp.zeros(4) for V in Vs):
            continue
        trace_matrix=sp.eye(4)
        for i in range(4):
            trace_matrix=trace_matrix*Vs[i]*(slash(kline[i])+mass[nxt[i]]*sp.eye(4))
        tr=sp.factor(sp.expand(sp.trace(trace_matrix)))
        if sp.simplify(tr)!=0:
            real_survivors.append((cycle,path))
check("real-scalar projection has four nonzero cycle/path rows in this limit",
      sp.Integer(len(real_survivors)-4))

print("MU surviving row:", mu[0][0], mu[0][1], "channel", mu[0][2])
print("TAU surviving row:", tau[0][0], tau[0][1], "channel", tau[0][2])
print("REAL-SCALAR surviving rows:", real_survivors)
print(f"RESULT: {checks} exact complex-external projection checks passed; each flavor selects one cycle/path in the zero-mixing limit.")
print("SCOPE: complex external-field orientation and s/u routing only; not the finite-mixing Wilson coefficient.")
print("OPEN: finite-mixing mass-path sums, common graph multiplicities, EFT soft/counterterm subtraction, and final UV-EFT match.")
