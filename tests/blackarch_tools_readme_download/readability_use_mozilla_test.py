from javascript import require
# fuck that.
read_html = require("./readability_html.js").read_html # must use .js extension. fuck.
# fucking working.
# what the fuck are you waiting for? just dump shit!
# Readability = require("@mozilla/readability")
# R = require("@mozilla/readability").Readability
# # JSDOM = require("jsdom")
# J = require("jsdom").JSDOM
# ## name collision?

# # print(dir(JSDOM))
if __name__ == "__main__":
    filepath = "fastgithub_readme.html"
    article = read_html(filepath)
    import rich
    rich.print(article)

# with open("fastgithub_readme.html", "r") as f:
#     html = f.read()
#     # url = "https://github.com/dotnetcore/FastGithub"
#     # do not provide url. JSDOM won't load shit.
#     print('loading JSDOM') # shit man. do not load shit!
#     # taking forever? fuck!
#     doc = J(html) # just because you cannot load this stuff. how about create some javascript library for this task. use module.export instead.
#     print("STEP 2")
#     reader = R(doc.window.document)
#     print("STEP 3")
#     article = reader.parse()
#     print("ARTICLE?")
#     import rich

#     rich.print(article)
