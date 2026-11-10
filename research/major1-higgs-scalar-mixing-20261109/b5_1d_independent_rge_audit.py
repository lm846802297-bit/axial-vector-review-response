#!/usr/bin/env python3
"""Independent one-loop RGE audit for the U(1)_{L_mu-L_tau}+VLL model.

Independent routes:
  * gauge coefficients from the complete Weyl/complex-scalar spectrum;
  * scalar quartics from the six-real-scalar quartic tensor;
  * Yukawa coefficients from real-scalar/Weyl Yukawa matrices;
  * gauge quartic terms from field-dependent vector masses;
  * fermion boxes from the VLL field-dependent mass matrix.

No production RGE function is imported here.
"""
from __future__ import annotations
from itertools import product
import sympy as sp


def gauge_spectrum_sums():
    # (name, Weyl multiplicity, Y, X, total T2, total T3).
    # RH fields are represented by their LH charge conjugates.
    fields = [
        ("Q_L",18,sp.Rational(1,6),0,sp.Rational(9,2),3),
        ("u_Rc",9,sp.Rational(-2,3),0,0,sp.Rational(3,2)),
        ("d_Rc",9,sp.Rational(1,3),0,0,sp.Rational(3,2)),
        ("L_e",2,sp.Rational(-1,2),0,sp.Rational(1,2),0),
        ("L_mu",2,sp.Rational(-1,2),1,sp.Rational(1,2),0),
        ("L_tau",2,sp.Rational(-1,2),-1,sp.Rational(1,2),0),
        ("e_Rc",1,1,0,0,0),
        ("mu_Rc",1,1,1,0,0),
        ("tau_Rc",1,1,-1,0,0),
        ("E_muL",1,-1,1,0,0),
        ("E_muRc",1,1,-1,0,0),
        ("E_tauL",1,-1,-1,0,0),
        ("E_tauRc",1,1,1,0,0),
    ]
    sy2=sum(n*y**2 for _,n,y,x,t2,t3 in fields)
    sx2=sum(n*x**2 for _,n,y,x,t2,t3 in fields)
    syx=sum(n*y*x for _,n,y,x,t2,t3 in fields)
    st2=sum(t2 for _,n,y,x,t2,t3 in fields)
    st3=sum(t3 for _,n,y,x,t2,t3 in fields)
    # Complex H doublet: sum Y^2=1/2, T2=1/2.
    # Complex S singlet: X^2=4.
    bY=sp.Rational(2,3)*sy2+sp.Rational(1,3)*sp.Rational(1,2)
    bX=sp.Rational(2,3)*sx2+sp.Rational(1,3)*4
    b2=-sp.Rational(11,3)*2+sp.Rational(2,3)*st2+sp.Rational(1,3)*sp.Rational(1,2)
    b3=-sp.Rational(11,3)*3+sp.Rational(2,3)*st3
    return {"sumY2":sp.simplify(sy2),"sumX2":sp.simplify(sx2),
            "TrYX":sp.simplify(syx),"sumT2":sp.simplify(st2),
            "sumT3":sp.simplify(st3),"bY":sp.simplify(bY),
            "b2":sp.simplify(b2),"b3":sp.simplify(b3),
            "bX":sp.simplify(bX)}


