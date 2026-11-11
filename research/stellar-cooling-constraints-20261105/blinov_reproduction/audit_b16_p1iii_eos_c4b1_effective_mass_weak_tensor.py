#!/usr/bin/env python3
"""C4-B1: effective-mass quasiparticle weak tensor and vector-Ward checks."""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

from audit_b16_p1iii_eos_full_radial_occupation import load_profile

HERE = Path(__file__).resolve().parent
KERNEL_PATH = HERE/"audit_b16_p1iii_b_stationary_dirac_trace.py"
_SPEC = importlib.util.spec_from_file_location("c4b1_stationary_kernel", KERNEL_PATH)
kernel = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(kernel)

METRIC = kernel.METRIC
GAMMA = kernel.GAMMA
GAMMA5 = kernel.GAMMA5
SIGMA = kernel.SIGMA
IDENT = kernel.IDENT
MASS = kernel.MASS
SPECIES = ("n", "p")
PROFILE_INDICES = (0, 96, 196, 300)
Q_VALUES = (30.0, 100.0, 200.0, 500.0)
P_VALUES = (100.0, 300.0, 600.0)
COS_PQ_VALUES = (-0.6, 0.2, 0.8)


def slash(vector: np.ndarray) -> np.ndarray:
    return sum(METRIC[mu]*vector[mu]*GAMMA[mu] for mu in range(4))


def dbar(matrix: np.ndarray) -> np.ndarray:
    return GAMMA[0]@matrix.conj().T@GAMMA[0]


def _bilinear_tensor(
    left_vertices: list[np.ndarray],
    right_vertices: list[np.ndarray],
    p: np.ndarray,
    pp: np.ndarray,
    mstar: float,
) -> np.ndarray:
    si = slash(p)+mstar*IDENT
    sf = slash(pp)+mstar*IDENT
    barred = [dbar(vertex) for vertex in right_vertices]
    return np.asarray([
        [
            0.5*np.trace(sf@left_vertices[mu]@si@barred[nu])
            for nu in range(4)
        ]
        for mu in range(4)
    ], dtype=complex)


def quasiparticle_tensor(
    p: np.ndarray,
    pp: np.ndarray,
    q: np.ndarray,
    mstar: float,
    target: str,
) -> dict[str, np.ndarray | float]:
    """Use m* in on-shell quasiparticle spinors, vacuum M_N in form factors.

    q = p'*-p* and both quasiparticles have the same local m*. The weak
    magnetism denominator and form-factor dipole scale retain the physical
    vacuum nucleon mass M_N, not m*.
    """
    if target not in SPECIES:
        raise ValueError("target must be n or p")
    m_vac = MASS[target]
    q_cov = METRIC*q
    q2 = float(q[1:]@q[1:]-q[0]*q[0])
    if q2 < -1e-10:
        raise ValueError("spacelike momentum transfer required")
    f1, ga, f2 = kernel.ff(max(q2, 0.0), target, m_vac)
    vector_vertices, axial_vertices = [], []
    for mu in range(4):
        pauli = sum(
            SIGMA[mu][alpha]*METRIC[alpha]*q[alpha]
            for alpha in range(4)
        )
        vector_vertices.append(
            f1*GAMMA[mu]+1j*f2/(2.0*m_vac)*pauli
        )
        axial_vertices.append(-ga*GAMMA[mu]@GAMMA5)

    hvv = _bilinear_tensor(vector_vertices, vector_vertices, p, pp, mstar)
    haa = _bilinear_tensor(axial_vertices, axial_vertices, p, pp, mstar)
    hva = _bilinear_tensor(vector_vertices, axial_vertices, p, pp, mstar)
    hav = _bilinear_tensor(axial_vertices, vector_vertices, p, pp, mstar)
    return {
        "H_VV": hvv,
        "H_AA": haa,
        "H_VA": hva,
        "H_AV": hav,
        "H_total": hvv+haa+hva+hav,
        "q_cov": q_cov,
        "Q2_MeV2": max(q2, 0.0),
        "M_vac_MeV": m_vac,
        "mstar_MeV": mstar,
    }


