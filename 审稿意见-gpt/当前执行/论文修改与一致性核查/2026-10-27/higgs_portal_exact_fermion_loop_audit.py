#!/usr/bin/env python3
"""Exact one-loop charged-lepton/VLL h-s mixing audit; Python standard library only.

The full UV fermion loop is evaluated in the exact mass-eigenstate basis for
each 2x2 charged-lepton/VLL block. The finite hard momentum dependence is
defined as [Pi_UV(m_h^2)-Pi_UV(0)] minus the light diagonal bubble difference.
It is combined with the EFT soft bubble/contact term under the explicit
matching benchmark lambda_HS^EFT(M_E)=0. This is a one-loop fermion-sector
calculation and a first-pass pole diagnostic, not a full experimental recast.
"""
from math import atan, log, pi, sqrt
import cmath

MH, VH, GAMMA_H = 125.25, 246.22, 0.00407
ME, THETA_L = 20_000.0, 1.0e-2
ML = {"mu": 0.1056583755, "tau": 1.77686}
BENCHMARKS = (("A_open_AA", 70.886458, 10.0),
              ("B_closed_AA", 315.0, 63.0))


def adaptive_simpson(f, a, b, eps=1e-10, depth=24):
    fa, fb = f(a), f(b)
    m, fm = (a+b)/2, f((a+b)/2)
    whole = (b-a)*(fa+4*fm+fb)/6
    def rec(a,b,fa,fm,fb,whole,eps,depth):
        m=(a+b)/2
        lm,rm=(a+m)/2,(m+b)/2
        flm,frm=f(lm),f(rm)
        left=(m-a)*(fa+4*flm+fm)/6
        right=(b-m)*(fm+4*frm+fb)/6
        delta=left+right-whole
        if depth<=0 or abs(delta)<=15*eps:
            return left+right+delta/15
        return rec(a,m,fa,flm,fm,left,eps/2,depth-1)+rec(m,b,fm,frm,fb,right,eps/2,depth-1)
    return rec(a,b,fa,fm,fb,whole,eps,depth)


def A0(m, mu=ME):
    return m*m*(1-log(m*m/(mu*mu))) if m else 0.0


def B0(s, m1, m2, mu=ME):
    """MS-bar finite B0 for the real momenta used in the hard matching."""
    if abs(m1-m2) <= 1e-12*max(m1,m2):
        m=(m1+m2)/2
        if abs(s)<1e-18:
            return complex(-log(m*m/(mu*mu)),0)
        if s>4*m*m:
            beta=sqrt(1-4*m*m/s)
            return complex(-log(m*m/(mu*mu))+2-beta*log((1+beta)/(1-beta)),pi*beta)
        if 0<s<4*m*m:
            b=sqrt(4*m*m/s-1)
            return complex(-log(m*m/(mu*mu))+2-2*b*atan(1/b),0)
    def f(x):
        d=x*m1*m1+(1-x)*m2*m2-x*(1-x)*s
        if d<=0:
            raise ValueError("Unequal-mass benchmark unexpectedly crosses threshold")
        return -log(d/(mu*mu))
    ratio=min(m1,m2)**2/max(m1,m2)**2
    pts=sorted(set([0.0,1.0]+[x for x in
        (ratio,10*ratio,100*ratio,1000*ratio,1e-4,1e-3,1e-2,.1,.5,.9)
        if 0<x<1]))
    return complex(sum(adaptive_simpson(f,a,b) for a,b in zip(pts[:-1],pts[1:])),0)


def B0_second_sheet(s,m,mu=ME):
    beta=cmath.sqrt(1-4*m*m/s)
    return -log(m*m/(mu*mu))+2-beta*cmath.log((1+beta)/(1-beta))+1j*pi*beta


def block(flavor,vs):
    ml=ML[flavor]
    mL=ME*THETA_L
    thetaR_input=ml/(ME*THETA_L)
    mR=ME*thetaR_input
    tL=.5*__import__("math").atan2(2*mL*ME,ME*ME+mR*mR-mL*mL)
    tR=.5*__import__("math").atan2(2*mR*ME,mL*mL+ME*ME-mR*mR)
    cL,sL=__import__("math").cos(tL),__import__("math").sin(tL)
    cR,sR=__import__("math").cos(tR),__import__("math").sin(tR)
    tr=mL*mL+mR*mR+ME*ME
    det=mL*mL*mR*mR
    root=sqrt(tr*tr-4*det)
    masses=(sqrt((tr-root)/2),sqrt((tr+root)/2))
    yh0=((cL*sR,cL*cR),(sL*sR,sL*cR))
    ys0=((sL*cR,-sL*sR),(-cL*cR,cL*sR))
    yh=tuple(tuple(mL/VH*x for x in row) for row in yh0)
    ys=tuple(tuple(mR/vs*x for x in row) for row in ys0)
    return masses,yh,ys


