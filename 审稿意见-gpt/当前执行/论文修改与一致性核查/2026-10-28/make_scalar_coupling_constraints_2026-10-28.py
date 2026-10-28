#!/usr/bin/env python3
"""Reproduce the source-anchored scalar--muon coupling summary used in the referee response.

Source-reported inputs:
- Binary pulsar periastron advance: sensitivity interval 1e-17--2e-15 eV,
  best-sensitivity point near 4e-16 eV, coupling O(1e-21) (Liu & Tang, arXiv:2501.10927).
- Neutron-star cooling: y_sμμ <= 7.4e-14 for m_s <= 1 keV.
- SN 1987A cooling, conservative cold-SN model: y_sμμ <= 4.2e-9 for m_s <= 1 keV.
  This line represents the selected cooling threshold only, not the separate
  trapping/explosion-energy exclusion (Fiorillo et al., arXiv:2605.24094; Caputo et al., arXiv:2109.03244).
- Diffuse supernova gamma-ray background: y_sμμ <= 4e-11 over approximately
  100 keV--O(10) MeV (Caputo et al., arXiv:2109.03244).

This is a schematic summary of selected source-reported bounds, not a combined
exclusion contour. Fifth-force constraints are omitted because their translation
to a direct y_sμμ bound is matching-dependent.
"""
import matplotlib.pyplot as plt

OUT = "scalar_coupling_constraints_2026-10-28.pdf"
fig, ax = plt.subplots(figsize=(7.8, 4.6))
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-17, 1e7)
ax.set_ylim(1e-22, 1e-8)

ax.axvspan(1e-17, 2e-15, color="tab:blue", alpha=0.14,
           label="Binary-pulsar sensitivity interval", zorder=0)
ax.scatter([4e-16], [1e-21], s=38, color="tab:blue", zorder=4,
           label="Binary pulsar: best-sensitivity point")
ax.hlines(7.4e-14, 1e-17, 1e3, color="tab:green", linewidth=1.8,
          label="Neutron-star cooling (approx.)")
ax.hlines(4.2e-9, 1e-17, 1e3, color="tab:orange", linewidth=1.8,
          linestyle="--", label="SN 1987A cooling (conservative model)")
ax.hlines(4e-11, 1e5, 1e7, color="tab:red", linewidth=1.8,
          linestyle="-.", label="Diffuse supernova gamma-ray background")

ax.set_xlabel(r"Scalar mass $m_s$ [eV]")
ax.set_ylabel(r"Scalar--muon Yukawa $|y_{s\mu\mu}|$")
ax.grid(True, which="major", alpha=0.28, linewidth=0.6)
ax.grid(True, which="minor", alpha=0.12, linewidth=0.4)
ax.legend(loc="lower right", fontsize=7.6, framealpha=0.96,
          borderpad=0.65, labelspacing=0.45, handlelength=2.4)
fig.tight_layout(pad=1.0)
fig.savefig(OUT, format="pdf", bbox_inches="tight")
print(OUT)
