# you may increase the span for whoosh to search, since this is not ai backed
from semantic_ai_search_base_conv_with_step_charbased import (
    listOfCleanedMergedConvGroupWithLineIndexMapping,
)

from lazero.utils.logger import sprint

# a single document, unparsed!
# you know there will be newline for this search engine.

# remember this shit is long!

# but what if we don't simply import 'data'? instead we do the search against our convoluted array?

from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh import index
import os, os.path
from whoosh import qparser
# from whoosh.highlight import HtmlFormatter

from whoosh import scoring

# question: how to tokenize chinese text?
# better search for 'whoosh 中文搜索' 'whoosh + jieba'
schema = Schema(
    title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True), lineRange=STORED()
)

indexDirectory = 'index_dir2'
# create empty index directory

if not os.path.exists(indexDirectory):
    os.mkdir(indexDirectory)

ix = index.create_in(indexDirectory, schema)
writer = ix.writer()

# for i in range(df):
# it will not be duplicated.
for elem in listOfCleanedMergedConvGroupWithLineIndexMapping:
    data = elem["conv_group_merged"]
    lineRange = elem["line_range"]
    writer.add_document(
        title="jq manual", content=data, lineRange=lineRange, path="jq_man.log"
    )
writer.commit()

# https://stackoverflow.com/questions/19477319/whoosh-accessing-search-page-result-items-throws-readerclosed-exception
# http://annamarbut.blogspot.com/2018/08/whoosh-pandas-and-redshift-implementing.html
# https://ai.intelligentonlinetools.com/ml/search-text-documents-whoosh/
def index_search(dirname, search_fields, search_query):
    ix = index.open_dir(dirname)
    schema = ix.schema

    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema, group=og)

    q = mp.parse(search_query)

    # what is this q?
    # sprint(q)
    # breakpoint()
    # (title:math OR content:math OR title:addition OR content:addition)
    # why you have case conversion? why the fuck?

    with ix.searcher(weighting=scoring.TF_IDF()) as s:
        results = s.search(q, terms=True, limit=5)  # what fucking terms?
        results.fragmenter.charlimit = 100000
        # how about let's set it as max char length among our document database?
        print("Search Results: ")
        # shall you replace the formatter.
        # formatter_join_token = str(uuid.uuid4())
        # results.formatter = ListFormatter
        # it is some kind of 'html formatter', so we use BeautifulSoup
        # results.formatter = HtmlFormatter(between=formatter_join_token)
        # this time we do not use the formatter?
        # i mean it will join the results with some magic UUID, so you may have chance of spliting it out.
        # but to get the position is not so easy.
        # you may want the context and the exact line number.
        # line number? use string slice and count('\n') please.
        # or we could directly use the highlighter without whoosh?
        for hitIndex, hit in enumerate(results): # we cannot override the imported 'index'
            score = hot.
            print('HIT:',hitIndex)
            # print(hit)
            # breakpoint()
            content = hit['content']
            # reversed stem highlight!
            sprint('content:',content)
            # sprint(dir(hit))
            # print(hit.matched_terms) # too long.
            # print(dir(hit.matched_terms)) # method?
            # (Pdb) hit.matched_terms()
            # [('content', b'addition'), ('content', b'math')]
            # breakpoint()
            # ['__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_fields', 'clear', 'docnum', 'fields', 'get', 'highlights', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'matched_terms', 'more_like_this', 'pos', 'rank', 'reader', 'results', 'score', 'searcher', 'update', 'values']
            # fragments = hit.fragments('content')
            # print(fragments)
            # sprint(highlights)
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

# query = "apply recursive every"
query = "github" # find the damn link!
# query = "apply every recursive"  # seems not so good.
# query = "math addition"
# must not with reader closed.
# results_dict = index_search(indexDirectory, ['title','content'], query)
index_search(indexDirectory, ["title", "content"], query)
# breakpoint()
# for hit in results_dict:
#     print(hit.highlights('content'))
# it is a single document, with no hits!
