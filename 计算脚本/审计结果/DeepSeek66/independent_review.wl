ClearAll @@ Names["Global" <> FromCharacterCode[96] <> "*"];
identities=0;counterexamples=0;
verify[label_,expr_] := Module[{r=FullSimplify[expr,Assumptions->c>0&&v>0&&w>0&&m>0&&mu>0]},
 If[And@@(TrueQ[#===0]&/@Flatten[{r}]),identities++;Print["VERIFIED ",label],
 Print["FAIL CORRECT IDENTITY ",label," ",InputForm[r]];Exit[2]]];
reject[label_,claimed_,correct_] := Module[{d=N[claimed-correct,30]},
 If[TrueQ[Abs[d]>10^-15],counterexamples++;
 Print["COUNTEREXAMPLE ",label," | claimed=",N[claimed,18]," | correct=",N[correct,18]," | difference=",d],
 Print["FAIL TO FALSIFY ",label," ",InputForm[d]];Exit[3]]];
Print["ENGINE ",$Version];
mass=c (v+h) (w+s)/2;
verify["radial h vertex from original mass",(D[mass,h]/.{h->0,s->0})-c w/2];
verify["radial s vertex from original mass",(D[mass,s]/.{h->0,s->0})-c v/2];
verify["unavoidable mixed contact",D[mass,h,s]-c/2];
reject["wrong bubble hh/ss ratio at v=3,w=4",9/16,16/9];

d1=k2-m^2;d2=k2+2 kp+p2-m^2;
verify["exact PV numerator",k2+kp+m^2-(d1+d2)/2-(2 m^2-p2/2)];
reject["B0 bracket at m=1,p2=-1",1+1/2,2+1/2];
reject["UV bracket at m=1,p2=-1",2+1/2,3+1/2];
verify["A0 pole remains one times m squared",m^2+(2 m^2-p2/2)-(3 m^2-p2/2)];
reject["B0 finite at zero with m=mu=1",2,0];

b[z_] := Which[
 z<0,2-Sqrt[1-4/z] Log[(Sqrt[1-4/z]+1)/(Sqrt[1-4/z]-1)],
 z==0,0,
 0<z<4,2-2 Sqrt[4/z-1] ArcTan[1/Sqrt[4/z-1]],
 z==4,2,
 z>4,2-Sqrt[1-4/z] Log[(1+Sqrt[1-4/z])/(1-Sqrt[1-4/z])]+I Pi Sqrt[1-4/z]];
integralCount=0;
Do[
 roots=If[z>=4,DeleteDuplicates[{(1-Sqrt[1-4/z])/2,(1+Sqrt[1-4/z])/2}],{}];
 bounds=Join[{x,0},roots,{1}];
 rr=NIntegrate[-Log[Abs[1-z x (1-x)]],Evaluate[bounds],WorkingPrecision->40,AccuracyGoal->25,PrecisionGoal->25];
 ii=If[z>4,NIntegrate[Pi,{x,roots[[1]],roots[[2]]},WorkingPrecision->40,AccuracyGoal->25,PrecisionGoal->25],0];
 If[!TrueQ[Abs[rr+I ii-N[b[z],35]]<10^-23],Print["FAIL INTEGRAL ",z];Exit[4]];
 integralCount++;Print["INTEGRAL z=",z," | B0fin(m=mu=1)=",N[rr+I ii,18]],
 {z,{-1,1,5}}];
reject["published B0 additive constant, spacelike z=-1",2+b[-1],b[-1]];
reject["imaginary I2 at z=5 in the fixed Feynman convention",-Pi/Sqrt[5],Pi/Sqrt[5]];
reject["scalar absorptive part at z=5 after stripping q*g^2",-6 Pi/Sqrt[5],2 Pi/Sqrt[5]];

mf=(v+h) (w+s);
v1=-mf^4 (Log[mf^2]-3/2);
hess=Table[D[v1,{h,s}[[i]],{h,s}[[j]]],{i,2},{j,2}]/.{h->0,s->0,v->1,w->1};
verify["CW Hessian fixes full finite Pi(0)",hess-{{4,8},{8,4}}];
fullPi=-hess;
reject["rank one for full massive C5 self energy at p2=0",0,Det[fullPi]];

reject["opposite pole shift in document example",36000/10000-5481/10000,36000/10000+5481/10000];
gamma={{(1+alpha) zz-1,0},{0,zz-4}};
zeroDet=Det[gamma]/.zz->0;
rootProduct=4/(1+alpha);
reject["det Gamma(0) is not product of momentum-dependent pole masses",zeroDet/.alpha->1/10,rootProduct/.alpha->1/10];

kg={{1,1/5},{1/5,1}};hh={{1,0},{0,4}};
trueChar=Det[zz kg-hh];
claimedChar=zz^2-5 zz+4;
verify["omitted Khs squared term",claimedChar-trueChar-zz^2/25];
reject["claimed exact scalar characteristic polynomial at z=1",claimedChar/.zz->1,trueChar/.zz->1];
rootsWrong=zz/.Solve[trueChar==0,zz];
Print["GAUGE_SCALAR_MIXUP | no scalar-derivative Wilson: correct scalar masses2={1,4}; using gauge K0 gives ",N[rootsWrong,15]];

(* At the author's example point, reproduce their number from the wrong kernel.
   This confirms that agreement of quadrature with a formula does not fix its input. *)
a=4 (1-Log[4]);br=-Log[4]+b[-5/4];
dsValue=-4 (9/10)^2 (a+(4+5/2) (br+2));
trueBubble=-4 (9/10)^2 (a+(8+5/2) br);
Print["AUTHOR_ANCHOR | erroneous written expression=",N[dsValue,18],
 " | correct bubble with same arbitrary coupling, q stripped=",N[trueBubble,18]];
reject["same-input full bubble anchor",dsValue,trueBubble];

Print["RESULT: ",identities," independent symbolic identities verified; ",
 counterexamples," explicit claimed relations falsified; ",integralCount," independent B0 integrals passed"];
Print["Scope: no prior chapter checker was used as the physical ground truth. No FeynArts/FeynCalc was loaded."];
Exit[0];
