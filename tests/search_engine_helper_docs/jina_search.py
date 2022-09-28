from semantic_ai_search_base_conv_with_step_charbased import listOfCleanedMergedConvGroupWithLineIndexMapping, linewise

query = "math addition"

from docarray import Document, DocumentArray

da = DocumentArray(Document(text=s.strip()) for s in d.text.split('\n') if s.strip())
da.apply(Document.embed_feature_hashing, backend='process')

q = (
    Document(text=query)
    .embed_feature_hashing()
    .match(da, metric='jaccard', use_scipy=True)
)

print(q.matches[:5, ('text', 'scores__jaccard__value')])