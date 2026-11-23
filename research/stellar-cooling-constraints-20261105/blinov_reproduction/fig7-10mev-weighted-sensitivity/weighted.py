"""Literal Fig. 7 B.1/B.2 channel tangent sensitivities, not a model fit."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import scipy

from inputs.reference import radial_rule, load_profile, local_rates, scalar_optical_depths
from inputs.audit_b16_global_redshift import eq_b1_source_measure, float_array_sha256

HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
CHANNELS = ("neutrino", "semi_compton")
NATIVE_KEYS = {"neutrino": "neutrino_production", "semi_compton": "compton_production"}


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(name):
    return json.loads((INPUTS / name).read_text(encoding="utf-8"))


def recovered_energy_grid(spectral, mass, max_energy):
    lo = np.full_like(spectral, float(mass))
    hi = np.full_like(spectral, max_energy + 1.0)
    for _ in range(100):
        energy = (lo + hi) / 2
        current = energy ** 2 * np.sqrt((energy - mass) * (energy + mass)) / (2*np.pi**2)
        smaller = current < spectral
        lo = np.where(smaller, energy, lo)
        hi = np.where(smaller, hi, energy)
    return (lo + hi) / 2


def tangents(sources, columns, angle_weights, g):
    """Sources per g² at (r,E); columns per g² at (r,cosine,E)."""
    tau = {name: g*g * columns[name] for name in CHANNELS}
    source_angle = {name: sources[name][:, None, :] * angle_weights[None,:,None]
                    for name in CHANNELS}
    total_tau = sum(tau.values())
    survival = np.exp(-total_tau)
    total_source_angle = sum(source_angle.values())
    escaped = total_source_angle * survival
    z = float(escaped.sum())
    thin = float(total_source_angle.sum())
    response = {}
    for name in CHANNELS:
        source_only = float(np.sum(source_angle[name]*survival)/z)
        opacity_only = -float(np.sum(escaped*tau[name])/z)
        response[name] = {
            "thin_source_fraction": float(source_angle[name].sum()/thin),
            "source_only_dlnL_dln_channel_rate": source_only,
            "opacity_only_dlnL_dln_channel_rate": opacity_only,
            "same_channel_source_opacity_matched_dlnL_dln_channel_rate": (
                source_only + opacity_only),
        }
    tau_mean = float(np.sum(escaped * total_tau)/z)
    return {
        "luminosity_erg_s": g*g*z,
        "thin_luminosity_erg_s": g*g*thin,
        "escape_probability": z/thin,
        "escape_weighted_mean_tau": tau_mean,
        "escape_weighted_tau_variance": float(np.sum(escaped*(total_tau-tau_mean)**2)/z),
        "dlnL_dlng": 2*(1-tau_mean),
        "channel_tangents": response,
    }


def run():
    archive = read_json("high_order.json")
    result = archive["result"]
    shape = read_json("fig7-shape-native.json")
    profile = INPUTS / "sfho188_digitized.csv"
    assert file_sha(profile) == archive["profile_sha256"] == shape["baseline_profile_sha256"]
    assert file_sha(INPUTS / "reference.py") == result["code_sha256"]["reference_script"]
    q = archive["quadratures"]
    m, radius = result["mass_MeV"], q["radius_km"]
    r, rw = radial_rule(radius, q["source_radial_order"])
    path_r, _ = radial_rule(radius, q["opacity_order"])
    path_r = np.unique(np.r_[0., path_r, radius])
    sp = load_profile(profile, r)
    op = load_profile(profile, path_r)
    e = np.unique(np.r_[m+np.geomspace(max(m*1.e-6,1.e-6), q["energy_offset_MeV"],
                                        q["base_energy_order"]), m/op["lapse"]])
    e = e[e > m*(1.+1.e-10)]
    ids = archive["grid_identity"]
    assert float_array_sha256(r) == ids["source_grid_sha256"]
    assert float_array_sha256(path_r) == ids["opacity_grid_sha256"]
    assert len(e) == ids["energy_node_count"]
    e_recovered = recovered_energy_grid(np.asarray(result["eq_b1_source_measure"][
        "spectral_measure_MeV3"]), m, m+q["energy_offset_MeV"])
    assert np.allclose(e, e_recovered, rtol=5.e-14, atol=1.e-13)
    def rates(p):
        return local_rates(m, e[None,:], p["T"][:,None], p["mu_numu"][:,None], p["mu_mu"][:,None])
    src_rates, op_rates = rates(sp), rates(op)
    assert not np.any(src_rates["dimuon_production"]) and not np.any(op_rates["dimuon_production"])
    x = e[None,:]/op["T"][:,None]
    balance = -np.expm1(-x)*np.exp(np.minimum(x,700.))
    def cols(reduced):
        return scalar_optical_depths(r, path_r, reduced, m, e, radius, q["angular_order"],
                                     q["path_order"])
    C, a = cols(op_rates["reduced_absorption"])
    J, _ = eq_b1_source_measure(r,rw,e,sp["lapse"],m,src_rates["production"])
    columns, sources = {}, {}
    for name, key in NATIVE_KEYS.items():
        sources[name], _ = eq_b1_source_measure(r,rw,e,sp["lapse"],m,src_rates[key])
        columns[name], a_ch = cols(balance*op_rates[key])
        assert np.array_equal(a_ch,a)
    c_closure = float(np.max(np.abs(sum(columns.values())-C)/np.maximum(C, 1e-300)))
    j_closure = float(np.max(np.abs(sum(sources.values())-J)/np.maximum(J, 1e-300)))
    assert c_closure<1e-12 and j_closure<1e-12
    del C, J
    assert all(np.all(np.isfinite(c) & (c>=0.)) for c in columns.values())
    assert all(np.all(np.isfinite(s) & (s>=0.)) for s in sources.values())
    native = result["eq_b2_fixed_omega_baseline"]["points"]
    assert len(native) == len(shape["aligned_vertices"]) == 25
    points = []
    matched_closure = 0.
    for v, w in zip(native,shape["aligned_vertices"]):
        g = v["g"]
        assert g == w["g"]
        assert v["reference_luminosity_erg_s"] == w["luminosity_erg_s"]["ref"]
        assert v["calculated_luminosity_erg_s"] == w["luminosity_erg_s"]["fixed"]
        row = tangents(sources, columns, a, g)
        error_L = row["luminosity_erg_s"]/v["calculated_luminosity_erg_s"]-1.
        error_thin = row["thin_luminosity_erg_s"]/v["optically_thin_luminosity_erg_s"]-1.
        assert abs(error_L)<2e-10 and abs(error_thin)<2e-10
        match_sum = sum(vals["same_channel_source_opacity_matched_dlnL_dln_channel_rate"]
                        for vals in row["channel_tangents"].values())
        matched_closure = max(matched_closure, abs(match_sum-row["dlnL_dlng"]/2.))
        row.update(g=g, x=w["g_squared_normalized"], baseline_li_relative_residual=error_L,
                   baseline_thin_relative_residual=error_thin,
                   digitized_fig7_luminosity_erg_s=v["reference_luminosity_erg_s"])
        points.append(row)
    assert matched_closure < 2e-13
    # d(-ln Q)/dx = <g_*²*column> = <tau(g)>/x. Convexity brackets each secant.
    slopes = np.array([row["escape_weighted_mean_tau"]/row["x"] for row in points])
    x_grid = np.array([row["x"] for row in points])
    q_grid = np.array([row["luminosity_erg_s"]/row["g"]**2 for row in points])
    secants = -np.diff(np.log(q_grid))/np.diff(x_grid)
    shape_secants = np.asarray(shape["shape_all_vertices"]["fixed"]["negative_log_secants"])
    assert len(shape_secants) == len(secants) == 24
    secant_error = float(np.max(np.abs(secants-shape_secants)))
    assert secant_error < 5.e-10
    lower = slopes[1:]
    upper = slopes[:-1]
    slack = float(min(np.min(secants-lower), np.min(upper-secants)))
    assert slack > -2e-10
    marked = [0, int(np.argmax([p["digitized_fig7_luminosity_erg_s"] for p in points])), len(points)-1]
    return {
        "scope": "Pure-vector 10 MeV literal B.1/B.2, fixed omega, Euclidean chords, reconstructed profile; not Croon, #123 C1, full GR, or a constraint.",
        "method": "First derivatives at unmodified rates. No finite rate scaling, calibration, or model fit.",
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "quadrature": q, "input_sha256": {p.name:file_sha(p) for p in sorted(INPUTS.iterdir()) if p.is_file()},
        "numerical_checks": {
            "source_and_opacity_grid_sha256_exact": True,
            "energy_grid_sha256_match": float_array_sha256(e) == ids["energy_grid_sha256"],
            "energy_grid_current_sha256": float_array_sha256(e),
            "energy_grid_max_abs_delta_mev_vs_inverted_native_spectral_measure": float(np.max(np.abs(e-e_recovered))),
            "maximum_source_channel_closure_relative": j_closure,
            "maximum_column_channel_closure_relative": c_closure,
            "maximum_luminosity_closure_relative": max(abs(p["baseline_li_relative_residual"]) for p in points),
            "maximum_thin_closure_relative": max(abs(p["baseline_thin_relative_residual"]) for p in points),
            "maximum_matched_channel_sum_vs_half_coupling_derivative": matched_closure,
            "minimum_secant_bracket_slack": slack,
            "maximum_secant_absolute_difference_vs_pr121_native": secant_error,
            "negative_log_secants": secants.tolist(),
            "negative_log_derivatives_endpoints": slopes.tolist(),
        },
        "weak_peak_strong_indices": marked, "points": points,
    }


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    output=parser.parse_args().output
    output.write_text(json.dumps(run(),indent=2,sort_keys=True, allow_nan=False)+"\n")
