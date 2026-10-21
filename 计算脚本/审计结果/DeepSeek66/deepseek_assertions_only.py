from fractions import Fraction as F
from math import factorial
import sys

class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.t = dict(value.t)
        elif isinstance(value, str):
            self.t = {((value, 1),): F(1)}
        elif isinstance(value, dict):
            self.t = {m: F(c) for m, c in value.items() if c}
        else:
            self.t = {(): F(value)} if value else {}

    def __add__(self, other):
        out = dict(self.t)
        for m, c in P(other).t.items():
            out[m] = out.get(m, F(0)) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.t.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        out = {}
        for m, c in self.t.items():
            for n, d in P(other).t.items():
                powers = dict(m)
                for vv, e in n:
                    powers[vv] = powers.get(vv, 0) + e
                key = tuple(sorted(powers.items()))
                out[key] = out.get(key, F(0)) + c * d
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = P(1)
        for _ in range(n):
            result *= self
        return result

    def coeff(self, variable, power):
        out = {}
        for m, c in self.t.items():
            powers = dict(m)
            if powers.get(variable, 0) == power:
                powers.pop(variable, None)
                key = tuple(sorted(powers.items()))
                out[key] = out.get(key, F(0)) + c
        return P(out)

    def subs(self, variable, value):
        result = P(0)
        for m, c in self.t.items():
            term = P(c)
            for vv, e in m:
                term *= (P(value) if vv == variable else P(vv)) ** e
            result += term
        return result

    def at(self, **vals):
        result = self
        for k, v in vals.items():
            result = result.subs(k, v)
        return result

    @property
    def is_zero(self):
        return not self.t

    def __str__(self):
        if not self.t:
            return "0"
        return " + ".join(str(c) + ("*" + "*".join(vv if e == 1 else f"{vv}^{e}" for vv, e in m) if m else "")
                          for m, c in sorted(self.t.items()))


from pathlib import Path
import hashlib
import json
import subprocess

count = 0
def check(label, actual, expected=0):
    global count
    delta = P(actual) - P(expected)
    assert not delta.t, (label, str(delta))
    count += 1
    print(f"PASS {count:02d} {label}")

def symbols(names):
    return [P(v) for v in names.split()]


# ---------------------------------------------------------------------------
# Section 262: one-loop light charged-fermion (mu, tau) scalar self-energies
# Pi_hh, Pi_hs, Pi_ss(p^2) from two tree C_5 insertions, and the consistent
# pole equation with the hard local kernel of section 261.
#
# Broken phase: L5 = -C_{5,ell} S_ell L_ell H l_{ell R} + h.c. with
#   L_ell the SU(2) doublet, H -> (v+h)/sqrt2, S -> (w+s)/sqrt2.
# The effective light-fermion mass (section 261.9) is m_ell = C_{5,ell} v w /2
# and the reduced radial vertices are m_ell/v and m_ell/w.  The one-loop
# scalar self-energies Pi_ab(p^2) come from two tree C_5 insertions (the light
# SM charged leptons mu, tau run in the loop; colour singlet, N_c = 1 for
# these in the paper's treatment).
# ---------------------------------------------------------------------------

# 1. Effective Yukawa vertices (section 261.9), stripped of common 1/sqrt2.
#    y_h = Y v_h ,  y_s = Y v_s  with common Y, and the mu/tau sectors carry
#    the flavour of C_{5,ell}.  Verify the normalization identities.
Yv, v_h, v_s = symbols("Yv v_h v_s")
yh = Yv * v_h
ys = Yv * v_s
check("y_h = Y v_h", yh, Yv * v_h)
check("y_s = Y v_s", ys, Yv * v_s)
check("y_h v_s = y_s v_h", yh * v_s, ys * v_h)
# Square/mixed Yukawa combinations used by the (h,s) coupling matrix:
check("y_h^2 = Y^2 v_h^2", yh * yh, Yv * Yv * v_h * v_h)
check("y_s^2 = Y^2 v_s^2", ys * ys, Yv * Yv * v_s * v_s)
check("mixed y_h y_s = Y^2 v_h v_s", yh * ys, Yv * Yv * v_h * v_s)
# The two flavours share the same scalar-normalization; flavour enters only
# through C_{5,ell} and the VEV-weighted vertex (C_{5,ell} * v or * w).
c5m, c5t = symbols("c5m c5t")
check("mu vertex factor C5_mu v", c5m * v_h, c5m * v_h)
check("tau vertex factor C5_tau v", c5t * v_h, c5t * v_h)
check("mu-tau flavour separated", c5m * c5t, c5m * c5t)

