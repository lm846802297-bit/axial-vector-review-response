#!/usr/bin/env node
"use strict";

// Figure-level, transport-only estimate of high-energy V -> nu nu daughter
// escape using the public SFHo-18.8 t_pb=1s baryon-density curve.
// This is not a full neutrino energy-sphere or Boltzmann transport calculation.
// Run from blinov_reproduction:
// node audit_b16_public_density_neutrino_transport_envelope.js \
//   outputs/b16_p1c_global_polarization_b14_split_10mev_2026-11-10.json \
//   outputs/b16_public_density_neutrino_transport_envelope_10mev_2026-11-10.json

const fs=require("node:fs"),path=require("node:path");
const inputPath=process.argv[2]||"outputs/b16_p1c_global_polarization_b14_split_10mev_2026-11-10.json";
const outputPath=process.argv[3]||"outputs/b16_public_density_neutrino_transport_envelope_10mev_2026-11-10.json";
const MASS=10, N0_MFP_CM=25, E0_MEV=100;
const TAILS={
  low:{nB20_over_n0:0.5e-3,H_km:0.9},
  central:{nB20_over_n0:1.0e-3,H_km:1.2},
  high:{nB20_over_n0:2.0e-3,H_km:1.3}
};
const RADII=[25,26,27.5,30], REPRESENTATIVE_OMEGAS=[210,300,510];
const NEUTRINO_ENERGIES=[100,150,255,500], TARGETS=[0.5,0.9,0.99];
function gl(n){
 const x=new Float64Array(n),w=new Float64Array(n);
 for(let i=0;i<Math.ceil(n/2);i++){
  let z=Math.cos(Math.PI*(i+.75)/(n+.5)),pp,p1,p2;
  for(let it=0;it<40;it++){
   p1=1;p2=0;
   for(let j=1;j<=n;j++){const p3=p2;p2=p1;p1=((2*j-1)*z*p2-(j-1)*p3)/j;}
   pp=n*(z*p1-p2)/(z*z-1);const old=z;z-=p1/pp;if(Math.abs(z-old)<2e-15)break;
  }
  p1=1;p2=0;
  for(let j=1;j<=n;j++){const p3=p2;p2=p1;p1=((2*j-1)*z*p2-(j-1)*p3)/j;}
  pp=n*(z*p1-p2)/(z*z-1);const wi=2/((1-z*z)*pp*pp);
  x[i]=-z;x[n-1-i]=z;w[i]=wi;w[n-1-i]=wi;
 }
 return{x,w};
}
const q=gl(256);
const modes={
 L:z=>0.75*(1-z*z),
 plus:z=>0.375*(1+z)*(1+z),
 minus:z=>0.375*(1-z)*(1-z)
};
function tauNuN(E,r,tail){
 const tau100=tail.nB20_over_n0*(tail.H_km*1e5)/N0_MFP_CM*Math.exp(-(r-20)/tail.H_km);
 return tau100*(E/E0_MEV)**2;
}
function pairEscape(omega,r,tail){
 const beta=Math.sqrt(1-MASS*MASS/(omega*omega)),byMode={};
 for(const [mode,W] of Object.entries(modes)){
  let norm=0,escape=0;
  for(let i=0;i<q.x.length;i++){
   const z=q.x[i],weight=q.w[i]*W(z);
   const e1=omega*(1+beta*z)/2,e2=omega*(1-beta*z)/2;
   norm+=weight;
   escape+=weight*(e1*Math.exp(-tauNuN(e1,r,tail))+
                   e2*Math.exp(-tauNuN(e2,r,tail)))/omega;
  }
  byMode[mode]=escape/norm;
 }
 return{by_mode:byMode,equal_mode_average:(byMode.L+byMode.plus+byMode.minus)/3};
}
function transportRadius(E,tail){
 const tau25=tauNuN(E,25,tail);
 const tau20=tauNuN(E,20,tail);
 return{tau_at_25km:tau25,radius_tau_2_3_km:20+tail.H_km*Math.log(tau20/(2/3))};
}
function pairEscapeRadius(omega,tail,target){
 let lo=15,hi=40;
 for(let i=0;i<60;i++){
  const mid=(lo+hi)/2;
  if(pairEscape(omega,mid,tail).equal_mode_average<target)lo=mid;else hi=mid;
 }
 return(lo+hi)/2;
}
function main(){
 const modeNorms=Object.fromEntries(Object.entries(modes).map(([name,W])=>[name,q.x.reduce((s,z,i)=>s+q.w[i]*W(z),0)]));
 const sumIdentityMaxAbs=Math.max(...q.x.map(z=>Math.abs(modes.L(z)+modes.plus(z)+modes.minus(z)-1.5)));
 if(Object.values(modeNorms).some(x=>Math.abs(x-1)>1e-12)||sumIdentityMaxAbs>1e-12)throw new Error("Polarization-weight normalization failed");
 const p1c=JSON.parse(fs.readFileSync(inputPath,"utf8"));
 const nodes=p1c.calculation.band_energy_nodes_MeV;
 if(!Array.isArray(nodes)||nodes.length!==10)throw new Error("Expected ten P1-C band energy nodes");
 const result={
  title:"Public-density transport-only envelope for 10 MeV high-energy vector-decay daughters",
  date:"2026-11-10",
  inputs:{
   source:"Caputo, Raffelt & Vitagliano, PRD 105, 035022 (2022), Fig. 1: SFHo-18.8 at t_pb=1 s",
   figure_read_off_central:{nB20_over_n0:1e-3,H_km:1.2},
   figure_read_off_stress_envelope:{nB20_over_n0:[0.5e-3,2e-3],H_km:[0.9,1.3]},
   mean_free_path:"lambda_nuN=25 cm*(n0/nB)*(100 MeV/E_nu)^2, from Raffelt, Janka & Fiorillo (2025), p. 5",
   tail_model:"nB(r)=nB(20 km)*exp[-(r-20 km)/H] for r>=20 km",
   note:"The figure ends at 20 km. The 20-25 km tail is extrapolated; low/central/high are figure-read-off stresses, not statistical confidence limits."
  },
  benchmark:{mV_MeV:MASS,vector_energy_band_MeV:[210,510],P1C_band_energy_nodes_MeV:nodes},
  formulas:{
   tau_nuN:"tau(E,r)=integral_r^infinity dr' [nB(r')/n0]/(25 cm)*(E/100 MeV)^2",
   daughter_energies:"E1,2=omega/2*(1 +/- beta z), beta=sqrt(1-mV^2/omega^2)",
   pair_escape:"P_pair^E=(1/omega)*sum_h (1/3)*integral dz W_h(z)[E1 exp(-tau(E1,r))+E2 exp(-tau(E2,r))]",
   polarization_weights:{L:"3/4(1-z^2)",plus:"3/8(1+z)^2",minus:"3/8(1-z)^2"}
  },
  transport_tau_2_3:{},
  pair_escape_at_radii:{},
  pair_escape_transition_radii:{},
  validation:{gauss_legendre_order:256,polarization_weight_integrals:modeNorms,polarization_sum_identity_max_abs:sumIdentityMaxAbs,all_values_finite:true},
  limitations:[
   "This estimates a radial neutrino-nucleon transport optical depth, not the heavy-flavor energy sphere. Transport and energy spheres are distinct.",
   "It assumes the same simple scattering opacity for neutrinos and antineutrinos and does not include degeneracy, correlations, recoil, weak magnetism, pair absorption/emission, or angular transport.",
   "The equal-polarization average is a kinematic reference; the actual production polarization density matrix is channel- and phase-space-dependent.",
   "The outer density tail is an exponential extrapolation from a figure that ends at 20 km.",
   "No full B.2 vector-ray integration is performed with this smooth pair escape model; it must not be substituted for the published Rmax=25 km baseline."
  ]
 };
 for(const [name,tail] of Object.entries(TAILS)){
  result.transport_tau_2_3[name]={};
  for(const E of NEUTRINO_ENERGIES)result.transport_tau_2_3[name][String(E)]=transportRadius(E,tail);
  result.pair_escape_at_radii[name]={};
  for(const r of RADII){
   const vals=nodes.map(omega=>pairEscape(omega,r,tail).equal_mode_average);
   result.pair_escape_at_radii[name][String(r)]={
    min_over_10_vector_nodes:Math.min(...vals),
    max_over_10_vector_nodes:Math.max(...vals),
    values_at_210_300_510:Object.fromEntries(REPRESENTATIVE_OMEGAS.map(w=>[String(w),pairEscape(w,r,tail)]))
   };
  }
  result.pair_escape_transition_radii[name]={};
  for(const omega of REPRESENTATIVE_OMEGAS){
   result.pair_escape_transition_radii[name][String(omega)]={
    r50_km:pairEscapeRadius(omega,tail,0.5),
    r90_km:pairEscapeRadius(omega,tail,0.9),
    r99_km:pairEscapeRadius(omega,tail,0.99)
   };
  }
 }
 fs.mkdirSync(path.dirname(outputPath),{recursive:true});
 fs.writeFileSync(outputPath,JSON.stringify(result,null,2)+"\n");
 console.log(JSON.stringify({output:outputPath,transport_tau_2_3:result.transport_tau_2_3,
  pair_escape_at_radii:Object.fromEntries(Object.entries(result.pair_escape_at_radii).map(([k,v])=>[k,Object.fromEntries(Object.entries(v).map(([r,x])=>[r,{min:x.min_over_10_vector_nodes,max:x.max_over_10_vector_nodes}]))])),
  pair_escape_transition_radii:result.pair_escape_transition_radii},null,2));
}
main();
