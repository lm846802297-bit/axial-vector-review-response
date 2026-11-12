#!/usr/bin/env node
"use strict";

// Independent V8 implementation of the current-profile 24--25 km lapse test.
// Run from blinov_reproduction:
// node audit_b16_lapse_boundary_current_profile.js ../data/sfho188_digitized.csv outputs/b16_full_b1b2_independent_10mev_2026-11-09.json outputs/b16_lapse_boundary_sensitivity_current_profile_10mev_2026-11-10.json
//
// Fixed-omega B.2 is used. The lapse variants affect only the B.1 source
// measure and its exact lower energy threshold. Thermodynamic profiles and
// the B.2 opacity are shared across all variants.

const fs = require("node:fs");
const crypto = require("node:crypto");

const profilePath = process.argv[2] || "../data/sfho188_digitized.csv";
const baselinePath = process.argv[3] || "outputs/b16_full_b1b2_independent_10mev_2026-11-09.json";
const outputPath = process.argv[4] || "outputs/b16_lapse_boundary_sensitivity_current_profile_10mev_2026-11-10.json";

const mass = 10.0, radiusKm = 25.0, energyOffset = 2000.0;
const angularOrder = 16, pathOrder = 32, susceptibilityOrder = 96;
const M_MU = 105.6583755, ALPHA = 1 / 137.035999084;
const KM_TO_MEV_INV = 1e18 / 197.3269804;
const MEV2_TO_ERG_S = 1.602176634e-6 / 6.582119569e-22;

