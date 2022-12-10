var { Readability } = require('@mozilla/readability');
// var { JSDOM } = require('jsdom');
var J = require('jsdom');
let JSDOM = J.JSDOM // working.
// let JSDOM = J
// var doc = new JSDOM("<body>Look at this cat: <img src='./cat.jpg'></body>", {
//   url: "https://www.baidu.com" // fine now? you do not load shits from that url ?
// });
const fs = require("fs");
mpath = "fastgithub_readme"
var content = fs.readFileSync(mpath, {encoding: "utf8"})
var doc = new JSDOM(content);
let reader = new Readability(doc.window.document);
let article = reader.parse();
console.log("ARTICLE?")
console.log(article)