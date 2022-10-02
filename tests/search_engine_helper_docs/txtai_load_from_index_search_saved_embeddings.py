import numpy as np
# from txtai.embeddings import Embeddings

# embeddings = Embeddings()
embeddings = np.fromfile('ids.txt', dtype=np.float32).reshape(-1,768)
# embeddings.load("./multilingual_index_demo") # no model out there! fuck.
print("LOAD COMPLETE")
ann_query_embedding = np.fromfile("ann_query_embedding.txt",dtype=np.float32).reshape(1,-1)
# SHAPE: (1, 768) DTYPE: float32

# it still needs gpu.
# reshape this thing.

limit = 5
