from javascript import require
# Readability = require("@mozilla/readability")
R = require("@mozilla/readability").Readability
# JSDOM = require("jsdom")
J = require("jsdom").JSDOM
## name collision?

# print(dir(JSDOM))
with open("fastgithub_readme.html", "r") as f:
    html = f.read()
    # url = "https://github.com/dotnetcore/FastGithub"
    # do not provide url. JSDOM won't load shit.
    print('loading JSDOM') # shit man. do not load shit!
    # taking forever? fuck!
    doc = J(html) # just because you cannot load this stuff. how about create some javascript library for this task. use module.export instead.
    print("STEP 2")
    reader = R(doc.window.document)
    print("STEP 3")
    article = reader.parse()
    print("ARTICLE?")
    import rich

    rich.print(article)
