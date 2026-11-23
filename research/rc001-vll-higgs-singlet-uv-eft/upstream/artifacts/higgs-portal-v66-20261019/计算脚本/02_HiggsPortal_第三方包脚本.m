(* ============================================================ *)
(*  Higgs-portal 一圈混合 —— 第三方包脚本（PART B）                *)
(*                                                              *)
(*  ⚠ 本文件**不要整体运行**。                                     *)
(*    每个 STEP 依赖不同的外部包，请：                             *)
(*      1) 先安装并把包加载路径设好                                *)
(*      2) 单独运行对应 STEP 的代码块                              *)
(*                                                              *)
(*  依赖的外部包：                                                 *)
(*    STEP 10  FeynRules    —— 用 03_FeynRules模型文件_HPLT.fr    *)
(*    STEP 11  FeynArts     —— 需 STEP 10 生成的 HPLT.mod          *)
(*    STEP 12  FeynCalc                                           *)
(*    STEP 13  Package-X                                          *)
(*    STEP 14  LoopTools                                          *)
(*    STEP 15  Collier                                            *)
(*    STEP 16  SARAH + SPheno —— 用 04_SARAH模型文件_HPLT.m       *)
(*    STEP 17  HiggsTools    —— C++/Python，见 05_HiggsTools_LHC约束扫描.py *)
(*                                                              *)
(*  每个 STEP 都给出"预期判据"，其值来自已跑通的 numpy/sympy/mpmath。 *)
(*                                                              *)
(*  ⚠ 免责：以下代码块在沙盒中**未执行**（无 Mathematica）。         *)
(*     如报错请把错误信息发回。                                     *)
(* ============================================================ *)

Print["========================================================="];
Print("  02_HiggsPortal_第三方包脚本.m                              ");
Print("  请勿整体运行 —— 逐节运行，逐包加载                        ");
Print("=========================================================");

Print["若某步 Limit 返回未求值，改用高精度数值收敛（路径 C），该路径必定可行。"];
Print["PART B 在第 10 步之后：FeynRules / FeynArts / FeynCalc / Package-X / LoopTools / Collier / SARAH+SPheno / HiggsTools"];


(* ============================================================ *)
(*                                                              *)
(*   P A R T   B  ——  使用第三方包的计算                         *)
(*                                                              *)
(*   每个包一节，可单独运行。运行前请先把对应包载入路径设好。      *)
(*                                                              *)
(*   总原则：                                                    *)
(*     - FeynRules  : 从拉氏量生成 Feynman 规则 / 模型文件         *)
(*     - FeynArts   : 自动枚举一圈图  —— 防止"漏图"（本次主要风险） *)
(*     - FeynCalc   : 张量约化 + Passarino-Veltman                *)
(*     - Package-X  : 解析闭式一圈积分                            *)
(*     - LoopTools  : 数值 PV（快速核对）                          *)
(*     - Collier    : 数值 PV（独立实现，用来交叉检验 LoopTools）   *)
(*     - SARAH+SPheno: 圈修正质量矩阵（端到端，最强独立检验）       *)
(*     - HiggsTools : 真实 LHC 约束（把我用的经验阈值换成拟合）     *)
(*                                                              *)
(*   ⚠ 免责：以下代码块在沙盒中**未执行**（无 Mathematica）。      *)
(*     语法按各包标准用法编写，已在每个代码块后给出                 *)
(*     "预期输出/预期判据"，其值来自已跑通的 sympy / mpmath。      *)
(*                                                              *)
(* ============================================================ *)

Print[""];
Print["############################################################"];
Print["# STEP 10 : FeynRules —— 生成模型文件（Feynman 规则源头）    #"];
Print["############################################################"];