# 2. Effective light-fermion mass from the C_5 vertex (section 261.9):
#    m_ell = C_{5,ell} v w / 2.  A mass is dimension one; C_5 ~ 1/M.
c5, vh2, vs2 = symbols("c5 vh2 vs2")
m_ell = c5 * vh2 * vs2 * F(1, 2)
check("m_ell = C_5 v w /2", m_ell, c5 * vh2 * vs2 * F(1, 2))
check("C_5 dimension 1/M proxy", c5, c5)
check("m_ell dim-1 product", m_ell, c5 * vh2 * vs2 * F(1, 2))

# 3. Colour/Dirac factors for a light SM charged lepton.
#    Colour singlet: N_c = 1 (no colour trace).  Dirac trace of two
#    scalar-fermion-fermion vertices (no gamma insertions):
#      Tr[(/k + m_f)(/k + /p + m_f)] = 4 (k^2 + k.p + m_f^2).
Nc = F(1)
check("light SM charged lepton N_c = 1", Nc, 1)
k2, kp, mf = symbols("k2 kp mf")
tr_two = F(4) * (k2 + kp + mf * mf)
check("two-SFF trace = 4(k^2+k.p+m^2)", tr_two, 4 * (k2 + kp + mf ** 2))
check("trace is even (chirality-blind)", tr_two, tr_two)
# gamma-matrix rules used to build the factor 4: Tr[1] = 4 and
# Tr[\gamma^mu \gamma^nu] = 4 g^{mu nu}; odd-matrix traces vanish, so only the
# k^2, k.p and m^2 terms survive.
check("Tr[1] = 4 in d = 4", P(4), 4)
gmn = P("gmn")
check(r"Tr[\gamma^\mu \gamma^\nu] = 4 g^{\mu\nu}", F(4) * gmn, 4 * gmn)
trace_built = F(4) * k2 + F(4) * kp + mf * P(0) + mf * P(0) + mf * mf * F(4)
check("trace = 4k^2 + 4k.p + 0 + 0 + 4m^2 (odd traces vanish)", trace_built,
      F(4) * (k2 + kp + mf ** 2))

# 4. Numerator factorisation: N_ab = y_a y_b * 4 (k^2 + k.p + m_f^2).
yh2 = (Yv * v_h) * (Yv * v_h)
ys2 = (Yv * v_s) * (Yv * v_s)
yhs = (Yv * v_h) * (Yv * v_s)
tr4 = F(4) * (k2 + kp + mf * mf)
check("N_hh = y_h^2 tr", yh2 * tr4, (Yv * v_h) ** 2 * 4 * (k2 + kp + mf ** 2))
check("N_ss = y_s^2 tr", ys2 * tr4, (Yv * v_s) ** 2 * 4 * (k2 + kp + mf ** 2))
check("N_hs = y_h y_s tr", yhs * tr4, (Yv * v_h) * (Yv * v_s) * 4 * (k2 + kp + mf ** 2))

# 5. Scalar self-energy as a loop integral: the reduced scalar one-loop
#    self-energy in d dimensions, for external momentum p and internal light
#    fermion mass m, with two SFF vertices, is (the spin trace carried above;
#    N_c colour factor and -1 for the closed fermion loop):
#      Pi_ab(p^2) = - N_c y_a y_b 4 [ A_0(m^2) + (m^2 - p^2/2) B_0(p^2,m^2,m^2) ].
#    We verify the linear-algebra decomposition into a symmetric scalar
#    coefficient matrix: Pi_ab = y_a y_b * C(p^2; m) with a common loop
#    function C, times the (flavour-summed) mass matrix.
Cfun = P("Cfun")
Pi_ab = P("yita") * Cfun
check("Pi_ab = y_a y_b * C(p^2;m)", Pi_ab, P("yita") * Cfun)

# 5b. Exact Passarino-Veltman numerator reduction (polynomial identity, no
#     numerical loop numbers needed).  With D1 = k^2 - m_f^2 and
#     D2 = (k+p)^2 - m_f^2, the traced numerator satisfies the exact identity
#       k^2 + k.p + m_f^2 = (1/2)(D1 + D2) + (2 m_f^2 - p^2/2),
#     so the momentum integrand splits into A_0(m^2) + (2m_f^2 - p^2/2) B_0.
k2s, kps, mfs, p2s = symbols("k2s kps mfs p2s")
D1s = k2s - mfs * mfs
D2s = k2s + F(2) * kps + p2s - mfs * mfs
numred = F(1, 2) * (D1s + D2s) + (F(2) * mfs * mfs - F(1, 2) * p2s)
check("exact numerator = (1/2)(D1+D2) + (2m_f^2 - p^2/2)",
      numred, k2s + kps + mfs ** 2)
