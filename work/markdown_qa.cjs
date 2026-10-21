const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const mod='C:/Users/84680/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked';
 const {marked}=await import(pathToFileURL(require.resolve(mod)).href);
 const dir=path.join(process.cwd(),'审稿意见-gpt');
 const file=fs.readdirSync(dir).find(n=>n.startsWith('审稿意见分析v5.7'));
 const source=fs.readFileSync(path.join(dir,file),'utf8');
 const tokens=marked.lexer(source,{gfm:true});
 let tables=0,headings=0,broken=[];
 marked.walkTokens(tokens,t=>{
  if(t.type==='heading')headings++;
  if(t.type==='table'){
   tables++;
   t.rows.forEach((r,i)=>{if(r.length!==t.header.length)broken.push([tables,i]);});
  }
 });
 if(broken.length)throw Error(JSON.stringify(broken));
 console.log(JSON.stringify({markdown_tables:tables,headings,broken_tables:broken.length}));
})().catch(e=>{console.error(e);process.exit(1);});
