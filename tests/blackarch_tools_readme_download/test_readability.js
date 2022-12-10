var { Readability } = require('@mozilla/readability');
var { JSDOM } = require('jsdom');
var doc = new JSDOM("<body>Look at this cat: <img src='./cat.jpg'></body>", {
  url: "https://www.baidu.com" // fine now?
});
let reader = new Readability(doc.window.document);
let article = reader.parse();
console.log("ARTICLE?")