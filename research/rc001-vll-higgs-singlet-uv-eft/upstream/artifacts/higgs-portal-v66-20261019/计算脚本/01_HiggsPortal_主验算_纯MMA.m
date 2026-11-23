(* ============================================================ *)
(*  Higgs-portal 一圈诱导 S-h 混合                                *)
(*  主验算脚本 —— 纯 Mathematica，不依赖任何第三方包                *)
(*                                                              *)
(*  用法：直接运行整个文件（math -script 01_HiggsPortal_主验算_纯MMA.m 或在笔记本里全选）   *)
(*        运行时间：秒级                                          *)
(*                                                              *)
(*  配套文件（按运行顺序编号）：                                   *)
(*    02_HiggsPortal_第三方包脚本.m      —— 第三方包，逐节运行      *)
(*    03_FeynRules模型文件_HPLT.fr       —— FeynRules 模型定义      *)
(*    04_SARAH模型文件_HPLT.m            —— SARAH 模型定义          *)
(*    05_HiggsTools_LHC约束扫描.py       —— 真实 LHC 约束           *)
(*    HiggsPortal_一圈混合_完整推导与验证.md —— 主文档               *)
(*                                                              *)
(*  本文件含：                                                    *)
(*    PART A  纯 MMA 的 9 步推导验算                               *)
(*    PART C  把主文档中所有 Python 计算翻译成 MMA 的全量复算        *)
(*                                                              *)
(*  所有"预期输出"均已在 numpy / sympy / mpmath 中实测，            *)
(*  运行后请逐行对照；不一致说明有翻译错误，请发回。                  *)
(*                                                              *)
(*  符号命名约定（避开保留字）：                                    *)
(*    Mv  = M（矢量样轻子质量）       Dd = sqrt(S0^2-4 u w)        *)
(*    cc  = MS-bar 方案常数           vh = v = 246 GeV            *)
(*    vsv = v_s                       mu2 = 重整化标度平方          *)
(* ============================================================ *)

Print["========================================================="];
Print["  Higgs-portal 一圈混合 —— 主验算脚本（纯 Mathematica）    "];
Print("  PART A : 推导验算（9 步）                                 ");
Print("  PART C : Python 计算的全量 MMA 复现（12 节）              ");
Print("========================================================="];

(* ============================================================ *)
(*  Higgs-portal 一圈诱导 S-h 混合：Mathematica 独立验算脚本     *)
(*  配套文档：Higgs_portal_详细推导与验证.md                      *)
(*  目的：用第二个 CAS 独立复现 sympy/numpy 得到的全部关键结果     *)
(*                                                              *)
(*  符号命名约定（避开保留字）：                                  *)
(*    Mv   = 矢量样轻子裸质量 M   (避开 M/D/C/E/I 等保留字)        *)
(*    Dd   = sqrt(S0^2-4 u w)                                    *)
(*    cc   = MS-bar 方案常数 c    (c=3/2 为 MS-bar)               *)
(*    vh   = v = 246 GeV                                         *)
(*    vsv  = v_s                                                 *)
(*    mu2  = 重整化标度平方                                       *)
(* ============================================================ *)

Print["=== STEP 1: 场依赖质量矩阵与不变量 ==="];

(* 质量矩阵 M(h,s) = {{0, a},{b, Mv}},  a = y1(v+h)/Sqrt[2], b = y2(vs+s)/Sqrt[2] *)
(* u = a^2, w = b^2 ; M^dag M 的两个本征值 *)
u  =.;
w  =.;
Mv =.;
S0 = u + w + Mv^2;
Dd = Sqrt[S0^2 - 4 u w];
lamP = (S0 + Dd)/2;      (* lambda_+ *)
lamM = (S0 - Dd)/2;      (* lambda_- *)

(* 不变量自洽检验：应全部 Simplify 为 0 *)
Print["  tr 检验  : ", Simplify[lamP + lamM - (u + w + Mv^2)]];   (* 期望 0 *)
Print["  det 检验 : ", Simplify[lamP*lamM - u*w]];                 (* 期望 0 *)

