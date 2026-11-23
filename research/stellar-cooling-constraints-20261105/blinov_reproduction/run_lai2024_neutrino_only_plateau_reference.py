"""Generate the Lai Eq. (E2) neutrino-only plateau reference on the public SFHo profile."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from croon_c0_luminosity import DEFAULT_PROFILE, T_NU_MEV, neutrinosphere_radius
from lai2024_plateau_equation_audit import lai_neutrino_only_plateau

OUTPUT = Path(__file__).resolve().parent / "outputs" / "lai2024_neutrino_only_plateau_reference_2026-11-19.json"
MASSES_MEV = [2.0e-6, 1.0e-5, 0.1, 1.0, 10.0]


def main() -> None:
    profile_path = Path(DEFAULT_PROFILE)
    rows = np.genfromtxt(profile_path, delimiter=",", names=True)
    r_nu = neutrinosphere_radius(rows["r_km"], rows["T_MeV"], T_NU_MEV)
    results = [
        lai_neutrino_only_plateau(
            mass_MeV=mass,
            temperature_MeV=T_NU_MEV,
            neutrinosphere_radius_km=r_nu,
            energy_order=256,
            tail_in_T=40.0,
        )
        for mass in MASSES_MEV
    ]
    result = {
        "title": "Lai et al. Eq. (E2): neutrino-only thin-shell plateau reference",
        "profile_file": profile_path.name,
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "profile_row_count": int(len(rows)),
        "neutrinosphere_definition": "outward T=3 MeV crossing",
        "neutrinosphere_radius_km": float(r_nu),
        "surface_temperature_MeV": float(T_NU_MEV),
        "raffelt_reference_erg_s": 3.0e52,
        "masses_MeV": MASSES_MEV,
        "results": results,
        "scope": "neutrino-pair coalescence/decay only; excludes semi-Compton, loop bremsstrahlung, and the full coupled attenuation network",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "profile_sha256": result["profile_sha256"],
        "R_nu_km": result["neutrinosphere_radius_km"],
        "results": [
            {
                "mass_MeV": x["mass_MeV"],
                "L_nu_only_plateau_erg_s": x["L_nu_only_plateau_erg_s"],
                "ratio_to_Raffelt": x["L_nu_only_plateau_erg_s"] / 3.0e52,
            }
            for x in results
        ],
        "output": str(OUTPUT),
    }, indent=2))


if __name__ == "__main__":
    main()
