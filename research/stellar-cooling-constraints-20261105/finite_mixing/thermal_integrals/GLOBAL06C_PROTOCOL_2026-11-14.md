# Global-06C: full-profile high-order B.13 kernel convergence

## Purpose and status
Global-06C isolates and closes the local B.13 quadrature-accuracy gap identified after Global-07's first energy/radial integration. This protocol does not claim a completed calculation or accepted luminosity.

## Frozen physics baseline
- SFHo-18.8, post-bounce 1 s, 1687 radial profile nodes.
- $m_{A'}=10$ MeV, pure-vector benchmark: $g_V/g_X=1$, $g_A/g_X=0$.
- Exact-recoil moving-muon semi-Compton kernel B.13.
- Keep $mu^-$ and $mu^+$ and $L,+,-$ polarization channels separate.
- Do not alter B.16 literature baseline, scalar B.2 reference, prior runs, or axial limits.

## Stage A: directional diagnosis
At $r=8.482141202$ km and $x={0.05,0.5,2,6,11.196,18,26.228,36}$, use the all-high anchor $(36,20,20,20)$. Vary one coordinate at a time:
- $n_p$: 20, 24, 28, 32, 36;
- $n_\mu,n_\gamma,n_\phi$: 12, 14, 16, 18, 20.
Compare every charge, polarization, production, absorption, reduced-absorption and spectral-source channel with the anchor. Record detailed balance, final-muon shell, and positivity checks. This diagnoses sensitivity; it is not itself a convergence proof.

## Stage B: full-profile high-order calculation
After Stage A identifies dominant directions, run all 1687 radial vertices and the complete formal energy grid. Retain original chunks and write new high-order chunks separately. For each effective channel, require two successive order upgrades below 0.1%; extend the ladder when needed. Preserve per-channel values and absolute errors for channels near zero.

## Stage C: interpolation and independent validation
Rebuild the energy interpolant only from accepted high-order nodes. Directly recompute independent energy midpoints and radial midpoints. Do not reuse the old 0.51514% interpolation claim as an acceptance result for the new table.

## Stage D: B.1 source correction
Compute old and new optically thin source integrals on identical grids and weights:
$L_{\rm thin}=\sum_{r,x,h}W_{r,x,h}K_{r,x,h}$.
Report separate charge and polarization contributions and the weighted global correction. Do not infer a global luminosity correction from the largest local relative error.

## Acceptance gates
1. Full-profile high-order local kernels pass the per-channel successive-order criterion.
2. Detailed balance and final-muon shell remain within the established $2\times10^{-10}$ tolerance; rates finite and nonnegative.
3. New energy/radial interpolation checks pass the project's 1% limit.
4. Independent B.1 energy and radial integrations converge below 1%.
5. Preserve raw chunks, SHA-256 manifest, exact source revision, parameters, logs, and reproducible tests.

Global-08/B.2, final SN1987A curves, and axial updates remain blocked until these gates pass. Merge research PRs with **Create a merge commit**, preserving original research commits.
