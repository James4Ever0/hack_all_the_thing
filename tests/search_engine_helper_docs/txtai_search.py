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

    embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"}) # same as the 'indexed' demo.

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
    data = np.array([embeddings.transform((None, row, None)) for row in progressbar.progressbar(data_source)]) # we need something other than this. fast info retrieval.
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
        uids = [sorted(enumerate(score), key=lambda x: x[1], reverse=True) for score in scores]
        # #b: index of the query, produced result
        # #doc: index of the document of the produced data
        # #data: different position inside the data, representing different values: (index, score)
        #                    #b #doc #data
        uid_list_top5 = uids[0][:5][:5]
        # this is a list, not a numpy array!
        # what is this shit anyway?
        print(uid_list_top5) # we need different results. 
        breakpoint()
        # for uid in uid_list_top5:
        #     answer = data_source[uid]
        #     print("{}:".format(uid),answer)