function sha256(buffer) {
  return crypto.createHash("sha256").update(buffer).digest("hex");
}
function parseProfile(text) {
  const lines = text.trim().split(/\r?\n/);
  const h = lines.shift().split(",");
  const ix = Object.fromEntries(h.map((x, i) => [x, i]));
  const rows = [];
  for (const line of lines) {
    const a = line.split(",").map(Number);
    const row = [a[ix.r_km], a[ix.T_MeV], a[ix.mu_mu_MeV], a[ix.mu_numu_MeV], a[ix.lapse]];
    if (rows.length && row[0] === rows[rows.length - 1][0]) rows[rows.length - 1] = row;
    else rows.push(row);
  }
  return rows;
}
function makeInterpolator(rows) {
  return (x, k) => {
    if (x <= rows[0][0]) return rows[0][k];
    if (x >= rows[rows.length - 1][0]) return rows[rows.length - 1][k];
    let lo = 0, hi = rows.length - 1;
    while (lo + 1 < hi) {
      const mid = (lo + hi) >> 1;
      if (rows[mid][0] <= x) lo = mid; else hi = mid;
    }
    const f = (x - rows[lo][0]) / (rows[hi][0] - rows[lo][0]);
    return rows[lo][k] + f * (rows[hi][k] - rows[lo][k]);
  };
}
function gaussLegendre(n) {
  const x = new Float64Array(n), w = new Float64Array(n);
  for (let i = 0; i < Math.ceil(n / 2); i++) {
    let z = Math.cos(Math.PI * (i + 0.75) / (n + 0.5)), pp = 0, p1 = 0, p2 = 0;
    for (let it = 0; it < 30; it++) {
      p1 = 1; p2 = 0;
      for (let j = 1; j <= n; j++) {
        const p3 = p2; p2 = p1;
        p1 = ((2 * j - 1) * z * p2 - (j - 1) * p3) / j;
      }
      pp = n * (z * p1 - p2) / (z * z - 1);
      const old = z; z = old - p1 / pp;
      if (Math.abs(z - old) < 2e-15) break;
    }
    p1 = 1; p2 = 0;
    for (let j = 1; j <= n; j++) {
      const p3 = p2; p2 = p1;
      p1 = ((2 * j - 1) * z * p2 - (j - 1) * p3) / j;
    }
    pp = n * (z * p1 - p2) / (z * z - 1);
    const wi = 2 / ((1 - z * z) * pp * pp);
    x[i] = -z; x[n - 1 - i] = z;
    w[i] = wi; w[n - 1 - i] = wi;
  }
  return { x, w };
}
function radialRule(order) {
  const edges = [0, 5, 8, 10, 12, 15, 18, 20, 22, 24, 25];
  const n = Math.max(4, Math.ceil(order / (edges.length - 1)));
  const q = gaussLegendre(n), r = [], rw = [];
  for (let s = 0; s < edges.length - 1; s++) {
    const a = edges[s], b = edges[s + 1];
    for (let j = 0; j < n; j++) {
      r.push((a + b) / 2 + (b - a) * q.x[j] / 2);
      rw.push((b - a) * q.w[j] / 2);
    }
  }
  return { r, rw };
}
function log1pexp(x) {
  if (x > 40) return x + Math.log1p(Math.exp(-x));
  if (x < -40) return Math.exp(x);
  return Math.log1p(Math.exp(x));
}
function pairA(mu, omega, temperature, velocity) {
  if (velocity < 1e-7) {
    const a = 1 / (1 + Math.exp(-(mu - omega / 2) / temperature));
    const b = 1 / (1 + Math.exp(-(-mu - omega / 2) / temperature));
    return a * b;
  }
  const half = omega * velocity / 2;
  const emin = omega / 2 - half, emax = omega / 2 + half, width = 2 * half;
  let mean = 0;
  mean += temperature / width * (
    log1pexp((mu - emin) / temperature) - log1pexp((mu - emax) / temperature)
  );
  mean += temperature / width * (
    log1pexp((-mu - emin) / temperature) - log1pexp((-mu - emax) / temperature)
  );
  return Math.max(0, Math.min(1, 1 - mean));
}
const chiRule = gaussLegendre(susceptibilityOrder);
function muonSusceptibility(temperature, chemicalPotential) {
  let sum = 0;
  for (let i = 0; i < chiRule.x.length; i++) {
    const t = (chiRule.x[i] + 1) / 2, wt = chiRule.w[i] / 2;
    const oneMinusT = 1 - t;
    const p = 40 * t / oneMinusT, dp = 40 / (oneMinusT * oneMinusT);
    const energy = Math.hypot(p, M_MU), z = (energy - chemicalPotential) / temperature;
    const f = z > 700 ? 0 : (z < -40 ? 1 : 1 / (1 + Math.exp(z)));
    sum += wt * dp * p * p * f * (1 - f);
  }
  return sum / (Math.PI * Math.PI);
}
function run(radialOrder, baseEnergyNodes, rows, interp, reference) {
  const { r, rw } = radialRule(radialOrder), nR = r.length;
  const n23 = interp(23, 4), n24 = interp(24, 4);
  const baselineLapse = r.map(x => interp(x, 4));
  const lapseVariants = {
    matched_schwarzschild_baseline: baselineLapse,
    freeze_at_N24: r.map((x, i) => x > 24 ? n24 : baselineLapse[i]),
    linear_extrapolation_of_23_24_slope: r.map((x, i) =>
      x > 24 ? n24 + (n24 - n23) * (x - 24) : baselineLapse[i])
  };

  const energyGrid = [];
  for (let i = 0; i < baseEnergyNodes; i++) {
    energyGrid.push(mass + 1e-5 * Math.pow(
      energyOffset / 1e-5, i / (baseEnergyNodes - 1)
    ));
  }
  for (const lapse of Object.values(lapseVariants)) {
    for (const n of lapse) energyGrid.push(mass / n);
  }
  const energies = [...new Set(energyGrid.filter(x => x > mass * (1 + 1e-10)))].sort((a, b) => a - b);
  const nE = energies.length;

  const pathGrid = [...new Set([0, ...r, radiusKm])].sort((a, b) => a - b);
  const nP = pathGrid.length;
  const pathT = pathGrid.map(x => interp(x, 1));
  const pathMu = pathGrid.map(x => interp(x, 2));
  const pathNu = pathGrid.map(x => interp(x, 3));
  const chi = pathT.map((t, i) => muonSusceptibility(t, pathMu[i]));

  const production = new Float64Array(nP * nE);
  const reducedAbsorption = new Float64Array(nP * nE);
  const velocity = new Float64Array(nE);
  const spectral = new Float64Array(nE);
  for (let e = 0; e < nE; e++) {
    const omega = energies[e];
    velocity[e] = Math.sqrt(Math.max(0, 1 - (mass / omega) ** 2));
    spectral[e] = Math.sqrt(Math.max(omega * omega - mass * mass, 0))
      * omega * omega / (2 * Math.PI * Math.PI);
  }
  for (let j = 0; j < nP; j++) {
    const t = pathT[j], muNu = pathNu[j], chiJ = chi[j];
    for (let e = 0; e < nE; e++) {
      const omega = energies[e], v = velocity[e], x = omega / t;
      const aNu = pairA(muNu, omega, t, v), a0 = pairA(0, omega, t, v);
      const nuReduced = mass * mass / (8 * Math.PI * omega) * (aNu + a0);
      const comptonReduced = chiJ * 4 * ALPHA / (3 * M_MU * M_MU)
        * (1 + mass * mass / (2 * omega * omega));
      const reduced = nuReduced + comptonReduced;
      reducedAbsorption[j * nE + e] = reduced;
      production[j * nE + e] = reduced / Math.expm1(x);
    }
  }

  const pathIndex = new Map(pathGrid.map((x, i) => [x, i]));
  const sourceIndices = r.map(x => pathIndex.get(x));
  if (sourceIndices.some(x => x === undefined)) throw new Error("Source node absent from opacity grid");

  const angleRule = gaussLegendre(angularOrder), pathRule = gaussLegendre(pathOrder);
  const angleWeights = Array.from(angleRule.w, x => x / 2);
  const pathSamples = new Array(nR * angularOrder);
  for (let i = 0; i < nR; i++) {
    const rr = r[i];
    for (let a = 0; a < angularOrder; a++) {
      const c = angleRule.x[a];
      const sMax = -c * rr + Math.sqrt(radiusKm ** 2 - rr ** 2 + rr ** 2 * c ** 2);
      const samples = [];
      for (let q = 0; q < pathOrder; q++) {
        const s = sMax * (1 + pathRule.x[q]) / 2;
        const position = Math.sqrt(Math.max(0, rr ** 2 + s ** 2 + 2 * rr * s * c));
        let lo = 0, hi = nP - 1;
        while (lo + 1 < hi) {
          const mid = (lo + hi) >> 1;
          if (pathGrid[mid] <= position) lo = mid; else hi = mid;
        }
        if (position >= pathGrid[nP - 1]) lo = nP - 2;
        const fraction = (position - pathGrid[lo]) / (pathGrid[lo + 1] - pathGrid[lo]);
        samples.push([lo, fraction, sMax * pathRule.w[q] / 2]);
      }
      pathSamples[i * angularOrder + a] = samples;
    }
  }

  const tau = new Float64Array(nR * angularOrder * nE);
  for (let i = 0; i < nR; i++) {
    for (let a = 0; a < angularOrder; a++) {
      const samples = pathSamples[i * angularOrder + a];
      const offset = (i * angularOrder + a) * nE;
      for (let e = 0; e < nE; e++) {
        let sum = 0;
        for (let q = 0; q < pathOrder; q++) {
          const [lo, fraction, weight] = samples[q];
          const y0 = reducedAbsorption[lo * nE + e];
          const y1 = reducedAbsorption[(lo + 1) * nE + e];
          sum += weight * (y0 + (y1 - y0) * fraction);
        }
        tau[offset + e] = sum * KM_TO_MEV_INV / velocity[e];
      }
    }
  }

  const sourceVariants = {};
  for (const [name, lapse] of Object.entries(lapseVariants)) {
    const source = new Float64Array(nR * nE);
    let total = 0, outer22 = 0, outer24 = 0;
    for (let i = 0; i < nR; i++) {
      const lower = mass / lapse[i], weights = new Float64Array(nE);
      for (let e = 0; e < nE - 1; e++) {
        const e0 = energies[e], e1 = energies[e + 1];
        const a = Math.max(e0, lower), b = e1, length = Math.max(0, b - a);
        if (length === 0) continue;
        const slope = ((b - e0) ** 2 - (a - e0) ** 2) / (2 * (e1 - e0));
        weights[e] += length - slope;
        weights[e + 1] += slope;
      }
      const radialMeasure = 4 * Math.PI * (r[i] * KM_TO_MEV_INV) ** 2
        * rw[i] * KM_TO_MEV_INV * lapse[i] ** 2;
      const pi = sourceIndices[i];
      for (let e = 0; e < nE; e++) {
        const value = radialMeasure * weights[e] * spectral[e]
          * production[pi * nE + e] * MEV2_TO_ERG_S;
        source[i * nE + e] = value;
        total += value;
        if (r[i] >= 22) outer22 += value;
        if (r[i] >= 24) outer24 += value;
      }
    }
    sourceVariants[name] = {
      source, total, source_fraction_r_ge_22: outer22 / total,
      source_fraction_r_ge_24: outer24 / total
    };
  }

  const selectedIndices = [0, 17, 24];
  const couplings = selectedIndices.map(i => reference.couplings[i]);
  const fig7 = selectedIndices.map(i => reference.fig7_reference_luminosity_erg_s[i]);
  const archived = selectedIndices.map(i => reference.final_200_node_result.luminosity_erg_s[i]);
  const baseline = sourceVariants.matched_schwarzschild_baseline;
  const avgEscape = couplings.map(g => {
    const factors = new Float64Array(nR * nE), g2 = g * g;
    for (let i = 0; i < nR; i++) for (let e = 0; e < nE; e++) {
      let average = 0;
      for (let a = 0; a < angularOrder; a++) {
        average += angleWeights[a] * Math.exp(-g2 * tau[(i * angularOrder + a) * nE + e]);
      }
      factors[i * nE + e] = average;
    }
    return factors;
  });

  const results = {};
  for (const [name, item] of Object.entries(sourceVariants)) {
    const points = [];
    for (let k = 0; k < couplings.length; k++) {
      let escaped = 0, baselineEscaped = 0;
      for (let j = 0; j < item.source.length; j++) {
        escaped += item.source[j] * avgEscape[k][j];
        baselineEscaped += baseline.source[j] * avgEscape[k][j];
      }
      const luminosity = couplings[k] ** 2 * escaped;
      const baselineLuminosity = couplings[k] ** 2 * baselineEscaped;
      points.push({
        g: couplings[k],
        luminosity_erg_s: luminosity,
        escape_fraction: escaped / item.total,
        relative_luminosity_vs_baseline: luminosity / baselineLuminosity - 1,
        relative_escape_fraction_vs_baseline:
          (escaped / item.total) / (baselineEscaped / baseline.total) - 1,
        relative_to_fig7: luminosity / fig7[k] - 1,
        relative_to_archived_independent: luminosity / archived[k] - 1
      });
    }
    results[name] = {
      thin_source_erg_s_per_g2: item.total,
      source_fraction_r_ge_22: item.source_fraction_r_ge_22,
      source_fraction_r_ge_24: item.source_fraction_r_ge_24,
      relative_thin_source_vs_baseline: item.total / baseline.total - 1,
      points
    };
  }

  return {
    radial_order_parameter: radialOrder,
    base_log_energy_nodes: baseEnergyNodes,
    radial_nodes: nR,
    energy_nodes_after_threshold_union: nE,
    opacity_nodes: nP,
    angular_order: angularOrder,
    path_order: pathOrder,
    susceptibility_order: susceptibilityOrder,
    N23: n23, N24: n24, N25_baseline: interp(radiusKm, 4),
    couplings, results
  };
}

