# do not use streamlit this time. maybe you want repl?
# check the damn GPU usage!

from txtai.embeddings import Embeddings

# seems it can pull out the right thing.
# but the ram consumption?
# 1455MiB. this is high.
# this is a search application! damn it.

from semantic_ai_search_base_conv_with_step_charbased import listOfCleanedMergedConvGroupWithLineIndexMapping

data = [elem['conv_group_merged'] for elem in listOfCleanedMergedConvGroupWithLineIndexMapping]

if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # progressbar? 

    embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
    # loading this thing?
    # warning! this is a huge model. could crash my freaking device.

    # Get index of best section that best matches query
    uid = embeddings.similarity(query, data)[0][0]
    answer = data[uid]