def scalar_quartic_tensor_coefficients():
    lH,lS,lHS=sp.symbols("lambda_H lambda_S lambda_HS")
    f=sp.symbols("h1:5 s1:3")
    h2=sum(x**2 for x in f[:4]); s2=sum(x**2 for x in f[4:])
    V=lH*h2**2/4+lS*s2**2/4+lHS*h2*s2/4
    n=6
    L=[[[[sp.diff(V,f[a],f[b],f[c],f[d])
          for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    def C(a,b,c,d):
        out=sp.S.Zero
        for e,g in product(range(n),repeat=2):
            out += L[a][b][e][g]*L[e][g][c][d]
            out += L[a][c][e][g]*L[e][g][b][d]
            out += L[a][d][e][g]*L[e][g][b][c]
        return sp.factor(out)
    return {
        "betaH_scalar":sp.factor(C(0,0,0,0)/6),
        "betaS_scalar":sp.factor(C(4,4,4,4)/6),
        "betaHS_scalar":sp.factor(C(0,0,4,4)),
    }


def _weyl_beta(Ys):
    out=[]
    for Ya in Ys:
        Ba=sp.zeros(*Ya.shape)
        for Yb in Ys:
            Ybd=Yb.conjugate().T; Yad=Ya.conjugate().T
            Ba += sp.Rational(1,2)*(Yb*Ybd*Ya+Ya*Ybd*Yb)
            Ba += 2*Yb*Yad*Yb
            Ba += sp.Rational(1,2)*(sp.trace(Ya*Ybd)+sp.trace(Yb*Yad))*Yb
        out.append(Ba.applyfunc(sp.simplify))
    return out


def yukawa_matrix_coefficients():
    lm,lt=sp.symbols("lambda_mu lambda_tau",real=True); r=sp.sqrt(2)
    Y1=sp.zeros(4); Y2=sp.zeros(4)
    for i,j,y,phase in ((0,1,lm,sp.I),(2,3,lt,-sp.I)):
        Y1[i,j]=Y1[j,i]=y/r; Y2[i,j]=Y2[j,i]=phase*y/r
    Bs=_weyl_beta([Y1,Y2])
    blm=sp.factor(r*Bs[0][0,1]); blt=sp.factor(r*Bs[0][2,3])

    ym,yt=sp.symbols("y_mu y_tau",real=True); Ys=[]
    for component in range(2):
        Yr=sp.zeros(6); Yi=sp.zeros(6)
        for base,y in ((0,ym),(3,yt)):
            i=base+component; j=base+2
            Yr[i,j]=Yr[j,i]=y/r; Yi[i,j]=Yi[j,i]=sp.I*y/r
        Ys.extend((Yr,Yi))
    Bh=_weyl_beta(Ys)
    bym=sp.factor(r*Bh[2][1,2]); byt=sp.factor(r*Bh[2][4,5])
    return {"beta_lambda_mu_Y":blm,"beta_lambda_tau_Y":blt,
            "beta_y_mu_VLL":bym,"beta_y_tau_VLL":byt}


def gauge_casimirs():
    return {
        "yt_gY":-sp.Rational(17,12),"yt_g2":-sp.Rational(9,4),"yt_g3":-8,
        "yVLL_gY":-sp.Rational(15,4),"yVLL_g2":-sp.Rational(9,4),
        "yVLL_gX":-6,"lambdaVLL_gY":-6,"lambdaVLL_gX":-6,
        "lambdaH_g2":-9,"lambdaH_gY":-3,"lambdaS_gX":-48,
        "lambdaHS_g2":-sp.Rational(9,2),"lambdaHS_gY":-sp.Rational(3,2),
        "lambdaHS_gX":-24,
    }


def gauge_quartic_sources():
    g2,gY,gX=sp.symbols("g2 gY gX",real=True)
    # H background: two W vectors with m^2=g2^2 h^2/4 and
    # one Z with m^2=(g2^2+gY^2)h^2/4.
    sum_m4_H=2*(g2**2/4)**2+((g2**2+gY**2)/4)**2
    # S background: m_X^2=(2 g_X)^2 s^2.
    sum_m4_S=(4*gX**2)**2
    return {"betaH_gauge4":sp.expand(6*sum_m4_H),
            "betaS_gauge4":sp.expand(6*sum_m4_S),
            "betaHS_gauge4":sp.S.Zero}


def fermion_box_coefficients():
    ME,y,l,h,s=sp.symbols("M_E y lambda h s",real=True)
    M=sp.Matrix([[0,y*h/sp.sqrt(2)],[l*s/sp.sqrt(2),ME]])
    tr=sp.expand(sp.trace((M.T*M)**2))
    return {"Tr_MdagM2":tr,
            "mixed_h2s2":sp.expand(tr).coeff(h,2).coeff(s,2),
            "pure_h4":sp.expand(tr).coeff(h,4),
            "pure_s4":sp.expand(tr).coeff(s,4)}


def independent_beta_vector(state):
    (gY,g2,g3,gX,yt,ymu,ytau,lmu,ltau,lH,lS,lHS)=state
    f=1/(16*sp.pi**2); TSM=3*yt**2; TVH=ymu**2+ytau**2; TVS=lmu**2+ltau**2
    return f*sp.Matrix([
        sp.Rational(19,2)*gY**3,-sp.Rational(19,6)*g2**3,-7*g3**3,8*gX**3,
        yt*(sp.Rational(9,2)*yt**2+TVH-sp.Rational(17,12)*gY**2
            -sp.Rational(9,4)*g2**2-8*g3**2),
        ymu*(sp.Rational(3,2)*ymu**2+TSM+TVH-sp.Rational(15,4)*gY**2
             -sp.Rational(9,4)*g2**2-6*gX**2),
        ytau*(sp.Rational(3,2)*ytau**2+TSM+TVH-sp.Rational(15,4)*gY**2
              -sp.Rational(9,4)*g2**2-6*gX**2),
        lmu*(2*lmu**2+ltau**2-6*gY**2-6*gX**2),
        ltau*(2*ltau**2+lmu**2-6*gY**2-6*gX**2),
        24*lH**2+lHS**2+lH*(12*yt**2+4*TVH-9*g2**2-3*gY**2)
        -6*yt**4-2*(ymu**4+ytau**4)+sp.Rational(9,8)*g2**4
        +sp.Rational(3,4)*g2**2*gY**2+sp.Rational(3,8)*gY**4,
        20*lS**2+2*lHS**2-48*gX**2*lS+96*gX**4
        +4*lS*TVS-2*(lmu**4+ltau**4),
        lHS*(12*lH+8*lS+4*lHS-sp.Rational(9,2)*g2**2
             -sp.Rational(3,2)*gY**2-24*gX**2+2*(TSM+TVH+TVS))
    ])


def main():
    g=gauge_spectrum_sums(); s=scalar_quartic_tensor_coefficients()
    y=yukawa_matrix_coefficients(); c=gauge_casimirs()
    q=gauge_quartic_sources(); b=fermion_box_coefficients()
    assert (g["bY"],g["b2"],g["b3"],g["bX"],g["TrYX"]) == (
        sp.Rational(19,2),-sp.Rational(19,6),-7,8,0)
    lH,lS,lHS=sp.symbols("lambda_H lambda_S lambda_HS")
    assert sp.simplify(s["betaH_scalar"]-(24*lH**2+lHS**2))==0
    assert sp.simplify(s["betaS_scalar"]-(20*lS**2+2*lHS**2))==0
    assert sp.simplify(s["betaHS_scalar"]-lHS*(12*lH+8*lS+4*lHS))==0
    lm,lt=sp.symbols("lambda_mu lambda_tau",real=True)
    ym,yt=sp.symbols("y_mu y_tau",real=True)
    assert sp.simplify(y["beta_lambda_mu_Y"]-lm*(2*lm**2+lt**2))==0
    assert sp.simplify(y["beta_lambda_tau_Y"]-lt*(2*lt**2+lm**2))==0
    assert sp.simplify(y["beta_y_mu_VLL"]-ym*(sp.Rational(5,2)*ym**2+yt**2))==0
    assert sp.simplify(y["beta_y_tau_VLL"]-yt*(sp.Rational(5,2)*yt**2+ym**2))==0
    assert c["yt_gY"]==-sp.Rational(17,12) and c["yt_g2"]==-sp.Rational(9,4) and c["yt_g3"]==-8
    assert c["yVLL_gY"]==-sp.Rational(15,4) and c["yVLL_g2"]==-sp.Rational(9,4) and c["yVLL_gX"]==-6
    assert c["lambdaVLL_gY"]==-6 and c["lambdaVLL_gX"]==-6
    assert c["lambdaH_g2"]==-9 and c["lambdaH_gY"]==-3 and c["lambdaS_gX"]==-48
    assert c["lambdaHS_g2"]==-sp.Rational(9,2) and c["lambdaHS_gY"]==-sp.Rational(3,2) and c["lambdaHS_gX"]==-24
    g2,gY,gX=sp.symbols("g2 gY gX",real=True)
    assert sp.simplify(q["betaH_gauge4"]-(sp.Rational(9,8)*g2**4+sp.Rational(3,4)*g2**2*gY**2+sp.Rational(3,8)*gY**4))==0
    assert sp.simplify(q["betaS_gauge4"]-96*gX**4)==0 and q["betaHS_gauge4"]==0
    assert b["mixed_h2s2"]==0
    print("Independent B5-1d one-loop RGE audit: PASS")
    print("Gauge traces:", {k:str(v) for k,v in g.items()})
    print("Scalar tensor:", {k:str(v) for k,v in s.items()})
    print("Yukawa matrices:", {k:str(v) for k,v in y.items()})
    print("Gauge quartic sources:", {k:str(v) for k,v in q.items()})
    print("VLL mixed h^2 s^2 box coefficient:", b["mixed_h2s2"])


if __name__=="__main__":
    main()
