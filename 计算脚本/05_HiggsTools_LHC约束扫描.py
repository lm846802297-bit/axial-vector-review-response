#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================
  05_HiggsTools_LHC约束扫描.py
  HiggsTools 扫描：把"经验阈值"换成真实 LHC 约束
================================================================

目的
----
主文档第 10 节用的实验阈值是**经验值**：
    sin(theta) <~ 0.1 - 0.3        (Higgs 信号强度)
    BR(h -> SS) <~ 10%             (Higgs 不可见/额外衰变)

本脚本用 HiggsTools（HiggsBounds-6 + HiggsSignals-3 的合并库）
把这些换成**合作组级别**的真实拟合，直接回答审稿人 2.1 的要求：
"定量计算 + 现有希格斯测量的限制"。

输出三项（就是审稿人要的答案）
------------------------------
  1) 真实的 sin(theta) 上限            -> 替代 0.1-0.3
  2) 125 GeV 附近排除带的真实宽度       -> 替代我估的 0.87 / 3.47 GeV
  3) M（矢量样轻子质量）的真实上限       -> 替代我估的 1.8 TeV

依赖
----
    pip install higgstools          # 官方 PyPI 包，含预编译二进制
或自行编译：https://higgstools.hepforge.org

输入
----
需要每个参数点的模型预言。两种模式：
  (a) effC 模式：给出 Higgs 耦合标度因子（相对 SM）—— 本脚本默认用这个
  (b) SLHA 模式：从 SPheno/MadGraph 输出读（见文件末尾说明）

本脚本自带一个"由解析公式生成 effC"的生成器，
因此**不需要**先跑 SPheno 就能用 —— 便于快速扫描。

⚠ 免责：HiggsTools 未在本沙盒安装，本脚本**未执行**。
   语法按 HiggsTools 2.x Python API 编写，如报错请把错误信息发回。
