from javascript import require

Readabilityequire('@mozilla/readability').Readability
JSDOM = require('jsdom').JSDOM
var doc = new JSDOM(html, {
  url: url
});
let reader = new Readability(doc.window.document);
let article = reader.parse();