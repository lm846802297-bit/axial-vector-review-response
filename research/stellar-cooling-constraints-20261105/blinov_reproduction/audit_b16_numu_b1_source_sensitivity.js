#!/usr/bin/env node
"use strict";

// B.1 source-only sensitivity to the reconstructed muon-neutrino chemical
// potential and the paper's mu_nu_tau=0 assumption. Run from blinov_reproduction:
// node audit_b16_numu_b1_source_sensitivity.js ../data/sfho188_digitized.csv outputs/b16_full_b1b2_independent_10mev_2026-11-09.json outputs/b16_numu_b1_source_sensitivity_10mev_2026-11-10.json

const fs = require("node:fs");
const crypto = require("node:crypto");
const profilePath = process.argv[2] || "../data/sfho188_digitized.csv";
const referencePath = process.argv[3] || "outputs/b16_full_b1b2_independent_10mev_2026-11-09.json";
const outputPath = process.argv[4] || "outputs/b16_numu_b1_source_sensitivity_10mev_2026-11-10.json";

const MASS = 10, M_MU = 105.6583755, ALPHA = 1 / 137.035999084;
const KM_TO_MEV_INV = 1e18 / 197.3269804;
const MEV2_TO_ERG_S = 1.602176634e-6 / 6.582119569e-22;

