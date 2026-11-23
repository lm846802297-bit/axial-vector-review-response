# RC-001 — Explicit common-\(k\) shift maps for Yukawa endpoints and scalar seagulls

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVj  
**Status:** all 12 Yukawa-endpoint terms from the two matter-line WTIs and all six scalar-seagull routings have been explicitly mapped onto the corresponding three-W reference momenta. The shifts match not only the adjacent light propagators and internal-W momentum, but also the heavy-channel momentum. This supplies the graph-specific kinematic alignment that was left abstract in the universal Lorentz-kernel audit. It is a routing result; it does not by itself cancel the weak tensors or the seagull Lorentz contacts.

## 1. Five-point momentum convention

Use all incoming external momenta
\[
p_1+p_2+p_3+p_4+q=0,
\qquad
p_4=-p_1-p_2-p_3-q,
\]
and define \(P_L=p_1+p_2\). The loop momentum is \(k\). For the cross-vertex three-W reference graph,
\[
r_A^{3W}=k-p_A,\qquad
r_B^{3W}=k+p_B+q,\qquad
h^{3W}=k-P_L,
\]
with internal-W momenta
\[
k_A^{3W}=k,\qquad k_B^{3W}=k+q.
\]
For the same-vertex three-W reference graph,
\[
r_F^{3W}=k+p_F+q,\qquad
r_S^{3W}=p_S-k,\qquad
h^{3W}=p_F+p_S+q,
\]
with internal-W momenta
\[
k_S^{3W}=k,\qquad k_F^{3W}=k+q.
\]

## 2. Cross-vertex Yukawa endpoints

For LD-W-01/02/05/06 the B1 routes are
\[
r_A^Y=k-p_A-q,\qquad r_A^W=k-p_A,
\]
\[
r_B^W=k+p_B,\qquad r_B^Y=k+p_B+q.
\]

### A-side Yukawa endpoint

The A-line WTI term adjacent to the Yukawa vertex carries
\[
r_A^Y=k_{\rm old}-p_A-q,\quad
r_B=k_{\rm old}+p_B,\quad
h_A=k_{\rm old}-P_L-q,\quad
k_W=k_{\rm old}.
\]
Shift the integration variable
\[
k_{\rm old}=k+q.
\]
Then
\[
r_A^Y\to k-p_A=r_A^{3W},
\]
\[
r_B\to k+p_B+q=r_B^{3W},
\]
\[
h_A\to k-P_L=h^{3W},
\]
\[
k_W\to k+q=k_B^{3W}.
\]
Thus the A-side Yukawa endpoint term aligns with the \(D(k+q)\) term in the contracted three-W propagator chain.

### B-side Yukawa endpoint

The B-line Yukawa endpoint is already in the common \(k\) routing:
\[
r_A=k-p_A=r_A^{3W},\quad
r_B^Y=k+p_B+q=r_B^{3W},
\]
\[
h=k-P_L=h^{3W},\qquad
k_W=k=k_A^{3W}.
\]
It therefore aligns with the \(D(k)\) term.

These two maps are checked for each of LD-W-01, LD-W-02, LD-W-05 and LD-W-06. The heavy momentum is included in every equality; the shift is not merely a relabeling of the massless propagators.

## 3. Same-vertex Yukawa endpoints

For LD-W-03/04,
\[
r_F^Y=k+p_F+q,\qquad r_F^W=k+p_F,
\]
\[
r_S^W=p_S-k,\qquad r_S^Y=p_S-k+q,
\]
and the heavy momentum is \(h=p_F+p_S+q\).

### F-side Yukawa endpoint

Without shifting \(k\),
\[
r_F^Y=k+p_F+q=r_F^{3W},
\]
\[
r_S^W=p_S-k=r_S^{3W},
\]
\[
h=p_F+p_S+q=h^{3W},
\qquad k_W=k=k_S^{3W}.
\]
This term aligns with \(D(k)\).

### S-side Yukawa endpoint

Shift \(k_{\rm old}=k+q\). Then
\[
r_S^Y=p_S-k_{\rm old}+q=p_S-k=r_S^{3W},
\]
\[
r_F^W=k_{\rm old}+p_F=k+p_F+q=r_F^{3W},
\]
\[
h=p_F+p_S+q=h^{3W},
\qquad k_W=k+q=k_F^{3W}.
\]
This term aligns with \(D(k+q)\).

