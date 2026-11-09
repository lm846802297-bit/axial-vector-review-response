#!/usr/bin/env python3
"""Exact-basis one-loop fermion contribution to the (h,s) self-energy matrix.

Original mu/tau plus VLL sector only. Convention:
Gamma_inv = p^2 I - M_loc^2 + Pi_RC; Plan-B Pi_B=-Pi_RC.
This is a fermion-sector subcalculation, not a complete scalar pole prediction.
"""
from __future__ import annotations
import json
from functools import lru_cache
from math import log, pi, sqrt
import numpy as np
from scipy.integrate import quad

MH=125.25
VH=246.22
ME=20_000.0
THETA_L=1.0e-2
MU_R=ME
LEPTONS={"mu":0.1056583755,"tau":1.77686}
BENCHMARKS=(("A_open_AA",70.886458,10.0),("B_closed_AA",315.0,63.0))
PAIRS=(("h","h"),("h","s"),("s","s"))

def a0bar(mass):
    return mass*mass*(1.0-log(mass*mass/(MU_R*MU_R))) if mass else 0.0

@lru_cache(maxsize=128)
def b0bar(p2,mi,mj):
    """Finite B0bar with +i*pi absorptive part above the two-fermion cut."""
    roots=[]
    if p2>0.0:
        disc=(mi*mi-mj*mj-p2)**2-4.0*p2*mj*mj
        if disc>=0.0:
            for z in np.roots([p2,mi*mi-mj*mj-p2,mj*mj]):
                if abs(z.imag)<1.0e-10 and 0.0<z.real<1.0:
                    roots.append(float(z.real))
    points=sorted([0.0,*roots,1.0])
    real_part=0.0
    negative_intervals=[]
    for lo,hi in zip(points[:-1],points[1:]):
        mid=0.5*(lo+hi)
        dmid=mid*mi*mi+(1.0-mid)*mj*mj-mid*(1.0-mid)*p2
        if dmid<0.0:
            negative_intervals.append((lo,hi))
        def integrate_segment(a,b,root_left=False,root_right=False):
            if root_left and root_right:
                midpoint=0.5*(a+b)
                return integrate_segment(a,midpoint,True,False)+integrate_segment(midpoint,b,False,True)
            if root_left or root_right:
                length=b-a
                def endpoint_integrand(t):
                    if t==0.0:
                        return 0.0
                    x=a+length*t*t if root_left else b-length*t*t
                    denominator=x*mi*mi+(1.0-x)*mj*mj-x*(1.0-x)*p2
                    return -log(abs(denominator)/(MU_R*MU_R))*2.0*length*t
                return quad(endpoint_integrand,0.0,1.0,epsabs=2e-10,epsrel=2e-10,limit=300)[0]
            def regular_integrand(x):
                denominator=x*mi*mi+(1.0-x)*mj*mj-x*(1.0-x)*p2
                return -log(abs(denominator)/(MU_R*MU_R))
            return quad(regular_integrand,a,b,epsabs=2e-10,epsrel=2e-10,limit=300)[0]
        root_left=any(abs(lo-root)<1e-9 for root in roots)
        root_right=any(abs(hi-root)<1e-9 for root in roots)
        real_part+=integrate_segment(lo,hi,root_left,root_right)
    imag_part=pi*sum(hi-lo for lo,hi in negative_intervals)
    return complex(real_part,imag_part)

@lru_cache(maxsize=16)
def mass_eigenstate_data(vs,ml):
    """Leading-seesaw benchmark inputs followed by exact SVD diagonalization."""
    theta_r=ml/(ME*THETA_L)
    y=sqrt(2.0)*ME*THETA_L/VH
    lam=sqrt(2.0)*ME*theta_r/vs
    mass_matrix=np.array([[0.0,y*VH/sqrt(2.0)],[lam*vs/sqrt(2.0),ME]])
    ul,masses,vh=np.linalg.svd(mass_matrix,full_matrices=False)
    ur=vh.T
    gamma_h=np.array([[0.0,y/sqrt(2.0)],[0.0,0.0]])
    gamma_s=np.array([[0.0,0.0],[lam/sqrt(2.0),0.0]])
    gh=ul.T@gamma_h@ur
    gs=ul.T@gamma_s@ur
    return masses,gh,gs

def one_flavor_entry(vs,ml,p2,a,b):
    """Return Pi_RC^F_ab and UV coefficients for one charged-lepton family."""
    masses,gh,gs=mass_eigenstate_data(vs,ml)
    ga=gh if a=="h" else gs
    gb=gh if b=="h" else gs
    total=0.0j
    uv_p2=0.0j
    uv_local=0.0j
    for i in range(2):
        for j in range(2):
            mi,mj=masses[i],masses[j]
            b0=b0bar(float(p2),float(mi),float(mj))
            cab=ga[i,j]*np.conj(gb[i,j])+np.conj(ga[j,i])*gb[j,i]
            dab=ga[i,j]*gb[j,i]+np.conj(ga[j,i])*np.conj(gb[i,j])
            kernel=a0bar(float(mi))+a0bar(float(mj))+(mi*mi+mj*mj-p2)*b0
            total+=cab*kernel+2.0*mi*mj*dab*b0
            uv_p2+=cab
            uv_local+=cab*2.0*(mi*mi+mj*mj)+2.0*mi*mj*dab
    return -total/(16.0*pi*pi),uv_p2,uv_local