(* FeynRules 模型文件不是 MMA 脚本，而是一个 .fr 文件。
   把下面 '8< ... 8<' 标记之间的内容**另存为 HPLT.fr**，然后：
       << FeynRules`
       LoadModel["HPLT.fr"];
       FeynmanRules[ LTotal ]            (* 生成全部顶点 *)
       WriteFeynArtsOutput[ LTotal ]     (* 导出 FeynArts 模型文件 HPLT.mod *)
       WriteUFO[ LTotal ]                (* 导出 UFO，给 MadGraph / HiggsTools 用 *)

(* --------------- 8< --------------- 保存为 HPLT.fr --------------- 8< ---------------
M$ModelName = "HPLT";

(* ---- 指标 ---- *)
IndexRange[ Index[Generation] ] = Range[3];
IndexStyle[ Index[Generation], i ];
IndexRange[ Index[Colour] ] = Range[3];
IndexStyle[ Index[Colour], a ];

(* ---- 规范群：SM 三个 + 新的 U(1)_X ---- *)
(* FeynRules 中 U(1) 需给每代的电荷，故用列表 *)
U1XchargesL = { 0, +1, -1};   (* L_e, L_mu, L_tau  的 X 电荷 *)
U1XchargesR = { 0, -1, +1};   (* eR,  muR,  tauR   的 X 电荷 —— 注意 muR 为 -1，轴向 *)
U1XchargesE = {     +1, -1};  (* E_mu, E_tau 两个矢量样轻子（单态，Y=-1）*)

(* ---- 场 ---- *)
M$ClassesDescription = {

  (* 轻子二重态 L_i = (nu, e)_L :  SU(2) 二重, Y=-1/2, X 见上 *)
  F[1] == { ClassName -> LL,
            ClassMembers -> {LLe, LLmu, LLtau},
            Indices -> {Index[Generation]},
            FlavorIndex -> Generation,
            SelfConjugate -> False,
            QuantumNumbers -> {Y -> -1/2, X -> U1XchargesL},
            Mass -> 0, Width -> 0 },

  (* 右手带电轻子 eR_i : SU(2) 单态, Y=-1 *)
  F[2] == { ClassName -> eR,
            ClassMembers -> {eRe, eRmu, eRtau},
            Indices -> {Index[Generation]},
            FlavorIndex -> Generation,
            SelfConjugate -> False,
            QuantumNumbers -> {Y -> -1, X -> U1XchargesR},
            Mass -> 0, Width -> 0 },

  (* 矢量样轻子 E : SU(2) 单态, Y=-1, X = +1 (E_mu) / -1 (E_tau) —— 左右手同荷 *)
  F[3] == { ClassName -> EE,
            ClassMembers -> {EEmu, EEtau},
            Indices -> {Index[Generation]},
            FlavorIndex -> Generation,
            SelfConjugate -> False,
            QuantumNumbers -> {Y -> -1, X -> U1XchargesE},
            Mass -> {ME, 0}, Width -> 0 },

  (* Higgs 二重态 : Y=+1/2, X=0 *)
  S[1] == { ClassName -> H,
            SelfConjugate -> False,
            QuantumNumbers -> {Y -> 1/2, X -> 0},
            VEV -> vh/Sqrt[2],
            Mass -> {MH, 0}, Width -> 0 },

  (* 破缺 U(1)_X 的复单态 S : Y=0, X=+2  *)
  S[2] == { ClassName -> Sg,
            SelfConjugate -> False,
            QuantumNumbers -> {Y -> 0, X -> 2},
            VEV -> vsv/Sqrt[2],
            Mass -> {MS, 0}, Width -> 0 }
};

(* ---- 拉氏量 ---- *)
LGauge := ... (* 规范动能项，FeynRules 可自动由 Gauge 定义生成 *)

(* 关键项：*)
(*   1) H 与矢量样轻子的混合          : -y1  LLbar . H . EE     (X: -1 + 0 + 1 = 0  OK) *)
(*   2) S 与右手轻子的混合            : -y2  EEbar . eR . S     (X: -1 - 1 + 2 = 0  OK) *)
(*   3) 禁戒项（务必确认生成不出来）    : -yd  LLbar . H . eR    (X: -1 + 0 - 1 = -2 ✗) *)
(*   4) Higgs-portal（本问题主角）     : -lamHS (Hdag.H)(Sdag.S) (X: 0 + 0        = 0  OK) *)

LYuk := - y1[ij] LLbar[i] . H . EE[j]  - y2[ij] EEbar[i] . eR[j] . Sg
        - yd[ij] LLbar[i] . H . eR[j]      (* 应被 FeynRules 判定为**非规范不变**并报错 *);

LScalar := - MuH2 (Hdag.H) - MuS2 (Sdag.S)
           - lamH (Hdag.H)^2 - lamS (Sdag.S)^2
           - lamHS (Hdag.H)(Sdag.S);       (* <-- 本问题的主角，规范不变 + 可重整 *)

(* ---- 自检：让 FeynRules 校验规范不变性 ---- *)
(* CheckQuantumNumbers[ LTotal ]   应通过 *)
(* CheckDiagonalMassTerms[ LTotal ] 应通过 *)
(* 若 LYuk 中的 yd 项被报"非规范不变"，说明电荷指派正确 —— 这正是我们要的 *)
--------------- 8< --------------- HPLT.fr 结束 --------------- 8< --------------- *)
*)

Print["  FeynRules 用法（在 MMA 中）："];
Print["     << FeynRules`"];
Print["     LoadModel[\"HPLT.fr\"];"];
Print["     verts = FeynmanRules[LTotal];  Length[verts]"];
Print["     WriteFeynArtsOutput[LTotal];   (* -> HPLT.mod 供 FeynArts 用 *)"];
Print["     WriteUFO[LTotal];              (* -> UFO 供 MadGraph / HiggsTools 用 *)"];
Print["  预期判据："];
Print["     (a) 顶点数 > 0，且含 h-s-EEbar-EE 的四点接触项（如下）"];
Print["     (b) 尝试加入 -yd LLbar.H.eR 应被判为**非规范不变**（电荷 -2 != 0）"];
Print["     (c) lamHS 项被接受（电荷 0）—— 这确认第 3 节的地基"];

(* 关于"接触项"的提醒 —— 这是另一份文档 Step 0.4 给出的项，极易漏 *)
Print[""];
Print["  ⚠ 关键提醒：积掉 E 后 EFT 里会出现接触项  h s fbar f，" ];
Print["     系数 = m_f/(v v_s)。它的一圈 tadpole 与泡图**同量级**" ];
Print("     （实测 泡图/接触项 = 0.895，两者同量级），只算泡图会差约 2 倍多。"];


Print[""];
Print["############################################################"];
Print["# STEP 11 : FeynArts —— 自动枚举一圈图（防"漏图"）          #"];
Print["############################################################"];

(* 前置：需要 STEP 10 生成的 HPLT.mod，放到 $FeynArtsDir/Models/ 下 *)
Print["  前置：把 FeynRules 生成的 HPLT.mod 复制到 $FeynArtsDir/Models/"];
Print["  这是本次**最重要**的一步 —— 本次事故根源就是手画漏了 E 圈。"];

(*
<< FeynArts`

(* 我们要的是 S -> h 的**非对角两点函数**（一圈）*)
tops = CreateTopologies[1, 1 -> 1,
         ExcludeTopologies -> {Tadpoles, WFCorrections}];
Print["  一维入一维出的自能拓扑数 = ", Length[tops]];

(* 插入场：外腿 S -> h，内部允许任意费米子 *)
diags = InsertFields[tops, {S[2]} -> {S[1]},
          Model -> "HPLT",
          InsertionLevel -> {Particles},
          Restrictions -> {NoGhost, NoElectronHCoupling}];

(* 若模型把 h 作为 S[1] 的分量，外腿写法可能是 {Sg} -> {H}，
   请按 HPLT.mod 中的实际场名调整 *)

Print["  自动生成的一圈图总数 = ", Length[diags]];

(* ★ 核心检验：统计内部线含 E（矢量样轻子）的图占多少 *)
containsE[d_] := ! FreeQ[d, EEmu | EEtau];
nE    = Length[Select[diags, containsE]];
nOnly = Length[diags] - nE;
Print["  含 E 的图  = ", nE];
Print["  不含 E 的图 = ", nOnly];

amps = CreateFeynAmp[diags];
Print["  振幅数 = ", Length[amps]];

(* 导出给 FeynCalc / FormCalc *)
ampsFC = FeynCalc`FCFAConvert[CreateFeynAmp[diags], IncomingMomenta -> {p},
           OutgoingMomenta -> {p}, LorentzIndexNames -> {mu},
           UndoChiralSplittings -> True, ChangeDimension -> D,
           List -> False, DropSumOver -> True,
           SMP -> True, Contract -> True];
*)

Print["  预期判据："];
Print["     1) Length[diags] > 0，且**含 E 的图必须存在**（nE > 0）"];
Print["     2) 若 nE == 0，说明模型文件里 E 的耦合没写对 —— 一定是 STEP 10 的错"];
Print["     3) 含 E 的图的贡献应**主导**：重态/轻态 = 1.58e3 / 1.76e4 / 7.03e4"];
Print["        （M = 300 / 1000 / 2000 GeV，来自已跑通的 numpy）"];
Print["  这正是"自动枚举"相对"手画"的价值：不靠人记住，靠软件列全。"];


Print[""];
Print["############################################################"];
Print("# STEP 12 : FeynCalc —— 张量约化 + Passarino-Veltman        #");
Print("############################################################");

(*
<< FeynCalc`
$LoadAddOns = {"TID", "PaVe", "Tarcer"};
<< FeynCalc`

(* ---- 12a. 先做纯代数的张量积分约化（不需要模型文件）---- *)
(* 我们要的组合：Wick 转动后被积函数 (-q^2 + Delta)/(q^2+Delta)^2 *)

(* 维数正规化通式 *)
momInt[a_, b_, dd_, Del_] := (1/(4 Pi)^(dd/2)) *
   Gamma[a + dd/2] Gamma[b - a - dd/2] /
   (Gamma[dd/2] Gamma[b]) Del^(dd/2 + a - b);

I0 = momInt[0, 2, d, Delta];   (* ∫ 1/(q^2+Delta)^2 *)
Q2 = momInt[1, 2, d, Delta];   (* ∫ q^2/(q^2+Delta)^2 *)
J  = Simplify[-Q2 + Delta I0]; (* ∫ (-q^2+Delta)/(q^2+Delta)^2 *)

Print["  J / (Delta I0) = ", Simplify[J/(Delta I0)]];
Print["  d -> 4 极限   = ", Limit[Simplify[J/(Delta I0)], d -> 4]];
*)
Print["  预期输出（sympy 已实测）："];
Print["     J/(Delta I0) = 2 (d-1)/(d-2)"];
Print["     d -> 4      = 3                      <-- 核对另一份文档的 3 Delta I0"];
Print["     (d=4-eps 展开 = epsilon/2 + 3)"];

(*
(* ---- 12b. 完整的两点函数：泡图 ---- *)
(* Pi(p^2) = -i yS yH ∫ d^dk/(2Pi)^d Tr[(kSlash+m1)(kSlash+pSlash+m2)] /
                                       ((k^2-m1^2)((k+p)^2-m2^2))       *)
(* 迹 = 4 (k^2 + k.p + m1 m2) *)

(* 用 FeynCalc 的 TID 自动约化 *)
amp = (-I yS) (I yH) (-1) * 4 * (
        FVD[k, mu] FVD[k, mu] + FVD[k, mu] FVD[p, mu] + m1 m2 ) *
      FAD[{k, m1}, {k + p, m2}];

ampTID = TID[amp, p];                 (* 张量积分约化 *)
ampPV  = ToPaVe[ampTID, p];           (* 转 Passarino-Veltman *)
ampRed = PaVeReduce[ampPV];           (* 化为 A0 / B0 等标量积分 *)
Print["  约化结果 = ", ampRed];

(* 手算对照（m1 = m2 = m 时）：*)
(*   ∫ k^2/(..) = A0[m] + m^2 B0[p^2,m,m]                              *)
(*   ∫ k.p/(..) = -(1/2) p^2 B0[p^2,m,m]                                *)
(*   => Pi 的被积积分 = 4[ A0 + (2 m^2 - p^2/2) B0 ]                    *)
*)
Print["  手算对照（m1=m2=m）："];
Print["     Pi 对应积分 = 4 [ A0[m] + (2 m^2 - p^2/2) B0[p^2, m, m] ]"];
Print["     应能被 PaVeReduce 复现 —— 若不符，检查 FAD 的号规与 (-1) 费米子因子"];

Print[""];
Print["  ⚠ 注意三个易错点："];
Print["     (1) 费米子圈的 (-1) 因子与闭费米子链 —— 漏了整体差一个负号"];
Print("     (2) 号规：FeynCalc 用 FAD[{k,m}] = 1/(k^2-m^2)，与本文一致");
Print("     (3) 不等质量 m1 != m2 时 k.p 项含 [A0[m2]-A0[m1]]，不能照抄等质量式");


Print[""];
Print["############################################################"];
Print("# STEP 13 : Package-X —— 解析闭式一圈积分                     #");
Print("############################################################");

(*
<< X`                      (* Package-X 2.x *)
<< X`LoopIntegrate`        (* 若需要 LIntegrate *)

(* ---- 13a. 直接要解析结果 ---- *)
Print["  B0 解析式 : ", ScalarB0[pp, m1, m2]];
Print["  B1 解析式 : ", ScalarB1[pp, m1, m2]];
Print["  B00 解析式: ", ScalarB00[pp, m1, m2]];
Print["  DiscB     : ", DiscB[pp, m1, m2]];

(* Package-X 给的是**闭式**（含 Log 与 DiscB），可与我的解析式逐项对照 *)

(* ---- 13b. 用 LIntegrate 做原始积分 ---- *)
res = LIntegrate[ ( SPD[q] ) / (SPD[q] - Delta)^2, q ];
Print["  LIntegrate = ", res];
*)

Print["  预期判据："];
Print["     Package-X 的 ScalarB0 在 UV 发散部分应给出 1/eps + ln(mu^2/...) 结构，"];
Print("     与本文第 8 节的 ln(m^2/mu^2) - c + 1 对照 —— **注意是 (c-1) 不是 (c-1/2)**"];
Print("");
Print("     我早先写成 ln - c + 1/2，sympy FullSimplify 实测应为 ln - c + 1；");
Print("     c = 3/2 (MS-bar) 时两者都是 ln - 1/2，数值巧合相同，但一般 c 下差一个常数。");
Print("");
Print("     轻子项最终结果（已验证）：");
Print("        dm2_sh(light) = -(m^4/(Pi^2 v vs)) [ ln(m^2/mu^2) - c + 1 ]");
Print("        tau, vs=30 GeV, mu=125 GeV :  1.233000e-03 GeV^2");
Print("        （numpy 数值 1.233000e-03 vs sympy 解析 1.232999e-03，相对差 9.2e-8）");


Print[""];
Print["############################################################"];
Print("# STEP 14 : LoopTools —— 数值 Passarino-Veltman                #");
Print("############################################################");

(*
<< LoopTools`
SetMu[125.];        (* 重整化标度，与本文 mu = 125 GeV 一致 *)
SetDelta[0.];       (* IR 正规化；本问题无 IR 发散，取 0 *)
SetUV[1];           (* UV 发散正规化方案，LoopTools 默认用 1/eps 展开 *)

(* 用 PV 组装泡图贡献（等质量 m1=m2=m 时）*)
(*   Integral = 4 [ A0[m] + (2 m^2 - p^2/2) B0[p^2, m, m] ]  / (16 Pi^2) *)

bubble[p2_, m_] := 4 ( A0[m] + (2 m^2 - p2/2) B0[p2, m, m] ) / (16 Pi^2);

Print["  m=1.777 (tau), p^2 = 0    : ", bubble[0.,    1.777]];
Print["  m=1.777 (tau), p^2 = mh^2 : ", bubble[125.^2, 1.777]];
Print["  m=Mv=1000 (E 圈), p^2=0   : ", bubble[0.,    1000.]];
*)

Print["  预期判据（定性）："];
Print("     (a) 轻子圈结果 ~ 1e-3 GeV^2 量级（与解析 1.233e-03 对照）");
Print("     (b) E 圈（m = Mv = 1000 GeV）应比轻子圈大 ~4 个数量级");
Print("     (c) LoopTools 用 1/eps 展开，需与本文 MS-bar(c=3/2) 做方案换算：");
Print("        1/eps 极点 + ln(mu^2) 的组合 → ln(m^2/mu^2) - 3/2 + 1");
Print("");
Print("  ⚠ 方案换算是数值核对时最容易出错的地方。");
Print("     建议：**不要**直接比绝对值，而是比");
Print("        dm2(E 圈) / dm2(轻子圈)  —— 该比值与方案无关，应 ≈ 1.76e4 (M=1 TeV)");


Print[""];
Print["############################################################"];
Print("# STEP 15 : Collier —— 独立数值实现（交叉检验 LoopTools）      #");
Print("############################################################");

(*
<< Collier`

(* Collier 用 Denner-Dittmaier-Hofer 算法，支持复数质量，数值最稳健 *)
(* 函数名前缀 CO_ *)
b0  = CO_B0 [125.^2, 1.777, 1.777];
b1  = CO_B1 [125.^2, 1.777, 1.777];
b00 = CO_B00[125.^2, 1.777, 1.777];

Print["  CO_B0  = ", b0];
Print["  CO_B1  = ", b1];
Print["  CO_B00 = ", b00];

(* 与 LoopTools 同名函数逐点比对 —— 两个独立实现应吻合到机器精度 *)
*)
Print["  预期判据："];
Print("     Collier 与 LoopTools 的 B0/B1/B00 应吻合到 ~1e-10（同方案下）");
Print("     若两套独立实现不一致，先查：");
Print("       - SetMu / 重整化标度是否一致");
Print("       - 号规：Collier 与 LoopTools 对 B1 定义的符号约定可能不同");
Print("       - 是否都在 (m1,m2) 对称点");


Print[""];
Print["############################################################"];
Print("# STEP 16 : SARAH + SPheno —— 圈修正质量矩阵（最强端到端）     #");
Print("############################################################");

(* 这是**最省事也最权威**的独立检验：SPheno 直接输出圈修正的标量质量矩阵，
   其非对角元就是 dm2_Sh。SPheno 内部含**所有**粒子的一圈贡献（含 E），
   因此**不会漏图** —— 这正是本次事故的根源。 *)

Print["  SARAH 模型文件（非 SUSY；建议以 SARAH 自带的 SM 模型为模板改）"];
Print("  --------------- 8< --------------- SARAH/Models/HPLT/HPLT.m --------------- ");
Print("
Model`Name = \"HPLT\";
Model`NameLaTeX = \"Higgs-Portal axial Lmu-Ltau\";
Model`Authors = \"...\";
Model`Date = \"2026-01-01\";

(* ---- 规范群 ---- *)
Gauge[[1]] = {B,   U[1], hypercharge, g1, False};
Gauge[[2]] = {WB, SU[2], left,        g2, True };
Gauge[[3]] = {G,  SU[3], color,       g3, False};
Gauge[[4]] = {X,  U[1],  xcharge,     gX, False};

(* ---- 费米子 ---- *)
(* 语法：{Name, 代数, 分量, Y, SU(2)维数, SU(3)维数, X电荷(按代列表)} *)
FermionFields[[1]] = {LL, 3, {vL, eL}, -1/2, 2, 1, { 0, +1, -1}};
FermionFields[[2]] = {eR, 3,  eR,      -1,   1, 1, { 0, -1, +1}};
FermionFields[[3]] = {EE, 2,  EE,      -1,   1, 1, {    +1, -1}};  (* 矢量样 *)

(* ---- 标量 ---- *)
ScalarFields[[1]] = {H,  1, {Hp, H0},  1/2, 2, 1, 0};
ScalarFields[[2]] = {Sg, 1,  Ss,        0,  1, 1, 2};

(* ---- 相互作用（按 SARAH 非 SUSY 写法）---- *)
SuperPotential = - y1 LL.H.EE - y2 EE.eR.Sg - MuH2 H.H - MuS2 Sg.Sg;

(* ---- 标量势中的 portal（本问题主角）---- *)
(* 在 SARAH 中通过 DEFINITION / Parameters 给出 lamHS *)
Parameters`ToSolve = {muH2, muS2};

(* ---- 让 SPheno 输出圈修正质量矩阵 ---- *)
OnlyLowEnergySPheno = True;
");
Print("  --------------- 8< --------------- 模型文件结束 --------------- 8< --------------- ");

Print[""];
Print["  运行流程：");
Print["     (* 在 MMA 中 *)"];
Print("     << SARAH`");
Print("     Start[\"HPLT\"];");
Print("     MakeAll[];              (* 生成 SPheno 源码 *)"];
Print("");
Print("     (* 在 shell 中 *)"];
Print("     cd SARAH/Output/HPLT/EWSB/SPheno");
Print("     make");
Print("     ./bin/SPhenoLesHouches.in");
Print("");
Print("  关键：在 Les Houches 输入里设 flag，让 SPheno 输出**圈修正**质量矩阵");
Print("     Block SPhenoInput");
Print("       55  1          (* 输出 loop-corrected 质量矩阵 *)");
Print("       57  1          (* 输出 DeWitt 有效势/圈修正 *)");
Print("");
Print("  然后从 SLHA 输出中读标量的 (1,2) 非对角元 = dm2_Sh");

Print[""];
Print("  预期判据（本文主公式）："];
Print("     dm2_Sh = -(y1 y2)^2 v v_S/(8 Pi^2) = - M^2 m_l^2/(2 Pi^2 v v_S)");
Print("");
Print("     M[GeV]   y1y2    |dm2|[GeV^2]   lamHS^rad    |dm2|/mh^2");
Print("     300      0.144    1.95           2.64e-04      1.25e-04");
Print("     500      0.241    5.42           7.34e-04      3.47e-04");
Print("     1000     0.482   21.68           2.94e-03      1.39e-03");
Print("     1500     0.722   48.77           6.61e-03      3.12e-03");
Print("     2000     0.963   86.71           1.17e-02      5.55e-03");
Print("     3000     1.445  195.09           2.64e-02      1.25e-02");
Print("");
Print("     (tau 扇区, v_S = 30 GeV；mu 扇区小 (m_mu/m_tau)^2 = 1/283，可忽略)");
Print("");
Print("  ★ 若 SPheno 给出同量级结果 => 三重独立验证通过（CW / FeynCalc / SPheno）");
Print("  ⚠ 若差因子 2  => 先查 S 的 Sqrt[2] 归一化（本文用 S=(v_S+s)/Sqrt[2]）");
Print("  ⚠ 若差 ~1e4  => SPheno 没把 E 的耦合写进去，回查模型文件");


Print[""];
Print["############################################################"];
Print("# STEP 17 : HiggsTools —— 把实验约束从"经验值"换成真实拟合     #");
Print("############################################################");

(* 本文第 10 节用的是经验阈值：sin(theta) <~ 0.1-0.3, BR(h->SS) <~ 10%
   HiggsTools (= HiggsBounds-6 + HiggsSignals-3 合并后的 C++ 库) 可以把
   这些换成**合作组级别**的真实结果。这是回应审稿人"定量 + 实验限制"
   的关键一步。*)

Print["  HiggsTools 2.x 是 C++ 库 + Python 绑定，不是 MMA 包。"];
Print("  流程：FeynRules -> UFO -> (MadGraph 或自写) -> SLHA -> HiggsTools");
Print("");
Print("  ---- 17a. Python 接口（推荐）----");
Print("
from higgstools import HiggsBounds, HiggsSignals, predictions

# 从 SLHA 读模型预言
pred = predictions.Predictions()
hb_effc = predictions.Predictions()
hs_effc = predictions.Predictions()

# effC 模式：给 Higgs 的耦合标度因子（相对 SM）
hs = HiggsSignals(...)
result = hs(pred)
print("chi^2 =", result, "  nObs =", ...)

hb = HiggsBounds(...)
res = hb(pred)
print("excluded:", res.selected_limit)
");
Print("");
Print("  ---- 17b. 命令行（若装了 HiggsBounds-5 / HiggsSignals-2 老版）----");
Print("
./HiggsSignals 2 effC  MyModel/effC  latestresults  peak  2 effC
    # 参数: <nHiggs> <PDF> <模型目录> <实验集> <理论质量不确定性方法> ...
./HiggsBounds LandH effC MyModel/LandH 4 8
    # <分析> <输入模式> <目录> <LEP?TeV?> <LHC?>
");
Print("");
Print("  ---- 17c. 用 SPheno 的 SLHA 直接喂 ----");
Print("     SARAH 生成的 SPheno 会输出 HiggsBounds/Signals 需要的 SLHA block：");
Print("       Block MASS, Block SMINPUTS, Block HIGGSCOUPLINGS...");
Print("     或用 effective coupling 输入模式（effC）");

Print[""];
Print("  本文经验值 vs HiggsTools 应给出的结果（供对照）：");
Print("     M[GeV]   lamHS^rad   BR(h->SS)[%]   判定(经验阈值 10%)");
Print("     300      2.64e-04     0.01          安全");
Print("     1000     2.94e-03     1.00          安全");
Print("     1500     6.61e-03     4.85          安全");
Print("     1770     9.20e-03     9.00          临界");
Print("     2000     1.18e-02    13.88          排除");
Print("");
Print("     => 本文估算：M <~ 1.8 TeV (v_S = 30 GeV, BR < 10%)");
Print("     => 标度：lamHS ∝ M^2,  BR ∝ M^4");
Print("");
Print("  用 HiggsTools 做完后应能给出：");
Print("     (1) 真实的 sin(theta) 上限（替代我的 0.1-0.3 经验值）");
Print("     (2) 125 GeV 附近排除带的**真实宽度**（替代我的 0.87 / 3.47 GeV 估算）");
Print("     (3) M 上限的真实数值（替代我的 1.8 TeV）");
Print("");
Print("  这三项就是审稿人要的答案 —— 建议直接做成论文里的图。");


Print[""];
Print["############################################################"];
Print("# 附录 A : 各包获取与版本                                     #");
Print("############################################################");
Print("
  FeynRules     https://feynrules.irmp.ucl.ac.be       (自带安装说明)
  FeynArts      https://feynarts.de                     (需配 $FeynArtsDir)
  FeynCalc      https://feyncalc.github.io              (MMA paclet, 可 FCInstall)
  Package-X     https://packagex.hepforge.org           (Hiren Patel)
  LoopTools     https://feynarts.de/looptools           (与 FeynArts 同源)
  Collier       https://collier.hepforge.org            (Denner/Dittmaier/Hofer)
  SARAH         https://sarah.hepforge.org              (非 SUSY 亦可)
  SPheno        https://spheno.hepforge.org             (随 SARAH 生成)
  HiggsTools    https://higgstools.hepforge.org         (HB-6 + HS-3, C++/Python)
  pySecDec      https://secdec.hepforge.org             (本问题一圈，不必用)
");

Print[""];
Print("############################################################"];
Print("# 附录 B : 若要给审稿人最强的证据，按这个顺序做                 #");
Print("############################################################");
Print("
  1) PART A STEP 5   : 极限系数 = 2（高精度收敛必过）—— 确认主公式系数
  2) PART A STEP 6   : 方案无关性（扫 cc）—— 确认没算漏项
  3) STEP 11 FeynArts: 自动枚举，确认含 E 的图存在且主导 —— 确认物理完备
  4) STEP 16 SPheno  : 圈修正质量矩阵非对角元 —— 端到端独立验证
  5) STEP 17 HiggsTools: 真实 LHC 边界 —— 把经验阈值换成拟合
");
Print("  第 3 步是本次事故的直接对策：");
Print("    手画漏了 E 圈，导致结果小 1.8e4 倍，结论从"必须挖带"变成"可忽略"。");
Print("    自动枚举可以杜绝这类错误。");

Print[""];
Print["=== PART B 结束 ==="];
