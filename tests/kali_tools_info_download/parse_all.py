# sort and get order.
import os

htmls = os.listdir(".")
htmls = [ x for x in htmls if x.endswith(".html")]
htmls.sort()
for fname in htmls:
    with open(fname,'r') as f:
        content = f.read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, features='lxml')
        # case by case. please.
        print("filename?", fname)
        if fname == "kali_official.html":
            ...
        elif fname == "kali_tools_all.html":
            ...
        elif fname == "pentest_tools_with_name.html":
            cname = "main-content"
            mc = soup.find("div",class_=cname)
            parts = mc.find_all("div", class_="mynav")
            for p in parts:
                # there are two things, one is the "h2" heading the other is the "ul" list
                print("____"*3)
                mhead = p.find("h2")
                print("heading?", mhead.text)
                mlist = p.find("ul")
                for elem in mlist.find_all("li"):
                    # check if there's link
                    a = elem.find('a')
                    if a is not None:
                        print("FOUND A:",a.text)
                        print("A LINK:",a.attr('href'))
                    else:
                        print("elem?", elem.text.strip())