def light_light_entry_plan_b(vs,ml,p2,a,b):
    """Exact light-light mass-eigenstate term in the Pi_B=-Pi_RC convention."""
    masses,gh,gs=mass_eigenstate_data(vs,ml)
    ga=gh if a=="h" else gs
    gb=gh if b=="h" else gs
    mass=float(masses[1])
    cab=ga[1,1]*np.conj(gb[1,1])+np.conj(ga[1,1])*gb[1,1]
    dab=ga[1,1]*gb[1,1]+np.conj(ga[1,1])*np.conj(gb[1,1])
    b0=b0bar(float(p2),mass,mass)
    kernel=2.0*a0bar(mass)+(2.0*mass*mass-p2)*b0
    return (cab*kernel+2.0*mass*mass*dab*b0)/(16.0*pi*pi)

def run_benchmark(label,vs,m_a):
    entries={}
    for a,b in PAIRS:
        full0=fullh=light0=lighth=0.0j
        uv_p2=uv_local=0.0j
        for ml in LEPTONS.values():
            p0,p2_coeff,local_coeff=one_flavor_entry(vs,ml,0.0,a,b)
            ph,_,_=one_flavor_entry(vs,ml,MH*MH,a,b)
            full0+=p0
            fullh+=ph
            uv_p2+=p2_coeff
            uv_local+=local_coeff
            light0+=light_light_entry_plan_b(vs,ml,0.0,a,b)
            lighth+=light_light_entry_plan_b(vs,ml,MH*MH,a,b)
        full_diff_plan_b=-(fullh-full0)
        light_diff_plan_b=lighth-light0
        hard_diff_plan_b=full_diff_plan_b-light_diff_plan_b
        entries[a+b]={
            "Pi_RC_mh2_GeV2":[float(fullh.real),float(fullh.imag)],
            "Pi_RC_0_GeV2":[float(full0.real),float(full0.imag)],
            "full_momentum_difference_PiB_GeV2":[float(full_diff_plan_b.real),float(full_diff_plan_b.imag)],
            "light_light_momentum_difference_PiB_GeV2":[float(light_diff_plan_b.real),float(light_diff_plan_b.imag)],
            "hard_momentum_difference_PiB_GeV2":[float(hard_diff_plan_b.real),float(hard_diff_plan_b.imag)],
            "UV_p2_coefficient_sum_C":[float(uv_p2.real),float(uv_p2.imag)],
            "UV_local_coefficient_sum":[float(uv_local.real),float(uv_local.imag)],
        }
    absorptive=np.array([
        [entries["hh"]["Pi_RC_mh2_GeV2"][1],entries["hs"]["Pi_RC_mh2_GeV2"][1]],
        [entries["hs"]["Pi_RC_mh2_GeV2"][1],entries["ss"]["Pi_RC_mh2_GeV2"][1]],
    ])
    eigenvalues=np.linalg.eigvalsh(absorptive)
    entries["absorptive_matrix_PiRC_GeV2"]=absorptive.tolist()
    entries["absorptive_eigenvalues_GeV2"]=eigenvalues.tolist()
    entries["absorptive_determinant_GeV4"]=float(np.linalg.det(absorptive))
    entries["absorptive_offdiagonal_saturation_ratio"]=float(absorptive[0,1]/sqrt(absorptive[0,0]*absorptive[1,1]))
    entries["benchmark"]={"name":label,"vs_GeV":vs,"mA_GeV":m_a,"gX":m_a/(2.0*vs),"ME_GeV":ME,"theta_mu_L":THETA_L,"theta_tau_L":THETA_L}
    expected={
        "A_open_AA":(0.11313331009059611,0.0240304439859),
        "B_closed_AA":(0.02545910994964451,0.00540772399471),
    }[label]
    assert abs(entries["hs"]["Pi_RC_mh2_GeV2"][1]-expected[0])<2e-10
    assert abs(entries["hs"]["hard_momentum_difference_PiB_GeV2"][0]-expected[1])<2e-9
    assert abs(entries["hs"]["UV_p2_coefficient_sum_C"][0])<1e-12
    assert abs(entries["hs"]["UV_local_coefficient_sum"][0])<1e-5
    for entry in ("hh","hs","ss"):
        assert abs(entries[entry]["hard_momentum_difference_PiB_GeV2"][1])<1e-9
    assert eigenvalues[0]>=-1e-10 and eigenvalues[1]>0.0
    assert abs(entries["absorptive_offdiagonal_saturation_ratio"]-1.0)<1e-8
    return entries

def main():
    output={
        "scope":"exact mass-eigenstate mu/tau plus VLL fermion-loop sector only",
        "convention":"Gamma_inv = p^2 I - M_loc^2 + Pi_RC; Pi_B=-Pi_RC",
        "renormalization_scale_GeV":MU_R,
        "external_momentum_GeV2":MH*MH,
        "benchmarks":{label:run_benchmark(label,vs,m_a) for label,vs,m_a in BENCHMARKS},
        "interpretation_limits":[
            "The diagonal entries require their own mass and wave-function counterterms; they are not physical pole shifts.",
            "Only mu, tau and their vector-like partners are included, not top, W, Z, A', Goldstone, ghost or scalar loops.",
            "The light-light absorptive matrix is a fermion-sector unitarity check, not the full Higgs or singlet width matrix.",
            "If these explicit mu/tau cuts are retained in a propagator, do not add their partial widths a second time through fixed diagonal widths.",
            "The hard momentum differences are finite fermion-sector matching subcalculations; complete same-order EFT soft terms and counterterms remain required.",
            "No complex poles, residues, detector observables, or allowed/excluded intervals are computed here."
        ]
    }
    print(json.dumps(output,indent=2))
    return output

if __name__=="__main__":
    main()
