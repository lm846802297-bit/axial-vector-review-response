# P1-IIIe-C3B: full-radial finite-difference step scan

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose

C3-B scans the central finite-difference step used in the C3-A density-derivative identity. The scan covers both nucleon species at all 301 radii of the \(t_{\rm pb}=1\) s Caputo SFHo-18.8 published-figure snapshot.

At each radius and for each step, \(T\), \(m_N^*\), \(U_N\), and \(\xi_{\rm SPP}\) are held fixed. Only \(\mu_N^{\rm nonrel}\), equivalently \(\nu_N\), is shifted by \(\pm h\). The direct blocked integral is held fixed as the reference.

## 2. Scan setup

The nine tested step fractions are
\[
\frac{h}{T}=
\{10^{-2},3\times10^{-3},10^{-3},3\times10^{-4},
2\times10^{-4},10^{-4},3\times10^{-5},10^{-5},3\times10^{-6}\}.
\]
Every density integral uses 2048-point Gauss-Legendre momentum quadrature and a \(45T\) kinetic-energy tail. The long-form output contains \(301\times2\times9=5418\) rows.

## 3. Maximum relative residuals

| \(h/T\) | Neutron maximum | Proton maximum |
|---:|---:|---:|
| \(10^{-2}\) | \(1.7166\times10^{-6}\) | \(1.5239\times10^{-5}\) |
| \(10^{-3}\) | \(1.7166\times10^{-8}\) | \(1.5239\times10^{-7}\) |
| \(10^{-4}\) | \(1.8305\times10^{-10}\) | \(1.5451\times10^{-9}\) |
| \(3\times10^{-5}\) | \(3.1934\times10^{-10}\) | \(1.9787\times10^{-10}\) |
| \(10^{-5}\) | \(9.7392\times10^{-10}\) | \(5.7046\times10^{-10}\) |
| \(3\times10^{-6}\) | \(3.3367\times10^{-9}\) | \(1.6150\times10^{-9}\) |

At \(h/T=10^{-2}\rightarrow10^{-3}\), reducing the step by a factor of ten reduces the maximum residual by approximately 100 for both species:
\[
\frac{\epsilon_{\max}(10^{-2})}{\epsilon_{\max}(10^{-3})}
\simeq100.00.
\]
This is the expected \(O(h^2)\) central-difference truncation regime.

At \(3\times10^{-6}\), and depending on the quadrature backend already at \(10^{-5}\), the residual begins to rise again. This is consistent with floating-point cancellation in the subtraction \(n'(\nu+h)-n'(\nu-h)\), rather than a failure of the thermodynamic identity. The location of the roundoff floor is implementation-dependent.

## 4. Selected shared step

The common working step retained for C3 is
\[
\boxed{h/T=3.0\times10^{-5}}.
\]
In the direct JavaScript scan it gives a worst-case relative residual of
\[
3.19\times10^{-10},
\]
while the independent NumPy/SciPy Python CI reconstruction gives
\[
1.54\times10^{-10}.
\]
The exact smallest residual at \(10^{-5}\) versus \(3\times10^{-5}\) depends on the quadrature backend: the JavaScript calculation favors \(3\times10^{-5}\), while the Python reconstruction has a slightly smaller roundoff residual at \(10^{-5}\). We therefore retain \(3\times10^{-5}\) as the conservative common setting already used in C3-A; it is stable in both independent implementations and remains far below the \(10^{-8}\) acceptance threshold.

## 5. Acceptance and interpretation

C3-B acceptance:
- all 301 radii, both species, and all nine step sizes are present;
- the selected shared step has maximum relative residual below \(10^{-8}\) for both species;
- the large-step error ratio is between 80 and 120, consistent with second-order truncation;
- all direct factors are in \((0,1)\), and all finite-difference derivatives are positive.

**C3-B direct numerical status: PASS.**

The scan validates the numerical derivative and selects a stable shared step. It does not change the primary EOS chemical potentials, C2 occupations, or direct-integral \(F_{NN}^{\rm deg}\) values.

## 6. Scope boundary and next stage

This remains a local static calculation at one radial snapshot. It does not yield a time-space weighted core average, dynamic \(W_N^{\mu\nu}(q_0,q;r)\), B.2 opacity, transport, luminosity, or an axial cooling curve.

Next is C3-C: characterize the radial dependence of the already-validated local \(F_{nn}^{\rm deg}(r)\) and \(F_{pp}^{\rm deg}(r)\), and compare it against \(T(r)\), \(m_N^*(r)\), \(\nu_N(r)\), and the free-nucleon/cluster composition. This is still diagnostic; it is not yet a global cooling weight.
