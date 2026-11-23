(* ::Title:: *)
(* Key result audit: one-loop Higgs-portal threshold from a Dirac fermion *)

(* Scope:
   - Checks the effective-potential algebra used in Sections 272-273.
   - Does NOT generate FeynArts diagrams or execute FeynCalc.
   - Convention: V_eff^1 = -(1/(16 Pi^2)) Sum_i x_i^2
       (Log[x_i/muR2] - 3/2), with x_i fermion mass-squared eigenvalues.
*)

ClearAll["Global`*"];

(* Symbols *)
A = Unique["A"];                 (* |y|^2 H^\dagger H *)
B = Unique["B"];                 (* |lambda|^2 S^\dagger S *)
M2 = Unique["M2"];               (* M_E^2, positive *)
L = Unique["L"];                 (* Log[M2/muR2] *)

(* Sum of squared eigenvalues: x_+ + x_- = M2+A+B,
   x_+ x_- = A B. Thus Sum[x_i^2] = (Sum[x_i])^2 - 2 Product[x_i]. *)
uvPoly = Expand[(M2 + A + B)^2 - 2 A B];
uvCrossCoeff = Coefficient[Coefficient[uvPoly, A], B];

(* Heavy eigenvalue to quartic field order:
   x_+ = M2 + A + B - A B/M2 + O(fields^6).
   For F(x)=x^2(Log[x/muR2]-3/2):
   F'(M2)=2 M2 (L-1), F''(M2)=2 L.
   The AB coefficient is -F'(M2)/M2 + F''(M2). *)
Fp = 2 M2 (L - 1);
Fpp = 2 L;
finiteCWCrossCoeff = FullSimplify[-Fp/M2 + Fpp];

(* Dirac fermion one-loop effective-potential prefactor. *)
deltaLambdaPerFlavor = FullSimplify[-finiteCWCrossCoeff/(16 Pi^2)];

expected = {0, 2, -1/(8 Pi^2)};
actual = {uvCrossCoeff, finiteCWCrossCoeff, deltaLambdaPerFlavor};
checks = Thread[FullSimplify[actual - expected] == 0];

Print["{UV AB coefficient in Sum[x_i^2], finite CW AB coefficient, Delta lambda per flavor}"];
Print[actual];
Print["Checks: ", checks];

If[And @@ checks,
  Print["PASS: exact effective-potential algebra checks passed."],
  Print["FAIL: inspect conventions and expansion."]
];

(* Two-flavor result:
   Delta lambda_HS = -(Abs[yMu]^2 Abs[lamMu]^2
                       + Abs[yTau]^2 Abs[lamTau]^2)/(8 Pi^2). *)
ClearAll[yMu, yTau, lamMu, lamTau];
deltaLambdaHS = -(
    Abs[yMu]^2 Abs[lamMu]^2 + Abs[yTau]^2 Abs[lamTau]^2
  )/(8 Pi^2);
Print["Two-flavor threshold: ", deltaLambdaHS];

(* Optional seesaw mapping, for degenerate M_E:
   |y_l lambda_l|^2 = 4 M_E^2 m_l^2/(v_h^2 v_s^2). *)
ClearAll[ME, mMu, mTau, vh, vs];
deltaLambdaSeesaw = -ME^2 (mMu^2 + mTau^2)/(2 Pi^2 vh^2 vs^2);
Print["Seesaw-rewritten threshold: ", deltaLambdaSeesaw];

(* Important: this is not a FeynCalc box-diagram calculation. *)
