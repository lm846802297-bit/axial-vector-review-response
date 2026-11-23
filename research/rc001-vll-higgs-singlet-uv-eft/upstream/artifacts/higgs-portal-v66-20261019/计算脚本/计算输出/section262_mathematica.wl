ClearAll @@ Names["Global" <> FromCharacterCode[96] <> "*"];
count = 0;
assumptions = cc > 0 && vv > 0 && ww > 0 && mu > 0;
check[name_, expr_, extra_: True] := Module[{res},
 res = FullSimplify[Flatten[{expr}], Assumptions -> assumptions && extra];
 If[And @@ (TrueQ[# === 0] & /@ res),
  count++; Print["PASS ", count, " ", name],
  Print["FAIL ", name, " residual=", InputForm[res]]; Exit[2]]
];
Print["ENGINE ", $Version];
Print["SYSTEM ", $SystemID];
g0 = KroneckerProduct[PauliMatrix[3], IdentityMatrix[2]];
gam = Prepend[Table[I KroneckerProduct[PauliMatrix[2], PauliMatrix[i]], {i, 3}], g0];
k = {k0, k1, k2, k3}; pp = {p0, p1, p2, p3};
metric = {1, -1, -1, -1};
slash[a_] := Sum[metric[[i]] a[[i]] gam[[i]], {i, 4}];
num = Tr[(slash[k] + mm IdentityMatrix[4]).(slash[k + pp] + mm IdentityMatrix[4])];
check["explicit massive Dirac trace",
 num - 4 (Sum[metric[[i]] k[[i]] (k[[i]] + pp[[i]]), {i, 4}] + mm^2)];
check["PV numerator reduction",
 4 (kk + kp + mm^2) - 2 ((kk - mm^2) + (kk + 2 kp + ss - mm^2) + 4 mm^2 - ss)];
bubble = -2 q ga gb (2 aa + (4 mm^2 - ss) bb);
contact = -4 q mm hab aa;
bare = bubble + contact;
pole = Coefficient[Expand[bare /. {aa -> mm^2 (uv + 1 - lm), bb -> uv + bf}], uv];
check["massive UV pole",
 pole - (2 q ga gb (ss - 6 mm^2) - 4 q mm^3 hab)];
massFun = cc rho sig/2;
g = {D[massFun, rho], D[massFun, sig]};
hs = Table[D[massFun, {rho, sig}[[i]], {rho, sig}[[j]]], {i, 2}, {j, 2}];
vac = {rho -> vv, sig -> ww};
m0 = massFun /. vac; gv = g /. vac; hv = hs /. vac;
check["C5 radial vertices", {gv[[1]] - cc ww/2, gv[[2]] - cc vv/2, hv[[1, 2]] - cc/2}];
check["no diagonal contact vertices", {hv[[1, 1]], hv[[2, 2]]}];
vLoop = q massFun^4 (uv + 3/2 - Log[massFun^2/mu^2]);
vHess = Table[D[vLoop, {rho, sig}[[i]], {rho, sig}[[j]]], {i, 2}, {j, 2}] /. vac;
lz = Log[m0^2/mu^2];
piZero = Table[
 -2 q gv[[i]] gv[[j]] (2 m0^2 (uv + 1 - lz) + 4 m0^2 (uv - lz)) -
 4 q m0^3 hv[[i, j]] (uv + 1 - lz), {i, 2}, {j, 2}];
check["bubble plus contact is minus CW Hessian", piZero + vHess];
tad = (D[vLoop, rho] /. vac);
check["CW tadpole sign", tad - 4 q m0^3 gv[[1]] (uv + 1 - lz)];
uvPot = q uv massFun^4;
uvHess = Table[D[uvPot, {rho, sig}[[i]], {rho, sig}[[j]]], {i, 2}, {j, 2}] /. vac;
massPole = Table[-12 q uv gv[[i]] gv[[j]] m0^2 - 4 q uv m0^3 hv[[i, j]], {i, 2}, {j, 2}];
check["dimension8 UV potential", uvHess + massPole];
check["dimension8 invariant monomial", massFun^4 - cc^4 (rho^2/2)^2 (sig^2/2)^2];
kin = q uv (g[[1]] dh + g[[2]] ds)^2;
check["product derivative radial action",
 kin - q uv cc^2 (sig^2 dh^2/4 + rho^2 ds^2/4 + rho sig dh ds/2)];
check["kinetic rank one", Det[Outer[Times, gv, gv]]];
check["radial orthogonal null direction", gv.{vv, -ww}];
check["phase current product direct", 2 ar br + 2 ai bi - (4 ar br - (-4 ai bi))/2];
check["phase current product conjugate", 2 ar br - 2 ai bi - (4 ar br + (-4 ai bi))/2];
ct = -a (rhMix + rsMix + od/2 - sign oj/2);
ctEom = ct /. rhMix -> (rem - od + (fh + fs) x y + (y jh + x js)/2);
ctEom = ctEom /. rsMix -> -rem;
check["complete EOM counterterm", ctEom -
 a (od/2 + sign oj/2 - (fh + fs) x y - (y jh + x js)/2)];
check["C hard-log counterterm control", -2 D[a (ll - 3/2), ll] - 2 (-a)];
check["CD hard-log counterterm control", -2 D[a (7/6 - ll/2), ll] - a];
check["CJ hard-log counterterm control", -2 D[-sign a (ll - 2)/2, ll] - sign a];
bSeries = Sum[z^n (n!)^2/(n (2 n + 1)!), {n, 1, 5}];
diffSeries = Normal[Series[-z lm + (z - 4) bSeries, {z, 0, 4}]];
check["low momentum difference moments",
 diffSeries - ((-lm - 2/3) z + z^2/10 + z^3/140 + z^4/1260)];
finite = bare /. {aa -> mm^2 (1 - lm), bb -> -lm + bf};
finiteZero = bare /. {ss -> 0, aa -> mm^2 (1 - lm), bb -> -lm};
check["finite subtracted momentum kernel",
 finite - finiteZero - 2 q ga gb (-ss lm + (ss - 4 mm^2) bf)];
check["massless finite scalar kernel",
 (bubble /. {mm -> 0, aa -> 0, bb -> bmassless}) - 2 q ga gb ss bmassless];
check["beta cubed absorptive factor",
 (-2 q ga gb (4 mm^2 - ss) Pi beta /. mm^2 -> ss (1 - beta^2)/4) -
 2 q ga gb Pi ss beta^3];
bbLow = 2 - 2 Sqrt[4/z - 1] ArcTan[1/Sqrt[4/z - 1]];
check["below threshold B0 derivative", D[bbLow, z] - (2 bbLow - z)/(z (z - 4)), 0 < z < 4];
bbHigh = 2 - Sqrt[1 - 4/z] Log[(1 + Sqrt[1 - 4/z])/(1 - Sqrt[1 - 4/z])] +
 I Pi Sqrt[1 - 4/z];
check["above threshold B0 derivative", D[bbHigh, z] - (2 bbHigh - z)/(z (z - 4)), z > 4];
check["optical width normalization",
 (2 q yy^2 Pi ss beta^3 /. q -> 1/(16 Pi^2)) - Sqrt[ss] (yy^2 Sqrt[ss] beta^3/(8 Pi)), ss > 0];

bClosed[zz_] := Which[
 zz < 0, 2 - Sqrt[1 - 4/zz] Log[(Sqrt[1 - 4/zz] + 1)/(Sqrt[1 - 4/zz] - 1)],
 zz == 0, 0,
 0 < zz < 4, 2 - 2 Sqrt[4/zz - 1] ArcTan[1/Sqrt[4/zz - 1]],
 zz == 4, 2,
 zz > 4, 2 - Sqrt[1 - 4/zz] Log[(1 + Sqrt[1 - 4/zz])/(1 - Sqrt[1 - 4/zz])] +
 I Pi Sqrt[1 - 4/zz]
];
numCount = 0;
Do[
 cuts = If[zz >= 4, DeleteDuplicates[{(1 - Sqrt[1 - 4/zz])/2, (1 + Sqrt[1 - 4/zz])/2}], {}];
 bounds = Join[{xx, 0}, cuts, {1}];
 real = NIntegrate[-Log[Abs[1 - zz xx (1 - xx)]], Evaluate[bounds],
   WorkingPrecision -> 40, AccuracyGoal -> 25, PrecisionGoal -> 25];
 imag = If[zz > 4, NIntegrate[Pi, {xx, cuts[[1]], cuts[[2]]},
   WorkingPrecision -> 40, AccuracyGoal -> 25, PrecisionGoal -> 25], 0];
 err = Abs[real + I imag - N[bClosed[zz], 35]];
 If[! TrueQ[err < 10^-23], Print["FAIL NUMERIC ", zz, " ", err]; Exit[3]];
 numCount++;
 Print["INTEGRAL z=", InputForm[zz], " real=", N[real, 18], " imag=", N[imag, 18], " error=", N[err, 3]],
 {zz, {-2, 1, 39/10, 4, 5, 10}}];
Print["RESULT: ", count, " Mathematica symbolic checks passed; ", numCount, " high-precision B0 integrals passed"];
Print["No FeynArts/FeynCalc or other loop package was loaded or run."];
Exit[0];
