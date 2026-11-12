#!/usr/bin/env python3
"""Pole-residue audit for archived Plan-C-lite approximate 2x2 propagator."""
import math, cmath
MH=125.25; VH=246.22; ME=20000.0; GH=0.00407
LEPTONS=(0.1056583755,1.77686)
def a0bar(m,mu): return m*m*(1.0-math.log(m*m/(mu*mu)))
def b0_second(s,m,mu):
    beta=cmath.sqrt(1.0-4.0*m*m/s)
    return -math.log(m*m/(mu*mu))+2.0-beta*cmath.log((1.0+beta)/(1.0-beta))+1j*math.pi*beta
def qsum(vs): return sum(2.0*m*m/(VH*vs) for m in LEPTONS)
def pi_hs(s,vs,mu=ME):
    soft=0j
    for m in LEPTONS:
        yprod=m*m/(VH*vs); b0=b0_second(s,m,mu)
        soft+=yprod*(4.0*a0bar(m,mu)+2.0*(4.0*m*m-s)*b0)/(16.0*math.pi**2)
        soft+=4.0*m**4/(VH*vs)*(1.0-math.log(m*m/(mu*mu)))/(16.0*math.pi**2)
    return soft-qsum(vs)/(16.0*math.pi**2)*(math.log(ME*ME/(mu*mu))-2.0/3.0)*s
def gamma_aa(ms,vs,ma):
    if ms<=2.0*ma:return 0.0
    x=(ma/ms)**2
    return ms**3/(32.0*math.pi*vs**2)*(1.0-4.0*x+12.0*x*x)*math.sqrt(1.0-4.0*x)
def gamma_ll(ms,vs,m):
    if ms<=2.0*m:return 0.0
    return m*m*ms/(8.0*math.pi*vs**2)*(1.0-4.0*m*m/ms**2)**1.5
def gamma_s(ms,vs,ma): return gamma_aa(ms,vs,ma)+sum(gamma_ll(ms,vs,m) for m in LEPTONS)
def roots_for(ms,vs,ma):
    a=MH*MH-1j*MH*GH; b=ms*ms-1j*ms*gamma_s(ms,vs,ma)
    def det(z):
        p=pi_hs(z,vs)
        return (z-a)*(z-b)-p*p
    p0=pi_hs((MH*MH+ms*ms)/2.0,vs); zref=(a+b)/2.0
    split=cmath.sqrt(((a-b)/2.0)**2+p0*p0); roots=[]
    for z in (zref+split,zref-split):
        for _ in range(100):
            step=1e-4+1e-6j
            der=(det(z+step)-det(z-step))/(2.0*step)
            dz=det(z)/der; z-=dz
            if abs(dz)<1e-12: break
        if abs(det(z))>1e-7: raise RuntimeError(f"root residual {abs(det(z))}")
        roots.append(z)
    return a,b,roots,det
def residue_rows(ms,vs,ma):
    a,b,roots,det=roots_for(ms,vs,ma); rows=[]
    for z in roots:
        step=1e-4+1e-6j
        fp=(det(z+step)-det(z-step))/(2.0*step); p=pi_hs(z,vs)
        rhh=(z-b)/fp; rss=(z-a)/fp; rhs=p/fp; pole=cmath.sqrt(z)
        rows.append((pole.real,-2.0*pole.imag,rhh,rss,rhs,abs(det(z))))
    return rows
def main():
    for name,vs,ma in (("A",70.886458,10.0),("B",315.0,63.0)):
        for ms in (100.0,125.25,150.0):
            rows=residue_rows(ms,vs,ma); sum_hh=sum(r[2] for r in rows)
            print(f"{name} m_s={ms:.2f} GeV")
            for mass,width,rhh,rss,rhs,res in rows:
                print(f" pole m={mass:.9f} GeV Gamma={width*1e3:.6f} MeV")
                print(f" R_hh={rhh.real:+.9g}{rhh.imag:+.9g}i; R_ss={rss.real:+.9g}{rss.imag:+.9g}i; R_hs={rhs.real:+.9g}{rhs.imag:+.9g}i; |F|={res:.2e}")
            print(f" sum R_hh={sum_hh.real:.10f}{sum_hh.imag:+.3e}i")
            assert abs(sum_hh-1.0)<2e-5
            assert max(r[5] for r in rows)<1e-7
    print("PASS: six two-pole root pairs converge with small determinant residual.")
    print("PASS: sum of h-channel residues is unity to numerical precision in this kernel.")
    print("LIMIT: complex residues are not probabilities or signal strengths.")
    print("LIMIT: fixed widths and selected Plan-C-lite matching kernel are inherited.")
if __name__=="__main__": main()
