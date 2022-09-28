from semantic_ai_search_base_conv_with_step_charbased import listOfCleanedMergedConvGroupWithLineIndexMapping, linewise

query = "math addition"`

from docarray import Document, DocumentArray

d = Document(uri='https://www.gutenberg.org/files/1342/1342-0.txt').load_uri_to_text()
da = DocumentArray(Document(text=s.strip()) for s in d.text.split('\n') if s.strip())
da.apply(Document.embed_feature_hashing, backend='process')

q = (
    Document(text='she smiled too much')
    .embed_feature_hashing()
    .match(da, metric='jaccard', use_scipy=True)
)

print(q.matches[:5, ('text', 'scores__jaccard__value')])