#!/usr/bin/env python3
"""Numerical audit for Major Point 1: portal threshold and Higgs-mixing diagnostics."""
import math

VH=246.22
MH=125.25
MH2=MH**2
MU=0.990
SIGMA_DOWN=0.051
MU95=MU-1.645*SIGMA_DOWN
THETA95=math.asin(math.sqrt(1-MU95))
TAN2_95=math.tan(2*THETA95)

benchmarks={
 "A":{"vs":70.886458,"portal":-0.21076398,"delta_res":0.656933835,"msmax":355.4,"mA":10.0},
 "B":{"vs":315.0,"portal":-0.01067338,"delta_res":0.147834009,"msmax":1579.2,"mA":63.0},
}
expected_mass2={"A":-3678.60356,"B":-827.819609}
for name,b in benchmarks.items():
    delta=b["portal"]*VH*b["vs"]
    assert abs(delta-expected_mass2[name])<0.02
    low2=MH2-2*abs(delta)/TAN2_95
    high2=MH2+2*abs(delta)/TAN2_95
    low=math.sqrt(max(0,low2))
    high=math.sqrt(high2)
    b["uncompensated_delta"]=delta
    b["uncompensated_rate_diagnostic_interval"]=(low,high)
    for ms in (10.0,100.0,150.0,200.0,b["msmax"]):
        theta=0.5*math.atan(2*abs(delta)/abs(MH2-ms**2))
        mu=math.cos(theta)**2
        assert 0<=mu<=1
    for target in (0.1,0.01,THETA95):
        halfwidth=b["delta_res"]/(MH*math.tan(2*target))
        assert halfwidth>0
        b.setdefault("residual_halfwidths_GeV",{})[str(target)]=halfwidth

# h -> A'A' width coefficient for the singlet component of the 125-GeV-like state.
A=benchmarks["A"]
x=(A["mA"]/MH)**2
phase=(1-4*x+12*x*x)*math.sqrt(1-4*x)
gamma_coeff=MH**3/(32*math.pi*A["vs"]**2)*phase
assert 3.73<gamma_coeff<3.76
assert 2*benchmarks["B"]["mA"]>MH
gamma_sm=0.0041
sin2_for_ten_percent=0.1*gamma_sm/gamma_coeff
assert 1.0e-4<sin2_for_ten_percent<1.2e-4

print(f"ATLAS-inspired one-sided Gaussian mu_95 lower = {MU95:.6f}")
print(f"Illustrative |theta| upper = {THETA95:.6f} rad")
for name,b in benchmarks.items():
    lo,hi=b["uncompensated_rate_diagnostic_interval"]
    print(f"{name}: delta_portal = {b['uncompensated_delta']:.6f} GeV^2")
    print(f"{name}: uncompensated single-pole rate diagnostic interval = [{lo:.3f}, {hi:.3f}] GeV")
    for target,half in b["residual_halfwidths_GeV"].items():
        print(f"{name}: residual |theta|={float(target):.6f} halfwidth = {half*1000:.3f} MeV")
print(f"Benchmark A Gamma(h1->A'A') = {gamma_coeff:.6f} GeV * sin^2(theta)")
print(f"Benchmark A sin^2(theta) for 10% SM-width benchmark = {sin2_for_ten_percent:.7g}")
print("PASS: portal-curvature products, rate-bound intervals, resonance windows, and A'A' threshold/width.")
print("LIMIT: no full complex-pole solution, detector-level likelihood, or model-specific ATLAS recast.")
