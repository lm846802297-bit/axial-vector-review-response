"""Audit saved scan evidence and summarize actual numerical differences."""
import hashlib
import json
from pathlib import Path
import numpy as np
from run_scan import find_intervals

OUT = Path(__file__).resolve().parent / 'outputs'

def read(name):
    return json.loads((OUT / (name + '.json')).read_text(encoding='utf-8'))

def by_mass(data):
    return {r['mass_MeV']: r for r in data['results']}

def differences(base, alternate):
    rows = []
    for mass in sorted(base.keys() & alternate.keys()):
        a = base[mass]['intervals_4p4e52']
        b = alternate[mass]['intervals_4p4e52']
        if len(a) == len(b) == 1:
            rows.append(dict(mass_MeV=mass, lower_relative=b[0][0]/a[0][0]-1,
                             upper_relative=b[0][1]/a[0][1]-1))
    return rows

def main():
    scans = {n: read(n) for n in ['axial', 'vector', 'endpoint', 'convergence',
        'refined_fast', 'cutoff', 'sensitivity_half', 'sensitivity_double',
        'sensitivity_radius20', 'sensitivity_numu0', 'coupling_refinement']}
    base = by_mass(scans['axial']) | by_mass(scans['endpoint'])
    for name, scan in scans.items():
        gs = np.asarray(scan['couplings'])
        assert np.all(np.diff(gs) > 0)
        for row in scan['results']:
            lum = np.asarray(row['luminosity_erg_s'])
            assert len(lum) == len(gs) and np.all(np.isfinite(lum)) and np.all(lum >= 0)
            assert abs(sum(row['thin_fractions'].values())-1) < 1e-12
            for key, threshold in [('intervals_4p4e52', 4.4e52), ('intervals_3e52', 3e52)]:
                assert find_intervals(gs, lum, threshold) == row[key], (name, row['mass_MeV'])
    comparisons = {n: differences(base, by_mass(d)) for n, d in scans.items()
                   if n not in ['axial', 'vector', 'endpoint']}
    report = dict(
        baseline_config=scans['axial']['config'], baseline_mass_count=len(scans['axial']['results']),
        plotted_axial_mass_count=len(base), coupling_count=len(scans['axial']['couplings']),
        comparisons=comparisons,
        muon_spin_degeneracy_factor=2,
        endpoint_intervals={str(m):base[m]['intervals_4p4e52'] for m in [250.,255.,260.,265.,270.]},
        largest_surface_blackbody_erg_s=max(r['surface_blackbody_erg_s'] for r in base.values()),
        low_mass_3e52_g_per_mass_MeV=base[.01]['intervals_3e52'][0][0]/.01,
        representative_results={str(m):{k:v for k,v in base[m].items() if k!='luminosity_erg_s'}
                                for m in [.01,1.,10.,100.,200.,250.,255.]},
        scan_sha256={n:hashlib.sha256((OUT/(n+'.json')).read_bytes()).hexdigest() for n in scans},
    )
    (OUT/'numerical_validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['baseline_mass_count','plotted_axial_mass_count',
        'coupling_count','optimized_column_luminosity_relative_difference_above_1e40',
        'largest_surface_blackbody_erg_s','low_mass_3e52_g_per_mass_MeV']},indent=2))
    for n, rows in comparisons.items():
        print(n,'max absolute boundary relative changes',
              [max(abs(row[k]) for row in rows) for k in ['lower_relative','upper_relative']])

if __name__=='__main__': main()
