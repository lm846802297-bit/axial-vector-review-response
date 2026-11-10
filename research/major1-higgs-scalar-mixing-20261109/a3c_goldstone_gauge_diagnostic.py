#!/usr/bin/env python3
"""A3c R_xi diagnostic of the unphysical Goldstone cuts in the hs subset."""
import math

mh=125.25
v=246.22
mW=80.379
mZ=91.1876
benchmarks={
    "A":{"vS":70.886458,"mX":10.0},
    "B":{"vS":315.0,"mX":63.0},
}
lamH=mh**2/(2*v**2)
s=mh**2

def beta_goldstone(xi,m):
    z=1.0-4.0*xi*m*m/s
    return math.sqrt(z) if z>0.0 else 0.0

def im_coeff(vS,mX,xi):
    lamS=mh**2/(2*vS**2)
    bW=beta_goldstone(xi,mW)
    bZ=beta_goldstone(xi,mZ)
    bX=beta_goldstone(xi,mX)
    # Im Pi_hs^Goldstone / (lambda_HS*v*vS)
    # Im B0 = pi beta; overall 1/(16 pi^2).
    coeff=(2*lamH*bW+lamH*bZ+lamS*bX)/(16*math.pi)
    return lamS,(bW,bZ,bX),coeff

def main():
    print(f"m_h={mh} GeV; lambda_H(tree)={lamH:.12g}; p^2=m_h^2")
    for name,p in benchmarks.items():
        print(name)
        for xi in (0.5,1.0,2.0,4.0,10.0,40.0):
            lamS,betas,coeff=im_coeff(p["vS"],p["mX"],xi)
            print(f"  xi={xi:4.1f}: lambda_S={lamS:.9g}, beta_(W,Z,X)={betas}, "
                  f"ImPi_hs/(lambda_HS*v*vS)={coeff:.12g} GeV^0")
    # Feynman gauge thresholds.
    assert beta_goldstone(1.0,mW)==0.0
    assert beta_goldstone(1.0,mZ)==0.0
    assert beta_goldstone(1.0,10.0)>0.0
    assert beta_goldstone(1.0,63.0)==0.0
    # A common xi=0.5 opens the W Goldstone cut and both X-Goldstone cuts.
    assert beta_goldstone(0.5,mW)>0.0
    assert beta_goldstone(0.5,63.0)>0.0
    # A common xi=40 closes all these cuts at p^2=m_h^2.
    assert all(beta_goldstone(40.0,m)==0.0 for m in (mW,mZ,10.0,63.0))
    print("PASS: gauge-dependent threshold locations and absorptive coefficients.")
    print("LIMIT: Goldstone subset only; its imaginary part is not a physical width.")
if __name__=="__main__": main()