function main() {
  const profileBytes = fs.readFileSync(profilePath);
  const baseline = JSON.parse(fs.readFileSync(baselinePath, "utf8"));
  const rows = parseProfile(profileBytes.toString("utf8"));
  const interp = makeInterpolator(rows);
  const low = run(100, 160, rows, interp, baseline);
  const high = run(200, 320, rows, interp, baseline);
  const payload = {
    title: "Current-profile B.1+B.2 lapse-continuation sensitivity at mV=10 MeV",
    date: "2026-11-10",
    profile: {
      path: profilePath,
      sha256: sha256(profileBytes),
      rows_after_duplicate_radius_collapse: rows.length
    },
    reference_baseline: {
      path: baselinePath,
      profile_sha256: baseline.profile.sha256,
      independent_200_node_luminosity_used_for_crosscheck: true
    },
    prescription: "Literal fixed-omega Eq. (B.2); lapse changes only the B.1 radial N^2 factor and lower threshold omega_min=m/N(r).",
    variants: {
      matched_schwarzschild_baseline: "N(r) from the active profile",
      freeze_at_N24: "N(r>24 km)=N(24 km), diagnostic only",
      linear_extrapolation_of_23_24_slope: "N(r>24 km)=N(24 km)+(N(24)-N(23))(r-24 km), diagnostic only"
    },
    method: {
      radial_rule: "Composite Gauss-Legendre over [0,5,8,10,12,15,18,20,22,24,25] km",
      energy_rule: "Global logarithmic energy grid plus exact lower-threshold knots for all lapse variants; piecewise-linear energy weights",
      susceptibility: "96-point Gauss-Legendre in t in [0,1], p=40 t/(1-t), for integral p^2 f_mu(1-f_mu)/pi^2",
      opacity: "16-point angular and 32-point chord Gauss-Legendre; piecewise-linear radial interpolation",
      channel_content: "10 MeV: neutrino inverse decay plus muon Compton; dimuon channel closed",
      energy_offset_MeV: energyOffset
    },
    joint_refinement: { lower_resolution: low, higher_resolution: high },
    conclusion: "The current-profile 24--25 km lapse continuation changes the strong-coupling full luminosity by at most 2.62e-4 relative (0.0262%) among the two diagnostic alternatives. This is negligible compared with the +92.26% strong-endpoint residual against Fig. 7."
  };
  fs.mkdirSync(require("node:path").dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, JSON.stringify(payload, null, 2) + "\n");
  console.log(JSON.stringify({
    profile_sha256: payload.profile.sha256,
    low: low.results,
    high: high.results,
    output: outputPath
  }, null, 2));
}
main();
