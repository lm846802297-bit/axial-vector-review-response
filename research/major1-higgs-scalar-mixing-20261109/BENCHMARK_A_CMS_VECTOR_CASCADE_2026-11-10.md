# Major Point 1 — Benchmark-A vector cascade and CMS \(\mu\mu\tau\tau\) search applicability

**Purpose:** quantify whether the open \(A'A'\) channel in Benchmark A is potentially relevant to existing Higgs exotic-decay searches. This is a leading isolated-pole estimate, not an experimental recast.

## 1. Benchmark-A pole-induced \(h_1\to A'A'\)

For the exact-momentum fermion-sector matched Plan-C-lite propagator at \(m_s=m_h=125.25\) GeV, the isolated narrow Higgs-like pole has the residue ratio
\[
r_{s/h}\equiv\frac{R_{hs}}{R_{hh}}
\simeq-2.4131\times10^{-4}+8.8128\times10^{-4}i,
\qquad |r_{s/h}|=9.1372\times10^{-4}.
\]
Interpreting this as a small pole-component ratio in the isolated-pole limit gives
\[
f_s\simeq\frac{|r_{s/h}|^2}{1+|r_{s/h}|^2}
=8.3489\times10^{-7}.
\]
For \(m_{A'}=10\) GeV and \(v_s=70.886458\) GeV,
\[
\Gamma(s\to A'A')\big|_{m_s=m_h}
=3.743676~{\rm GeV}.
\]
Hence the leading pole estimate is
\[
\Gamma(h_1\to A'A')\simeq
3.1255\times10^{-6}~{\rm GeV},
\qquad
{\cal B}(h_1\to A'A')\simeq7.6685\times10^{-4},
\]
using the Plan-C-lite Higgs-like pole width \(4.07269\) MeV. This estimate uses the pole residue ratio; it is not yet the fully factorized, gauge-independent physical vertex/residue calculation.

## 2. \(A'\) branching fractions at \(m_{A'}=10\) GeV

In the pure-axial benchmark, neglecting the much smaller loop-induced kinetic-mixing channels,
\[
\Gamma(A'\to\ell^+\ell^-)
=\frac{g_X^2m_{A'}}{12\pi}
\left(1-\frac{4m_\ell^2}{m_{A'}^2}\right)^{3/2},
\]
and the two massless left-handed neutrino channels together give
\[
\Gamma(A'\to\nu\bar\nu)_{\mu,\tau}
=\frac{g_X^2m_{A'}}{12\pi}.
\]
With \(g_X=0.0705353\):
\[
{\cal B}_{\mu\mu}=0.354875,\quad
{\cal B}_{\tau\tau}=0.290013,\quad
{\cal B}_{\nu\nu}=0.355112.
\]
The identical-vector-boson cascade with one dimuon and one ditau decay therefore has
\[
{\cal B}(A'A'\to\mu\mu\tau\tau)
=2{\cal B}_{\mu\mu}{\cal B}_{\tau\tau}
=0.205836.
\]
Taking the production rate of the isolated Higgs-like pole to be SM-like at this order gives the theory-level product
\[
\boxed{
\frac{\sigma(pp\to h_1)}{\sigma_{\rm SM}}\,
{\cal B}(h_1\to A'A'\to\mu\mu\tau\tau)
\simeq1.5785\times10^{-4}.
}
\]
This is the quantity to compare with a model-independent \(\sigma_H{\cal B}(H\to aa\to\mu\mu\tau\tau)/\sigma_{\rm SM}\) limit, before correcting for the different spin and polarization acceptance.

## 3. Relevant 2026 CMS analysis — close topology, not a direct limit

CMS-SUS-23-005 (CERN-EP-2026-200, arXiv:2609.12683) searches for
\[
H\to aa\to\mu\mu\tau\tau
\]
using \(138~\mathrm{fb}^{-1}\) at 13 TeV. For \(m_H=125\) GeV, its model-independent 95% CL limits span \(5\times10^{-5}\) to \(2.7\times10^{-4}\) over \(m_a=3.6\)--21 GeV. The paper explicitly notes peaking structures around \(m_a\simeq10\) GeV caused by \(\Upsilon\) resonances. The predicted Benchmark-A product \(1.58\times10^{-4}\) is therefore of the same order as this search's sensitivity envelope; it cannot be dismissed as obviously negligible.

However, CMS generated a **pseudoscalar** \(a\), whereas the model predicts a **spin-1 axial vector** \(A'\). At \(m_{A'}=10\) GeV, the scalar-to-vector-pair amplitude from \(sA'_\mu A'^\mu\) gives
\[
{\cal A}_{00}\propto \frac{m_h^2}{2m_{A'}^2}-1=77.4378,
\qquad
F_L=\frac{|{\cal A}_{00}|^2}{|{\cal A}_{00}|^2+2}
=0.999667.
\]
The two \(A'\) bosons are therefore almost entirely longitudinal. Their leptonic decay angular distributions differ from those of pseudoscalars, so CMS efficiencies and limits cannot be transferred directly. The \(m_{A'}=10\) GeV point also lies in the \(\Upsilon\)-background region identified by CMS.

## 4. Required recast inputs

A valid recast must:
1. generate \(h_1\to A'_L A'_L\) with the longitudinal vector polarization density matrix;
2. decay one \(A'\to\mu^+\mu^-\) and the other \(A'\to\tau^+\tau^-\), including tau spin correlations and subsequent tau decays;
3. reproduce the CMS trigger, boosted-\(\tau\) reconstruction, isolation, \(m_{\mu\mu}\) windows, and two-dimensional fit variables;
4. include the \(\Upsilon\)-region background treatment and evaluate the exact \(m_{A'}=10\) GeV observed/expected limit;
5. account for the two-pole Higgs line shape if the singlet pole overlaps the 125 GeV state.

Until this vector-specific recast is done, the CMS result is a strong motivation for a dedicated check, not an exclusion. The calculation does show that Benchmark A's exotic Higgs channel is experimentally relevant enough that it must be included in the referee discussion.

**References:** CMS Collaboration, CMS-SUS-23-005, CERN-EP-2026-200, arXiv:2609.12683 (2026); ATLAS Collaboration, HIGP-2025-19, CERN-EP-2026-228, arXiv:2608.07332 (2026).
