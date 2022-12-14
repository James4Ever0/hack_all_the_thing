# do not use streamlit this time. maybe you want repl?
# check the damn GPU usage!

# are you sure indexed search is the same as similarity search?

from txtai.embeddings import Embeddings
from lazero.utils.logger import sprint
# seems it can pull out the right thing.
# but the ram consumption?
# 1455MiB. this is high.
# this is a search application! damn it.

# we still got some unfixed hyphen problems. damn.

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
    os.environ["http_proxy"] = ""
    os.environ["https_proxy"] = ""
    os.environ["all_proxy"] = ""
    # progressbar?

# needs to query from huggingface?
# will this fucking work?
    embeddings = Embeddings(
        {'path': 'sentence-transformers/all-MiniLM-L6-v2'} # official
        # {"path": "sentence-transformers/nli-mpnet-base-v2"} # original
    )  # same as the 'indexed' demo.

    # loading this thing?
    # warning! this is a huge model. could crash my freaking device.

    # Get index of best section that best matches query
    print("MODEL READY")
    print("type 'q' to quit")

    # strange.

    # Convert queries to embedding vectors
    print("loading data_source")
    import progressbar

    # but i want to ask, what can be the 'tags'?

    embeddings.index((uid, text, None) for uid, text in enumerate(progressbar.progressbar(data_source))) # are you sure that this progressbar will work?
    # generator? are we passing a generator?
    # this is quick! fuck.

    # Extract uid of first result
    # search result format: (uid, score)
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
        # the "1" is the limit. how about let's make it into 5?
        limit = 5
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
            sprint("score:", score)
