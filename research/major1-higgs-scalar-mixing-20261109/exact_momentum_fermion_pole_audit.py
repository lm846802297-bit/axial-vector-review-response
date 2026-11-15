#!/usr/bin/env python3
"""Exact-momentum fermion-sector matched complex-pole diagnostic.

The finite B0bar Feynman-parameter integral uses composite Gauss-Legendre
quadrature with geometric endpoint refinement and root-neighbourhood panels.
The calculation remains a fermion-sector subset with fixed Plan-C-lite
diagonal-width inputs; it is not a gauge-complete physical pole prediction.
"""
import math, cmath
from functools import lru_cache
import numpy as np
from numpy.polynomial.legendre import leggauss
MH=125.25; VH=246.22; ME=20000.0; THETA_L=1e-2
MU=ME; GAMMA_H=0.00407
B0_GL_ORDER=64
LEPTONS={"mu":0.1056583755,"tau":1.77686}
def a0bar(m): return m*m*(1.0-math.log(m*m/(MU*MU))) if m else 0.0
@lru_cache(maxsize=4)
def _gauss_rule(n=64):
    return leggauss(n)

@lru_cache(maxsize=4096)
def b0bar_cached(sr,si,mi,mj,second):
    """Finite B0bar Feynman-parameter integral by composite Gauss-Legendre.

    Geometric panels resolve the O(m_light^2/m_heavy^2) endpoint layer in
    hierarchical heavy-light pairs. Panels around the real-part roots resolve
    the finite-width logarithmic transition above open thresholds.
    """
    s=complex(sr,si)
    if abs(s.imag)<1e-18 and s.real>0:
        s+=1e-8j
    aa=s.real
    bb=mi*mi-mj*mj-s.real
    cc=mj*mj
    roots=[]
    disc=bb*bb-4.0*aa*cc
    if aa and disc>=0:
        for x in ((-bb-math.sqrt(disc))/(2.0*aa),(-bb+math.sqrt(disc))/(2.0*aa)):
            if 0.0<x<1.0:
                roots.append(x)
    points=[0.0,1.0]+roots
    # Resolve the small endpoint layer when one internal mass is much heavier.
    if mi>mj and mi>0.0:
        delta=(mj/mi)**2
        for k in range(-2,16):
            x=delta*(10.0**k)
            if 0.0<x<0.1:
                points.append(x)
    if mj>mi and mj>0.0:
        delta=(mi/mj)**2
        for k in range(-2,16):
            x=1.0-delta*(10.0**k)
            if 0.9<x<1.0:
                points.append(x)
    # Resolve the complex-log transition around each real-part root.
    for root in roots:
        slope=abs(2.0*s.real*root+bb)
        width=abs(s.imag)/max(slope,1e-300)
        for k in range(-2,12):
            dx=width*(10.0**k)
            left,right=root-dx,root+dx
            if 0.0<left<1.0:
                points.append(left)
            if 0.0<right<1.0:
                points.append(right)
    points=sorted(set(points))
    nodes,weights=_gauss_rule(B0_GL_ORDER)
    total=0j
    for lo,hi in zip(points[:-1],points[1:]):
        x=(lo+hi)/2.0+(hi-lo)/2.0*nodes
        den=x*mi*mi+(1.0-x)*mj*mj-x*(1.0-x)*s
        values=-np.log(den/(MU*MU))
        total+=(hi-lo)/2.0*np.dot(weights,values)
    if second and si<0.0 and s.real>(mi+mj)**2:
        kallen=(s-(mi+mj)**2)*(s-(mi-mj)**2)
        total+=2j*math.pi*cmath.sqrt(kallen)/s
    return complex(total)

def b0bar(s,mi,mj,second=False):
    z=complex(s); return b0bar_cached(float(z.real),float(z.imag),float(mi),float(mj),bool(second))
@lru_cache(maxsize=32)
def mass_basis(vs,ml):
    theta_r=ml/(ME*THETA_L); y=math.sqrt(2.0)*ME*THETA_L/VH; lam=math.sqrt(2.0)*ME*theta_r/vs
    mass_matrix=np.array([[0.0,y*VH/math.sqrt(2.0)],[lam*vs/math.sqrt(2.0),ME]])
    ul,masses,vh=np.linalg.svd(mass_matrix,full_matrices=False); ur=vh.T
    yh0=np.array([[0.0,y/math.sqrt(2.0)],[0.0,0.0]])
    ys0=np.array([[0.0,0.0],[lam/math.sqrt(2.0),0.0]])
    return masses,ul.T@yh0@ur,ul.T@ys0@ur
