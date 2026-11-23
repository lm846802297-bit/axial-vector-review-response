from pathlib import Path
import re,math,hashlib,json,collections
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'审稿意见-gpt'/'审稿意见分析v5.7-物理校核与专题连续阅读版.md'
src=next((ROOT/'审稿意见-gpt').glob('审稿意见分析v5.6*.md'))
s=p.read_text(encoding='utf-8');old=src.read_text(encoding='utf-8')
assert hashlib.sha256(src.read_bytes()).hexdigest()=='79c75142ea0ea180e4665f8713377eeb27cf33c3005041965af1dcab6e8d6e08'
ids=lambda t:re.findall(r'^### ((?:R-|M[1-4]-|m[1-6]-|REC-|ST-|SRC-)[^\s：:]+)',t,re.M)
assert ids(s)==ids(old) and len(ids(s))==59
def cids(t):
 t=t[t.index('## 附录 C：'):t.index('## 附录 D：')]
 return re.findall(r'^\|\s*\*\*([A-H]-\d+)\*\*',t,re.M)
assert cids(s)==cids(old) and len(cids(s))==38,(len(cids(s)),len(cids(old)))
heads=re.findall(r'^#{3,6} (\d+(?:\.\d+)+) ',s,re.M)
assert len(heads)==len(set(heads))
assert all(k in heads for k in re.findall(r'§(\d+(?:\.\d+)+)',s))
for ch in range(2,6):
 stages=re.findall(r'^### ('+str(ch)+r'\.[1-8]) ',s,re.M)
 assert stages==[f'{ch}.{i}' for i in range(1,9)],stages
assert not [(i,ord(c)) for i,c in enumerate(s) if ord(c)<32 and c not in '\n\r']
assert collections.Counter(re.findall(r'\\begin\{([^}]+)\}',s))==collections.Counter(re.findall(r'\\end\{([^}]+)\}',s))
assert s.count(r'\[')==s.count(r'\]')
assert s.count(r'\(')==s.count(r'\)')
anchors=re.findall(r'<a id="([^"]+)"></a>',s)
assert len(anchors)==len(set(anchors))
for link in re.findall(r'\]\(#([^)]+)\)',s):
 assert link in anchors,link
# Table widths allow optional trailing pipes and escaped pipes.
def cells(line):
 a=re.split(r'(?<!\\)\|',line.strip())
 if a[0]=='':a=a[1:]
 if a[-1]=='':a=a[:-1]
 return a
table_errors=[];tables=0
lines=s.splitlines()
for i,l in enumerate(lines):
 if re.match(r'^\s*\|?\s*:?-{3,}:?\s*\|',l):
  tables+=1;n=len(cells(l))
  j=i-1
  if len(cells(lines[j]))!=n:table_errors.append((j+1,len(cells(lines[j])),n))
  j=i+1
  while j<len(lines) and lines[j].lstrip().startswith('|'):
   if len(cells(lines[j]))!=n:table_errors.append((j+1,len(cells(lines[j])),n))
   j+=1
assert not table_errors,table_errors[:20]
# Independent analytic rotation and inverse reconstruction, with both signs and orderings.
worst=0;cases=0
for a in [10000,15625,20000]:
 for b in [9999.9,15625,20000.1]:
  for d in [-100,-1,0,1,100]:
   if a==b and d==0:continue
   al=.5*math.atan2(2*d,b-a)
   th=al if abs(al)<=math.pi/4 else al-math.copysign(math.pi/2,al)
   c=math.cos(th);sn=math.sin(th)
   x=a*c*c+b*sn*sn-2*d*sn*c;y=a*sn*sn+b*c*c+2*d*sn*c
   off=(a-b)*sn*c+d*(c*c-sn*sn)
   residues=[off,x*c*c+y*sn*sn-a,x*sn*sn+y*c*c-b,(y-x)*sn*c-d]
   worst=max(worst,max(abs(q) for q in residues));cases+=1
   assert max(abs(q) for q in residues)<1e-8
tau=1.77686
v1=math.sqrt(2)*tau/(.01*math.sqrt(4*math.pi));v2=math.sqrt(2)*tau/(.01*4*math.pi)
assert round(v1,1)==70.9 and round(v2,1)==20.0
# Omission is invisible to a BR sum computed from the same incomplete channel list.
full=[1.,2.,3.];partial=full[:2]
assert sum(x/sum(partial) for x in partial)==1 and sum(partial)!=sum(full)
result={'original_unchanged':True,'atomic_ids':59,'high_level_ids':38,'major_stages':32,
        'section_references_resolve':True,'tables_checked':tables,'control_chars':0,
        'math_environments_balanced':True,'rotation_cases':cases,'max_residual_GeV2':worst,
        'conditional_vS_GeV':[v1,v2],'chars':len(s),'lines':len(lines),'output_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(ROOT/'work/validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