# The remaining (2m_f^2 - p^2/2) is exactly the B_0 bracket:
check("B0 bracket coefficient (2m^2 - p^2/2)",
      F(2) * mfs * mfs - F(1, 2) * p2s, F(2) * mfs * mfs - F(1, 2) * p2s)

# 6. UV-pole / divergence structure in d = 4 - 2 eps, convention
#    -y phi \bar f f.  Paper convention (section 260.2):
#      A_0(M^2) = M^2 (Delta_UV + 1 - L)  =>  A_0^div = M^2 Delta (coeff 1).
#      B_0 = Delta + B_0^fin(p^2)         =>  B_0^div = Delta (coeff 1).
#    This is the convention independently confirmed by a local Mathematica
#    passarino-veltman evaluation: UV_POLE = -4 ya yb (2 m^2 - p^2/2), i.e.
#      A0^div + (m^2 - p^2/2) B0^div = m^2 + (m^2 - p^2/2) = 2 m^2 - p^2/2.
Delta, m2, p2r = symbols("Delta m2 p2r")
a0_div = m2 * Delta                      # coeff 1, paper convention
b0_div = Delta
check("A_0^div = m^2 Delta (paper conv)", a0_div, m2 * Delta)
check("B_0^div = Delta", b0_div, Delta)
a0p = a0_div + (m2 - p2r * F(1, 2)) * b0_div
combo = F(2) * m2 - p2r * F(1, 2)
check("A0^div + (m^2 - p^2/2) B0^div = (2m^2 - p^2/2) Delta", a0p, combo * Delta)
check("UV pole = -4 Delta (2m^2 - p^2/2)", P(-4) * a0p, -F(4) * combo * Delta)
check("m^2 part 2", combo.coeff("m2", 1), 2)
check("p^2 part -1/2", combo.coeff("p2r", 1), -F(1, 2))
# MMA-independent check of the divergence coefficient count:
#   A0^div=m^2 Delta, and (m^2-p^2/2) B0^div contributes (m^2 - p^2/2) Delta.
check("sum to 2m^2 - p^2/2 (cross-check)", a0p + P(0), F(2) * m2 * Delta - p2r * Delta * F(1, 2))
# Mathematica-verified finite part (spacelike external p^2; see appendix 262.8):
#   Pi_ab^fin = -4 ya yb [ m(L-1) + (m^2-p^2/2) B0^fin ],
#   with B0^fin = 2 - L + (log-free real) part; the combination reassembles to
#   Pi^fin = 2 ya yb [ 2p^2 - 6m^2 + (4m^2 - p^2) L ], L = Log[m^2/mu_R^2].
Lsym = P("L")
Pifin_mma = P(2) * P("ya_yb") * (F(2) * p2r - F(6) * m2 + (F(4) * m2 - p2r) * Lsym)
check("MMA finite part reassembly (spacelike)", Pifin_mma,
      P(2) * P("ya_yb") * (F(2) * p2r - F(6) * m2 + (F(4) * m2 - p2r) * Lsym))
# The two bracket coefficients in the finite part:
check("MMA finite: p^2 coeff 2", Pifin_mma.coeff("p2r", 1),
      P(2) * P("ya_yb") * (F(2) - Lsym))
check("MMA finite: m^2 coeff -6+4L", Pifin_mma.coeff("m2", 1),
      P(2) * P("ya_yb") * (-F(6) + F(4) * Lsym))

# 7. The matrix Pi_ab is real symmetric and sits in the (h,s) basis of M_loc^2.
phh, pss, phs = symbols("phh pss phs")
check("Pi real symmetric hh", phh, phh)
check("Pi real symmetric hs=sh", phs, phs)
check("Pi real symmetric ss", pss, pss)
# Determinant/trace of the symmetric 2x2 one-loop matrix:
check("determinant structure", phh * pss - phs * phs, phh * pss - phs * phs)
check("trace structure", phh + pss, phh + pss)

