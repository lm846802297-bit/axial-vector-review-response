"""Leading tree-level s -> A' f fbar cascade below the on-shell A'A' threshold.

The function treats one A' as on shell and the second A' as virtual. It uses
massless left-handed nu_mu/nu_tau currents and the original mass-basis charged-
lepton A' couplings (dominantly axial, with the small vector admixture fixed by
theta_R). It is defined only for m_s/2 <= m_A' < m_s. The two-virtual-vector
four-body region m_A' >= m_s is not included.

This is a leading tree-level calculation in unitary gauge with a running A'
width in the virtual propagator. It is not a detector-level recast.
"""
from __future__ import annotations
import math
from functools import lru_cache
import numpy as np
from radial_scalar_widths import M_MU_GEV, M_TAU_GEV


@lru_cache(maxsize=8)
def _legendre_rule(order: int):
    nodes, weights = np.polynomial.legendre.leggauss(order)
    return nodes, weights


def aprime_running_width(q2: np.ndarray, gX: float,
                         theta_mu_R: float = 1.0e-2,
                         theta_tau_R: float = 1.0e-2) -> np.ndarray:
    """Running A' width to two massless Weyl neutrinos and axial/vector mu,tau."""
    q2=np.asarray(q2,dtype=float)
    q=np.sqrt(q2)
    total_factor=np.ones_like(q2)  # nu_mu + nu_tau, each one Weyl species
    for mf,theta in ((M_MU_GEV,theta_mu_R),(M_TAU_GEV,theta_tau_R)):
        beta=np.sqrt(np.maximum(0.0,1.0-4.0*mf*mf/np.maximum(q2,1e-300)))
        r=mf*mf/np.maximum(q2,1e-300)
        gV2=math.sin(theta)**4
        gA2=math.cos(theta)**4
        total_factor += gV2*beta*(1.0+2.0*r)+gA2*beta**3
    return gX*gX*q/(12.0*math.pi)*total_factor


def off_shell_aprime_three_body_width(
    ms_GeV: float,
    mA_GeV: float,
    gX: float,
    *,
    theta_mu_R: float = 1.0e-2,
    theta_tau_R: float = 1.0e-2,
    quadrature_order: int = 192,
) -> dict:
    """Compute s -> A' + (A'^* -> nu nu, mu mu, tau tau) for ms/2<=mA<ms.

    The A' in the final state is on shell; the second vector is virtual.
    The output includes channel-by-channel partial widths. For ms<2mA this
    channel is distinct from the on-shell two-body s->A'A' mode.
    """
    if ms_GeV<=0 or mA_GeV<=0 or gX<=0:
        raise ValueError("masses and gX must be positive")
    if quadrature_order<32:
        raise ValueError("quadrature_order must be at least 32")
    if mA_GeV < ms_GeV/2.0:
        return {"nu_nu":0.0,"mu_mu":0.0,"tau_tau":0.0,"total":0.0,
                "status":"on_shell_AAprime_pair_open; do_not_add_three_body_separately"}
    if mA_GeV >= ms_GeV:
        return {"nu_nu":0.0,"mu_mu":0.0,"tau_tau":0.0,"total":0.0,
                "status":"both_Aprime_legs_virtual; four_body_modes_not_included"}

    tmax=(ms_GeV-mA_GeV)**2
    nodes,weights=_legendre_rule(quadrature_order)
    t=0.5*tmax*(nodes+1.0)
    wt=0.5*tmax*weights
    x=(mA_GeV/ms_GeV)**2
    y=t/(ms_GeV*ms_GeV)
    lam=np.maximum(0.0,(1.0-x-y)**2-4.0*x*y)
    sqrt_lam=np.sqrt(lam)
    k2_over_mA2=lam/(4.0*x*y)
    longitudinal_factor=(1.0-t/(mA_GeV*mA_GeV))**2
    vs=mA_GeV/(2.0*gX)
    g_sAA=2.0*mA_GeV*mA_GeV/vs
    propagator_den=(t-mA_GeV*mA_GeV)**2+t*aprime_running_width(
        t,gX,theta_mu_R,theta_tau_R
    )**2

    def integrate_current(mf: float | None, species: str, theta: float = 0.0) -> float:
        if species=="neutrino":
            beta=np.ones_like(t)
            h_s=gX*gX*(4.0*t/3.0)  # two massless Weyl neutrinos
            h_00=np.zeros_like(t)
        else:
            threshold=4.0*mf*mf
            beta=np.sqrt(np.maximum(0.0,1.0-threshold/np.maximum(t,1e-300)))
            r=mf*mf/np.maximum(t,1e-300)
            gV2=gX*gX*math.sin(theta)**4
            gA2=gX*gX*math.cos(theta)**4
            h_s=gV2*(4.0/3.0)*(t+2.0*mf*mf)+gA2*(4.0/3.0)*(t-4.0*mf*mf)
            h_00=gA2*8.0*mf*mf*np.ones_like(t)
            h_s=np.where(t>=threshold,h_s,0.0)
            h_00=np.where(t>=threshold,h_00,0.0)
            beta=np.where(t>=threshold,beta,0.0)
        tensor=(3.0+k2_over_mA2)*h_s+k2_over_mA2*longitudinal_factor*h_00
        integrand=(g_sAA*g_sAA/(256.0*math.pi**3*ms_GeV)
                   *sqrt_lam*beta*tensor/propagator_den)
        return float(np.sum(wt*integrand))

    w_nu=integrate_current(None,"neutrino")
    w_mu=integrate_current(M_MU_GEV,"charged",theta_mu_R)
    w_tau=integrate_current(M_TAU_GEV,"charged",theta_tau_R)
    return {"nu_nu":w_nu,"mu_mu":w_mu,"tau_tau":w_tau,
            "total":w_nu+w_mu+w_tau,
            "status":"one_on_shell_one_virtual_Aprime_tree_level_three_body_included"}


def aprime_decay_widths(mA_GeV: float, gX: float,
                        theta_mu_R: float = 1.0e-2,
                        theta_tau_R: float = 1.0e-2) -> dict:
    """On-shell A' partial widths and branching fractions in the original model.

    Includes two massless Weyl neutrino species and charged mu/tau axial-vector
    couplings with the small vector admixture induced by theta_R. No electron
    coupling is introduced.
    """
    if mA_GeV<=0 or gX<=0:
        raise ValueError("mA_GeV and gX must be positive")
    widths={"nu_nu":gX*gX*mA_GeV/(12.0*math.pi),"mu_mu":0.0,"tau_tau":0.0}
    for name,mf,theta in (("mu_mu",M_MU_GEV,theta_mu_R),("tau_tau",M_TAU_GEV,theta_tau_R)):
        if mA_GeV>2.0*mf:
            r=mf*mf/(mA_GeV*mA_GeV)
            beta=math.sqrt(1.0-4.0*r)
            gV2=gX*gX*math.sin(theta)**4
            gA2=gX*gX*math.cos(theta)**4
            widths[name]=mA_GeV/(12.0*math.pi)*beta*(gV2*(1.0+2.0*r)+gA2*(1.0-4.0*r))
    total=sum(widths.values())
    br={k:v/total for k,v in widths.items()} if total>0 else {}
    from radial_scalar_widths import HBAR_C_GEV_M
    return {"partial_widths_GeV":widths,"total_width_GeV":total,
            "branching_fractions":br,"ctau_m":HBAR_C_GEV_M/total if total>0 else math.inf}