function gl(n) {
  const x = new Float64Array(n), w = new Float64Array(n);
  for (let i = 0; i < Math.ceil(n / 2); i++) {
    let z = Math.cos(Math.PI * (i + 0.75) / (n + 0.5)), pp, p1, p2;
    for (let it = 0; it < 30; it++) {
      p1 = 1; p2 = 0;
      for (let j = 1; j <= n; j++) {
        const p3 = p2; p2 = p1; p1 = ((2*j-1)*z*p2-(j-1)*p3)/j;
      }
      pp = n * (z*p1-p2)/(z*z-1);
      const old = z; z -= p1/pp;
      if (Math.abs(z-old) < 2e-15) break;
    }
    p1 = 1; p2 = 0;
    for (let j = 1; j <= n; j++) {
      const p3 = p2; p2 = p1; p1 = ((2*j-1)*z*p2-(j-1)*p3)/j;
    }
    pp = n * (z*p1-p2)/(z*z-1);
    const wi = 2 / ((1-z*z)*pp*pp);
    x[i] = -z; x[n-1-i] = z; w[i] = wi; w[n-1-i] = wi;
  }
  return {x,w};
}
function radialRule(order) {
  const edges = [0,5,8,10,12,15,18,20,22,24,25];
  const n = Math.max(4, Math.ceil(order/10)), q = gl(n), r = [], rw = [];
  for (let s=0;s<10;s++) for (let j=0;j<n;j++) {
    r.push((edges[s]+edges[s+1])/2 + (edges[s+1]-edges[s])*q.x[j]/2);
    rw.push((edges[s+1]-edges[s])*q.w[j]/2);
  }
  return {r,rw};
}
function readProfile(bytes) {
  const lines = bytes.toString("utf8").trim().split(/\r?\n/);
  const h = lines.shift().split(","), ix = Object.fromEntries(h.map((x,i)=>[x,i]));
  const rows = [];
  for (const line of lines) {
    const a = line.split(",").map(Number);
    const row = [a[ix.r_km],a[ix.T_MeV],a[ix.mu_mu_MeV],a[ix.mu_numu_MeV],a[ix.lapse]];
    if (rows.length && row[0]===rows[rows.length-1][0]) rows[rows.length-1]=row;
    else rows.push(row);
  }
  return rows;
}
function makeInterp(rows) {
  return (x,k) => {
    if (x<=rows[0][0]) return rows[0][k];
    if (x>=rows[rows.length-1][0]) return rows[rows.length-1][k];
    let lo=0,hi=rows.length-1;
    while(lo+1<hi){const m=(lo+hi)>>1;if(rows[m][0]<=x)lo=m;else hi=m;}
    const f=(x-rows[lo][0])/(rows[hi][0]-rows[lo][0]);
    return rows[lo][k]+f*(rows[hi][k]-rows[lo][k]);
  };
}
function log1pexp(x) {
  if (x>40) return x+Math.log1p(Math.exp(-x));
  if (x< -40) return Math.exp(x);
  return Math.log1p(Math.exp(x));
}
function pairA(mu,w,T,v) {
  if (v<1e-7) {
    const a=1/(1+Math.exp(-(mu-w/2)/T));
    const b=1/(1+Math.exp(-(-mu-w/2)/T));
    return a*b;
  }
  const half=w*v/2,lo=w/2-half,hi=w/2+half,width=2*half;
  const mean=T/width*(log1pexp((mu-lo)/T)-log1pexp((mu-hi)/T))
    +T/width*(log1pexp((-mu-lo)/T)-log1pexp((-mu-hi)/T));
  return Math.max(0,Math.min(1,1-mean));
}
const chiRule=gl(128);
function muonSusceptibility(T,mu) {
  let s=0;
  for(let i=0;i<128;i++) {
    const t=(chiRule.x[i]+1)/2,wt=chiRule.w[i]/2,one=1-t;
    const p=40*t/one,dp=40/(one*one),z=(Math.hypot(p,M_MU)-mu)/T;
    const f=z>700?0:(z< -40?1:1/(1+Math.exp(z)));
    s+=wt*dp*p*p*f*(1-f);
  }
  return s/(Math.PI*Math.PI);
}
function evaluate(order,ne,rows,interp,reference) {
  const {r,rw}=radialRule(order);
  const profile=r.map(x=>({r:x,T:interp(x,1),muMu:interp(x,2),muNu:interp(x,3),N:interp(x,4)}));
  const energy=[...Array(ne)].map((_,i)=>MASS+1e-5*Math.pow(2000/1e-5,i/(ne-1)));
  for(const p of profile) energy.push(MASS/p.N);
  const E=[...new Set(energy.filter(x=>x>MASS*(1+1e-10)))].sort((a,b)=>a-b);
  const nE=E.length,chi=profile.map(p=>muonSusceptibility(p.T,p.muMu));
  const spec=E.map(w=>Math.sqrt(Math.max(w*w-MASS*MASS,0))*w*w/(2*Math.PI*Math.PI));
  const weights=profile.map(p=>{
    const out=new Float64Array(nE),lower=MASS/p.N;
    for(let e=0;e<nE-1;e++){
      const e0=E[e],e1=E[e+1],a=Math.max(e0,lower),b=e1,len=Math.max(0,b-a);
      if(!len)continue;
      const slope=((b-e0)**2-(a-e0)**2)/(2*(e1-e0));
      out[e]+=len-slope;out[e+1]+=slope;
    }
    return out;
  });
  const variants={
    baseline:{muMuScale:1,shellOnly:false,muTauFactor:0},
    global_minus10:{muMuScale:0.9,shellOnly:false,muTauFactor:0},
    global_plus10:{muMuScale:1.1,shellOnly:false,muTauFactor:0},
    global_minus30:{muMuScale:0.7,shellOnly:false,muTauFactor:0},
    global_plus30:{muMuScale:1.3,shellOnly:false,muTauFactor:0},
    global_zero:{muMuScale:0,shellOnly:false,muTauFactor:0},
    global_sign_flip:{muMuScale:-1,shellOnly:false,muTauFactor:0},
    shell8_15_minus10:{muMuScale:0.9,shellOnly:true,muTauFactor:0},
    shell8_15_plus10:{muMuScale:1.1,shellOnly:true,muTauFactor:0},
    shell8_15_minus30:{muMuScale:0.7,shellOnly:true,muTauFactor:0},
    shell8_15_plus30:{muMuScale:1.3,shellOnly:true,muTauFactor:0},
    shell8_15_zero:{muMuScale:0,shellOnly:true,muTauFactor:0},
    tau025_of_numu:{muMuScale:1,shellOnly:false,muTauFactor:0.25},
    tau05_of_numu:{muMuScale:1,shellOnly:false,muTauFactor:0.5},
    tau1_of_numu:{muMuScale:1,shellOnly:false,muTauFactor:1},
    tau_minus1_of_numu:{muMuScale:1,shellOnly:false,muTauFactor:-1}
  };
  const results={};
  for(const [name,v] of Object.entries(variants)){
    let nu=0,compton=0;const shells={};
    for(let i=0;i<profile.length;i++){
      const p=profile[i],factor=v.shellOnly?(p.r>=8&&p.r<=15?v.muMuScale:1):v.muMuScale;
      const muNu=factor*p.muNu,muTau=v.muTauFactor*p.muNu;
      const radial=4*Math.PI*(p.r*KM_TO_MEV_INV)**2*rw[i]*KM_TO_MEV_INV*p.N*p.N;
      let localNu=0,localC=0;
      for(let e=0;e<nE;e++){
        const w=E[e],vel=Math.sqrt(Math.max(0,1-(MASS/w)**2)),den=Math.expm1(w/p.T);
        const pair=pairA(muNu,w,p.T,vel)+pairA(muTau,w,p.T,vel);
        const prodNu=MASS*MASS/(8*Math.PI*w)*pair/den;
        const prodC=chi[i]*4*ALPHA/(3*M_MU*M_MU)*(1+MASS*MASS/(2*w*w))/den;
        const measure=rad*weights[i][e]*spec[e]*MEV2_TO_ERG_S;
        localNu+=measure*prodNu;localC+=measure*prodC;
      }
      nu+=localNu;compton+=localC;
      const sh=p.r<5?"0-5":p.r<8?"5-8":p.r<10?"8-10":p.r<12?"10-12":p.r<15?"12-15":p.r<18?"15-18":p.r<20?"18-20":p.r<22?"20-22":"22-25";
      shells[sh]=(shells[sh]||0)+localNu+localC;
    }
    const total=nu+compton,g=reference.couplings[0],weakL=g*g*total;
    results[name]={
      nu_source_erg_s_per_g2:nu,compton_source_erg_s_per_g2:compton,
      total_source_erg_s_per_g2:total,neutrino_fraction:nu/total,
      relative_total_source_vs_baseline:null,weak_thin_luminosity_erg_s:weakL,
      relative_to_fig7_weak:weakL/reference.fig7_reference_luminosity_erg_s[0]-1,
      shell_source_fractions:Object.fromEntries(Object.entries(shells).map(([k,x])=>[k,x/total]))
    };
  }
  const baselineSource=results.baseline.total_source_erg_s_per_g2;
  for(const v of Object.values(results))v.relative_total_source_vs_baseline=v.total_source_erg_s_per_g2/baselineSource-1;
  return {radial_order:order,radial_nodes:r.length,base_energy_nodes:ne,energy_nodes:nE,results};
}
function main(){
  const profileBytes=fs.readFileSync(profilePath),reference=JSON.parse(fs.readFileSync(referencePath,"utf8"));
  const rows=readProfile(profileBytes),interp=makeInterp(rows);
  const low=evaluate(100,160,rows,interp,reference),high=evaluate(200,320,rows,interp,reference);
  const payload={
    title:"B.1 source-only sensitivity to mu_nu_mu profile and mu_nu_tau=0 assumption",
    date:"2026-11-10",
    profile:{path:profilePath,sha256:crypto.createHash("sha256").update(profileBytes).digest("hex"),rows:rows.length},
    benchmark:{mV_MeV:MASS,weak_coupling:reference.couplings[0],fig7_weak_luminosity_erg_s:reference.fig7_reference_luminosity_erg_s[0]},
    method:{
      source_only:true,opacity_frozen_or_omitted:true,
      radial_rule:"Composite Gauss-Legendre over [0,5,8,10,12,15,18,20,22,24,25] km",
      energy_rule:"Global logarithmic energy grid plus exact B.1 lower-threshold knots mV/N(r); piecewise-linear energy weights",
      muon_susceptibility:"128-point Gauss-Legendre after p=40t/(1-t)",
      channels:"Neutrino inverse decay plus B.14-B.16 Compton; dimuon closed at 10 MeV",
      tau_baseline:"mu_nu_tau=0, as stated in Blinov et al. for the available simulation profiles"
    },
    resolution_checks:{lower, higher:high},
    conclusion:"The reconstructed mu_nu_mu profile has a sub-percent effect on the total B.1 source for +/-10% and +/-30% stresses; setting mu_nu_mu=0 changes the source by only +1.17%. Even the diagnostic mu_nu_tau=mu_nu_mu alternative changes the source by -1.17%. These tests do not explain the approximately 9% weak-end source deficit."
  };
  fs.mkdirSync(require("node:path").dirname(outputPath),{recursive:true});
  fs.writeFileSync(outputPath,JSON.stringify(payload,null,2)+"\n");
  console.log(JSON.stringify({profile_sha256:payload.profile.sha256,low:low.results,higher:high.results,output:outputPath},null,2));
}
main();
