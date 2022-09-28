from semantic_ai_search_base_conv_with_step_charbased import (
    listOfCleanedMergedConvGroupWithLineIndexMapping,
    linewise,
)

query = "math addition"

from docarray import Document, DocumentArray
# A example multimodal document	
from docarray import dataclass, Document
from docarray.typing import Image, Text, JSON


@dataclass
class WPExcerpt:
    banner: Image
    headline: Text
    meta: JSON


a = WPArticle(
    banner='https://.../cat-dog-flight.png',
    headline='Everything to know about flying with pets, ...',
    meta={
        'author': 'Nathan Diller',
        'Column': 'By the Way - A Post Travel Destination',
    },
)

# d = Document(uri='https://www.gutenberg.org/files/1342/1342-0.txt').load_uri_to_text()
da = DocumentArray(
    Document(text=elem["conv_group_merged"])
    for elem in listOfCleanedMergedConvGroupWithLineIndexMapping
)
da.apply(Document.embed_feature_hashing, backend="process")

q = (
    Document(text=query)
    .embed_feature_hashing()
    .match(da, metric="jaccard", use_scipy=True)
)

print(q.matches[:5, ("text", "scores__jaccard__value")])
