from load_demo_data import data
from lazero.utils.logger import sprint

query = "math addition"

# we need exact location of the thing! scroll to it and display it!
from whoosh.highlight import highlight

text =data
terms = query # what is this terms?

excerpts = highlight(text, terms, analyzer, fragmenter, formatter, top=3,
                     scorer=BasicFragmentScorer, minscore=1, order=FIRST)