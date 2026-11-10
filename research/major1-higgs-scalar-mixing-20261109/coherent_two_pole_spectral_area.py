#!/usr/bin/env python3
"""Coherent h-channel spectral-area diagnostic using the Plan-C-lite kernel."""
import math, cmath
from scipy.integrate import quad
MH=125.25; VH=246.22; ME=20000.0; GH=0.00407
LEPTONS=(0.1056583755,1.77686)
def a0(m,mu): return m*m*(1.0-math.log(m*m/(mu*mu)))
def b0(s,m,mu):
    beta=cmath.sqrt(1.0-4.0*m*m/s)
    return -math.log(m*m/(mu*mu))+2.0-beta*cmath.log((1.0+beta)/(1.0-beta))+1j*math.pi*beta
def qsum(vs): return sum(2.0*m*m/(VH*vs) for m in LEPTONS)
def pi_hs(s,vs):
    soft=0j
    for m in LEPTONS:
        yp=m*m/(VH*vs); B=b0(s,m,ME)
        soft+=yp*(4.0*a0(m,ME)+2.0*(4.0*m*m-s)*B)/(16.0*math.pi**2)
        soft+=4.0*m**4/(VH*vs)*(1.0-math.log(m*m/(ME*ME)))/(16.0*math.pi**2)
    return soft-qsum(vs)/(16.0*math.pi**2)*(-2.0/3.0)*s
def gamma_aa(ms,vs,ma):
    if ms<=2.0*ma:return 0.0
    x=(ma/ms)**2
    return ms**3/(32.0*math.pi*vs**2)*(1.0-4.0*x+12.0*x*x)*math.sqrt(1.0-4.0*x)
def gamma_ll(ms,vs,m):
    if ms<=2.0*m:return 0.0
    return m*m*ms/(8.0*math.pi*vs**2)*(1.0-4.0*m*m/ms**2)**1.5
def gamma_s(ms,vs,ma): return gamma_aa(ms,vs,ma)+sum(gamma_ll(ms,vs,m) for m in LEPTONS)
def d_hh(m,ms,vs,ma):
    s=m*m; a=MH*MH-1j*MH*GH; b=ms*ms-1j*ms*gamma_s(ms,vs,ma); p=pi_hs(s,vs)
    return (s-b)/((s-a)*(s-b)-p*p)
def d_sm(m):
    s=m*m; a=MH*MH-1j*MH*GH
    return 1.0/(s-a)
def area_ratio(ms,vs,ma,lo=124.5,hi=126.0):
    points={lo,hi,MH,ms}
    for center in (MH,ms):
        for dx in (1e-5,2e-5,5e-5,1e-4,2e-4,5e-4,1e-3,2e-3,5e-3,.01,.03,.1,.3):
            for sign in (-1,1):
                x=center+sign*dx
                if lo<x<hi: points.add(x)
    points=sorted(points)
    f=lambda m:abs(d_hh(m,ms,vs,ma))**2
    g=lambda m:abs(d_sm(m))**2
    num=den=0.0
    for a,b in zip(points[:-1],points[1:]):
        num+=quad(f,a,b,epsabs=1e-10,epsrel=1e-7,limit=300)[0]
        den+=quad(g,a,b,epsabs=1e-10,epsrel=1e-7,limit=300)[0]
    return num/den
def main():
    cases=(("A",70.886458,10.0),("B",315.0,63.0))
    expected={("A",100.0):1.00003047,("A",125.25):0.99933966,("A",150.0):0.99996718,
              ("B",100.0):1.00000164,("B",125.25):0.98776507,("B",150.0):0.99999863}
    for name,vs,ma in cases:
        for ms in (100.0,125.25,150.0):
            ratio=area_ratio(ms,vs,ma)
            print(f"{name} m_s={ms:.2f} GeV: coherent h-channel area ratio={ratio:.9f}")
            assert abs(ratio-expected[(name,ms)])<2e-6
    print("PASS: all six coherent spectral-area ratios reproduce the archived integration values.")
    print("LIMIT: Plan-C-lite selected kernel, fixed widths, constant vertices, no backgrounds or detector likelihood.")
if __name__=="__main__": main()