def ward_residual(tensor: np.ndarray, q_cov: np.ndarray, *, first_index: bool) -> float:
    contracted = q_cov@tensor if first_index else tensor@q_cov
    denominator = np.linalg.norm(q_cov)*np.linalg.norm(tensor)
    return float(np.linalg.norm(contracted)/max(denominator, 1e-300))


def hermiticity_residual(tensor: np.ndarray) -> float:
    return float(
        np.linalg.norm(tensor-tensor.conj().T)
        / max(np.linalg.norm(tensor), 1e-300)
    )


def lepton_tensor(k: np.ndarray, kp: np.ndarray, antinu: bool) -> np.ndarray:
    first, second = (slash(k), slash(kp)) if antinu else (slash(kp), slash(k))
    return np.asarray([
        [
            np.trace(
                first@(METRIC[mu]*GAMMA[mu])@(IDENT-GAMMA5)
                @second@(METRIC[nu]*GAMMA[nu])@(IDENT-GAMMA5)
            )
            for nu in range(4)
        ]
        for mu in range(4)
    ], dtype=complex)


def _relative_difference(a: np.ndarray, b: np.ndarray) -> float:
    return float(
        np.linalg.norm(a-b)/max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    )


def _ward_scan(profile_rows: list[dict[str, float]]) -> list[dict]:
    records = []
    for index in PROFILE_INDICES:
        row = profile_rows[index]
        for target in SPECIES:
            mstar = row[f"mstar_{target}_MeV"]
            for qmag in Q_VALUES:
                for pabs in P_VALUES:
                    for cosine in COS_PQ_VALUES:
                        pz = pabs*cosine
                        px = pabs*math.sqrt(max(0.0, 1.0-cosine*cosine))
                        pvec = np.asarray([px, 0.0, pz])
                        ppvec = pvec+np.asarray([0.0, 0.0, qmag])
                        ei = math.sqrt(pabs*pabs+mstar*mstar)
                        ef = math.sqrt(float(ppvec@ppvec)+mstar*mstar)
                        q = np.asarray([ef-ei, 0.0, 0.0, qmag])
                        p = np.asarray([ei, *pvec])
                        pp = np.asarray([ef, *ppvec])
                        tensor = quasiparticle_tensor(p, pp, q, mstar, target)
                        hvv = tensor["H_VV"]
                        hva = tensor["H_VA"]
                        hav = tensor["H_AV"]
                        htotal = tensor["H_total"]
                        records.append({
                            "r_km": row["r_km"],
                            "species": target,
                            "mstar_MeV": mstar,
                            "q_MeV": qmag,
                            "p_MeV": pabs,
                            "cos_theta_pq": cosine,
                            "q0_MeV": float(q[0]),
                            "Q2_MeV2": tensor["Q2_MeV2"],
                            "ward_VV_first_index": ward_residual(hvv, tensor["q_cov"], first_index=True),
                            "ward_VA_vector_first_index": ward_residual(hva, tensor["q_cov"], first_index=True),
                            "ward_AV_vector_second_index": ward_residual(hav, tensor["q_cov"], first_index=False),
                            "hermiticity_VV": hermiticity_residual(hvv),
                            "hermiticity_AA": hermiticity_residual(tensor["H_AA"]),
                            "hermiticity_total": hermiticity_residual(htotal),
                            "decomposition_residual": _relative_difference(
                                htotal, hvv+tensor["H_AA"]+hva+hav
                            ),
                        })
    return records


