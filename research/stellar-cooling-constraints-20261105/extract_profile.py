"""Reconstruct public SFHo-18.8 figure curves, not original simulation tables.

Run with --source-dir containing SNProfile.pdf (2109.03244v3, figures/)
and SNModelComparison.pdf (2510.14469v1, figures/).
Use --download to fetch the public arXiv source archives into ignored latex-build.
Only numerical derivatives of plotted curves are committed; source PDFs are not
redistributed. Mapping is fixed to PDF drawing paths and tick coordinates.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import tarfile
import urllib.request
import numpy as np
import pymupdf
from scipy.integrate import quad
from scipy.special import expit

HERE = Path(__file__).resolve().parent
SOURCES = {
    "SNProfile.pdf": ("https://arxiv.org/src/2109.03244v3", "figures/SNProfile.pdf"),
    "SNModelComparison.pdf": ("https://arxiv.org/src/2510.14469v1", "figures/SNModelComparison.pdf"),
}
EXPECTED_SHA256 = {
    "SNProfile.pdf": "19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e",
    "SNModelComparison.pdf": "5cc8b07dad824b65391fae6229bb9eca138c1cf5ff0348c8aaf712779a2566f2",
}

def vertices(page, index):
    drawing = page.get_drawings()[index]
    points = []
    for item in drawing["items"]:
        if item[0] != "l":
            raise ValueError("Expected polyline; PDF source version changed")
        points.extend([tuple(item[1]), tuple(item[2])])
    points = np.asarray(points)
    order = np.argsort(points[:, 0], kind="stable")
    points = points[order]
    _, keep = np.unique(points[:, 0], return_index=True)
    return points[keep]

def caputo_curve(page, index, density=False):
    p = vertices(page, index)
    if density:
        r = (p[:, 0] - 47.52) * 20 / (324 - 47.52)
        y = 10**(-4 + (442.918 - p[:, 1]) / 41.4718)
    else:
        # Top panel starts at r=0.1 km; lower-panel x-axis starts at r=0.
        r = 0.1 + (p[:, 0] - 47.52) * 19.9 / (324 - 47.52)
        y = 10**((215.559 - p[:, 1]) / ((215.559-56.180)/2))
    return np.column_stack([r, y])

def ferreira_curve(page, index, quantity):
    p = vertices(page, index)
    x0 = 62.590 if quantity == "T" else 378.199
    r = (p[:, 0] - x0) * 20 / (321.938-x0 if quantity == "T" else 637.547-x0)
    if quantity == "T":
        y = 10 + (146.886-p[:, 1])*50/(146.886-15.543)
    elif quantity == "mu_mu":
        y = 50 + (300.168-p[:, 1])*250/(300.168-183.070)
    elif quantity == "lapse":
        y = .6 + (480.465-p[:, 1])*.3/(480.465-341.598)
    else:
        raise ValueError(quantity)
    return np.column_stack([r, y])

def interp(curve, r, right=None):
    return np.interp(r, curve[:, 0], curve[:, 1], right=right)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=HERE/"latex-build"/"sources")
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    args.source_dir.mkdir(parents=True, exist_ok=True)
    if args.download:
        for filename, (url, member) in SOURCES.items():
            archive = args.source_dir/(filename+".tar.gz")
            urllib.request.urlretrieve(url, archive)
            with tarfile.open(archive) as tar:
                (args.source_dir/filename).write_bytes(tar.extractfile(member).read())
    for name in SOURCES:
        actual = hashlib.sha256((args.source_dir/name).read_bytes()).hexdigest()
        if actual != EXPECTED_SHA256[name]:
            raise ValueError(f"Source PDF changed: {name}, SHA256={actual}")
    docs = {name:pymupdf.open(args.source_dir/name) for name in SOURCES}
    cap, fer = docs["SNProfile.pdf"][0], docs["SNModelComparison.pdf"][0]
    curves = {
        "T_caputo":caputo_curve(cap,0),
        "mu_mu_caputo":caputo_curve(cap,1),
        "minus_mu_numu_caputo":caputo_curve(cap,6),
        "plus_mu_numu_caputo":caputo_curve(cap,7),
        "n_mu_over_n0_caputo":caputo_curve(cap,161,True),
        "T_ferreira":ferreira_curve(fer,1,"T"),
        "mu_mu_ferreira":ferreira_curve(fer,394,"mu_mu"),
        "lapse_ferreira":ferreira_curve(fer,610,"lapse"),
    }
    out = HERE/"data"
    out.mkdir(exist_ok=True)
    for key, curve in curves.items():
        np.savetxt(out/(key+"_vertices.csv"),curve,delimiter=",",header="r_km,value",comments="",fmt="%.15g")
    base_r=np.linspace(0,25,501)
    # Preserve exact source-curve endpoints. In particular, the negative
    # muon-neutrino branch ends at 13.1099 km and is set to zero immediately
    # outside its plotted range. A 0.05 km-only grid would smear that cutoff
    # over the whole 13.10--13.15 km cell when downstream code uses np.interp.
    profile_knots = []
    for key in (
        "T_caputo", "mu_mu_caputo", "minus_mu_numu_caputo",
        "plus_mu_numu_caputo", "T_ferreira", "mu_mu_ferreira",
        "lapse_ferreira",
    ):
        # Retain every PDF polyline vertex, not just endpoints. This makes
        # interpolation of the CSV reproduce the digitized piecewise-linear
        # source curves exactly, including the final steep neutrino segment.
        profile_knots.extend(curves[key][:, 0])
    # Represent the adopted zero-outside-support convention with a near-step
    # rather than allowing np.interp to taper a branch over the next 0.05 km cell.
    support_epsilon_km = 1.0e-6
    profile_knots.extend([
        curves["minus_mu_numu_caputo"][-1, 0] + support_epsilon_km,
        curves["plus_mu_numu_caputo"][0, 0] - support_epsilon_km,
        curves["plus_mu_numu_caputo"][-1, 0] + support_epsilon_km,
        curves["mu_mu_caputo"][-1, 0] + support_epsilon_km,
    ])
    profile_knots = np.asarray(profile_knots, dtype=float)
    profile_knots = profile_knots[(profile_knots >= 0.0) & (profile_knots <= 25.0)]
    r=np.unique(np.r_[base_r, profile_knots])
    temp=interp(curves["T_caputo"],r)
    mu=interp(curves["mu_mu_caputo"],r,right=0.)
    numu=np.zeros_like(r)
    for key,sign in [("minus_mu_numu_caputo",-1),("plus_mu_numu_caputo",1)]:
        c=curves[key]
        selected=(r<=c[-1,0])
        if sign>0:
            selected &= r>=c[0,0]
        numu[selected]=sign*interp(c,r[selected])
    lc=curves["lapse_ferreira"]
    lapse=interp(lc,r)
    outside=r>lc[-1,0]
    # Match the exterior 1-2GM/r form continuously to the plotted lapse at rmax.
    schwarzschild_radius=lc[-1,0]*(1-lc[-1,1]**2)
    lapse[outside]=np.sqrt(1-schwarzschild_radius/r[outside])
    fer_temp=interp(curves["T_ferreira"],r,right=float("nan"))
    fer_mu=interp(curves["mu_mu_ferreira"],r,right=float("nan"))
    rows=np.column_stack([r,temp,mu,numu,lapse,fer_temp,fer_mu])
    header="r_km,T_MeV,mu_mu_MeV,mu_numu_MeV,lapse,T_Ferreira_MeV,mu_mu_Ferreira_MeV"
    np.savetxt(out/"sfho188_digitized.csv",rows,delimiter=",",header=header,comments="",fmt="%.15g")
    samples=[]
    for rr in [0,5,8,10,15,20,24,25]:
        tt=float(interp(curves["T_caputo"],rr))
        mm=float(interp(curves["mu_mu_caputo"],rr,right=0.))
        nfm=quad(lambda p:p*p*expit(-(np.sqrt(p*p+105.6583755**2)-mm)/tt),0,np.inf)[0]/np.pi**2/197.3269804**3
        nplot=float(interp(curves["n_mu_over_n0_caputo"],rr,right=float("nan")))*.181
        samples.append(dict(r_km=rr,T_MeV=tt,mu_mu_MeV=mm,
                            mu_mu_Ferreira_MeV=float(interp(curves["mu_mu_ferreira"],rr,right=float("nan"))),
                            n_mu_Fermi_fm3=nfm,n_mu_plotted_fm3=nplot,
                            lapse=float(np.interp(rr,r,lapse))))
    overlap=np.linspace(.2,20,400)
    t1=interp(curves["T_caputo"],overlap)
    t2=interp(curves["T_ferreira"],overlap)
    record={
        "generated_date":"2026-11-06",
        "identity":"Reconstructed SFHo-18.8, t_pb=1 s benchmark; not raw simulation data",
        "sources":{name:dict(arxiv_source_url=SOURCES[name][0],archive_member=SOURCES[name][1],
                             pdf_sha256=hashlib.sha256((args.source_dir/name).read_bytes()).hexdigest())
                   for name in SOURCES},
        "curve_path_indices":{"caputo":{"T":0,"mu_mu":1,"negative_mu_numu":6,"positive_mu_numu":7,"n_mu_over_n0":161},
                              "ferreira":{"T":1,"mu_mu":394,"lapse":610}},
        "curve_ranges":{key:[float(curve[0,0]),float(curve[-1,0])] for key,curve in curves.items()},
        "temperature_overlap_max_relative_difference":float(np.max(abs(t1-t2)/t1)),
        "lapse_exterior_continuation_schwarzschild_radius_km":float(schwarzschild_radius),
        "profile_grid": {
            "base_uniform_points": 501,
            "base_spacing_km": 0.05,
            "support_boundary_epsilon_km": 1.0e-6,
            "all_input_pdf_vertices_retained": True,
            "number_of_extra_source_vertices_and_support_knots": int(len(profile_knots)),
            "extra_source_knot_count_semantics": "Raw PDF vertices and support knots before union-grid deduplication; unique final added rows are recorded separately.",
            "final_csv_rows": int(len(r)),
            "unique_added_source_vertices_and_support_knots": int(len(r) - len(base_r)),
            "outer_shell_nodes_22_25_km": int(np.count_nonzero((r >= 22.0) & (r <= 25.0))),
            "outer_shell_base_grid_nodes_22_25_km": int(np.count_nonzero((base_r >= 22.0) & (base_r <= 25.0))),
            "outer_shell_additional_source_nodes_22_25_km": int(
                np.count_nonzero((r >= 22.0) & (r <= 25.0))
                - np.count_nonzero((base_r >= 22.0) & (base_r <= 25.0))
            ),
            "outer_shell_min_spacing_km": float(np.min(np.diff(r[(r >= 22.0) & (r <= 25.0)]))),
            "outer_shell_max_spacing_km": float(np.max(np.diff(r[(r >= 22.0) & (r <= 25.0)]))),
            "exact_source_knots_km": sorted(float(x) for x in profile_knots),
        },
        "assumptions":[
            "Caputo top-panel x axis is [0.1,20] km; bottom-panel x axis [0,20] km. Curves encode public PDF vertices beyond clipping frame.",
            "T used through25km from encoded public Caputo path, including off-frame vertices. No temperature tail fitted.",
            "mu_mu set0 beyond final encoded point where plotted value drops below1MeV; no effect expected on muon density in cold tail.",
            "mu_numu set0 in intervals not represented by the |mu_numu|>=1MeV logarithmic plot; use zero-chemical-potential sensitivity check.",
            "First available core point extended constantly to r=0 (first original plotted point at about0.116km).",
            "The CSV retains the 501-point 0.05 km base grid and every input PDF polyline vertex within 0--25 km. A 1e-6 km near-step preserves the adopted zero-outside-support convention for the muon-neutrino branches and the muon chemical-potential tail, rather than smearing their cutoffs across a full grid cell.",
            "Lapse uses Ferreira SFHo18.8 orange curve through24km, then matched exterior Schwarzschild form through25km.",
            "Ferreira mu_mu curve disagrees strongly with Caputo despite same profile label. It is retained only as diagnostic, not silently mixed into baseline.",
            "No permission-restricted Garching raw tables were accessed or redistributed.",
        ],
        "samples":samples,
    }
    # JSON null for diagnostics outside plotted ranges.
    def clean(obj):
        if isinstance(obj,float) and not np.isfinite(obj): return None
        if isinstance(obj,dict): return {k:clean(v) for k,v in obj.items()}
        if isinstance(obj,list): return [clean(v) for v in obj]
        return obj
    (out/"profile_provenance.json").write_text(json.dumps(clean(record),indent=2)+"\n",encoding="utf-8")
    assert np.all(np.diff(r)>0) and np.all(temp>0)
    assert np.all((lapse>0)&(lapse<1))
    assert all(len(c)>30 for c in curves.values())
    print(json.dumps(clean({"samples":samples,"temperature_overlap_max_relative_difference":record["temperature_overlap_max_relative_difference"]}),indent=2))
    print("Saved",out/"sfho188_digitized.csv")

if __name__=="__main__":
    main()
