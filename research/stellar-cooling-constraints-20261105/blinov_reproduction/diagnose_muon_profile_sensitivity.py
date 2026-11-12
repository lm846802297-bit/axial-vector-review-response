"""One-factor 10 MeV Fig. 7 sensitivity to the alternative muon chemical-potential curve."""
from __future__ import annotations
import argparse, hashlib, json, os, tempfile
from pathlib import Path
import numpy as np

try:
    from .diagnose_fig7_10mev_three_layer import DEFAULT_FIG7, decompose
except ImportError:
    from diagnose_fig7_10mev_three_layer import DEFAULT_FIG7, decompose

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_PROVENANCE = ROOT / "data" / "profile_provenance.json"
DEFAULT_OUTPUT = HERE / "outputs" / "muon_profile_sensitivity_10mev.json"


def write_ferreira_mu_profile(source: Path, target: Path) -> dict:
    data = np.genfromtxt(source, delimiter=",", names=True)
    required = {"r_km", "T_MeV", "mu_mu_MeV", "mu_numu_MeV",
                "lapse", "mu_mu_Ferreira_MeV"}
    missing = required.difference(data.dtype.names or ())
    if missing:
        raise ValueError(f"Profile is missing columns: {sorted(missing)}")
    alt_mu = np.asarray(data["mu_mu_Ferreira_MeV"], float)
    alt_mu = np.where(np.isfinite(alt_mu), alt_mu, 0.0)
    values = np.column_stack([data["r_km"], data["T_MeV"], alt_mu,
                              data["mu_numu_MeV"], data["lapse"]])
    np.savetxt(target, values, delimiter=",",
               header="r_km,T_MeV,mu_mu_MeV,mu_numu_MeV,lapse",
               comments="", fmt="%.12g")
    return {
        "n_rows": int(len(data)),
        "changed_column": "mu_mu_MeV <- mu_mu_Ferreira_MeV; nonfinite tail -> 0",
        "preserved_columns": ["r_km", "T_MeV", "mu_numu_MeV", "lapse"],
        "mu_mu_baseline_range_MeV": [float(np.nanmin(data["mu_mu_MeV"])),
                                     float(np.nanmax(data["mu_mu_MeV"]))],
        "mu_mu_ferreira_range_MeV": [float(np.min(alt_mu)), float(np.max(alt_mu))],
        "alternate_profile_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    }


def contour_crossings(points, threshold):
    ordered = sorted(points, key=lambda row: row["g"])
    result = []
    ystar = np.log(float(threshold))
    for a, b in zip(ordered[:-1], ordered[1:]):
        g0, g1 = float(a["g"]), float(b["g"])
        l0, l1 = float(a["calculated_luminosity_erg_s"]), float(b["calculated_luminosity_erg_s"])
        if l0 <= 0 or l1 <= 0:
            continue
        y0, y1 = np.log(l0), np.log(l1)
        if (y0-ystar)*(y1-ystar) > 0 or y1 == y0:
            continue
        t = (ystar-y0)/(y1-y0)
        result.append(float(np.exp(np.log(g0)+t*(np.log(g1)-np.log(g0)))))
    return result


def compact(report):
    pts = report["all_25_curve_points"]
    return {
        "curve_metrics": report["curve_metrics"],
        "contour_crossings_g": {
            "Lcrit_4p4e52": contour_crossings(pts, 4.4e52),
            "Lcrit_3p0e52": contour_crossings(pts, 3.0e52),
        },
        "selected_points": {
            name: {
                "g": row["g"],
                "relative_difference": row["relative_difference"],
                "thin_luminosity_erg_s": row["optically_thin_total_luminosity_erg_s"],
                "escape_fraction": row["total_escape_fraction"],
                "source_weighted_optical_depth": row["source_weighted_optical_depth"],
            } for name, row in report["selected_points"].items()
        },
        "curve_points": [
            {k: row[k] for k in ("g", "reference_luminosity_erg_s",
                                  "calculated_luminosity_erg_s", "relative_difference")}
            for row in pts
        ],
    }


def run(profile=DEFAULT_PROFILE, provenance=DEFAULT_PROVENANCE, fig7=DEFAULT_FIG7,
        nr=40, ne=100, na=16, ns=32):
    prov = json.loads(provenance.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="mu-profile-audit-") as tmp:
        alt_path = Path(tmp) / "sfho188_ferreira_mu_mu_only.csv"
        build = write_ferreira_mu_profile(profile, alt_path)
        base_report = decompose(profile, fig7, nr, ne, na, ns)
        alt_report = decompose(alt_path, fig7, nr, ne, na, ns)
    return {
        "title": "10 MeV Fig. 7 sensitivity to alternative muon chemical-potential profile",
        "status": "diagnostic_only_not_a_profile_replacement",
        "scope": "Only mu_mu(r) changes; T, mu_numu, lapse, mass, coupling grid, rates and transport are fixed.",
        "source_hashes": {
            "baseline_profile": hashlib.sha256(profile.read_bytes()).hexdigest(),
            "profile_provenance": hashlib.sha256(provenance.read_bytes()).hexdigest(),
            "fig7_reference": hashlib.sha256(fig7.read_bytes()).hexdigest(),
            "script": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "quadrature": {"radial": nr, "energy": ne, "angular": na, "path": ns},
        "profile_build": build,
        "provenance_assumptions": prov.get("assumptions", []),
        "baseline_caputo_mu_mu": compact(base_report),
        "ferreira_mu_mu_only": compact(alt_report),
        "interpretation": (
            "A changed curve diagnoses sensitivity to the reconstructed muon chemical-potential profile. "
            "It does not establish that the Ferreira curve is the correct profile for the Blinov snapshot. "
            "No alternative profile or normalization is adopted."
        ),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    p.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    p.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--nr", type=int, default=40)
    p.add_argument("--ne", type=int, default=100)
    p.add_argument("--na", type=int, default=16)
    p.add_argument("--ns", type=int, default=32)
    a = p.parse_args()
    report = run(a.profile, a.provenance, a.fig7, a.nr, a.ne, a.na, a.ns)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    for name in ("baseline_caputo_mu_mu", "ferreira_mu_mu_only"):
        print(name, json.dumps({"curve_metrics": report[name]["curve_metrics"],
                                "contour_crossings_g": report[name]["contour_crossings_g"]}, indent=2))
    print(f"Wrote {a.output}")


if __name__ == "__main__":
    main()