def pi_rc_entry(vs,ml,s,a,b,second=False):
    masses,yh,ys=mass_basis(vs,ml); ya=yh if a=="h" else ys; yb=yh if b=="h" else ys; total=0j
    for i in range(2):
        for j in range(2):
            mi,mj=float(masses[i]),float(masses[j]); B=b0bar(s,mi,mj,second)
            cab=ya[i,j]*np.conj(yb[i,j])+np.conj(ya[j,i])*yb[j,i]
            dab=ya[i,j]*yb[j,i]+np.conj(ya[j,i])*np.conj(yb[i,j])
            kernel=a0bar(mi)+a0bar(mj)+(mi*mi+mj*mj-s)*B
            total+=cab*kernel+2.0*mi*mj*dab*B
    return -total/(16.0*math.pi**2)
def pi_b_full(vs,s,second=False): return -sum(pi_rc_entry(vs,m,s,"h","s",second) for m in LEPTONS.values())
def pi_b_light(vs,s,second=False):
    total=0j
    for ml in LEPTONS.values():
        masses,yh,ys=mass_basis(vs,ml); m=float(masses[1])
        cab=yh[1,1]*np.conj(ys[1,1])+np.conj(yh[1,1])*ys[1,1]
        dab=yh[1,1]*ys[1,1]+np.conj(yh[1,1])*np.conj(ys[1,1])
        B=b0bar(s,m,m,second); kernel=2.0*a0bar(m)+(2.0*m*m-s)*B
        total+=(cab*kernel+2.0*m*m*dab*B)/(16.0*math.pi**2)
    return total
def contact_tadpole(vs): return sum(4.0*m**4/(VH*vs)*(1.0-math.log(m*m/(MU*MU)))/(16.0*math.pi**2) for m in LEPTONS.values())
def hard_momentum(vs,s,second=False): return (pi_b_full(vs,s,second)-pi_b_full(vs,0.0,False))-(pi_b_light(vs,s,second)-pi_b_light(vs,0.0,False))
def pi_matched(vs,s,second=False): return pi_b_light(vs,s,second)+contact_tadpole(vs)+hard_momentum(vs,s,second)
def gamma_aa(ms,vs,ma):
    if ms<=2.0*ma:return 0.0
    x=(ma/ms)**2; return ms**3/(32.0*math.pi*vs**2)*(1.0-4.0*x+12.0*x*x)*math.sqrt(1.0-4.0*x)
def gamma_ll(ms,vs,m):
    if ms<=2.0*m:return 0.0
    return m*m*ms/(8.0*math.pi*vs**2)*(1.0-4.0*m*m/ms**2)**1.5
def gamma_s(ms,vs,ma): return gamma_aa(ms,vs,ma)+sum(gamma_ll(ms,vs,m) for m in LEPTONS.values())
def poles_and_residues(ms,vs,ma):
    a=MH*MH-1j*MH*GAMMA_H; b=ms*ms-1j*ms*gamma_s(ms,vs,ma)
    def determinant(z):
        p=pi_matched(vs,z,True); return (z-a)*(z-b)-p*p
    p0=pi_matched(vs,(MH*MH+ms*ms)/2.0,False); split=cmath.sqrt(((a-b)/2.0)**2+p0*p0); roots=[]
    for z in ((a+b)/2.0+split,(a+b)/2.0-split):
        for _ in range(40):
            step=1e-4+1e-6j; derivative=(determinant(z+step)-determinant(z-step))/(2.0*step); dz=determinant(z)/derivative; z-=dz
            if abs(dz)<2e-10:break
        roots.append(z)
    rows=[]
    for z in roots:
        step=1e-4+1e-6j; fp=(determinant(z+step)-determinant(z-step))/(2.0*step); p=pi_matched(vs,z,True)
        rhh=(z-b)/fp; rss=(z-a)/fp; rhs=p/fp; pole=cmath.sqrt(z)
        rows.append({"mass":pole.real,"width":-2.0*pole.imag,"R_hh":rhh,"R_ss":rss,"R_hs":rhs,"residual":abs(determinant(z))})
    return rows

def main():
    references={"A":(70.886458,10.0,0.024030443985870786),"B":(315.0,63.0,0.005407723994710553)}
    for name,(vs,ma,hard_ref) in references.items():
        hard=hard_momentum(vs,MH*MH,False)
        if abs(hard.real-hard_ref)>2e-8 or abs(hard.imag)>2e-8: raise AssertionError((name,hard,hard_ref))
        for ms in (100.0,125.25,150.0):
            rows=poles_and_residues(ms,vs,ma)
            for r in rows: print(name,ms,r)
            assert abs(sum(r["R_hh"] for r in rows)-1.0)<3e-5
            assert max(r["residual"] for r in rows)<1e-7
    print("PASS")
if __name__=="__main__": main()