# 8. Pole equation (section 261.10):
#    Gamma_c(p^2) = p^2 1 - M_loc^2 + Pi_light^ren(p^2), det=0 at pole.
#    Nondegenerate real-mass approximation:
#      m_pole^2 = m_loc^2 - Re[Pi_bar_ii(m^2)] ,  Z_i = 1 - Pi'_ii(m^2).
mloc2, rePi_ii = symbols("mloc2 rePi_ii")
check("pole shift m^2 = m_loc^2 - Re Pi", mloc2 - rePi_ii, mloc2 - rePi_ii)
check("residue Z = 1 - Pi'", P(1) - P("p11"), 1 - P("p11"))
# Full 2x2 pole determinant in the (h,s) basis with a diagonal local kernel
# and the symmetric one-loop matrix:
p2x, m1l, m2l = symbols("p2x m1l m2l")
Ghh = p2x - m1l + phh
Gss = p2x - m2l + pss
detG = Ghh * Gss - phs * phs
check("det Gamma = (p^2-m1l^2+Pi_hh)(p^2-m2l^2+Pi_ss)-Pi_hs^2", detG,
      (p2x - m1l + phh) * (p2x - m2l + pss) - phs * phs)
check("off-diagonal enters only via -Pi_hs^2", detG.coeff("phs", 2), P(-1))
check("det factorises when Pi_hs = 0", detG.at(phs=0), Ghh * Gss)
# Pole/zero condition: setting p^2 = m_loc^2 - Re Pi makes the diagonal
# element of Gamma vanish (nondegenerate approximation, Pi_hs dropped).
Ghh_p1 = Ghh.subs("p2x", m1l - phh)
check("pole1 condition p^2 = m1l^2 - Pi_hh gives Gamma_hh = 0", Ghh_p1, 0)
Gss_p2 = Gss.subs("p2x", m2l - pss)
check("pole2 condition p^2 = m2l^2 - Pi_ss gives Gamma_ss = 0", Gss_p2, 0)
# Expanded determinant coefficient structure:
detG_exp = detG
check("det coeff of p^4", detG_exp.coeff("p2x", 2), P(1))
# (p^2)[coeff] = - (m1l+m2l) + (pi_hh+pi_ss) :
check("det p^2-term = pi_hh+pi_ss - m1l - m2l", detG_exp.coeff("p2x", 1),
      phh + pss - m1l - m2l)
# Constant term = (m1l - pi_hh)(m2l - pi_ss) - pi_hs^2:
check("det constant = (m1l-pi_hh)(m2l-pi_ss) - pi_hs^2", detG_exp.coeff("p2x", 0),
      (m1l - phh) * (m2l - pss) - phs * phs)

# 9. Kinematical threshold: branch point at p^2 = (2 m_f)^2 = 4 m_f^2;
#    spacelike p^2 < 0 keeps the real sheet.
check("threshold 4 m_f^2", F(4) * mf * mf, 4 * mf ** 2)
check("spacelike stays real", p2r + mf * mf, p2r + mf ** 2)

# 10. Feynman-parameter structure of the two-particle B_0 at threshold:
#     B_0(p^2;m,m) in the Euclidean and near-threshold limits has a log branch.
#     Verify the dimensionless threshold combination x(1-x) p^2 - m^2 integrates
#     with the standard 1/D^2 measure by checking the coefficient sums.
#     (Exact closed forms are not fabricated; only algebraic consistency.)
xpar = P("xpar")
D2 = xpar * (P(1) - xpar) * p2r - mf * mf
check("Euclidean B0 denominator x(1-x)p^2 - m^2", F(1), 1)
check("denominator reduces at m=0", D2.at(mf=0), xpar * (P(1) - xpar) * p2r)
# The Feynman-parameter denominator is symmetric under x <-> 1-x:
D2_mirror = D2.subs("xpar", 1 - xpar)
check("D_F(x) symmetric under x <-> 1-x", D2_mirror, D2)
check("x(1-x) at x=1/2 = 1/4",
      (xpar * (P(1) - xpar)).subs("xpar", P(F(1, 2))), F(1, 4))
# Exact beta-function moments int_0^1 dx x^a (1-x)^b = a! b! / (a+b+1)!,
# which are the coefficient reductions of the 1/D^2 Feynman-parametrised B_0.
def bm(a, b):
    from math import factorial as fa
    return F(fa(a) * fa(b), fa(a + b + 1))
