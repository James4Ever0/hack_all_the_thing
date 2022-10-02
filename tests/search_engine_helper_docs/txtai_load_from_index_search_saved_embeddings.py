import numpy as np
from txtai.embeddings import Embeddings

embeddings = Embeddings()
embeddings.load("./multilingual_index_demo")

ann_query_embedding = np.fromfile("ann_query_embedding.txt").reshape(1,-1)

# it still needs gpu.
# reshape this thing.

limit = 3
result = embeddings.ann.search(ann_query_embedding, limit) # how long does it take for you to load all these stuff?
print(result)
