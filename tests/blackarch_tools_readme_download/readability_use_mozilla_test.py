from javascript import require
import javascript
javascript.

Readability = require("@mozilla/readability")
# Readability = require("@mozilla/readability").Readability
JSDOM = require("jsdom")
req
# JSDOM = require("jsdom").JSDOM

print(dir(JSDOM))
with open("fastgithub_readme.html", "r") as f:
    html = f.read()
    # url = "https://github.com/dotnetcore/FastGithub"
    # do not provide url. JSDOM won't load shit.
    print('loading JSDOM') # shit man. do not load shit!
    # taking forever? fuck!
    doc = JSDOM(html)
    print("STEP 2")
    reader = Readability(doc.window.document)
    print("STEP 3")
    article = reader.parse()
    print("ARTICLE?")
    import rich

    rich.print(article)
