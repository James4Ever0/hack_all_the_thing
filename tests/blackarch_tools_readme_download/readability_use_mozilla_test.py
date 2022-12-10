from javascript import require

Readability = require("@mozilla/readability").Readability
JSDOM = require("jsdom").JSDOM
with open("fastgithub_readme.html", "r") as f:
    html = f.read()
    url = "https://github.com/dotnetcore/FastGithub"
    doc = JSDOM(html, {"url": url})
    reader = Readability(doc.window.document)
    article = reader.parse()
    print("ARTICLE?")
    import rich

    rich.print(article)