def _vacuum_mass_recovery() -> list[dict]:
    records = []
    for target in SPECIES:
        m = MASS[target]
        for energy in (50.0, 100.0, 255.0, 500.0):
            for cosine in (-0.9, -0.5, 0.0, 0.5, 0.9):
                k, kp, p, pp, q, _, _, hvv_ref, haa_ref, hva_ref = kernel.tensors(
                    energy, cosine, target
                )
                current = quasiparticle_tensor(p, pp, q, m, target)
                records.append({
                    "species": target,
                    "E_MeV": energy,
                    "cos_theta": cosine,
                    "relative_HVV_difference": _relative_difference(
                        current["H_VV"], hvv_ref
                    ),
                    "relative_HAA_difference": _relative_difference(
                        current["H_AA"], haa_ref
                    ),
                    "relative_HVA_difference": _relative_difference(
                        current["H_VA"]+current["H_AV"], hva_ref
                    ),
                })
    return records


def _va_sign_check(profile_rows: list[dict[str, float]]) -> list[dict]:
    records = []
    energy, outgoing, qmag, q0 = 100.0, 95.0, 50.0, 5.0
    kz = (qmag*qmag+energy*energy-outgoing*outgoing)/(2.0*qmag)
    kx = math.sqrt(energy*energy-kz*kz)
    k = np.asarray([energy, kx, 0.0, kz])
    kp = np.asarray([outgoing, kx, 0.0, kz-qmag])
    q = k-kp
    for index in PROFILE_INDICES:
        row = profile_rows[index]
        for target in SPECIES:
            mstar = row[f"mstar_{target}_MeV"]
            pabs = 200.0
            ei = math.sqrt(pabs*pabs+mstar*mstar)
            cosine = (2.0*ei*q0+q0*q0-qmag*qmag)/(2.0*pabs*qmag)
            if abs(cosine) >= 1.0:
                raise ArithmeticError("chosen VA sign benchmark is outside nucleon phase space")
            px = pabs*math.sqrt(1.0-cosine*cosine)
            pvec = np.asarray([px, 0.0, pabs*cosine])
            ppvec = pvec+np.asarray([0.0, 0.0, qmag])
            ef = math.sqrt(float(ppvec@ppvec)+mstar*mstar)
            p = np.asarray([ei, *pvec])
            pp = np.asarray([ef, *ppvec])
            tensor = quasiparticle_tensor(p, pp, q, mstar, target)
            lnu = lepton_tensor(k, kp, False)
            lanti = lepton_tensor(k, kp, True)
            def contract(lepton, hadron):
                return float(np.sum(lepton*hadron).real)
            vv_nu, vv_anti = contract(lnu, tensor["H_VV"]), contract(lanti, tensor["H_VV"])
            aa_nu, aa_anti = contract(lnu, tensor["H_AA"]), contract(lanti, tensor["H_AA"])
            va_nu = contract(lnu, tensor["H_VA"]+tensor["H_AV"])
            va_anti = contract(lanti, tensor["H_VA"]+tensor["H_AV"])
            records.append({
                "r_km": row["r_km"],
                "species": target,
                "mstar_MeV": mstar,
                "VV_relative_neutrino_antineutrino_difference":
                    abs(vv_nu-vv_anti)/max(abs(vv_nu), abs(vv_anti), 1e-300),
                "AA_relative_neutrino_antineutrino_difference":
                    abs(aa_nu-aa_anti)/max(abs(aa_nu), abs(aa_anti), 1e-300),
                "VA_relative_sign_flip_residual":
                    abs(va_nu+va_anti)/max(abs(va_nu), abs(va_anti), 1e-300),
            })
    return records


