# do not use streamlit this time. maybe you want repl?
# check the damn GPU usage!

from txtai.embeddings import Embeddings

# seems it can pull out the right thing.
# but the ram consumption?
# 1455MiB. this is high.
# this is a search application! damn it.


if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # progressbar? 