#!/usr/bin/env python3
"""Benchmark-A h -> A'A' -> mu mu tau tau applicability diagnostic."""
import math

mA=10.0
gX=0.07053533412545454
mh=125.25
vs=70.886458
mmu=0.1056583755
mtau=1.77686

base=gX*gX*mA/(12.0*math.pi)
gamma_mu=base*(1.0-4.0*mmu**2/mA**2)**1.5
gamma_tau=base*(1.0-4.0*mtau**2/mA**2)**1.5
gamma_nu=base  # two massless Weyl neutrinos combined
gamma_tot=gamma_mu+gamma_tau+gamma_nu
br_mu=gamma_mu/gamma_tot
br_tau=gamma_tau/gamma_tot
br_nu=gamma_nu/gamma_tot
br_mumu_tautau=2.0*br_mu*br_tau

# Exact-momentum matched A benchmark: isolated h-like pole residue ratio.
Rhh=1.0000007434316154+4.106739752940081e-7j
Rhs=-0.00024131115965366444+0.0008812811607869158j
r=Rhs/Rhh
singlet_fraction=abs(r)**2/(1.0+abs(r)**2)

x=(mA/mh)**2
phase=(1.0-4.0*x+12.0*x*x)*math.sqrt(1.0-4.0*x)
gamma_coefficient=mh**3/(32.0*math.pi*vs**2)*phase
gamma_hAA=gamma_coefficient*singlet_fraction
gamma_h_pole=0.004072688852170186
br_hAA=gamma_hAA/(gamma_h_pole+gamma_hAA)
cascade_product=br_hAA*br_mumu_tautau

# For a CP-even scalar coupled through g h V_mu V^mu:
A00=mh*mh/(2.0*mA*mA)-1.0
f_longitudinal=A00*A00/(A00*A00+2.0)

print(f"Gamma(A'->mumu)={gamma_mu:.12g} GeV")
print(f"Gamma(A'->tautau)={gamma_tau:.12g} GeV")
print(f"Gamma(A'->nu nu)={gamma_nu:.12g} GeV")
print(f"BR(mumu,tau tau,nu nu)=({br_mu:.9g},{br_tau:.9g},{br_nu:.9g})")
print(f"BR(AA->mumu tautau)={br_mumu_tautau:.12g}")
print(f"R_hs/R_hh={r}; |r|={abs(r):.12g}")
print(f"singlet pole fraction={singlet_fraction:.12g}")
print(f"Gamma(h1->A'A')={gamma_hAA:.12g} GeV")
print(f"BR(h1->A'A')={br_hAA:.12g}")
print(f"sigma/sigma_SM * BR(h1->A'A'->mumu tautau)~{cascade_product:.12g}")
print(f"longitudinal A' fraction in h->A'A'={f_longitudinal:.12g}")
assert abs(br_mu+br_tau+br_nu-1.0)<1e-12
assert 1.5e-4<cascade_product<1.7e-4
assert f_longitudinal>0.999
print("PASS: benchmark cascade branching and vector polarization arithmetic.")
print("LIMIT: isolated-pole estimate; no vector-specific detector simulation or CMS likelihood recast.")
