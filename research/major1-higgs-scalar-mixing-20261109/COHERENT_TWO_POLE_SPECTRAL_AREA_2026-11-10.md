# Major Point 1 — coherent two-pole h-channel spectral-area diagnostic

Using the Plan-C-lite approximate propagator, the \(h\)-source to SM-final-state resonant amplitude is proportional to the \(hh\) propagator entry:
\[
{\cal A}_{\rm res}(s)\propto D_{hh}(s)
=\frac{s-b}{(s-a)(s-b)-\Pi_{hs}(s)^2}.
\]
In the archived implementation, \(a=m_h^2-i m_h\Gamma_h\) and
\(b=m_s^2-i m_s\Gamma_s\), with \(D_{\rm SM}(s)=1/(s-a)\);
\(\Gamma_s\) is the sum of the implemented \(A'A'\), muon and tau
partial widths. The selected off-diagonal kernel and constants are defined in
[the archived script](coherent_two_pole_spectral_area.py), not a complete
renormalized self-energy. The script uses \(m_h=125.25\) GeV,
\(\Gamma_h=0.00407\) GeV and \(M_E=20\) TeV.

> **Window audit, 2026-11-14:** the archived script inserts \(m_s\) into
> the quadrature breakpoints even when it is outside the integration interval.
> Thus the 100 and 150 GeV cases in the table integrate beyond the stated
> window. The largest absolute change in the ratio when restricting the
> integration to 124.5–126.0 GeV is \(2.69\times10^{-8}\); the two
> 125.25 GeV cases are unchanged within numerical precision. The table below
> preserves the archived values. See the [audit record](SPECTRAL_WINDOW_AUDIT_2026-11-14.md)
> and [numerical comparison](spectral_window_audit_2026-11-14.csv).

The target coherent spectral-area proxy is defined over \(m\in[124.5,126.0]\) GeV:
\[
R_{\rm area}=
\frac{\int dm\,|D_{hh}(m^2)|^2}
{\int dm\,|D_{\rm SM}(m^2)|^2}.
\]
The calculation retains the full coherent two-pole denominator and interference; it does not add two independent Breit-Wigner rates.

| Benchmark | \(m_s\) [GeV] | \(R_{\rm area}\) |
|---|---:|---:|
| A | 100.00 | 1.0000305 |
| A | 125.25 | 0.9993397 |
| A | 150.00 | 0.9999672 |
| B | 100.00 | 1.0000016 |
| B | 125.25 | 0.9877651 |
| B | 150.00 | 0.9999986 |

In this simplified calculation, the exact-degeneracy area shift is about \(-0.066\%\) for A and \(-1.22\%\) for B. The sharp pointwise dip/peak structure in B therefore does not translate into a comparably large integrated h-channel area change once the two poles are treated coherently.

**Interpretation boundary:** this ratio is not an experimental signal strength. It assumes constant external production/decay vertices, fixed diagonal widths, the selected Plan-C-lite off-diagonal kernel, no backgrounds, and no detector response or acceptance. It is a theory-level coherent spectral-area diagnostic only. A detector-level result requires production-mode-dependent vertices, final-state-specific widths, parton luminosities, interference with continuum backgrounds, detector resolution/efficiency and the experimental likelihood.

## Reproduction and artifact provenance

- Archived implementation: [coherent_two_pole_spectral_area.py](coherent_two_pole_spectral_area.py).
- The original script is retained for historical reproduction only; it is not the authoritative strict-window producer. Use the restricted-window audit script and CSV for the target interval.
- Archived output: [coherent_two_pole_spectral_area.txt](coherent_two_pole_spectral_area.txt).
- Suggested command to regenerate the archived output: `python coherent_two_pole_spectral_area.py > coherent_two_pole_spectral_area.txt`. This reproduces the historical breakpoint behavior, including the out-of-window `m_s` breakpoint for the 100 and 150 GeV cases; it is not the strictly restricted-window result.
- Strict-window comparison: run `python spectral_window_audit_2026-11-14.py > spectral_window_audit_2026-11-14.csv`; the [window-audit record](SPECTRAL_WINDOW_AUDIT_2026-11-14.md) records Python 3.12.14 and SciPy 1.17.0 for that comparison.
- The exact historical shell command and runtime used to create the original `.txt` output were not separately preserved. The window-audit record states that the original script was also rerun and passed its six stored tolerance checks; those checks do not detect the breakpoint issue.