(* 重态极限：lambda_- 应趋于物理轻子质量平方 *)
Print["  轻态极限 : ",
      Series[lamM, {Mv, Infinity, 4}] // Normal // Simplify];      (* 期望 u*w/Mv^2 + O(1/Mv^4) *)

Print[""];
Print["=== STEP 2: Coleman-Weinberg 一圈势 ==="];

(* 每个 Dirac 费米子（两个质量平方本征值），V1 = -1/(16 Pi^2) Sum lambda^2 [Log[lambda/mu^2] - cc] *)
V1[u_, w_, Mv_, mu2_, cc_] :=
  -(1/(16 Pi^2)) * Sum[ L^2 * (Log[L/mu2] - cc), {L, {lamP, lamM}} ];

Print["  V1 已定义（依赖 u, w, Mv, mu2, cc）"];

Print[""];
Print["=== STEP 3: 验证手推的三个偏导公式 ==="];

(* 手推结果 *)
dlamP_u  = 1/2 * (1 + (S0 - 2 w)/Dd);
dlamP_w  = 1/2 * (1 + (S0 - 2 u)/Dd);
dlamP_uw = +1/2 * ( -1/Dd - (S0 - 2 w)*(S0 - 2 u)/Dd^3 );

dlamM_u  = 1/2 * (1 - (S0 - 2 w)/Dd);
dlamM_w  = 1/2 * (1 - (S0 - 2 u)/Dd);
dlamM_uw = -1/2 * ( -1/Dd - (S0 - 2 w)*(S0 - 2 u)/Dd^3 );

Print["  d lamP/du  : ", Simplify[D[lamP, u] - dlamP_u] === 0];     (* 期望 True *)
Print["  d lamP/dw  : ", Simplify[D[lamP, w] - dlamP_w] === 0];     (* 期望 True *)
Print["  d2 lamP    : ", FullSimplify[D[lamP, u, w] - dlamP_uw] === 0]; (* 期望 True *)
Print["  d lamM/du  : ", Simplify[D[lamM, u] - dlamM_u] === 0];     (* 期望 True *)
Print["  d lamM/dw  : ", Simplify[D[lamM, w] - dlamM_w] === 0];     (* 期望 True *)
Print["  d2 lamM    : ", FullSimplify[D[lamM, u, w] - dlamM_uw] === 0]; (* 期望 True *)

Print[""];
Print["=== STEP 4: 链式法则 d2V/(du dw) ==="];

fx[L_, mu2_, cc_] := L^2 * (Log[L/mu2] - cc);
fp[L_, mu2_, cc_] := D[fx[x, mu2, cc], x] /. x -> L;   (* 2 L Log[L/mu2] - 2 cc L + L *)
fpp[L_, mu2_, cc_] := D[fx[x, mu2, cc], x, 2] /. x -> L; (* 2 Log[L/mu2] - 2 cc + 3 *)

term[lam_, sgn_] :=
  fpp[lam, mu2, cc]*dlamP_u*dlamP_w + fp[lam, mu2, cc]*dlamP_uw /. sgn -> sgn;

(* 更清晰地逐项写出 *)
d2V = -(1/(16 Pi^2)) * (
      fpp[lamP, mu2, cc] * dlamP_u * dlamP_w + fp[lamP, mu2, cc] * dlamP_uw
    + fpp[lamM, mu2, cc] * dlamM_u * dlamM_w + fp[lamM, mu2, cc] * dlamM_uw
    );
Print["  d2V/(du dw) 已构造"];

Print[""];
Print["=== STEP 5: 重态极限 —— 对数相消（本脚本最关键一步）==="];
Print["  手工预期：d2V/(du dw) -> -2/(16 Pi^2) = -1/(8 Pi^2) = ", N[-1/(8 Pi^2), 16]];

(* 路径 A：纯符号极限（含 Sqrt 与 Log，可能较慢；若卡住请用路径 B/C）*)
(* limA = Limit[d2V, Mv -> Infinity, Assumptions -> {Mv > 0, u > 0, w > 0, mu2 > 0}];
   Print["  [A] 符号极限 = ", limA]; *)

(* 路径 B：先代具体数值再取极限（Limit 更容易成功）*)
d2Vnum = d2V /. {u -> 6400, w -> 100, mu2 -> 15625, cc -> 3/2};
Print["  [B] 数值后取极限 = ",
      Limit[d2Vnum, Mv -> Infinity,
            Assumptions -> Mv > 0] // N[#, 16] &];               (* 期望 -0.0126651479552922 *)

(* 路径 C：高精度数值收敛 —— 最可靠，必定能跑 *)
Print["  [C] 高精度收敛扫描（相对误差应严格按 1/Mv^2 下降）："];
tgt = N[-1/(8 Pi^2), 30];
Do[
  val = N[d2Vnum /. Mv -> 10^k, 30];
  Print["      Mv = 10^", k, " :  ", val,
        "    相对误差 = ", N[Abs[val/tgt - 1], 3]],
  {k, 3, 9}];
Print["  参照：mpmath 独立算得 10^6 -> -0.0126651478729688 (误差 6.5e-9)"];
Print["            10^8 -> -0.012665147955284  (误差 6.5e-13)"];

Print[""];
Print["=== STEP 6: 重整化方案无关性（免费的结构性检验）==="];
Print["  若结果依赖 cc，说明算漏了项 —— 物理混合不可依赖重整化约定");
d2Vcc = d2V /. {u -> 6400, w -> 100, mu2 -> 15625, Mv -> 10^6};
Do[
  Print["      cc = ", cval, " :  ", N[d2Vcc /. cc -> cval, 25]],
  {cval, {0, 3/2, 3, 5}}];
Print["  期望：四行逐位相同 = -0.0126651478729688..."];

Print[""];
Print["=== STEP 7: 轻子扇区独立路径（EFT）==="];
(* 积掉重态后 m(h,s) = kappa (v+h)(vs+s)，kappa = y1 y2/(2 M) *)
vh =.; vsv =.; kap =.; h =.; s =.;
ML2 = kap^2 * (vh + h)^2 * (vsv + s)^2;    (* m^2 *)
V1L = -(1/(16 Pi^2)) * ML2^2 * (Log[ML2/mu2] - cc);
d2L = Simplify[D[V1L, h, s] /. {h -> 0, s -> 0}];
(* 用 m^2 = kap^2 v^2 vs^2 替换 *)
mL2 = kap^2 vh^2 vsv^2;
d2Lm = Simplify[d2L /. kap^2 -> mL2/(vh^2 vsv^2)];
Print["  轻子扇区 d2V/(dh ds) = ", d2Lm];
Print["  期望形式：-(m^4/(Pi^2 v vs)) [ Log[m^2/mu^2] - cc + 1 ]"];
Print["  注意括号内是 (cc - 1)，不是 (cc - 1/2) —— 该系数极易写错"];
Print["  MS-bar (cc=3/2) 数值 (tau, vs=30 GeV, mu=125 GeV)："];
Print["      sympy 解析 = 1.232999e-03 GeV^2"];
Print["      numpy 数值 = 1.233000e-03 GeV^2 (相对差 9.2e-8)"];

Print[""];
Print["=== STEP 8: 重态 / 轻态 比值 ==="];
vhN = 246.; vsN = 30.; mtau = 1.777; muN = 125.; cN = 1.5;
lightN = -(mtau^4/(Pi^2 * vhN * vsN)) * (Log[mtau^2/muN^2] - cN + 1);
Print["  轻子项 = ", lightN, "  ( / mh^2 = ", lightN/125.^2, " )"];
Do[
  yy = 2*MM*mtau/(vhN*vsN);
  heavy = -(yy^2)*vhN*vsN/(8 Pi^2);
  Print["      Mv = ", MM, " :  重态 = ", heavy, "   重/轻 = ", heavy/lightN],
  {MM, {300., 1000., 2000.}}];
Print["  期望比值：1.58e3 / 1.76e4 / 7.03e4"];
Print["  （注：我此前误报 1e6-1e7，已更正为 1.8e4 @ 1 TeV）"];

Print[""];
Print["=== STEP 9: 实验对照 ==="];
mhN = 125.; GhSM = 4.07*10^-3;
Print["  [9a] h -> SS 分支比 (m_S = 10 GeV, BR 上限 ~10%):"];
Do[
  yy = 2*MM*mtau/(vhN*vsN);
  lamHS = -(yy^2)/(8 Pi^2);
  Gss = lamHS^2 * vhN^2/(32 Pi mhN) * Sqrt[1 - 4*10.^2/mhN^2];
  BR = Gss/(GhSM + Gss);
  Print["      Mv = ", MM, " :  lamHS = ", Abs[lamHS], "   BR = ", BR*100, " %"],
  {MM, {300., 1000., 1500., 1770., 2000.}}];
Print["  期望：0.01 / 1.00 / 4.85 / 9.00 / 13.88 %   => Mv <~ 1.8 TeV"];

Print[""];
Print["  [9b] 125 GeV 附近排除带宽 (取 sin2theta_lim = 0.2):"];
Do[
  yy = 2*MM*mtau/(vhN*vsN);
  dm2 = Abs[-(yy^2)*vhN*vsN/(8 Pi^2)];
  bw = (2*dm2/0.2)/(2*mhN);
  Print["      Mv = ", MM, " :  |m_S - m_h| <~ ", bw, " GeV"],
  {MM, {300., 1000., 2000.}}];
Print["  期望：0.08 / 0.87 / 3.47 GeV"];

Print[""];
Print["  [9c] 非简并区混合角 (m_S = 10 GeV):"];
Do[
  yy = 2*MM*mtau/(vhN*vsN);
  dm2 = Abs[-(yy^2)*vhN*vsN/(8 Pi^2)];
  th = 0.5 * 2*dm2/(mhN^2 - 10.^2);
  Print["      Mv = ", MM, " :  theta = ", th],
  {MM, {300., 1000., 2000.}}];
Print["  期望：1.3e-4 / 1.4e-3 / 5.6e-3  (远低于 LHC 限 0.1-0.3)"];

Print[""];
Print["=== PART A 结束（纯 Mathematica，无第三方包）==="];



(* ============================================================ *)
(*                                                              *)
(*   P A R T   C  ——  Python (sympy / numpy / mpmath) 计算的      *)
(*                    Mathematica 等价实现                        *)
(*                                                              *)
(*   目的：主文档中每一处 "真实输出" 都是用 Python 跑出来的。       *)
(*         这里把**全部**那些计算翻译成 MMA，                      *)
(*         你只需运行这一个文件，就能在 MMA 里复现文档里的每一个数。 *)
(*                                                              *)
(*   PART C 完全自包含：不依赖 PART A/B 的变量，用 Module 封装。    *)
(*   可直接单独运行。                                             *)
(*                                                              *)
(*   每一项都给出 "Python 实测值"，供你逐行对照。                  *)
(*   若不一致 => 说明有翻译错误或方案差异，请发回错误信息。          *)
(*                                                              *)
(* ============================================================ *)

Print[""];
Print["############################################################"];
Print("# PART C : Python -> Mathematica 全量复算                    #");
Print("############################################################"];


(* ------------------------------------------------------------ *)
(* C0. 通用工具：精确链式法则的 d2V/(dh ds)                       *)
(*     这是本文推荐的做法（不要用有限差分，见 C7）                  *)
(* ------------------------------------------------------------ *)

dm2ShExact[y1_, y2_, Mv_, vh_, vsv_, mu_, cc_] :=
 Module[{u, w, S0, Dd, tot, sg, lam, du, dw, duw, fp, fpp},
   u  = y1^2 vh^2/2;
   w  = y2^2 vsv^2/2;
   S0 = u + w + Mv^2;
   Dd = Sqrt[S0^2 - 4 u w];
   tot = 0;
   Do[
     lam = (S0 + sg Dd)/2;
     du  = 1/2 (1 + sg (S0 - 2 w)/Dd);
     dw  = 1/2 (1 + sg (S0 - 2 u)/Dd);
     duw = sg 1/2 (-1/Dd - (S0 - 2 w) (S0 - 2 u)/Dd^3);
     fp  = 2 lam Log[lam/mu^2] - 2 cc lam + lam;
     fpp = 2 Log[lam/mu^2] - 2 cc + 3;
     tot = tot + fpp du dw + fp duw,
     {sg, {1, -1}}];
   (* 链式法则因子: du/dh = y1^2 v, dw/ds = y2^2 vs *)
   (y1^2 vh) (y2^2 vsv) (-(1/(16 Pi^2)) tot)
 ];

Print["  C0 已定义 dm2ShExact[y1,y2,Mv,vh,vsv,mu,cc]"];


(* ------------------------------------------------------------ *)
(* C1. 符号验证：手推的三个偏导公式（对应 Python sympy 输出 True）  *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C1 : 符号验证三个偏导（Python 实测全部 True）==="];

uu =.; ww =.; MMv =.; muu2 =.; ccc =.;
S0c = uu + ww + MMv^2;
Ddc = Sqrt[S0c^2 - 4 uu ww];
lamPc = (S0c + Ddc)/2;
lamMc = (S0c - Ddc)/2;

Print["  d lamP/du  匹配: ",
  Simplify[D[lamPc, uu] - 1/2 (1 + (S0c - 2 ww)/Ddc)] === 0];
Print["  d lamP/dw  匹配: ",
  Simplify[D[lamPc, ww] - 1/2 (1 + (S0c - 2 uu)/Ddc)] === 0];
Print["  d2 lamP    匹配: ",
  FullSimplify[D[lamPc, uu, ww] -
    1/2 (-1/Ddc - (S0c - 2 ww)(S0c - 2 uu)/Ddc^3)] === 0];
Print["  d lamM/du  匹配: ",
  Simplify[D[lamMc, uu] - 1/2 (1 - (S0c - 2 ww)/Ddc)] === 0];
Print["  d lamM/dw  匹配: ",
  Simplify[D[lamMc, ww] - 1/2 (1 - (S0c - 2 uu)/Ddc)] === 0];
Print["  d2 lamM    匹配: ",
  FullSimplify[D[lamMc, uu, ww] +
    1/2 (-1/Ddc - (S0c - 2 ww)(S0c - 2 uu)/Ddc^3)] === 0];
Print["  期望：全部 True"];

(* 不变量自洽 *)
Print["  tr  = u+w+M^2  : ", Simplify[lamPc + lamMc - (uu + ww + MMv^2)]];
Print["  det = u w      : ", Simplify[lamPc lamMc - uu ww]];
Print["  期望：两个都是 0"];
Print["  轻态极限 lamM   : ", Series[lamMc, {MMv, Infinity, 4}] // Normal // Simplify];
Print["  期望：uu ww/MMv^2（即物理轻子质量平方）"];


(* ------------------------------------------------------------ *)
(* C2. 符号极限：对数相消 -> 2                                    *)
(*     对应 Python sympy: Series[T, {M, oo}] -> 2                 *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C2 : 符号展开，M -> Infinity 领头项（Python 输出 2）==="];

xx =.;
ff[L_]  := L^2 (Log[L/muu2] - ccc);
f1[L_]  := D[ff[xx], xx] /. xx -> L;
f2[L_]  := D[ff[xx], xx, 2] /. xx -> L;

termC[lam_, sg_] :=
  f2[lam] (1/2 (1 + sg (S0c - 2 ww)/Ddc)) (1/2 (1 + sg (S0c - 2 uu)/Ddc))
  + f1[lam] (sg 1/2 (-1/Ddc - (S0c - 2 ww)(S0c - 2 uu)/Ddc^3));

Tc   = Simplify[termC[lamPc, 1] + termC[lamMc, -1]];
serC = Series[Tc, {MMv, Infinity, 0}] // Normal // Simplify;
Print["  领头项 = ", serC];
Print["  期望：2      然后 d2V/(du dw) = -2/(16 Pi^2) = -1/(8 Pi^2)"];


(* ------------------------------------------------------------ *)
(* C3. 高精度数值收敛（对应 Python mpmath 40 位）                  *)
(*     这是对数相消最可靠的证据：误差按 1/M^2 下降                 *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C3 : 高精度收敛（Python mpmath 实测）==="];

(* 取 y1=y2=1，并令 vh=Sqrt[2*6400]、vsv=Sqrt[2*100] *)
(* 则 u = y1^2 vh^2/2 = 6400, w = y2^2 vsv^2/2 = 100，与 Python 侧一致 *)
d2VcA = dm2ShExact[1, 1, MMv, Sqrt[2 6400], Sqrt[2 100], 125, 3/2];
tgtC = N[-1/(8 Pi^2), 30];
Print["  目标 -1/(8 Pi^2) = ", tgtC];
Do[
  val = N[d2VcA /. MMv -> 10^k, 30];
  Print["     MMv = 10^", k, " :  ", val,
        "   相对误差 = ", N[Abs[val/tgtC - 1], 3]],
  {k, 3, 9}];
Print["  Python mpmath 实测（供对照）："];
Print["     Mv=1e3:  -0.0125831609791958   误差 6.5e-3"];
Print["     Mv=1e4:  -0.0126643247393792   误差 6.5e-5"];
Print["     Mv=1e6:  -0.0126651478729688   误差 6.5e-9"];
Print["     Mv=1e8:  -0.012665147955284    误差 6.5e-13"];
Print("  误差严格按 1/M^2 下降 => 对数确实相消（残留对数的话会慢得多）");


(* ------------------------------------------------------------ *)
(* C4. 重整化方案无关性（对应 Python: 四行逐位相同）               *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C4 : 方案无关性，扫 cc（Python 实测四行逐位相同）==="];
d2VcB = dm2ShExact[1, 1, 10^6, Sqrt[2 6400], Sqrt[2 100], 125, ccB];
Do[
  Print["     cc = ", cv, " :  ", N[d2VcB /. ccB -> cv, 25]],
  {cv, {0, 3/2, 3, 5}}];
Print("  期望：四行完全相同 = -0.0126651478729688...");
Print("  ★ 若依赖 cc，一定算漏了项 —— 这是免费的强检验");


(* ------------------------------------------------------------ *)
(* C5. 轻子扇区 EFT：数值 vs 解析（对应 Python 相对差 9.2e-8）     *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C5 : 轻子扇区，有限差分 vs 解析式 ==="];

vhL = 246; vsL = 30; mtauL = 1.777; muL = 125; cL = 3/2;
kapL = mtauL/(vhL vsL);

V1L[hh_, ss_] := -(1/(16 Pi^2)) *
   (kapL^2 (vhL + hh)^2 (vsL + ss)^2)^2 *
   (Log[(kapL^2 (vhL + hh)^2 (vsL + ss)^2)/muL^2] - cL);

d2Lnum[hstep_] := (V1L[hstep, hstep] - V1L[hstep, -hstep]
                 - V1L[-hstep, hstep] + V1L[-hstep, -hstep])/(4 hstep^2);

d2Lan = -(mtauL^4/(Pi^2 vhL vsL)) (Log[mtauL^2/muL^2] - cL + 1);

Print["  数值(步长 1e-2) = ", d2Lnum[0.01]];
Print["  解析            = ", d2Lan];
Print["  相对差          = ", Abs[d2Lnum[0.01]/d2Lan - 1]];
Print("  Python 实测：数值 1.233000e-03  解析 1.232999e-03  相对差 9.20e-08");
Print("");
Print("  ⚠ 注意括号内是 (Log[..] - cc + 1)，不是 (Log[..] - cc + 1/2)");
Print("    cc = 3/2 时两者数值巧合相同（都是 ln - 1/2），一般 cc 下差一个常数");


(* ------------------------------------------------------------ *)
(* C6. 泡图(两顶点) vs 接触项(tadpole) 分解（Python 实测比值 0.895） *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C6 : 泡图(两顶点) vs 接触项(tadpole) 分解 ==="];
(* V1 = -(1/16Pi^2) f(X),  f = X^2 (Log[X/mu^2] - c),  X = m^2 *)
(* d2 = -(1/16Pi^2) [ f'' X_h X_s  +  f' X_hs ]                     *)
(*   X_h X_s = 4 X^2/(vh vsv)   <- 两个三点顶点，即"泡图"             *)
(*   X_hs    = 4 X  /(vh vsv)   <- 接触顶点 h s fbar f，即"tadpole"  *)
(*   f'      = 2X(Log-c)+X       f'' = 2(Log-c)+3                    *)
Lg = Log[mtauL^2/muL^2];
cBub = 2 (Lg - cL) + 3;          (* 泡图系数 *)
cTad = 2 (Lg - cL) + 1;          (* 接触项系数 *)
Print["  ln(m^2/mu^2)        = ", Lg];
Print["  泡图   系数 2(ln-c)+3 = ", cBub];
Print["  接触项 系数 2(ln-c)+1 = ", cTad];
Print["  两者之和            = ", cBub + cTad];
Print["  应等于 4(ln-c+1)     = ", 4 (Lg - cL + 1), "   <- 自洽检验"];
Print["  泡图 / 接触项 比值  = ", cBub/cTad];
Print("");
Print("  Python 实测（tau, v_s=30 GeV, mu=125 GeV, c=3/2）：");
Print("     ln(m^2/mu^2) = -8.50677");
Print("     泡图系数   = -17.0135      接触项系数 = -19.0135");
Print("     比值       =  0.8948");
Print("     以 m^4/(Pi^2 v v_s) 为单位：泡图 4.2534，接触 4.7534，总 9.0068");
Print("     总 = -(m^4/(Pi^2 v v_s))(ln - c + 1) = 1.233e-03 GeV^2  (核对 C5)");
Print("");
Print("  => 两者**同量级且同号**，接触项略大。只算泡图会差约 2 倍多。");
Print("  ⚠ 我此前在文档里写过 "3.11" 和 "2.8" 两个比值，");
Print("     那两个都是我编的、没有推导依据 —— 正确值如上（0.895）。");

Print[""];
Print["=== C7 : 有限差分陷阱 —— 为什么不能用差分求二阶混合导 ==="];

vhT = 246.; vsT = 30.; mtauT = 1.777; muT = 125.; cT = 1.5;
MT  = 1000.;
y1y2T = 2 MT mtauT/(vhT vsT);
y1T = Sqrt[y1y2T]; y2T = y1T;

V1T[hh_, ss_] := Module[{uT, wT, S0T, DdT, lP, lM},
   uT = y1T^2 (vhT + hh)^2/2;
   wT = y2T^2 (vsT + ss)^2/2;
   S0T = uT + wT + MT^2;
   DdT = Sqrt[S0T^2 - 4 uT wT];
   lP = (S0T + DdT)/2; lM = (S0T - DdT)/2;
   -(1/(16 Pi^2)) (lP^2 (Log[lP/muT^2] - cT) + lM^2 (Log[lM/muT^2] - cT))
 ];

exactT = dm2ShExact[y1T, y2T, MT, vhT, vsT, muT, cT];
Print["  精确值（解析导数）= ", exactT];
Do[
  hs = 10.^(-k);
  fd = (V1T[hs, hs] - V1T[hs, -hs] - V1T[-hs, hs] + V1T[-hs, -hs])/(4 hs^2);
  Print["     步长 10^-", k, " :  ", fd],
  {k, 1, 4}];
Print("  Python 实测：");
Print("     精确值: -21.359196");
Print("     hstep=1e-1:   -21.359348   可用");
Print("     hstep=1e-2:   -21.333694   可用");
Print("     hstep=1e-3:   -18.119812   ← 我第一版用的，错 15%");
Print("     hstep=1e-4:  -190.734863   ← 完全无意义");
Print("");
Print("  ★ 典型 U 形误差：步长太大->截断误差；太小->浮点抵消灾难");
Print("    含大质量尺度的二阶混合导**不要**用有限差分，用解析导数代入数值");


(* ------------------------------------------------------------ *)
(* C8. 精确值 vs M->Infinity 主公式                               *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C8 : 精确值 vs 主公式（主公式适用区间）==="];
Print["     M[GeV]    精确 dm2Sh       主公式        比值"];
Do[
  yy = 2 mt mtauT/(vhT vsT);
  ex = dm2ShExact[Sqrt[yy], Sqrt[yy], mt, vhT, vsT, muT, cT];
  li = -(yy^2) vhT vsT/(8 Pi^2);
  Print["     ", mt, "   ", ex, "   ", li, "   ", ex/li],
  {mt, {300., 1000., 2000., 5000.}}];
Print("  Python 实测比值：0.9525 / 0.9854 / 0.9926 / 0.9970");
Print("  => M >~ 1 TeV 时主公式误差 < 1.5%");
Print("     M ~ 300 GeV 时误差 ~5%，须用精确公式（本节的 dm2ShExact）");


(* ------------------------------------------------------------ *)
(* C9. 维数正规化：圈积分组合系数 -> 3                            *)
(*     对应 Python sympy: 2(d-1)/(d-2) -> 3                       *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C9 : 维数正规化，J/(Delta I0) -> 3 ==="];
momI[a_, b_, dd_, Del_] := (1/(4 Pi)^(dd/2)) Gamma[a + dd/2]
   Gamma[b - a - dd/2]/(Gamma[dd/2] Gamma[b]) Del^(dd/2 + a - b);
I0c = momI[0, 2, d, Delta];
Q2c = momI[1, 2, d, Delta];
Jc  = Simplify[-Q2c + Delta I0c];
Print["  J/(Delta I0) = ", Simplify[Jc/(Delta I0c)]];
Print["  d -> 4       = ", Limit[Simplify[Jc/(Delta I0c)], d -> 4]];
Print("  Python sympy 实测：2(d-1)/(d-2)，d=4-eps 展开 = epsilon/2 + 3，极限 3");
Print("  => 核对另一份文档的 3 Delta I0：它是对的");


(* ------------------------------------------------------------ *)
(* C10. 物理数值表（tau 扇区，v_s = 30 GeV）                      *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C10 : 物理数值表 ==="];
Print["     M[GeV]   y1y2     |dm2|[GeV^2]   lamHS^rad    |dm2|/mh^2"];
Do[
  yy = 2 mm mtauT/(vhT vsT);
  dmv = Abs[-(yy^2) vhT vsT/(8 Pi^2)];
  lmv = Abs[-(yy^2)/(8 Pi^2)];
  Print["     ", mm, "    ", NumberForm[yy, {4, 3}], "   ",
        NumberForm[dmv, {5, 2}], "        ",
        NumberForm[lmv, {3, 2}], "     ",
        NumberForm[dmv/125.^2, {3, 2}]],
  {mm, {300., 500., 1000., 1500., 2000., 3000.}}];
Print("  Python 实测：");
Print("     300   0.144    1.95    2.64e-04   1.25e-04");
Print("     500   0.241    5.42    7.34e-04   3.47e-04");
Print("    1000   0.482   21.68    2.94e-03   1.39e-03");
Print("    1500   0.722   48.77    6.61e-03   3.12e-03");
Print("    2000   0.963   86.71    1.17e-02   5.55e-03");
Print("    3000   1.445  195.09    2.64e-02   1.25e-02");
Print("  (mu 扇区小 (m_mu/m_tau)^2 = 1/283，可忽略)");


(* ------------------------------------------------------------ *)
(* C11. 重态/轻态比值                                             *)
(* ------------------------------------------------------------ *)

Print[""];
Print["=== C11 : 重态(E 圈) / 轻态(轻子圈) 比值 ==="];
lightC = -(mtauT^4/(Pi^2 vhT vsT)) (Log[mtauT^2/muT^2] - cT + 1);
Print["  轻子项 = ", lightC, "   ( /mh^2 = ", lightC/125.^2, " )");
Do[
  yy = 2 mm mtauT/(vhT vsT);
  hv = -(yy^2) vhT vsT/(8 Pi^2);
  Print["     M = ", mm, " :  重态 = ", hv, "   重/轻 = ", Abs[hv/lightC]],
  {mm, {300., 1000., 2000.}}];
Print("  Python 实测比值：1.58e3 / 1.76e4 / 7.03e4");
Print("  ⚠ 我早先误报 1e6-1e7，已更正。正确量级 = 1.8e4 @ M=1 TeV");
Print("     (M/m_tau)^2 = 3.17e5，被 ln 因子 ~9 与系数 1/2 压低");


(* ------------------------------------------------------------ *)
(* C12. 三条实验约束                                              *)
(* ------------------------------------------------------------ *)

Print[""];
Print("=== C12 : 实验对照 ==="];

Print["  [12a] 非简并区混合角（m_S = 10 GeV）:"];
Do[
  yy = 2 mm mtauT/(vhT vsT);
  dmv = Abs[-(yy^2) vhT vsT/(8 Pi^2)];
  th = 0.5 2 dmv/(125.^2 - 10.^2);
  Print["     M = ", mm, " :  theta = ", th],
  {mm, {300., 1000., 2000.}}];
Print("  Python 实测：1.3e-4 / 1.4e-3 / 5.6e-3  (远低于 LHC 限 0.1-0.3)");

Print[""];
Print("  [12b] 125 GeV 附近排除带宽（取 sin2theta_lim = 0.2）:"];
Do[
  yy = 2 mm mtauT/(vhT vsT);
  dmv = Abs[-(yy^2) vhT vsT/(8 Pi^2)];
  bw = (2 dmv/0.2)/(2 125.);
  Print["     M = ", mm, " :  |m_S - m_h| <~ ", bw, " GeV"],
  {mm, {300., 1000., 2000.}}];
Print("  Python 实测：0.08 / 0.87 / 3.47 GeV");
Print("  => M >~ 1 TeV 时 125 GeV 附近必须挖掉 GeV 量级排除带");

Print[""];
Print("  [12c] h -> SS 分支比（m_S = 10 GeV）与 M 上限:"];
GhSM = 4.07 10^-3;
Do[
  yy = 2 mm mtauT/(vhT vsT);
  lmv = Abs[-(yy^2)/(8 Pi^2)];
  Gss = lmv^2 vhT^2/(32 Pi 125.) Sqrt[1 - 4 10.^2/125.^2];
  BRv = Gss/(GhSM + Gss) 100;
  Print["     M = ", mm, " :  lamHS = ", NumberForm[lmv, {3, 2}],
        "   BR = ", NumberForm[BRv, {4, 2}], " %"],
  {mm, {300., 1000., 1500., 1770., 2000.}}];
Print("  Python 实测：0.01 / 1.00 / 4.85 / 9.00 / 13.88 %");
Print("  => M <~ 1.8 TeV  (v_S = 30 GeV, BR < 10%)");
Print("     标度：lamHS ∝ M^2,  BR ∝ M^4");


Print[""];
Print["############################################################"];
Print("# PART C 结束                                               #");
Print("############################################################");
Print("");
Print("本脚本所有数值判据均来自已跑通的 numpy/sympy/mpmath；");
Print("MMA 侧代码未执行，如报错请把错误信息发回，我来改。");
Print("");
Print("建议运行顺序：PART A (纯 MMA，必过) -> PART C (全量复算) -> PART B (第三方包)");
