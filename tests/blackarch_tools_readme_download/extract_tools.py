table_id = "tbl-minimalist"
# shit you fucking name
# just select "table" then run
from bs4 import BeautifulSoup


# you need something creative. if you have tools installed, then you would use commandline help or man pages.
# if not installed, use shortcut to search with keyword and user input, or parse readme from github, or just extract description.

# you would not have issue parsing this tool list on modifier, but with problem on this damn chromebook. fuck

# there's some crazy ctfer called fmyy with blog: https://fmyy.pro
# in this repo the author prefers a tool called pwn. wtf is that? just a process inspector or else?

filename = "tools.html"
with open(filename,'r') as f:
    content = f.read()
    soup = BeautifulSoup(content, features='lxml')
    # why there's no fucking table? wtf?
    tool_table = soup.find_all("table",id=table_id)
    print("table count?", len(tool_table))
    # now you have one single such table, convert it into csv please!
    target_csv = "tools.csv"
    mytable = tool_table[0]
    #print(dir(mytable))
    #print("contents:")
    #print(mytable.contents)
    # they say i should use pandas.
    import pandas as pd
    # even though there's no damn pandas, i will write the damn code just in case.
    # you shall write this in kaggle. fuck.
    # damn computer sucks.
    # just pass this shit into pandas?
#    import tempfile
#    with tempfile.NamedTemporaryFile("w+",suffix=".html") as tf:
#        tf.write(mytable)
#        tf.seek(0)
#        tfname = tf.name
    mcur = mytable.find_all("td", class_="tbl-homepage")
#    breakpoint()
    for m in mcur:
        # get the damn a_href shit!
        val = m.find("a")
        # href?
        href = val['href']
#        print("href?", href)
        val.string = href # when you do hy repl, you should consider replace the current statement with that "modified" statement, instead of this previous statement, treat it like a real runtime fix.
    # you must preprocess the column to make it somehow visible.e
    mtable = mytable.prettify("utf-8")
    df = pd.read_html(mtable)[0]
    #df = pd.read_html(tfname)[0]
    print("head?")
    print(df)
    df.to_csv(target_csv, index=False)
    print('write completed!')
    print('location?', target_csv)

