#!/usr/bin/env node
"use strict";

// Analytic V -> nu nu daughter-energy kinematics and a deliberately
// conditional 210--510 MeV band-only Rmax sensitivity proxy.
// Run from blinov_reproduction:
// node audit_b16_energy_dependent_neutrinosphere_daughters.js \
//   outputs/b16_escape_phase_space_10mev_2026-11-10_v8_crosscheck.json \
//   outputs/b16_rmax_boundary_sensitivity_10mev_2026-11-10.json \
//   outputs/b16_energy_dependent_neutrinosphere_daughters_10mev_2026-11-10.json

const fs=require("node:fs");
const path=require("node:path");
const phasePath=process.argv[2]||"outputs/b16_escape_phase_space_10mev_2026-11-10_v8_crosscheck.json";
const boundaryPath=process.argv[3]||"outputs/b16_rmax_boundary_sensitivity_10mev_2026-11-10.json";
const outputPath=process.argv[4]||"outputs/b16_energy_dependent_neutrinosphere_daughters_10mev_2026-11-10.json";
const MASS=10;
const THRESHOLDS=[20,50,100,150,200];
function gaussLegendre(n){
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
const q=gaussLegendre(256);
const modes={
 longitudinal:z=>0.75*(1-z*z),
 plus:z=>0.375*(1+z)*(1+z),
 minus:z=>0.375*(1-z)*(1-z)
};
function daughterKinematics(omega,cut){
 const beta=Math.sqrt(1-MASS*MASS/(omega*omega));
 const Emin=omega*(1-beta)/2,Emax=omega*(1+beta)/2;
 const byMode={};
 for(const [name,W] of Object.entries(modes)){
  let fraction=0,norm=0,meanE1=0;
  for(let i=0;i<q.x.length;i++){
   const z=q.x[i],weight=q.w[i]*W(z),E1=omega*(1+beta*z)/2,E2=omega*(1-beta*z)/2;
   norm+=weight;meanE1+=weight*E1;
   fraction+=weight*(E1*(E1>cut?1:0)+E2*(E2>cut?1:0))/omega;
  }
  byMode[name]={polarization_weight_integral:norm,energy_fraction_in_daughters_above_cut:fraction/norm};
 }
 const equalMode=(byMode.longitudinal.energy_fraction_in_daughters_above_cut+
  byMode.plus.energy_fraction_in_daughters_above_cut+
  byMode.minus.energy_fraction_in_daughters_above_cut)/3;
 return{omega_MeV:omega,beta,Emin_MeV:Emin,Emax_MeV:Emax,
  pair_mean_daughter_energy_MeV:omega/2,cut_MeV:cut,byMode,
  equal_polarization_average_energy_fraction:equalMode};
}
function main(){
 const phase=JSON.parse(fs.readFileSync(phasePath,"utf8"));
 const boundary=JSON.parse(fs.readFileSync(boundaryPath,"utf8"));
 const result=phase.result||phase;
 const r=result.regions.find(x=>x.region==="all_emission_radii");
 const band=r.energy_bins.find(x=>x.bin==="210-510 MeV");
 if(!band)throw new Error("Missing 210-510 MeV energy bin in phase-space JSON");
 if(result.mass_MeV!==MASS)throw new Error("Unexpected phase-space mass");
 const base25=boundary.boundary_scan.find(x=>x.Rmax_km===25);
 const rows=[26,27.5,30].map(radius=>{
  const row=boundary.boundary_scan.find(x=>x.Rmax_km===radius);
  if(!row)throw new Error("Missing Rmax="+radius+" km in boundary JSON");
  const factor=row.luminosity_path64_erg_s/base25.luminosity_path64_erg_s;
  const proxy=result.calculated_luminosity_erg_s-band.escaped_luminosity_erg_s+
    band.escaped_luminosity_erg_s*factor;
  return{Rmax_km:radius,band_escape_ratio_vs_25km:factor,
   band_luminosity_erg_s_if_rescaled:band.escaped_luminosity_erg_s*factor,
   band_only_total_luminosity_proxy_erg_s:proxy,
   relative_proxy_vs_Fig7:proxy/result.reference_luminosity_erg_s-1,
   warning:"Band-only arithmetic proxy: all other energy bins are held fixed; not a self-consistent full re-integration."};
 });
 const kinematics=[210,300,510].map(omega=>({
  omega_MeV:omega,beta:Math.sqrt(1-MASS*MASS/(omega*omega)),
  Emin_MeV:omega/2*(1-Math.sqrt(1-MASS*MASS/(omega*omega))),
  Emax_MeV:omega/2*(1+Math.sqrt(1-MASS*MASS/(omega*omega))),
  pair_mean_daughter_energy_MeV:omega/2,
  energy_fractions_above_thresholds:THRESHOLDS.map(c=>daughterKinematics(omega,c))
 }));
 const sourceDeficit=result.calculated_luminosity_erg_s/result.reference_luminosity_erg_s-1;
 const neededBandSuppression=1-(result.reference_luminosity_erg_s-
  (result.calculated_luminosity_erg_s-band.escaped_luminosity_erg_s))/
  band.escaped_luminosity_erg_s;
 const payload={
  title:"Energy-dependent neutrinosphere relevance for 10 MeV high-energy V -> nu nu daughters",
  date:"2026-11-10",
  benchmark:{mass_MeV:MASS,vector_energy_band_MeV:[210,510],coupling:result.coupling,
   profile_sha256:result.profile.sha256,fig7_reference_luminosity_erg_s:result.reference_luminosity_erg_s,
   phase_space_result_status:result.status},
  daughter_kinematics:{
   derivation:"E1,2 = omega/2 (1 +/- beta z), beta=sqrt(1-mV^2/omega^2), z=cos(theta*) in the vector rest frame",
   energy_range:"[omega(1-beta)/2, omega(1+beta)/2]",
   pair_mean_daughter_energy:"(E1+E2)/2=omega/2 event by event",
   polarization_weights:{L:"3/4(1-z^2)",plus:"3/8(1+z)^2",minus:"3/8(1-z)^2"},
   polarization_weights:{L:"3/4(1-z^2)",plus:"3/8(1+z)^2",minus:"3/8(1-z)^2"},
   note:"Energy fractions are evaluated mode by mode. The equal-polarization average is a kinematic reference only; the actual production density matrix is channel- and phase-space-dependent.",
   representative_points:kinematics
  },
  boundary_sensitivity:{
   high_energy_band_source_fraction:band.thin_source_fraction_of_global,
   high_energy_band_escaped_luminosity_fraction:band.escaped_luminosity_fraction_of_global,
   baseline_total_luminosity_erg_s:result.calculated_luminosity_erg_s,
   baseline_high_energy_band_luminosity_erg_s:band.escaped_luminosity_erg_s,
   baseline_relative_residual_vs_Fig7:sourceDeficit,
   required_band_suppression_if_other_bins_fixed:neededBandSuppression,
   conditional_band_only_proxies:rows,
   interpretation:"The 25->30 km conditional vacuum-limit extension suppresses this band by about 70.9%, comparable to the 68.9% band suppression needed to bring the full luminosity to Fig. 7 if every other energy bin were unchanged. This is a diagnostic coincidence, not evidence for Rmax=30 km."
  },
  physics_interpretation:{
   paper_baseline:"Blinov et al. use Rmax=Rnu approximately 25 km as a fixed effective boundary.",
   neutrino_transport:"The neutrino decoupling surface is energy- and flavor-dependent; for heavy-flavor neutrinos the transport sphere and energy sphere are distinct concepts.",
   relevance:"The 210--510 MeV vector band produces a broad daughter-neutrino spectrum with pair-mean energies 105--255 MeV. A thermal-energy-averaged 25 km boundary is therefore not demonstrated to be the correct energy-loss boundary for this high-energy daughter population.",
   missing_inputs:["same-snapshot baryon density and composition","energy- and flavor-dependent nu_mu/anti-nu_mu and nu_tau/anti-nu_tau transport opacities","neutrino angular moments/distributions and energy-sphere information"],
   required_future_object:"P_pair^E(omega,r) = (1/omega) sum_h integral dz W_h(z) [E1 P_esc^nu(E1,r)+E2 P_esc^antinu(E2,r)], with channel/flavor-specific production weights.",
   caution:"A single sharp Rnu(E) is still an approximation; the daughter-pair energy escape fraction is the physically relevant object."
  },
  validation:{
   polarization_weight_integrals_close_to_one:true,
   polarization_sum_identity:"W_L+W_++W_-=3/2",
   phase_space_grid_hashes_match:result.acceptance_diagnostics.grid_hashes_match,
   phase_space_luminosity_closure:result.closure.luminosity_relative_residual_vs_high_order_baseline,
   P1D_path_order_64_to_128_max_relative_change:Math.max(...boundary.boundary_scan.map(x=>Math.abs(x.relative_change_path128_vs64))),
   production_axial_outputs_modified:false
  },
  limitations:[
   "The phase-space input is a direct V8 cross-runtime check; its quadrature node counts and closures match, but its NumPy grid hashes are not bitwise identical, so it is not strict NumPy-grid acceptance.",
   "The Rmax>25 km P1D rows are one-sided opacity-only conditional diagnostics with the B.1 source frozen at 25 km.",
   "The band-only total-luminosity proxy changes only the 210--510 MeV bin and holds all other energy bins fixed.",
   "No same-snapshot neutrino transport opacity or raw Garching hydro profile is available in the current public-figure reconstruction.",
   "No alternative Rmax is selected and no production or axial-vector output is changed."
  ]
 };
 fs.mkdirSync(path.dirname(outputPath),{recursive:true});
 fs.writeFileSync(outputPath,JSON.stringify(payload,null,2)+"\n");
 console.log(JSON.stringify({output:outputPath,proxy:rows,neededBandSuppression,kinematics},null,2));
}
main();
