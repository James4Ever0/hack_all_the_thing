import numpy as np
from txtai.embeddings import Embeddings

embeddings = Embeddings()
embeddings.load("./multilingual_index_demo", model=False, query=False)
print("LOAD COMPLETE")
ann_query_embedding = np.fromfile("ann_query_embedding.txt",dtype=np.float32).reshape(1,-1)
# SHAPE: (1, 768) DTYPE: float32

# it still needs gpu.
# reshape this thing.

limit = 3
result = embeddings.ann.search(ann_query_embedding, limit) # how long does it take for you to load all these stuff?
print(result)
