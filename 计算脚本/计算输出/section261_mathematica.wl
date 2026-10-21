ClearAll @@ Names["Global" <> FromCharacterCode[96] <> "*"];
checks = 0;
check[name_, expr_] := Module[{res = Expand /@ Flatten[{expr}]},
  If[And @@ (TrueQ[# === 0] & /@ res),
    checks++; Print["PASS ", checks, " ", name],
    Print["FAIL ", name, " residual=", InputForm[res]]; Exit[2]]
];
tr1[x_?MatrixQ] := Map[tr1, x, {2}];
tr1[x_] := Normal[Series[x, {ep, 0, 1}]];
hes[fun_, vars_] := Table[D[fun, vars[[i]], vars[[j]]], {i, 2}, {j, 2}];
Print["ENGINE ", $Version];
Print["SYSTEM ", $SystemID];
pot = -mh x - ms y + lh x^2 + ls y^2 + lp x y +
  e30 x^3 + e03 y^3 + e21 x^2 y + e12 x y^2;
rad = pot /. {x -> rho^2/2, y -> sig^2/2};
vac = {rho -> vv, sig -> ww};
fx0 = D[pot, x] /. {x -> vv^2/2, y -> ww^2/2};
fy0 = D[pot, y] /. {x -> vv^2/2, y -> ww^2/2};
muRules = {
  mh -> lh vv^2 + lp ww^2/2 + 3 e30 vv^4/4 + e21 vv^2 ww^2/2 + e12 ww^4/4,
  ms -> ls ww^2 + lp vv^2/2 + 3 e03 ww^4/4 + e21 vv^4/4 + e12 vv^2 ww^2/2
};
check["tadpole h", (D[rad, rho] /. vac) - vv fx0];
check["tadpole s", (D[rad, sig] /. vac) - ww fy0];
check["stationary invariant derivatives", {fx0, fy0} /. muRules];
hess0 = (hes[rad, {rho, sig}] /. vac) /. muRules;
hessExpected = {
 {vv^2 (2 lh + 3 e30 vv^2 + e21 ww^2), vv ww (lp + e21 vv^2 + e12 ww^2)},
 {vv ww (lp + e21 vv^2 + e12 ww^2), ww^2 (2 ls + 3 e03 ww^2 + e12 vv^2)}
};
check["sextic radial Hessian", hess0 - hessExpected];
check["tadpole contribution before stationarity",
  (D[rad, {rho, 2}] /. vac) - hessExpected[[1, 1]] - fx0];
complexPot = pot /. {x -> (rho^2 + chi^2)/2, y -> (sig^2 + eta^2)/2};
check["Goldstone H potential mass",
  (D[complexPot, {chi, 2}] /. Join[vac, {chi -> 0, eta -> 0}]) - fx0];
check["Goldstone S potential mass",
  (D[complexPot, {eta, 2}] /. Join[vac, {chi -> 0, eta -> 0}]) - fy0];
kin = (dh^2 + ds^2)/2 + cx rho^2 dh^2 + cy sig^2 ds^2 +
  chd rho^2 dh^2/4 + cd rho sig dh ds;
kRad = hes[kin, {dh, ds}] /. vac;
check["radial kinetic matrix", kRad - {
 {1 + vv^2 (2 cx + chd/2), cd vv ww},
 {cd vv ww, 1 + 2 cy ww^2}}];
check["AH radial cancellation",
  2 (bh/3 - ah - 3 aw/4) + (-bh/2 + 4 ah)/2 - (5 bh/12 - 3 aw/2)];
m0 = {{aa, bb}, {bb, cc}};
dm = {{da, db}, {db, dc}};
em = {{eh, ex}, {ex, es}};
id = IdentityMatrix[2];
tm = id - ep em/2;
kt = id + ep em;
ht = m0 + ep dm;
mc = tr1[Transpose[tm].ht.tm];
check["canonical kinetic", tr1[Transpose[tm].kt.tm] - id];
check["mass anticommutator", mc - (m0 + ep (dm - (em.m0 + m0.em)/2))];
check["explicit mixed entry",
  mc[[1, 2]] - (bb + ep (db - (eh + es) bb/2 - ex (aa + cc)/2))];
check["generalized characteristic equation",
  tr1[Det[zz kt - ht]/Det[kt]] - tr1[Det[zz id - mc]]];
check["generalized polynomial coefficients",
 Det[zz {{kh, kx}, {kx, ks}} - m0] -
 ((kh ks - kx^2) zz^2 - (ks aa + kh cc - 2 kx bb) zz + aa cc - bb^2)];
rr = {{co, si}, {-si, co}};
rotated = Transpose[rr].m0.rr;
check["rotation sign",
 rotated[[1, 2]] - (bb (co^2 - si^2) + (aa - cc) co si)];
detVev = 4 lh ls - lp^2;
shiftNums = {2 ls px - lp py, 2 lh py - lp px};
check["fixed UV VEV shift", {{2 lh, lp}, {lp, 2 ls}}.shiftNums - detVev {px, py}];
vt = -mh rho^2/2 - ms sig^2/2 + lh rho^4/4 + ls sig^4/4 + lp rho^2 sig^2/4;
treeRules = {mh -> lh vv^2 + lp ww^2/2, ms -> ls ww^2 + lp vv^2/2};
vimage = vt - ep (aw rho^3 D[vt, rho]/4 + ass sig^3 D[vt, sig]);
newVac = {rho -> vv + ep aw vv^3/4, sig -> ww + ep ass ww^3};
check["gauge EOM shifted tadpole H", tr1[(D[vimage, rho] /. newVac) /. treeRules]];
check["gauge EOM shifted tadpole S", tr1[(D[vimage, sig] /. newVac) /. treeRules]];
oldHess = (hes[vt, {rho, sig}] /. vac) /. treeRules;
newHess = tr1[(hes[vimage, {rho, sig}] /. newVac) /. treeRules];
imageE = DiagonalMatrix[{-3 aw vv^2/2, -6 ass ww^2}];
imageT = id - ep imageE/2;
check["gauge EOM radial spectral matrix",
 tr1[Transpose[imageT].newHess.imageT] - oldHess];
rm = DiagonalMatrix[{rh, rs}];
gamma = zz id - m0 + ep rm zz^2;
field = id - ep rm.(zz id + m0)/2;
check["noncommuting p4 field transformation",
 tr1[Transpose[field].gamma.field] - (zz id - m0 + ep m0.rm.m0)];
vr = -(rh D[vt, rho]^2 + rs D[vt, sig]^2)/2;
check["p4 potential Hessian",
 ((hes[vr, {rho, sig}] /. vac) /. treeRules) + oldHess.rm.oldHess];
massFn = yy rho (1 - f0 - fxx rho^2/2 - fyy sig^2/2);
check["ordinary fermion h source",
 (D[massFn, rho] /. vac) - yy (1 - f0 - 3 fxx vv^2/2 - fyy ww^2/2)];
check["ordinary fermion s source", (D[massFn, sig] /. vac) + yy fyy vv ww];
weighted = lh vv^2 + ls ww^2;
mixed = -vv ww (kb - cp weighted + (2 lh cp + dd21) vv^2 +
 (2 ls cp + dd12) ww^2 + cder weighted);
check["zero UV portal combined matrix",
 mixed + vv ww (kb + (cp + cder) weighted + dd21 vv^2 + dd12 ww^2)];
flavorRules = {kb -> 2 q uu vy, cp -> q uu vy mi (ell - 3/2),
 cder -> q uu vy mi (7/6 - ell/2),
 dd21 -> -q uu^2 vy mi, dd12 -> -q uu vy^2 mi};
check["zero UV portal per flavor",
 (mixed /. flavorRules) + q vv ww uu vy (
 2 + mi ((ell/2 - 1/3) weighted - uu vv^2 - vy ww^2))];
Print["RESULT: ", checks, " Mathematica symbolic checks passed"];
Print["Scope: independent symbolic differentiation and matrix algebra; no loop diagram package was run."];
Exit[0];
