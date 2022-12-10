from javascript import require

var { Readability } = require('@mozilla/readability');
JSDOM = require('jsdom').JSDOM
var doc = new JSDOM(html, {
  url: url
});
let reader = new Readability(doc.window.document);
let article = reader.parse();