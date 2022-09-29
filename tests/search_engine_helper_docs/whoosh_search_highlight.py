from load_demo_data import data
from lazero.utils.logger import sprint

# a single document, unparsed!

# remember this shit is long!

from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import os, os.path
from whoosh import index
from whoosh import qparser

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True))

# create empty index directory

if not os.path.exists("index_dir"):
    os.mkdir("index_dir")

ix = index.create_in("index_dir", schema)
writer = ix.writer()

# for i in range(df):
# it will not be duplicated.
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

    # what is this q?
    # sprint(q)
    # breakpoint()
    # (title:math OR content:math OR title:addition OR content:addition)
    # why you have case conversion? why the fuck?

    
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 10) # what fucking terms?
        results.fragmenter.charlimit = 100000
        # how about let's set it as max char length among our document database?
        print("Search Results: ")
        # shall you replace the formatter.
        # results.formatter = ListFormatter
        # i mean it will join the results with some magic UUID, so you may have chance of spliting it out.
        # but to get the position is not so easy.
        # you may want the context and the exact line number.
        # line number? use please.
        # or we could directly use the highlighter without whoosh?
        for hit in results:
            # highlights = hit.highlights('content', top=5) # str. not list.
            highlights = hit.highlights('content', text=data)
            # sprint(dir(hit))
            # print(hit.matched_terms) # too long.
            # print(dir(hit.matched_terms)) # method?
            # (Pdb) hit.matched_terms()
            # [('content', b'addition'), ('content', b'math')]
            # breakpoint()
            # ['__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_fields', 'clear', 'docnum', 'fields', 'get', 'highlights', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'matched_terms', 'more_like_this', 'pos', 'rank', 'reader', 'results', 'score', 'searcher', 'update', 'values']
            # fragments = hit.fragments('content')
            # print(fragments)
            sprint(highlights)
            # it also contains the 'MATH' thing.
            # it is multi-sourced. separaed by three dots.
            # how it fucking works?
            # highlights = hit.highlights('content')
            # print(dir(highlights))
            # breakpoint()
            # may still not going to work.
            # no highlight?
            # 104797, which is 104k.
            # exceeds the freaking limit!
            # there is just one single hit. no other hits?
#             ters, like <b class="match term0">addition</b>, generally feed...and no result.

#    <b class="match term1">Addition</b>: +
    #    The operator + takes
    # what line?
        # print(results[0:10])
        # return results

query = "math addition"
# must not with reader closed.
# results_dict = index_search("index_dir", ['title','content'], query)
index_search("index_dir", ['title','content'], query)
# breakpoint()
# for hit in results_dict:
#     print(hit.highlights('content'))
# it is a single document, with no hits!