================================================================
"""

import numpy as np
import os
import sys

try:
    from higgstools import predictions, bounds, signals
    HAS_HT = True
except ImportError:
    HAS_HT = False
    print("⚠ 未检测到 higgstools。请先：  pip install higgstools")
    print("  本脚本将以'仅计算解析预言'模式运行（不做真实约束检验）。")


# ============================================================
#  0. 物理参数（与主文档一致）
# ============================================================

v     = 246.0        # GeV, Higgs VEV
mh    = 125.0        # GeV, Higgs 质量
mtau  = 1.777        # GeV
mmu   = 0.1057       # GeV
GhSM  = 4.07e-3      # GeV, SM Higgs 总宽度


def lambda_HS_rad(M, vs, m_lep=mtau):
    """
    辐射生成的 Higgs-portal 耦合（主文档主结果）

        lamHS^rad = -(y1 y2)^2 / (8 pi^2)
        y1 y2     = 2 M m_lep / (v v_s)

    注意：与 v, v_s **无关**，只由 y1*y2 决定。
    """
    y1y2 = 2.0 * M * m_lep / (v * vs)
    return -(y1y2 ** 2) / (8.0 * np.pi ** 2)


def dm2_Sh(M, vs, m_lep=mtau):
    """
    一圈诱导的 S-h 质量混合平方（主文档主结果）

        dm2_Sh = -(y1 y2)^2 v v_s / (8 pi^2)
               = - M^2 m_lep^2 / (2 pi^2 v v_s)
    """
    y1y2 = 2.0 * M * m_lep / (v * vs)
    return -(y1y2 ** 2) * v * vs / (8.0 * np.pi ** 2)


def mixing_angle(mS, M, vs, m_lep=mtau):
    """
    sin2theta = 2 dm2_Sh / (m_h^2 - m_S^2)

    ⚠ m_S -> m_h 时此式发散，此时应用简并微扰（theta -> 45 deg）。
      本函数做了截断保护。
    """
    dm2 = abs(dm2_Sh(M, vs, m_lep))
    denom = mh ** 2 - mS ** 2
    if abs(denom) < 1e-6:
        return 1.0          # 简并 => sin2theta -> 1 (theta -> 45 deg)
    s2 = 2.0 * dm2 / abs(denom)
    return min(s2, 1.0)     # 物理上限


def BR_hSS(mS, M, vs, m_lep=mtau):
    """
    h -> SS 分支比（m_S < m_h/2 时开启）

    注意：这条**不需要共振、不依赖混合角**，直接限 lamHS。
    """
    if mS >= mh / 2.0:
        return 0.0
    lam = abs(lambda_HS_rad(M, vs, m_lep))
    beta = np.sqrt(1.0 - 4.0 * mS ** 2 / mh ** 2)
    G = lam ** 2 * v ** 2 / (32.0 * np.pi * mh) * beta
    return G / (GhSM + G)


# ============================================================
#  1. 生成 effC（effective coupling）预言
# ============================================================

def make_effC(mS, M, vs, m_lep=mtau):
    """
    返回 Higgs 有效耦合标度因子字典（相对 SM）。

    有 S-h 混合角 theta 时，125 GeV 的 Higgs 耦合按 cos(theta) 压低：
        c_HVV = c_Hff = cos(theta)

    同时总宽度改变：
        Gamma = cos^2(theta) * Gamma_SM + Gamma(h -> SS)
        （后者在 m_S < m_h/2 时开启）

    标度因子的定义（HiggsSignals effC 约定）：
        c_X^2 = (coupling_X / coupling_X^SM)^2
        对"按总宽度归一"的观测量还要乘 Gamma_SM/Gamma
    """
    s2 = mixing_angle(mS, M, vs, m_lep)
    # sin2theta = s2  =>  sin^2(theta) = (1 - sqrt(1-s2^2))/2
    if s2 >= 1.0:
        sin2th = 0.5
    else:
        sin2th = (1.0 - np.sqrt(1.0 - s2 ** 2)) / 2.0
    cos2th = 1.0 - sin2th
    cos_th = np.sqrt(cos2th)

    br_ss = BR_hSS(mS, M, vs, m_lep)

    # 宽度比
    #  Gamma = cos^2 * Gamma_SM + Gamma_SS ;  Gamma_SS = br_ss/(1-br_ss) * cos^2 * Gamma_SM
    #  为简单起见直接用 BR 定义：Gamma_tot = cos^2*Gamma_SM/(1-br_ss)
    Gamma_ratio = cos2th / (1.0 - br_ss) if br_ss < 1.0 else np.inf

    return {
        "mh":      mh,
        "Gamma_ratio": Gamma_ratio,     # Gamma_tot / Gamma_SM
        "c_HZZ":   cos_th,
        "c_HWW":   cos_th,
        "c_Hbb":   cos_th,
        "c_Htautau": cos_th,
        "c_Hmumu":  cos_th,
        "c_Hgg":   cos_th,              # 近似：只含 SM 粒子圈时同样压低
        "c_Hgamgam": cos_th,
        "BR_SS":   br_ss,
        "sin2theta": s2,
        "lamHS":   abs(lambda_HS_rad(M, vs, m_lep)),
        "dm2_Sh":  abs(dm2_Sh(M, vs, m_lep)),
    }


# ============================================================
#  2. 扫描
# ============================================================

def scan_M(vs=30.0, M_list=None, mS=10.0):
    """扫 M，看 BR(h->SS) 与 sin(theta)。"""
    if M_list is None:
        M_list = [300., 500., 1000., 1250., 1500., 1770., 2000., 2500., 3000.]

    print("=" * 78)
    print("  扫 M（v_S = %.0f GeV, m_S = %.0f GeV）" % (vs, mS))
    print("=" * 78)
    print("  %8s %10s %12s %10s %12s" %
          ("M[GeV]", "lamHS^rad", "|dm2_Sh|", "BR(h->SS)", "sin(theta)"))
    print("  " + "-" * 74)
    rows = []
    for M in M_list:
        r = make_effC(mS, M, vs)
        s2 = r["sin2theta"]
        # sin(theta) from sin(2theta)
        sinth = np.sqrt((1.0 - np.sqrt(max(0., 1.0 - s2 ** 2))) / 2.0) if s2 < 1 else np.sqrt(0.5)
        print("  %8.0f %10.2e %12.2f %9.2f%% %12.2e" %
              (M, r["lamHS"], r["dm2_Sh"], r["BR_SS"] * 100, sinth))
        rows.append((M, r["lamHS"], r["dm2_Sh"], r["BR_SS"], sinth))
    print()
    print("  主文档的估算（供对照）：")
    print("    M=1000 : lamHS 2.94e-03, |dm2| 21.68, BR 1.00%")
    print("    M=1500 : lamHS 6.61e-03, |dm2| 48.77, BR 4.85%")
    print("    M=1770 : lamHS 9.20e-03, |dm2| ~68,   BR 9.00%  <- 临界")
    print("    M=2000 : lamHS 1.18e-02, |dm2| 86.71, BR 13.88% <- 排除(经验阈值)")
    print("  => 经验阈值给出 M <~ 1.8 TeV；标度 BR ∝ M^4")
    return rows


def scan_resonance(vs=30.0, M_list=None, sin2lim=0.2):
    """
    扫 M，算 125 GeV 附近的排除带宽度。

    |m_S^2 - m_h^2| <~ 2 |dm2_Sh| / sin2theta_lim
        => |m_S - m_h| <~ (2|dm2|/sin2lim) / (2 m_h)
    """
    if M_list is None:
        M_list = [300., 1000., 2000.]

    print()
    print("=" * 78)
    print("  125 GeV 附近排除带宽（sin2theta_lim = %.1f）" % sin2lim)
    print("=" * 78)
    for M in M_list:
        dm2 = abs(dm2_Sh(M, vs))
        dmsq = 2.0 * dm2 / sin2lim
        bw = dmsq / (2.0 * mh)
        print("    M = %6.0f GeV : |m_S - m_h| <~ %6.2f GeV" % (M, bw))
    print()
    print("  主文档估算：0.08 / 0.87 / 3.47 GeV （M = 300/1000/2000）")
    print("  => 用 HiggsTools 应能给出这条带的**真实**边界")
    print("     建议直接画进论文的参数空间图")


# ============================================================
#  3. HiggsTools 真实约束（需要安装）
# ============================================================

def run_higgstools(vs=30.0, mS=10.0, M_list=None):
    """
    调用 HiggsSignals / HiggsBounds。

    ⚠ 这是**未执行**的示例代码。HiggsTools 2.x 的 Python API 大致如下；
       具体签名请查你安装版本的文档。
    """
    if not HAS_HT:
        print()
        print("⚠ higgstools 未安装，跳过真实约束检验。")
        print("  安装：  pip install higgstools")
        return None

    if M_list is None:
        M_list = [500., 1000., 1500., 2000., 2500., 3000.]

    print()
    print("=" * 78)
    print("  HiggsTools 真实约束")
    print("=" * 78)

    # --- HiggsSignals : 信号强度 chi^2 ---
    try:
        hs = signals.HiggsSignals()          # 会加载内置实验数据集
        print("  HiggsSignals 已初始化，nObs =", getattr(hs, "n_observations", "?"))
    except Exception as e:
        print("  HiggsSignals 初始化失败：", e)
        hs = None

    # --- HiggsBounds : 是否被搜寻排除 ---
    try:
        hb = bounds.HiggsBounds()
        print("  HiggsBounds  已初始化")
    except Exception as e:
        print("  HiggsBounds 初始化失败：", e)
        hb = None

    print()
    print("  %8s %10s %12s %12s %10s" %
          ("M[GeV]", "sin(theta)", "BR(h->SS)", "chi2-HS", "HB排除?"))
    print("  " + "-" * 74)

    results = []
    for M in M_list:
        r = make_effC(mS, M, vs)

        # 构造 Predictions 对象
        # 实际 API：predictions.Predictions() 然后 add_particle(...)
        # 或从 SLHA 读： predictions.read_slha(path)
        # 这里给出伪代码结构
        try:
            pred = predictions.Predictions()
            # pred.add_particle(...)  # 按你的 HiggsTools 版本填充
            chi2 = "n/a" if hs is None else "?"
            excl = "n/a" if hb is None else "?"
        except Exception as e:
            chi2 = excl = "err:" + str(e)[:20]

        s2 = r["sin2theta"]
        sinth = np.sqrt((1.0 - np.sqrt(max(0., 1.0 - s2 ** 2))) / 2.0) if s2 < 1 else np.sqrt(0.5)
        print("  %8.0f %10.2e %11.2f%% %12s %10s" %
              (M, sinth, r["BR_SS"] * 100, chi2, excl))
        results.append((M, sinth, r["BR_SS"], chi2, excl))

    return results


# ============================================================
#  4. 输出"审稿人要的三项"
# ============================================================

def summary():
    print()
    print("=" * 78)
    print("  给审稿人的三项答案")
    print("=" * 78)
    print("""
  1) 真实的 sin(theta) 上限
       -> 由 HiggsSignals 的 chi^2 拟合给出
       -> 替代我用经验值 0.1 - 0.3 的估算

  2) 125 GeV 附近的排除带真实宽度
       -> 在 (m_S, M) 平面上扫，标出 HB 判为排除的区域
       -> 替代我估的 0.87 GeV (M=1 TeV) / 3.47 GeV (M=2 TeV)

  3) M 的真实上限
       -> 由 BR(h->SS) 与信号强度共同给出
       -> 替代我估的 1.8 TeV (v_S = 30 GeV)

  ★ 建议：把 (2) 和 (3) 做成论文里的一张图，
     这正好是审稿人 2.1(1) 那句反问暗示的方向 ——
     "UV 完成预言了一个处于对撞机可探测区间的标量"。
""")


# ============================================================
#  main
# ============================================================

if __name__ == "__main__":
    print(__doc__)

    vs_default = 30.0
    mS_default = 10.0

    # 1) 解析预言（不需要 HiggsTools，一定跑得通）
    scan_M(vs=vs_default, mS=mS_default)
    scan_resonance(vs=vs_default)

    # 2) 真实约束（需要 pip install higgstools）
    run_higgstools(vs=vs_default, mS=mS_default)

    summary()

    print()
    print("运行方式：")
    print("  python3 05_HiggsTools_LHC约束扫描.py")
    print()
    print("若只想看解析预言（不装 HiggsTools）：本脚本已自动降级，")
    print("上面第 1、2 部分会正常输出，第 3 部分显示 'n/a'。")
    print()
    print("⚠ 本脚本未在沙盒执行（无 higgstools）。如报错请把错误信息发回。")
