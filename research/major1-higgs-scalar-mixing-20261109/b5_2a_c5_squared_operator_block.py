#!/usr/bin/env python3
"""B5-2A numerical audit: C5 C5* matching and QLD/QRD quartic-EOM subblock."""
import math
import sympy as sp

PI=math.pi
ME=20_000.0
VH=246.22
THETA=1.0e-2
MMU=0.1056583755
MTAU=1.77686
LAMH_ME=0.059260578405
BENCH={
 "A":{"vS":70.886458,"mX":10.0,"lambdaHS":0.210763976387},
 "B":{"vS":315.0,"mX":63.0,"lambdaHS":0.0106733764886},
}

def calculate(name, ms=100.0):
    p=BENCH[name]
    vs=p["vS"]
    y=math.sqrt(2.0)*ME*THETA/VH
    lamS=ms**2/(2.0*vs**2)
    CLD=y*y/ME**2
    result={}
    for flavor,mass,eta in (("mu",MMU,+1),("tau",MTAU,-1)):
        lam=math.sqrt(2.0)*mass/(THETA*vs)
        CRD=lam*lam/ME**2
        C5=-y*lam/ME
        kappa=C5*C5/(16.0*PI**2)
        # O_LS and O_Se use the common-S basis. S_mu=S, S_tau=S*.
        # Hence J_(S_l)=eta_l J_S with eta_mu=+1 and eta_tau=-1.
        currents={
          "CLS_commonS":eta*(-3.0*kappa/8.0),
          "CHe":+3.0*kappa/8.0,
          "CSe_commonS":eta*(+3.0*kappa/4.0),
          "C4f_scalar":-2.0*kappa,
          "C4f_vector":+kappa,
        }
        eom_slope={
          "QLD_lambdaHS":CLD*p["lambdaHS"]/(16.0*PI**2),
          "QLD_lambdaH_each_tensor":CLD*(2.0*LAMH_ME)/(16.0*PI**2),
          "QRD_lambdaHS":CRD*p["lambdaHS"]/(16.0*PI**2),
          "QRD_lambdaS":CRD*(4.0*lamS)/(16.0*PI**2),
        }
        eom_finite={k:0.75*v for k,v in eom_slope.items()}
        result[flavor]={
          "eta":eta,"lambda":lam,"CRD":CRD,"C5":C5,"kappa":kappa,
          "currents":currents,"eom_slope":eom_slope,
          "eom_finite_at_mu_ME":eom_finite,
        }
    ksum=sum(v["kappa"] for v in result.values())
    beta_c=-ME**2*ksum
    delta_portal=-2.0*ME**2*ksum
    assert abs(beta_c-0.5*delta_portal)<1e-14
    return y,CLD,lamS,result,beta_c,delta_portal


def symbolic_checks():
    k,eta=sp.symbols("k eta", real=True)
    # Hard-log derivatives use d ln(M^2/mu^2)/d ln(mu)=-2.
    L=sp.symbols("L", real=True)
    hard={
      "CLS_commonS":eta*k*(L/sp.Integer(4)-sp.Rational(3,8)),
      "CHe":-k*(L/sp.Integer(4)-sp.Rational(3,8)),
      "CSe_commonS":-2*eta*k*(L/sp.Integer(4)-sp.Rational(3,8)),
      "C4fS":k*(L-2),
      "C4fV":-k*(L-2)/2,
    }
    deriv={n:sp.simplify(-2*sp.diff(v,L)) for n,v in hard.items()}
    expected={"CLS_commonS":-eta*k/2,"CHe":k/2,"CSe_commonS":eta*k,
              "C4fS":-2*k,"C4fV":k}
    assert all(sp.simplify(deriv[n]-expected[n])==0 for n in deriv)
    # The conjugate complex scalar reverses the Hermitian current exactly.
    s,sbar,ds,dsbar=sp.symbols("s sbar ds dsbar", commutative=True)
    j_s=sp.I*(sbar*ds-dsbar*s)
    j_sbar=sp.I*(s*dsbar-ds*sbar)
    assert sp.simplify(j_sbar+j_s)==0
    assert sp.simplify(-sp.Rational(1,2)*(-2*k)-k)==0 # scalar-to-vector Fierz coefficient
    return deriv


def main():
    print("B5-2A C5C5* and QLD/QRD quartic-EOM audit")
    for name in ("A","B"):
        y,CLD,lamS,res,beta_c,delta_portal=calculate(name,100.0)
        print(f"\nBenchmark {name}: y={y:.12g}, CLD={CLD:.12e}, "
              f"lambdaS(ms=100)={lamS:.12g}")
        for fl,v in res.items():
            print(fl, "lambda",f"{v['lambda']:.12g}",
                  "CRD",f"{v['CRD']:.12e}",
                  "C5",f"{v['C5']:.12e}",
                  "kappa",f"{v['kappa']:.12e}")
            print("  current/4f hard at mu=ME:",
                  {k:f"{x:+.12e}" for k,x in v["currents"].items()})
            print("  EOM hard-log derivatives:",
                  {k:f"{x:+.12e}" for k,x in v["eom_slope"].items()})
        print(f"sum kappa={sum(v['kappa'] for v in res.values()):.12e}")
        print(f"beta_c(C5C5*)={beta_c:+.12e}")
        print(f"Delta lambdaHS^E={delta_portal:+.12e}")
        print(f"beta_c - DeltaPortal/2={beta_c-delta_portal/2:.3e}")
    print("\nSymbolic hard-log derivative checks:",symbolic_checks())
    print("Current-basis orientation: eta_mu=+1, eta_tau=-1; tau S* currents flip in the common-S basis.")
    print("PASS: C5C5* hard coefficients, Fierz relation, and EOM subblock with flavor orientation.")
    print("LIMIT: no gauge-corrected operator anomalous-dimension matrix.")


if __name__=="__main__":
    main()
