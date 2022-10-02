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

embeddings.search()
for uid, score in uid_list_top5:
    uid = int(uid)
    # where is the damn score? wtf?
    answer = data_source[uid]
    print("{}:".format(uid), answer)
    print("score:", score)
# with open(storage_file_name, "w+") as f:
#     answers = []
#     for uid, score in uid_list_top5:
#         uid = int(uid)
#         answer = data_source[uid]
#         answers.append(answer)
#     data_example_json.update({"answers": answers})
#     f.write(json.dumps(data_example_json, ensure_ascii=False, indent=4))
#     print("write to %s" % storage_file_name)