def pi_full(s,data):
    masses,yh,ys=data
    total=0j
    ckin_sum=0.0
    for i,mi in enumerate(masses):
        for j,mj in enumerate(masses):
            ckin=yh[i][j]*ys[i][j]+yh[j][i]*ys[j][i]
            cmass=yh[i][j]*ys[j][i]+yh[j][i]*ys[i][j]
            ckin_sum+=ckin
            b=B0(s,mi,mj)
            total+=(ckin*(A0(mi)+A0(mj)+(mi*mi+mj*mj-s)*b)
                    +2*mi*mj*cmass*b)/(16*pi*pi)
    return total,ckin_sum


def pi_light(s,m,yh,ys):
    return yh*ys*(4*A0(m)+2*(4*m*m-s)*B0(s,m,m))/(16*pi*pi)


def hard_delta(vs):
    total=0j
    records={}
    ckin_all=0.0
    for flavor in ("mu","tau"):
        data=block(flavor,vs)
        masses,yh,ys=data
        ph,ck=pi_full(MH*MH,data)
        p0,ck0=pi_full(0.0,data)
        lh=pi_light(MH*MH,masses[0],yh[0][0],ys[0][0])
        l0=pi_light(0.0,masses[0],yh[0][0],ys[0][0])
        dh=(ph-p0)-(lh-l0)
        total+=dh
        ckin_all+=ck
        records[flavor]={"masses":masses,"full0":p0,"hard":dh,"ckin":ck}
    return total,records,ckin_all


def source_derivative(s,vs):
    q=sum(2*m*m/(VH*vs) for m in ML.values())
    return -q/(16*pi*pi)*(log(ME*ME/(ME*ME)-0.0)-2/3)*s


def soft_eft(s,vs):
    total=0j
    for m in ML.values():
        yprod=m*m/(VH*vs)
        if isinstance(s,(int,float)):
            b=B0(s,m,m)
        else:
            b=B0_second_sheet(s,m)
        bubble=yprod*(4*A0(m)+2*(4*m*m-s)*b)/(16*pi*pi)
        contact=4*m**4/(VH*vs)*(1-log(m*m/(ME*ME)))/(16*pi*pi)
        total+=bubble+contact
    return total


def hard_source(s,vs):
    q=sum(2*m*m/(VH*vs) for m in ML.values())
    return q/(24*pi*pi)*s


def pi_matched(s,vs,hard_at_mh):
    return soft_eft(s,vs)+hard_at_mh*s/(MH*MH)


def gamma_aa(ms,vs,ma):
    if 2*ma>=ms:return 0.0
    x=(ma/ms)**2
    return ms**3/(32*pi*vs**2)*(1-4*x+12*x*x)*sqrt(1-4*x)


def gamma_ll(ms,vs,m):
    if 2*m>=ms:return 0.0
    return m*m*ms/(8*pi*vs*vs)*(1-4*m*m/(ms*ms))**1.5


def gamma_s(ms,vs,ma):
    return gamma_aa(ms,vs,ma)+sum(gamma_ll(ms,vs,m) for m in ML.values())


def proxy(ms,vs,ma,p):
    a=MH*MH-1j*MH*GAMMA_H
    b=ms*ms-1j*ms*gamma_s(ms,vs,ma)
    return 2*abs(p)/abs(a-b)


