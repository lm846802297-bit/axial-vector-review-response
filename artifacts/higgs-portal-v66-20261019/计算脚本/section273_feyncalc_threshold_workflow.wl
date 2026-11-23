(* ::Title:: *)
(* Section 273: FeynCalc workflow scaffold for the Higgs portal threshold *)

(* IMPORTANT:
   1. This file is a reproducible scaffold, not a claimed FeynCalc run.
   2. Install compatible Mathematica, FeynArts and FeynCalc versions.
   3. Create a custom FeynArts model file defining H0, H0bar, S, Sbar,
      E_mu/E_tau, light leptons, masses, and all chiral Yukawa vertices.
   4. Replace all schematic particle labels in the FeynArts block below.
*)

(* ---------- A. Load packages ---------- *)
(* Uncomment and run in an environment where the packages are installed. *)
(*
<< FeynArts`
<< FeynCalc`
$FAVerbose = 0;
*)

(* ---------- B. FeynArts diagram-generation scaffold ---------- *)
(*
modelFile = "AxialVectorPortal";  (* custom .mod file, not a stock SM model *)
top = CreateTopologies[1, 2 -> 2];
ins = InsertFields[
  top,
  {S[H0], S[Sfield]} -> {S[H0bar], S[Sfieldbar]},
  Model -> modelFile,
  InsertionLevel -> {Classes}
];
ampFA = CreateFeynAmp[ins, Truncated -> True, PreFactor -> 1];

(* Inspect/retain only the E_l-light-lepton box diagrams. Confirm the
   diagram count and all conjugate/chiral vertices by hand. *)
ampFC = FCFAConvert[
  ampFA,
  IncomingMomenta -> {p1, p2},
  OutgoingMomenta -> {p3, p4},
  LoopMomenta -> {q},
  UndoChiralSplittings -> True,
  ChangeDimension -> D,
  List -> False,
  Contract -> True
];
ampDirac = DiracSimplify[ampFC, DiracTraceEvaluate -> True];
ampTID = TID[ampDirac, q, ToPaVe -> True];
ampPV = PaVeReduce[ampTID];
*)

(* ---------- C. Independent exact algebra check for the CW threshold ---------- *)
ClearAll[A, B, M2, muR2, L, Fp, Fpp, uvPoly, uvCrossCoeff,
  crossCoeff, deltaLambdaPerFlavor];

L = Log[M2/muR2];
Fp = 2 M2 (L - 1);
Fpp = 2 L;

(* Heavy eigenvalue: x_+ = M2 + A + B - A B/M2 + higher field order. *)
crossCoeff = FullSimplify[-Fp/M2 + Fpp];

(* UV-pole structure proportional to Sum_i x_i^2. *)
uvPoly = Expand[(M2 + A + B)^2 - 2 A B];
uvCrossCoeff = Coefficient[Coefficient[uvPoly, A], B];

(* Dirac-fermion CW prefactor -1/(16 Pi^2). *)
deltaLambdaPerFlavor = FullSimplify[-crossCoeff/(16 Pi^2)];

expected = {2, 0, -1/(8 Pi^2)};
actual = {crossCoeff, uvCrossCoeff, deltaLambdaPerFlavor};
Print["CW cross-check {finite coefficient, UV cross coefficient, Delta lambda}:"];
Print[actual];
If[FullSimplify[actual - expected] === {0, 0, 0},
  Print["PASS: exact Coleman-Weinberg algebra check."],
  Print["FAIL: compare conventions and expansion."]
];

(* This algebra check does not execute FeynCalc and does not replace
   the explicit FeynArts diagram calculation above. *)
