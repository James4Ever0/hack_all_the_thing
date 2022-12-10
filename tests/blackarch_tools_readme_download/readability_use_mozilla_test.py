from javascript import require

Readability= require('@mozilla/readability').Readability
JSDOM = require('jsdom').JSDOM
 doc =JSDOM(html, {
  url: url
});
let reader = new Readability(doc.window.document);
let article = reader.parse();