def analyze(profile_rows: list[dict[str, float]]) -> tuple[list[dict], list[dict], dict]:
    if len(profile_rows) != 301:
        raise ValueError("C4-B1 requires the validated 301-point C1 profile")
    ward_records = _ward_scan(profile_rows)
    recovery_records = _vacuum_mass_recovery()
    va_records = _va_sign_check(profile_rows)
    max_ward = max(
        max(
            record["ward_VV_first_index"],
            record["ward_VA_vector_first_index"],
            record["ward_AV_vector_second_index"],
        )
        for record in ward_records
    )
    max_hermiticity = max(
        max(record["hermiticity_VV"], record["hermiticity_AA"], record["hermiticity_total"])
        for record in ward_records
    )
    max_recovery = max(
        value
        for record in recovery_records
        for key, value in record.items()
        if key.startswith("relative_")
    )
    max_va = max(
        max(
            record["VV_relative_neutrino_antineutrino_difference"],
            record["AA_relative_neutrino_antineutrino_difference"],
            record["VA_relative_sign_flip_residual"],
        )
        for record in va_records
    )
    acceptance = {
        "effective_mass_ward_scan_cases": len(ward_records) == 288,
        "vector_ward_residual_below_1e_10": max_ward < 1e-10,
        "hadronic_tensor_hermiticity_below_1e_10": max_hermiticity < 1e-10,
        "mstar_equals_M_recovers_existing_P1IIIb_below_1e_12": max_recovery < 1e-12,
        "neutrino_antineutrino_VA_sign_structure_below_1e_10": max_va < 1e-10,
        "tensor_decomposition_exact": all(
            record["decomposition_residual"] < 1e-14 for record in ward_records
        ),
    }
    summary = {
        "title": "P1-IIIe-C4B1 effective-mass quasiparticle weak tensor",
        "date": "2026-11-11",
        "status": "PASS: vector Ward identity, hermiticity, vacuum-mass recovery, and VA sign checks",
        "scope": (
            "Local on-shell quasiparticle tensor algebra at four selected SFHo-18.8 radii; "
            "no momentum-integrated collision kernel or opacity."
        ),
        "convention": {
            "quasiparticle_spinor_mass": "m*_N(r)",
            "quasiparticle_energy": "E*_p=sqrt(p^2+m*_N(r)^2)",
            "form_factor_mass": "physical vacuum M_N",
            "weak_magnetism_denominator": "2 M_N (physical vacuum mass)",
            "vertex": "F1(Q2) gamma^mu + i F2(Q2)/(2 M_N) sigma^{mu alpha} q_alpha - G_A(Q2) gamma^mu gamma^5",
            "trace": "H^{mu nu}=1/2 Tr[(slash p'*+m*) Gamma^mu (slash p*+m*) barGamma^nu]",
            "excluded": ["RPA", "NN correlations", "in-medium vertex corrections", "additional baryons"],
        },
        "provenance": {
            "selected_profile_indices_zero_based": list(PROFILE_INDICES),
            "selected_radii_km": [profile_rows[index]["r_km"] for index in PROFILE_INDICES],
            "ward_scan_cases": len(ward_records),
            "vacuum_mass_recovery_cases": len(recovery_records),
            "VA_sign_cases": len(va_records),
        },
        "maxima": {
            "vector_ward_residual": max_ward,
            "tensor_hermiticity_residual": max_hermiticity,
            "mstar_equals_M_component_recovery_residual": max_recovery,
            "neutrino_antineutrino_VA_sign_residual": max_va,
        },
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "The local quasiparticle spinors use m*_N, while vacuum nucleon form factors and the weak-magnetism normalization retain physical M_N.",
            "For equal initial/final m*_N, the vector Ward identity holds on shell with the bare vector vertex and Pauli term.",
            "The m*_N=M_N limit reproduces the existing P1-IIIb stationary tensor exactly.",
            "This defines a minimal local quasiparticle embedding; it is not a full in-medium weak vertex or RPA response.",
            "The tensor is not yet integrated over the local Fermi sea and does not yet produce an EOS-dependent collision rate.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-B1 acceptance failed: {acceptance}")
    return ward_records, recovery_records, summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-ward-csv", type=Path, required=True)
    parser.add_argument("--output-recovery-csv", type=Path, required=True)
    args = parser.parse_args()
    rows = load_profile(args.profile)
    ward, recovery, summary = analyze(rows)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )
    for path, records in (
        (args.output_ward_csv, ward),
        (args.output_recovery_csv, recovery),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not records:
            raise ValueError("cannot write empty C4-B1 output")
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = __import__("csv").DictWriter(
                stream, fieldnames=list(records[0]), lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(records)
    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "maxima": summary["maxima"],
        "acceptance": summary["acceptance"],
    }, indent=2))


if __name__ == "__main__":
    main()
