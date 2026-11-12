#!/usr/bin/env python3
"""Independent audit of the tree-level s -> A'A', mu+mu-, tau+tau- widths."""
import math

MH=125.25
MMU=0.1056583755
MTAU=1.77686
BENCHMARKS={"A":(70.886458,10.0),"B":(315.0,63.0)}

def gamma_aa(ms,vs,ma):
    if ms<=2*ma:
        return 0.0
    x=(ma/ms)**2
    return ms**3/(32*math.pi*vs**2)*(1-4*x+12*x*x)*math.sqrt(1-4*x)

def gamma_ll(ms,vs,m):
    if ms<=2*m:
        return 0.0
    return m*m*ms/(8*math.pi*vs**2)*(1-4*m*m/ms**2)**1.5

def evaluate(ms,vs,ma):
    aa=gamma_aa(ms,vs,ma)
    mm=gamma_ll(ms,vs,MMU)
    tt=gamma_ll(ms,vs,MTAU)
    return aa,mm,tt,aa+mm+tt

def main():
    for label,(vs,ma) in BENCHMARKS.items():
        mmax=math.sqrt(8*math.pi)*vs
        print(f"Benchmark {label}: v_s={vs:.6f} GeV, m_A'={ma:.6f} GeV, m_s^max={mmax:.6f} GeV")
        for ms in (10.0,100.0,MH,150.0,200.0,mmax):
            aa,mm,tt,total=evaluate(ms,vs,ma)
            print(f"m_s={ms:.6f}: Gamma_AA={aa:.9g}, Gamma_mumu={mm:.9g}, "
                  f"Gamma_tautau={tt:.9g}, Gamma_total={total:.9g} GeV, "
                  f"Gamma_total/m_s={total/ms:.9g}")
        ratio=evaluate(mmax,vs,ma)[-1]/mmax
        assert 0.24<ratio<0.26
        print(f"PASS: width/mass at perturbativity ceiling = {ratio:.9g}")
    # Kinematic thresholds at the Higgs pole.
    assert 2*BENCHMARKS["A"][1] < MH
    assert 2*BENCHMARKS["B"][1] > MH
    print("PASS: h-pole s -> A'A' threshold is open for A and closed for B.")
    print("LIMIT: excludes mixing-induced SM channels, scalar-pair channels, and higher-order corrections.")

if __name__=="__main__":
    main()
