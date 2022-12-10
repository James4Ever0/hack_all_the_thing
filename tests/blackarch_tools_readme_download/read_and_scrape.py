import pandas

fpath = "tools.csv"

df = pandas.read_csv(fpath)

# print(df.head())

# visit "Website", set things under "Name", save other metadata along side.

# things may have the same website. are you sure you only want to scrape its first page? but maybe that's enough

# Version, Description, Category
# you should not iterate columns in this way.
# for col in df:
#    print(col)
#    print("___BREAK?___")

urlmap = {}
for index, row in df.iterrows():
    # jackpot?
    name = row["Name"]
    url = row["Website"]
    # and you want to avoid visiting the same website twice.
    urlmap.update({url: urlmap.get(url, []) + [name]})
#    print(row)
#    print("ROW?")

# now plan on urls.
for key, elem in urlmap.items():
    # now you must develop a tool for browsing both github pages (with your damn proxy) and other common pages, extracting HTML then send it to readbilityjs.
    # you want to be l33t then use elinks instead. i don't mind.
    print("KEY?", key) # this is the url
#    print("ELEM?", elem)
#    print("____"*3)
# you'd better use neo4j for this.