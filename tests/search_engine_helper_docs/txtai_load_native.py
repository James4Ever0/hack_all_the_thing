import numpy as np

from txtai.embeddings import Embeddings
from semantic_ai_search_base_conv_with_step_charbased import (
    listOfCleanedMergedConvGroupWithLineIndexMapping,
)

data_source = [
    elem["conv_group_merged"]
    for elem in listOfCleanedMergedConvGroupWithLineIndexMapping
]
embeddings = Embeddings({
            "path": "sentence-transformers/distiluse-base-multilingual-cased-v1"
        })
# data = np.load("ids.npy")  # format wrong! fuck.
# # 4.2M for ids.npy. whatever. 200 files may take 200*4 = 800MB.
# embeddings.load("./multilingual_index_demo") # no model out there! fuck.
print("LOAD COMPLETE")
# queries = np.load("ann_query_embedding.npy") # this is the live data. we will obtain this embedding from jina.
# SHAPE: (1, 768) DTYPE: float32

# it still needs gpu.
# reshape this thing.

limit = 5
query = 'recursive every element apply'
uid_list_top5= embeddings.search(query, limit) # what is this thing?
# print(uid_list_top5)
# breakpoint()
# [(849, 0.6242430210113525), (186, 0.6196383833885193), (823, 0.6172434687614441), (728, 0.6048709750175476), (1389, 0.6044095158576965)]
# something like this. pretty cool.

for uid, score in uid_list_top5:
    # uid = int(uid)
    # where is the damn score? wtf?
    answer = data_source[uid]
    print("{}:".format(uid), answer)
    print("score:", score)
