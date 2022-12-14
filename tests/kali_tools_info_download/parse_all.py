# sort and get order.
import os

htmls = os.listdir(".")
htmls = [x for x in htmls if x.endswith(".html")]
htmls.sort()
flag = 0  # so we can select. good!


def dict_list_write_to_csv(name,index =False):

            import pandas as pd

            df = pd.DataFrame(data=data)
            df.to_csv(name, index=index)

for fname in htmls:
    with open(fname, "r") as f:
        content = f.read()
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(content, features="lxml")
        # case by case. please.
        print("filename?", fname)
        if fname == "kali_official.html" and flag == 0:
            data = {"link":[],"name":[]}
            for div_card in soup.find_all("div", class_="card"):
                print("____" * 4)
                # print('card?',div_card)
                init = True
                for a in div_card.find_all("a"):
                    # print("elem A?", a)
                    link = a.attrs['href']
                    title = a.text.strip()
                    if title is "":
                        title = a.attrs.get('title',link.strip().replace("#","/").split("/")[-1].strip())
                    title = title.replace("$","").replace("\n","").strip()
                    print("TOOL:",title,"URL:",link)
                    data["link"].append(a_link:=link)
                    data["name"].append(a_text:=title)
                    if init: init=False
            data = 
        elif fname == "kali_tools_all.html" and flag == 1:
            ...
        elif fname == "pentest_tools_with_name.html" and flag == 2:
            data = {"heading": [], "name": [], "link": []}
            cname = "main-content"
            mc = soup.find("div", class_=cname)
            parts = mc.find_all("div", class_="mynav")
            for p in parts:
                # there are two things, one is the "h2" heading the other is the "ul" list
                # print("____"*3)
                mhead = p.find("h2").text.strip()
                # print("heading?", mhead)
                mlist = p.find("ul")
                for elem in mlist.find_all("li"):
                    # check if there's link
                    a = elem.find("a")
                    if a is not None:
                        a_text = a.text.strip()
                        a_link = a.attrs["href"]
                        # print("FOUND A:",a_text)
                        # print("A LINK:",a_link)
                    else:
                        a_text = elem.text.strip()
                        # print("elem?", a_text)
                        a_link = None  # might be NaN in this sense. check how to convert into pandas dataframe.
                    data["heading"].append(mhead)
                    data["link"].append(a_link)
                    data["name"].append(a_text)
            # now you turn the data into a pandas dataframe

