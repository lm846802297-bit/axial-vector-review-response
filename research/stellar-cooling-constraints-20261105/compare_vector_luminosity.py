"""Digitize all six Blinov Fig. 7 curves and compare the luminosity curves.

The source figure is from arXiv:2511.09619v2, luminosity_snapshot_t=1.pdf.
Use --source path/to/that.pdf. Only derived numerical vertices are saved.
The source PDF hash, drawing indices, path colours and item counts are pinned.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import fitz
from extract_vector_reference import polyline
from run_vector_audit import build,HERE
from transport import luminosities

HERE=Path(__file__).resolve().parent
EXPECTED_PDF_SHA256="4d7d1d10bfe2b52992af94df98749fa3adac887c009cbf98515fa12e6c48fdb5"
CURVES=[
    (1e-6,39,83,(0.12156862765550613,0.46666666865348816,0.7058823704719543)),
    (1e-5,40,83,(1.0,0.49803921580314636,0.054901961237192154)),
    (0.1,41,45,(0.1725490242242813,0.6274510025978088,0.1725490242242813)),
    (1.0,42,34,(0.8392156958580017,0.15294118225574493,0.1568627506494522)),
    (10.0,43,27,(0.5803921818733215,0.40392157435417175,0.7411764860153198)),
    (200.0,44,14,(0.5490196347236633,0.33725491166114807,0.29411765933036804)),
]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True)
    args=ap.parse_args()
    p=fitz.open(args.source)[0]
    out=HERE/'outputs'/'vector_audit';out.mkdir(parents=True,exist_ok=True)
    pdf_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest()
    if pdf_sha256!=EXPECTED_PDF_SHA256:
        raise ValueError(f'Pinned Fig. 7 source PDF changed: {pdf_sha256}')
    drawings=p.get_drawings()
    rows=[];points={}
    for mass,index,count,expected_color in CURVES:
        d=drawings[index]
        if len(d['items'])!=count:raise ValueError(f'Source PDF path changed for m={mass:g} MeV')
        if d['fill'] is not None or not np.allclose(d['color'],expected_color,rtol=0,atol=1e-8):
            raise ValueError(f'Source PDF path identity changed for m={mass:g} MeV')
        xy=polyline(d)
        alpha=10**(-22+16*(xy[:,0]-54.82951354980469)/(397.99951171875-54.82951354980469))
        g=np.sqrt(4*np.pi*alpha)
        light=10**(52+3*(195.54043579101562-xy[:,1])/(195.54043579101562-20.904434204101562))
        # Only vertices inside the visible frame, before any off-page tails.
        keep=(light>=1e52)&(light<=1e55)
        g,light=g[keep],light[keep]
        if len(g)<5:raise ValueError(f'Too few visible vertices for m={mass:g} MeV')
        points[str(mass)]={'g':g.tolist(),'luminosity_erg_s':light.tolist(),
                           'drawing_index':index,'drawing_color':list(d['color']),
                           'source_item_count':count}
        for variant in ['blinov_literal','blinov_average','thomson_modes','exact_recoil_scalar','exact_modes']:
            src,_,columns,angles=build(mass,HERE/'data'/'sfho188_digitized.csv',variant)
            actual=luminosities(src,columns,angles,g)
            for gg,ll,aa in zip(g,light,actual):
                rows.append({'mass_MeV':mass,'variant':variant,'g':gg,
                             'reference_erg_s':ll,'calculated_erg_s':aa,'relative_error':aa/ll-1})
    def paired_transport_effect(scalar_variant,mode_variant):
        scalar={(row['mass_MeV'],row['g']):row['calculated_erg_s']
                for row in rows if row['variant']==scalar_variant}
        mode={(row['mass_MeV'],row['g']):row['calculated_erg_s']
              for row in rows if row['variant']==mode_variant}
        result={}
        for mass in [1e-6,1e-5,0.1,1.,10.,200.]:
            ratios=[mode[(mass,g)]/scalar[(mass,g)]-1.0
                    for mm,g in scalar if mm==mass and (mm,g) in mode]
            result[str(mass)]={
                'mean_abs_luminosity_change':float(np.mean(np.abs(ratios))),
                'max_abs_luminosity_change':float(np.max(np.abs(ratios))),
            }
        return result

    data={'source_url':'https://arxiv.org/src/2511.09619v2',
          'archive_member':args.source.name,'pdf_sha256':pdf_sha256,
          'figure':'Blinov et al., JHEP 06 (2026) 155, Fig. 7; visually cross-checked against the version-of-record PDF',
          'reference_vertices':points,'comparison':rows,
          'controlled_transport_comparison':{
              'B14_scalar_sum_vs_polarization_average':paired_transport_effect('blinov_literal','blinov_average'),
              'B14_scalar_sum_vs_mode_resolved':paired_transport_effect('blinov_literal','thomson_modes'),
              'B14_polarization_average_vs_mode_resolved':paired_transport_effect('blinov_average','thomson_modes'),
              'fixed_target_exact_recoil_scalar_vs_mode_resolved':paired_transport_effect('exact_recoil_scalar','exact_modes'),
          }}
    (out/'luminosity_comparison.json').write_text(json.dumps(data,indent=2)+'\n')
    summary={}
    for mass in [1e-6,1e-5,0.1,1.,10.,200.]:
        summary[str(mass)]={}
        for variant in ['blinov_literal','blinov_average','thomson_modes','exact_recoil_scalar','exact_modes']:
            errors=[abs(row['relative_error']) for row in rows
                    if row['mass_MeV']==mass and row['variant']==variant]
            summary[str(mass)][variant]={
                'mean_abs_relative_error':float(np.mean(errors)),
                'max_abs_relative_error':float(np.max(errors)),
            }
    print({
        'literature_residuals':summary,
        'controlled_transport_comparison':data['controlled_transport_comparison'],
    })

if __name__=='__main__':main()
