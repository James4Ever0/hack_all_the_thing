import numpy as np
from txtai.embeddings import Embeddings

embeddings = Embeddings()
embeddings.load("./multilingual_index_demo")

embeddings.ann.search(queries)