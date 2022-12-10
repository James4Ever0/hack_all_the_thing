from javascript import require

Readability= require('@mozilla/readability').Readability
JSDOM = require('jsdom').JSDOM
with open("fastgithub_readme.html",'r') as f:
    html = f.read()
    url = 'https://github.com/'
 doc =JSDOM(html, {
  url: url
});
let reader = new Readability(doc.window.document);
let article = reader.parse();