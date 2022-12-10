var { Readability } = require('@mozilla/readability');
var { JSDOM } = require('jsdom');
const fs = require("fs");
// mpath = "fastgithub_readme.html"
module.exports = {
    read_html:(mpath) => {
    var content = fs.readFileSync(mpath, {encoding: "utf8"})
var doc = new JSDOM(content);
let reader = new Readability(doc.window.document);
let article = reader.parse()
}