# do not use streamlit this time. maybe you want repl?
# check the damn GPU usage!

from txtai.embeddings import Embeddings

# seems it can pull out the right thing.
# but the ram consumption?
# 1455MiB. this is high.
# this is a search application! damn it.

from semantic_ai_search_base_conv_with_step_charbased import listOfCleanedMergedConvGroupWithLineIndexMapping

data_source = [elem['conv_group_merged'] for elem in listOfCleanedMergedConvGroupWithLineIndexMapping]
import os
if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # progressbar? 

    embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
    # loading this thing?
    # warning! this is a huge model. could crash my freaking device.

    # Get index of best section that best matches query
    print("MODEL READY")
    print("type 'q' to quit")
    import numpy as np
    # strange.

        # Convert queries to embedding vectors
    print('loading data_source')
    import progressbar
    data = np.array([embeddings.transform((None, row, None)) for row in progressbar.progressbar(data_source)])
    # i need progressbar!

        # Dot product on normalized vectors is equal to cosine similarity

        # Add index and sort desc based on score
    uids = [sorted(enumerate(score), key=lambda x: x[1], reverse=True) for score in scores]
    while True:
        query = input("> ")
        if query == "q":
            print("quitting")
            break
        queries = [query]
        queries = np.array([embeddings.transform((None, q, None)) for q in queries])
        scores = np.dot(queries, data.T).tolist()

        # uid = embeddings.similarity(query, data)[0][0]
        uid = 
        answer = data_source[uid]
        print(answer)
