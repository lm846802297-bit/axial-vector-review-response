"""Extract contour polylines from pinned arXiv source figures.

Usage: python extract_vector_reference.py --source-root /path/to/sources
Required files are named in SOURCES below. No source PDF is redistributed.
The output is figure-digitized data, not original author numerical tables.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import fitz

HERE=Path(__file__).resolve().parent
SOURCES={
    'blinov':('blinov/combined_sn_bounds_hot_and_cold_with_mfp_cont.pdf',
              'https://arxiv.org/src/2511.09619v2'),
    'wang':('wang/Figures/mumtau_compare.pdf',
            'https://arxiv.org/src/2610.35379v1'),
}
EXPECTED_SHA256={
    'blinov':'98c87197308e230bd90521292d97d90bbf6a201202fa9a9a07f1e8f0d3330282',
    'wang':'47aadd4a8c728f0ccae2629c4d7ec5ce54837f959a73e24e04fef57ced326ea7',
}


def polyline(drawing):
    points=[]
    for item in drawing['items']:
        if item[0]!='l':
            raise ValueError('Expected line segments, not fitted Bezier curves')
        if not points:points.append(tuple(item[1]))
        if not np.allclose(points[-1],item[1],atol=1e-4):
            raise ValueError('Discontinuous source path')
        points.append(tuple(item[2]))
    return np.asarray(points)


def crossings(vertices,mass):
    """Intersect a closed log-space contour with a fixed mass, no extrapolation."""
    x,y=np.log10(vertices).T
    target=np.log10(mass)
    result=[]
    for j in range(len(x)-1):
        if min(x[j:j+2])<=target<=max(x[j:j+2]) and x[j]!=x[j+1]:
            result.append(10**(y[j]+(target-x[j])*(y[j+1]-y[j])/(x[j+1]-x[j])))
    unique=[]
    for value in sorted(result):
        if not unique or not np.isclose(value,unique[-1],rtol=1e-9,atol=0):
            unique.append(value)
    return unique


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,required=True)
    args=ap.parse_args()
    out=HERE/'data'/'vector_reference';out.mkdir(exist_ok=True)
    record={'kind':'Digitized public PDF paths; not author numerical tables','sources':{}}
    for name,(rel,url) in SOURCES.items():
        path=args.source_root/rel
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        if digest!=EXPECTED_SHA256[name]:
            raise ValueError(f'Source figure changed: {name}: {digest}')
        page=fitz.open(path)[0];drawings=page.get_drawings()
        if name=='blinov':
            index=78  # inner solid black contour = cold s18.8-SFHo, Fig. 4
            d=drawings[index]
            assert d['color']==(0.,0.,0.) and len(d['items'])==69
            xy=polyline(d)
            xmin,xmax=60.08762741088867,450.6876220703125
            ymin,ymax=21.502197265625,270.982177734375
            mass=10**(3*(xy[:,0]-xmin)/(xmax-xmin))  # MeV: 1 to 1000
            coupling=10**(-6-5*(xy[:,1]-ymin)/(ymax-ymin))
            threshold=4.4e52
        else:
            index=2  # pink filled SN1987A region, NOT purple LESN
            d=drawings[index]
            assert d['fill']==(1.,0.,0.) and len(d['items'])==135
            xy=polyline(d)
            xmin,x10=61.922000885009766,191.0229949951172
            y5,y6=10.800999641418457,46.399749755859375
            mass=10**((xy[:,0]-xmin)/(x10-xmin))
            coupling=10**(-5-(xy[:,1]-y5)/(y6-y5))
            threshold=3e52
        vertices=np.column_stack([mass,coupling])
        # Explicitly close only the filled polygon; Blinov's low-mass edges
        # are both at 1 MeV and no closure is needed for intersections.
        if name=='wang' and not np.allclose(xy[0],xy[-1]):
            vertices=np.vstack([vertices,vertices[0]])
        np.savetxt(out/f'{name}_cooling_vertices.csv',vertices,delimiter=',',
                   header='mass_MeV,coupling',comments='',fmt='%.12g')
        record['sources'][name]={'url':url,'archive_member':rel.split('/',1)[1],
            'pdf_sha256':digest,'drawing_index':index,
            'figure':4 if name=='blinov' else 12,'threshold_erg_s':threshold,
            'maximum_mass_vertex_MeV':float(mass.max()),
            'points':{str(m):crossings(vertices,m) for m in [1,10,100,200]},
            'uncertainty':'Path vertex extraction is exact up to PDF rounding; the published contour is coarse and its underlying interpolation/systematics are unknown.'}
    (out/'provenance.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