The heavy propagator is independent of the loop momentum in these same-vertex subgraphs, but its external-channel shift \(P_{FS}\to P_{FS}+q\) is retained exactly.

## 4. Scalar-seagull routing maps

The scalar seagull uses one scalar propagator and the two-gauge contact vertex. Its weak tensor and Lorentz factor remain distinct from the ordinary scalar-line insertion. The routing nevertheless aligns with the same three-W reference endpoints.

| Pair | Seagull endpoint | Required shift | Scalar momentum after shift | W momentum after shift |
|---|---|---|---|---|
| LD-W-02 | B scalar | none | \(k+p_B+q\) | \(k\) |
| LD-W-05 | A scalar | \(k_{\rm old}=k+q\) | \(k-p_A\) | \(k+q\) |
| LD-W-06 | A scalar | \(k_{\rm old}=k+q\) | \(k-p_A\) | \(k+q\) |
| LD-W-06 | B scalar | none | \(k+p_B+q\) | \(k\) |
| LD-W-03 | S scalar | \(k_{\rm old}=k+q\) | \(p_S-k\) | \(k+q\) |
| LD-W-04 | S scalar | \(k_{\rm old}=k+q\) | \(p_S-k\) | \(k+q\) |

In every row the heavy momentum also matches the corresponding three-W reference: \(k-P_L\) for the cross-vertex set and \(p_F+p_S+q\) for the same-vertex set.

This is only a momentum/denominator alignment. It does not identify the seagull anticommutator tensor with an ordered matter-line tensor and does not establish a cancellation of the \(q^\mu\) contact term.

## 5. Exact checks and reproduction

The exact symbolic audit is in
calculations/RC-001-dim6-WW-fivepoint-common-k-shift-maps.py
with output in
validation/RC-001-dim6-WW-fivepoint-common-k-shift-maps.txt.

It verifies:
- cross-vertex Yukawa endpoint maps: 8/8 maps, 128/128 vector components;
- same-vertex Yukawa endpoint maps: 4/4 maps, 64/64 vector components;
- all Yukawa endpoint maps: 12/12 maps, 192/192 vector components;
- cross-vertex scalar seagull maps: 4/4 maps, 48/48 vector components;
- same-vertex scalar seagull maps: 2/2 maps, 24/24 vector components;
- all scalar seagull maps: 6/6 maps, 72/72 vector components.

These are exact componentwise momentum identities in the local SymPy calculation session, not a GitHub Actions result or a FeynArts/QGRAF generation.

## 6. What the shift maps establish

The two propagator-difference terms from the three-W contraction have definite graph-level routing partners:
\[
D(k):\quad
\begin{cases}
\text{cross B-side Yukawa endpoint},\\
\text{same-vertex F-side Yukawa endpoint},
\end{cases}
\]
\[
D(k+q):\quad
\begin{cases}
\text{cross A-side Yukawa endpoint after }k_{\rm old}\to k+q,\\
\text{same-vertex S-side Yukawa endpoint after }k_{\rm old}\to k+q.
\end{cases}
\]
The scalar seagulls follow the corresponding shifts in the table above.

This removes the ambiguity about which common-\(k\) shift is required. It does **not** prove that these terms cancel in the full amplitude: their weak tensors, chiral projectors, scalar seagull contact factors and external-field endpoint terms must still be combined with the correct Feynman-rule phases.

## 7. Next calculation

The next step is to insert the actual pair-dependent endpoint numerators into these fixed maps:
1. retain the ordered weak tensors from the cross-vertex and same-vertex raw-index bridges;
2. combine the Yukawa-endpoint terms with the external-field gauge variations using the two Yukawa-singlet identities;
3. keep the scalar-line and scalar-seagull tensors separate until their full Lorentz factors are included;
4. combine the remaining internal-W commutator terms with the \(D(k)-D(k+q)\) three-W kernel;
5. retain \(R_{\rm FG}\) for the full gauge-fixing/ghost Slavnov–Taylor completion.

No loop integration, UV–EFT subtraction, transverse form factor, or Wilson coefficient is claimed in this stage.
