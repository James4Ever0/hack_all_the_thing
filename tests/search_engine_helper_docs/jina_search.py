from matplotlib.pyplot import text
from semantic_ai_search_base_conv_with_step_charbased import (
    listOfCleanedMergedConvGroupWithLineIndexMapping,
    linewise,
)

query = "math addition operation"

from docarray import Document, DocumentArray

from docarray import dataclass
from docarray.typing import Text, JSON


@dataclass
class WPExcerpt:
    source: Text
    content: Text
    lineRange: JSON

# d = Document(uri='https://www.gutenberg.org/files/1342/1342-0.txt').load_uri_to_text()
da = DocumentArray(
    Document(WPExcerpt(
        source="jq_man.log",
        content=elem["conv_group_merged"],  # must contain text/tags fields.
        lineRange=list(elem["line_range"]),
    ))
    for elem in listOfCleanedMergedConvGroupWithLineIndexMapping
)
da.apply(Document.embed_feature_hashing, backend="process")

# <Document ('id', 'adjacency', '_metadata', 'embedding', 'scores', 'chunks') at 3b330837d3111c7ded9bc83bb2808f2d>
# what is this shit?
q = (
    Document(text=query)
    .embed_feature_hashing(fields=('content',))
    .match(da, metric="jaccard", use_scipy=True)
)

# print(q.matches[:5, ("text", "scores__jaccard__value")])
docArray_5 = q.matches[:5]
# do we have other things?
print(q.embedding) # no embedding! wtf?
# {'multi_modal_schema': {'content': {'attribute_type': <AttributeType.DOCUMENT: 'document'>, 'type': 'Text', 'position': 0}}}
# print(docArray_5[0, ('text')])
mDocument = docArray_5[0]
# breakpoint()
print(mDocument.source.text)
# print(mDocument.content.text)
print(mDocument.lineRange.tags)
# [1933, 1936]
# how the fuck you have this?

# <Document ('id', 'adjacency', 'text', 'tags', 'embedding', 'scores') at 5b7fb3671d405bdb1840b2c2a2fd7c2f>
# we do not have other fields.
# it is not good! we do not have anything related to 'math' or 'addition' or 'operation'!

# still nothing? wtf?
