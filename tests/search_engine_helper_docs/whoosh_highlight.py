from load_demo_data import data

# a single document, unparsed!

# remember this shit is long!

from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import os, os.path
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True))

# create empty index directory

if not os.path.exists("index_dir"):
    os.mkdir("index_dir")

ix = index.create_in("index_dir", schema)
writer = ix.writer()

# for i in range(df):
writer.add_document(title="jq manual", content=data,path="jq_man.log")
writer.commit()

# https://stackoverflow.com/questions/19477319/whoosh-accessing-search-page-result-items-throws-readerclosed-exception
# http://annamarbut.blogspot.com/2018/08/whoosh-pandas-and-redshift-implementing.html
# https://ai.intelligentonlinetools.com/ml/search-text-documents-whoosh/
def index_search(dirname, search_fields, search_query):
    ix = index.open_dir(dirname)
    schema = ix.schema
    
    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema, group = og)

    
    q = mp.parse(search_query)
    
    
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 10)
        print("Search Results: ")
        
        
        print(results[0:10])

results_dict = index_search("index_dir", ['title','content'], u"northern minnesota"