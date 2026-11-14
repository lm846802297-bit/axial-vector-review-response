import concurrent.futures,subprocess,sys,re,hashlib,json
from pathlib import Path
base=Path('计算脚本/计算输出')
def run(n):
 p=base/f'section{n}_reproduce.py';log=base/f'section{n}_checks.txt'
 try:
  r=subprocess.run([sys.executable,str(p)],capture_output=True,text=True,encoding='utf-8',timeout=45)
  def norm(t):return re.sub(r'^Python:.*\n','',t.replace('\r\n','\n')).rstrip()+'\n'
  expected=log.read_text(encoding='utf-8-sig')
  return {'section':n,'exit':r.returncode,'stderr':r.stderr[-350:],'same_except_python_version':norm(r.stdout)==norm(expected),'result':next((l for l in r.stdout.splitlines() if l.startswith('RESULT:')),'MISSING'),'script_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'archive_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
 except Exception as e:return {'section':n,'error':repr(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:r=list(pool.map(run,list(range(250,260))+[261,262]))
p=base/'section260_reproduce.py'
a=subprocess.run([sys.executable,str(p)],capture_output=True,text=True,encoding='utf-8',timeout=45)
old=(base/'section260_checks.txt').read_text(encoding='utf-8-sig')
expected_prefix=old.split('RERUN 250',1)[0]
section260={'exit':a.returncode,'pass_lines_before_failure':sum(line.startswith('PASS ') for line in a.stdout.splitlines()),'prefix_matches_archived':a.stdout.rstrip()==expected_prefix.rstrip(),'error_last_line':a.stderr.strip().splitlines()[-1] if a.stderr.strip() else None,'script_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'archive_sha256':hashlib.sha256((base/'section260_checks.txt').read_bytes()).hexdigest()}
print(json.dumps({'python':sys.version.split()[0],'results':r,'section260':section260},ensure_ascii=False,indent=2))
