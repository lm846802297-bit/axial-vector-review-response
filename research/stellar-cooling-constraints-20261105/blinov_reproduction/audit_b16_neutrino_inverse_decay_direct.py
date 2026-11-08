"""Independent direct phase-space audit of B.4, B.6--B.10 and B.19.

The production/reference implementation uses a closed-form Fermi-pair
antiderivative and, separately, a 48-point mode-resolved angular quadrature.
This audit evaluates the neutrino inverse-decay collision integrals directly
with a higher-order Gauss-Legendre rule. It checks production, blocking,
detailed balance, the reduced opacity, and each vector polarization.

Only neutrino inverse decay is included. No source, coupling, opacity, or
luminosity rescaling is applied.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import sys
from scipy.special import expit
from numpy.polynomial.legendre import leggauss

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    from .reference import DEFAULT_PROFILE, fermi_pair_average
    import rates as production_rates
except ImportError:
    from reference import DEFAULT_PROFILE, fermi_pair_average
    import rates as production_rates

HERE=Path(__file__).resolve().parent
DEFAULT_OUTPUT=HERE/"outputs"/"b16_neutrino_inverse_decay_direct_10mev_2026-11-08.json"
MASS=10.0
POLARIZATION_LABELS=("L","+","-")
SAMPLE_RADII=(8.0,10.0,12.0,15.0,18.5,20.0,22.0,23.0,24.0,25.0)
SAMPLE_ENERGIES=(12.0,15.0,20.0,30.0,50.0,100.0,300.0)

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def direct_flavour_integrals(mass,omega,T,mu,order=512):
    """Direct z-integrals for one flavor, each fixed vector polarization."""
    z,w=leggauss(order)
    v=np.sqrt(max(1.0-(mass/omega)**2,0.0))
    e1=omega*(1.0+v*z)/2.0
    e2=omega*(1.0-v*z)/2.0
    f1=expit((mu-e1)/T)
    f2=expit((-mu-e2)/T)
    prod=f1*f2
    blocking=(1.0-f1)*(1.0-f2)
    W=np.stack((3.0*(1.0-z*z)/4.0,
                3.0*(1.0+z)**2/8.0,
                3.0*(1.0-z)**2/8.0),axis=-1)
    pref=mass*mass/(24.0*np.pi*omega)
    p=pref*np.einsum("z,zh->h",w*prod,W)
    a=pref*np.einsum("z,zh->h",w*blocking,W)
    return p,a

def direct_uniform_I(mass,omega,T,mu,order=512):
    z,w=leggauss(order)
    v=np.sqrt(max(1.0-(mass/omega)**2,0.0))
    e1=omega*(1.0+v*z)/2.0
    e2=omega*(1.0-v*z)/2.0
    pair=expit((mu-e1)/T)*expit((-mu-e2)/T)
    return float(0.5*np.dot(w,pair))

def relative(a,b):
    return abs(a-b)/max(abs(b),1e-300)

def run(profile_path=DEFAULT_PROFILE,mass=MASS,orders=(128,256,512)):
    profile=np.genfromtxt(profile_path,delimiter=",",names=True)
    radii=np.asarray(SAMPLE_RADII,float)
    Tvals=np.interp(radii,profile["r_km"],profile["T_MeV"])
    muvals=np.interp(radii,profile["r_km"],profile["mu_numu_MeV"])
    rows=[]
    maxima={
        "mode_production_vs_direct":0.0,
        "mode_absorption_vs_direct":0.0,
        "b19_ratio_residual":0.0,
        "b4_reduced_opacity_residual":0.0,
        "analytic_I_vs_direct":0.0,
        "mode_sum_vs_scalar_I":0.0,
        "quadrature_256_vs_512":0.0,
    }
    quadrature_convergence=[]
    for r,T,mu in zip(radii,Tvals,muvals):
        for omega in SAMPLE_ENERGIES:
            if omega<=mass: continue
            # Independent high-order direct phase-space result per flavor.
            p_mu,a_mu=direct_flavour_integrals(mass,omega,T,mu,512)
            p_tau,a_tau=direct_flavour_integrals(mass,omega,T,0.0,512)
            p_direct=p_mu+p_tau
            a_direct=a_mu+a_tau
            # Existing mode-resolved implementation, deliberately called at
            # its normal 48-point order, not reused for the direct result.
            p_code,a_code=production_rates.neutrino_rates(
                mass,omega,T,mu,order=48
            )
            p_code=np.asarray(p_code,float)
            a_code=np.asarray(a_code,float)
            # Existing scalar closed-form I, independently compared with the
            # uniform angular integral and with the polarization sum.
            I_direct=direct_uniform_I(mass,omega,T,mu,512)+direct_uniform_I(mass,omega,T,0.0,512)
            I_analytic=float(fermi_pair_average(mu,omega,T,np.sqrt(1-(mass/omega)**2))
                             +fermi_pair_average(0.0,omega,T,np.sqrt(1-(mass/omega)**2)))
            scalar_from_I=mass*mass/(8.0*np.pi*omega)*I_analytic
            scalar_from_modes=float(np.sum(p_code))
            prod_err=max(relative(p_code[i],p_direct[i]) for i in range(3))
            abs_err=max(relative(a_code[i],a_direct[i]) for i in range(3))
            b19=np.max(np.abs(p_direct-np.exp(-omega/T)*a_direct)
                       /np.maximum(np.abs(p_direct),1e-300))
            reduced_direct=(1.0-np.exp(-omega/T))*a_direct
            reduced_from_prod=(np.exp(omega/T)-1.0)*p_direct
            b4=np.max(np.abs(reduced_direct-reduced_from_prod)
                      /np.maximum(np.abs(reduced_direct),1e-300))
            ierr=relative(I_analytic,I_direct)
            sumerr=relative(scalar_from_modes,scalar_from_I)
            # Explicitly compare direct angular quadrature orders.
            p256,_=direct_flavour_integrals(mass,omega,T,mu,256)
            pt256,_=direct_flavour_integrals(mass,omega,T,0.0,256)
            qerr=max(relative(p256[i]+pt256[i],p_direct[i]) for i in range(3))
            for key,val in (
                ("mode_production_vs_direct",prod_err),
                ("mode_absorption_vs_direct",abs_err),
                ("b19_ratio_residual",float(b19)),
                ("b4_reduced_opacity_residual",float(b4)),
                ("analytic_I_vs_direct",ierr),
                ("mode_sum_vs_scalar_I",sumerr),
                ("quadrature_256_vs_512",qerr),
            ):
                maxima[key]=max(maxima[key],float(val))
            rows.append({
                "r_km":float(r),"T_MeV":float(T),"mu_numu_MeV":float(mu),
                "omega_MeV":float(omega),"omega_over_T":float(omega/T),
                "direct_nu_mu_prod_modes":p_mu.tolist(),
                "direct_nu_tau_prod_modes":p_tau.tolist(),
                "direct_total_prod_modes":p_direct.tolist(),
                "direct_total_abs_modes":a_direct.tolist(),
                "code_48point_prod_modes":p_code.tolist(),
                "code_48point_abs_modes":a_code.tolist(),
                "relative_error_prod_max_over_modes":float(prod_err),
                "relative_error_abs_max_over_modes":float(abs_err),
                "B19_detailed_balance_max_relative_residual":float(b19),
                "B4_reduced_opacity_max_relative_residual":float(b4),
                "analytic_I_vs_direct_uniform_angular_average":float(ierr),
                "mode_sum_vs_scalar_I_relative_residual":float(sumerr),
                "256_vs_512_direct_quadrature_max_relative_change":float(qerr),
                "per_mode_prod_over_abs":(p_direct/a_direct).tolist(),
                "expected_prod_over_abs":float(np.exp(-omega/T)),
                "reduced_absorption_modes":reduced_direct.tolist(),
            })
    # Sign reversal must leave the unpolarized neutrino-pair integral unchanged;
    # it swaps the two circular helicity labels.
    sign_rows=[]
    for r,T,mu in zip(radii,Tvals,muvals):
        for omega in (15.0,30.0,100.0):
            pp,_=direct_flavour_integrals(mass,omega,T,mu,512)
            pm,_=direct_flavour_integrals(mass,omega,T,-mu,512)
            sign_rows.append({
                "r_km":float(r),"omega_MeV":omega,
                "longitudinal_relative_change":relative(pp[0],pm[0]),
                "plus_minus_swapped_relative_change":max(relative(pp[1],pm[2]),relative(pp[2],pm[1])),
                "unpolarized_sum_relative_change":relative(np.sum(pp),np.sum(pm)),
            })
    max_sign=max(max(x["longitudinal_relative_change"],x["plus_minus_swapped_relative_change"],
                     x["unpolarized_sum_relative_change"]) for x in sign_rows)
    return {
        "title":"Direct phase-space audit of neutrino inverse decay at mV=10 MeV",
        "mass_MeV":mass,
        "profile":{"path":str(profile_path),"sha256":sha256(profile_path),
                   "identity":"reconstructed public-figure SFHo-18.8 profile, not raw Garching simulation data"},
        "configuration":{"direct_gauss_legendre_order":512,
                         "crosscheck_order":256,
                         "production_implementation_order":48,
                         "radii_km":list(SAMPLE_RADII),
                         "energies_MeV":list(SAMPLE_ENERGIES)},
        "equation_map":{
            "B.4":"Gamma_abs_star=(1-exp(-omega/T))*Gamma_abs",
            "B.6":"three mode angular weights W_L=3(1-z^2)/4, W_+=3(1+z)^2/8, W_-=3(1-z)^2/8",
            "B.7_to_B.10":"mode-resolved inverse neutrino decay production and blocking rates",
            "B.19":"Gamma_prod=exp(-omega/T)*Gamma_abs for each flavor and each vector polarization",
            "fixed_omega":"omega is held fixed along the path; T and mu_nu are local functions of r prime",
        },
        "maximum_residuals":maxima,
        "maximum_mu_sign_and_helicity_swap_residual":float(max_sign),
        "mu_sign_helicity_swap_checks":sign_rows,
        "pointwise_samples":rows,
        "scope":[
            "Independent direct angular phase-space integration; does not use the analytic antiderivative for its reference values.",
            "Checks each active flavor and each vector polarization.",
            "Compares the direct 512-point result to the existing 48-point mode-resolved code.",
            "Tests detailed balance and B.4 reduced opacity without fitting or rescaling.",
            "The outer profile is a public-figure reconstruction, not original Garching raw data.",
        ],
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    p.add_argument("--mass",type=float,default=MASS)
    a=p.parse_args()
    d=run(a.profile,a.mass)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"configuration":d["configuration"],"maximum_residuals":d["maximum_residuals"],
                      "maximum_mu_sign_and_helicity_swap_residual":d["maximum_mu_sign_and_helicity_swap_residual"]},indent=2))
    print(f"Saved {a.output}")

if __name__=="__main__":
    main()
