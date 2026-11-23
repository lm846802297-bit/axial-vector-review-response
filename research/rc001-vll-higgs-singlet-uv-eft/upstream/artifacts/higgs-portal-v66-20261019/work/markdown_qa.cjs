const fs = require('node:fs');
const path = require('node:path');

(async () => {
  // Install "marked" in the calling Node environment; no workstation-specific module path.
  const { marked } = await import('marked');
  const file = process.argv[2]
    ? path.resolve(process.argv[2])
    : path.join(__dirname, 'source-for-pandoc.md');
  if (!fs.existsSync(file)) {
    throw new Error(`Markdown source not found: ${file}`);
  }
  const source = fs.readFileSync(file, 'utf8');
  const tokens = marked.lexer(source, { gfm: true });
  let tables = 0;
  let headings = 0;
  const broken = [];
  marked.walkTokens(tokens, token => {
    if (token.type === 'heading') headings++;
    if (token.type === 'table') {
      tables++;
      token.rows.forEach((row, index) => {
        if (row.length !== token.header.length) broken.push([tables, index]);
      });
    }
  });
  if (broken.length) throw new Error(JSON.stringify(broken));
  console.log(JSON.stringify({
    source: file,
    markdown_tables: tables,
    headings,
    broken_tables: broken.length
  }));
})().catch(error => {
  console.error(error);
  process.exit(1);
});
