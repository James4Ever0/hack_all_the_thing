from load_demo_data import data
from lazero.utils.logger import sprint

query = "math addition"

# we need exact location of the thing! scroll to it and display it!
from whoosh.highlight import highlight

text =data
terms = set(query.split(" ")) # what is this terms?
# A sequence or set containing the query words to match, e.g. (“render”, “shader”).
formatter = 

from whoosh.highlight import BasicFragmentScorer, FIRST, ContextFragmenter, NullFormatter

class ListFormatter(NullFormatter):
    
from whoosh.analysis import StandardAnalyzer
charlimit = 1000000
analyzer = StandardAnalyzer
fragmenter = ContextFragmenter(charlimit = charlimit)
formatter = ListFormatter

excerpts = highlight(text, terms, analyzer, fragmenter, formatter, top=3,
                     scorer=BasicFragmentScorer, minscore=1, order=FIRST
                     )