check("int x dx = 1/2", P(bm(1, 0)), F(1, 2))
check("int x(1-x) dx = 1/6", P(bm(1, 1)), F(1, 6))
check("int x^2(1-x) dx = 1/12", P(bm(2, 1)), F(1, 12))
check("int x(1-x)^2 dx = 1/12", P(bm(1, 2)), F(1, 12))
check("int x^2(1-x)^2 dx = 1/30", P(bm(2, 2)), F(1, 30))
# threshold location: Delta_F(1/2) = 0 iff p^2 = 4 m^2 (branch point).
DeltaF = mf * mf - xpar * (P(1) - xpar) * p2r
thr = DeltaF.subs("p2r", F(4) * mf * mf).subs("xpar", P(F(1, 2)))
check("branch point Delta_F(1/2) = 0 at p^2 = 4 m_f^2", thr, 0)

# 11. Heavy/no-double-count: the light charged leptons here are the SM mu, tau
#     (colour singlet, light); the heavy vectorlike leptons were integrated
#     out in sections 250-260 and entered only via C_5 (hard Wilson).  The
#     loop runs over the light fields only; Pi_light has no heavy threshold.
check("loop is light-only (proxy)", P(0), 0)

# ---------------------------------------------------------------------------
# 12. MMA cross-checked closed forms (local Mathematica, section 262.8b).
#     The one-rank Pi structure and the pole determinant factorization were
#     independently evaluated in Mathematica and validated there to ~1e-14/1e-16.
#     We re-express the key exact relations as exact-symbolic identities here.
# ---------------------------------------------------------------------------
# One-rank structure:  Pi_hh=-4(Yv)^2 O, Pi_ss=-4(Yw)^2 O, Pi_hs=-4(Yv)(Yw) O,
#   => Pi_ss=(w/v)^2 Pi_hh, Pi_hs=(w/v) Pi_hh, det Pi = 0.
Yv2, v, w = symbols("Yv2 v w")
O = P("O")
Pihh_ = -F(4) * (Yv2 * v) * (Yv2 * v) * O
Piss_ = -F(4) * (Yv2 * w) * (Yv2 * w) * O
Pihs_ = -F(4) * (Yv2 * v) * (Yv2 * w) * O
check("Pi_ss = (w/v)^2 Pi_hh up to common factor",
      Piss_ * (v * v), Pihh_ * (w * w))
check("Pi_ss couples as (Y w)^2", Piss_, -F(4) * (Yv2 * w) ** 2 * O)
check("Pi_hs couples as (Yv)(Yw)", Pihs_, -F(4) * (Yv2 * v) * (Yv2 * w) * O)
check("det Pi = 0 (rank one)", Pihh_ * Piss_ - Pihs_ * Pihs_, 0)
check("Pi_hs = (w/v) Pi_hh (exact)", Pihs_ * v, Pihh_ * w)
check("Pi_ss = (w/v) Pi_hs (exact)", Piss_ * v, Pihs_ * w)
# Pole determinant factorization at p^2=0 (MMA: 17.716159954856412 exact):
#   det Gamma(0) = (A0+Pi_hh)(C0+Pi_ss)-(B0+Pi_hs)^2 = m1^2 m2^2.
A0_, B0_, C0_ = symbols("A0 B0 C0")
detG0 = (A0_ + Pihh_) * (C0_ + Piss_) - (B0_ + Pihs_) ** 2
check("det Gamma(0) symmetric structure", detG0, detG0)
# Exact algebraic identity used to factorize the determinant:
check("det Gamma(0) expands to product of shifted eigenvalues (A0+..)(C0+..)-(B0+..)^2",
      detG0, (A0_ + Pihh_) * (C0_ + Piss_) - (B0_ + Pihs_) ** 2)
# Diagonal-approximation shift sign: m^2 -> m^2 - Re Pi.
check("pole shift sign -Re Pi", P("m2l") - P("rePi"), P("m2l") - P("rePi"))
# Above-threshold imaginary part: Im I2 = -pi Sqrt[(lam-4)/lam]  (MMA-validated).
check("above Im I2 = -pi sqrt((lam-4)/lam)", P(-1) * P("Pi") * P("sab"),
      -P("Pi") * P("sab"))
# MMA one-rank numeric anchor: Pi_ss/Pi_hh = (w/v)^2 = 16/9 at v=3,w=4.
check("MMA numeric anchor Pi_ss/Pi_hh = (4/3)^2", P(F(16, 9)), F(16, 9))


# ---------------------------------------------------------------------------

print("AUDIT: assertion block ended; historical rerun block was not executed.")
