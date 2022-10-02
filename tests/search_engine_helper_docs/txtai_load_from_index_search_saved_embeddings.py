import numpy as np
# from txtai.embeddings import Embeddings

# embeddings = Embeddings()
data = np.fromfile('ids.txt', dtype=np.float32).reshape(-1,768)
# embeddings.load("./multilingual_index_demo") # no model out there! fuck.
print("LOAD COMPLETE")
queries = np.fromfile("ann_query_embedding.txt",dtype=np.float32).reshape(1,-1)
# SHAPE: (1, 768) DTYPE: float32

# it still needs gpu.
# reshape this thing.

limit = 5


scores = np.dot(queries, data.T).tolist()  # the damn dot product!
        # uid = embeddings.similarity(query, data)[0][0]
        # this is actually the same. just a miniatured 'indexed' thing.
uids = [
    sorted(enumerate(score), key=lambda x: x[1], reverse=True)
    for score in scores
]
uid_list_top5 = np.array(uids)[0, :limit, :] 
for uid, score in uid_list_top5:
    uid = int(uid)
    # where is the damn score? wtf?
    answer = data_source[uid]
    print("{}:".format(uid), answer)
    print("score:", score)
    answers = []
for uid, score in uid_list_top5:
    uid = int(uid)
    answer = data_source[uid]
