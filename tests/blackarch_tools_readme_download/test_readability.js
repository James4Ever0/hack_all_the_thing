var { Readability } = require('@mozilla/readability');
var { JSDOM } = require('jsdom');
// var doc = new JSDOM("<body>Look at this cat: <img src='./cat.jpg'></body>", {
//   url: "https://www.baidu.com" // fine now? you do not load shits from that url ?
// });
var doc = new JSDOM("<body>Look at this cat: <img src='./cat.jpg'></body>", {
    url: "https://www.baidu.com" // fine now? you do not load shits from that url ?
  });
let reader = new Readability(doc.window.document);
let article = reader.parse();
console.log("ARTICLE?")
console.log(article)