def pole_diagnostic(ms,vs,ma,hard):
    gs=gamma_s(ms,vs,ma)
    a=MH*MH-1j*MH*GAMMA_H
    b=ms*ms-1j*ms*gs
    def det(z):
        p=pi_matched(z,vs,hard)
        return (z-a)*(z-b)-p*p
    pref=pi_matched((MH*MH+ms*ms)/2,vs,hard)
    half=(a-b)/2
    split=cmath.sqrt(half*half+pref*pref)
    out=[]
    for z in ((a+b)/2+split,(a+b)/2-split):
        for _ in range(60):
            f=det(z); h=1e-4+1e-6j
            der=(det(z+h)-det(z-h))/(2*h)
            if abs(der)<1e-20:break
            dz=f/der; z-=dz
            if abs(dz)<1e-10:break
        mp=cmath.sqrt(z)
        if mp.real<0:mp=-mp
        p=pi_matched(z,vs,hard)
        out.append((mp.real,-2*mp.imag,abs((z-a)/p),abs(det(z))))
    return sorted(out,key=lambda r:r[1])


def edge(vs,ma,p,sign):
    lo,hi=0.0,.02
    f=lambda d:proxy(MH+sign*d,vs,ma,p)-.1
    if f(lo)*f(hi)>0:return None
    flo=f(lo)
    for _ in range(80):
        mid=(lo+hi)/2; fm=f(mid)
        if hi-lo<1e-12:break
        if flo*fm<=0:hi=mid
        else:lo,flo=mid,fm
    return (lo+hi)/2


def main():
    print("Exact one-loop h-s fermion-sector audit (MS-bar finite PV functions)")
    print("The model has no tree-level s-WW or s-tt vertex at zero portal; direct W/top loops vanish at this order.")
    print("Matching benchmark: lambda_HS^EFT(M_E)=0. The constant hard threshold is absorbed.")
    for label,vs,ma in BENCHMARKS:
        hard,records,ckin=hard_delta(vs)
        dlam=-sum((sqrt(2)*ME*THETA_L/VH*sqrt(2)*m/(THETA_L*vs))**2 for m in ML.values())/(8*pi*pi)
        full0=sum(r["full0"].real for r in records.values())
        th=full0/(VH*vs)
        source=hard_source(MH*MH,vs)
        soft=soft_eft(MH*MH,vs)
        total=soft+hard
        print(f"\\n{label}: v_s={vs:.9g} GeV, m_A'={ma:g} GeV, g_X={ma/(2*vs):.9g}")
        print(f"  perturbative m_s interval for lambda_S<=4pi: [10, {sqrt(8*pi)*vs:.6f}] GeV")
        print(f"  leading Delta lambda_HS^E={dlam:.12g}; exact Pi_UV(0)/(v_h v_s)={th:.12g}")
        print(f"  relative threshold mismatch={abs((th-dlam)/dlam):.4g}; sum C_kin={ckin:.3g}")
        for fl,r in records.items():
            print(f"  {fl}: m_light,m_heavy={r['masses'][0]:.9g},{r['masses'][1]:.9g} GeV; "
                  f"hard delta Pi={r['hard'].real:.10g}{r['hard'].imag:+.3g}i GeV^2; sum C_kin={r['ckin']:.3g}")
        print(f"  exact hard-minus-light delta Pi(m_h^2)={hard.real:.10g}{hard.imag:+.3g}i GeV^2")
        print(f"  source derivative estimate={source.real:.10g}{source.imag:+.3g}i GeV^2; "
              f"relative difference={abs((hard-source)/source):.4g}")
        print(f"  EFT soft bubble+contact={soft.real:.10g}{soft.imag:+.10g}i GeV^2")
        print(f"  matched Pi_hs(m_h^2)={total.real:.10g}{total.imag:+.10g}i GeV^2")
        print(f"  proxy 2|Pi/(a-b)| at m_s=m_h={proxy(MH,vs,ma,total):.9g}")
        print("  selected proxy points:")
        for ms in (10,50,100,124.5,125.0,125.25,125.5,126,150,200,sqrt(8*pi)*vs):
            print(f"    m_s={ms:.6g} GeV: {proxy(ms,vs,ma,total):.9g}")
        print(f"  proxy>=0.1 half-width: left={edge(vs,ma,total,-1)} GeV; right={edge(vs,ma,total,1)} GeV")
        print(f"  Gamma_s(m_h)={gamma_s(MH,vs,ma):.9g} GeV")
        for mp,g,w,res in pole_diagnostic(MH,vs,ma,hard):
            print(f"    pole m={mp:.9f} GeV, Gamma={g*1000:.6f} MeV, |s/h|={w:.6g}, residual={res:.3g}")
        assert abs(ckin)<1e-10
        assert abs((th-dlam)/dlam)<1e-3
        assert abs((hard-source)/source)<1e-3


if __name__=="__main__":
    main()
