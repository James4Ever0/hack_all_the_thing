# do not use streamlit this time. maybe you want repl?
# check the damn GPU usage!

from txtai.embeddings import Embeddings

# seems it can pull out the right thing.
# but the ram consumption?
# 1455MiB. this is high.
# this is a search application! damn it.

from semantic_ai_search_base_conv_with_step_charbased import (
    listOfCleanedMergedConvGroupWithLineIndexMapping,
)

data_source = [
    elem["conv_group_merged"]
    for elem in listOfCleanedMergedConvGroupWithLineIndexMapping
]
import os

if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # progressbar?

    embeddings = Embeddings(
        {"path": "sentence-transformers/nli-mpnet-base-v2"}
    )  # same as the 'indexed' demo.

    # loading this thing?
    # warning! this is a huge model. could crash my freaking device.

    # Get index of best section that best matches query
    print("MODEL READY")
    print("type 'q' to quit")
    import numpy as np

    # strange.

    # Convert queries to embedding vectors
    print("loading data_source")
    import progressbar

    embeddings.index([(uid, text, None) for uid, text in enumerate(progressbar.progressbar(data_source))]) # are you sure that this progressbar will work?

    # Extract uid of first result
    # search result format: (uid, score)
    uid = embeddings.search(query, 1)[0][0]
    # you want to use other methods?
    # embeddings.index # what is this fucking index?
    # document format: (id, data, tags)
    # i need progressbar!
    # Dot product on normalized vectors is equal to cosine similarity

    # Add index and sort desc based on score
    while True:
        query = input("> ")
        if query == "q":
            print("quitting")
            break
        queries = [query]
        queries = np.array([embeddings.transform((None, q, None)) for q in queries])
        scores = np.dot(queries, data.T).tolist()
        # uid = embeddings.similarity(query, data)[0][0]
        uids = [
            sorted(enumerate(score), key=lambda x: x[1], reverse=True)
            for score in scores
        ]
        # #b: index of the query, produced result
        # #doc: index of the document of the produced data
        # #data: different position inside the data, representing different values: (index, score)
        #          #b #doc #data
        # uid= uids[0][0][0]
        uid_list_top5 = np.array(uids)[0, :5, :]  # allow omitted index???
        # the thing is integer based. so the score is always zero.
        # uid_list_top5 = np.array(uids,dtype=int)[0,:5,0]
        # this is a list, not a numpy array!
        # what is this shit anyway?
        # print(uid_list_top5) # we need different results.
        # breakpoint()
        # you may want set some score filters.
        for uid, score in uid_list_top5:
            uid = int(uid)
            # where is the damn score? wtf?
            answer = data_source[uid]
            print("{}:".format(uid), answer)
            print("score:", score)
