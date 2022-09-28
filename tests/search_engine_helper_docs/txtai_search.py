# do not use streamlit this time. maybe you want repl?
# check the damn GPU usage!
import os

from txtai.embeddings import Embeddings

# seems it can pull out the right thing.
# but the ram consumption?
# 1455MiB. this is high.
# this is a search application! damn it.

class Application:
    """
    Main application.
    """

    def __init__(self):
        """
        Creates a new application.
        """

        # Create embeddings model, backed by sentence-transformers & transformers
        self.embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
        # warning! this is a huge model. could crash my freaking device.
    def run(self):
        """
        Runs a Streamlit application.
        """

        st.title("Similarity Search")
        st.markdown("This application runs a basic similarity search that identifies the best matching row for a query.")


        if query:
            # Get index of best section that best matches query
            uid = self.embeddings.similarity(query, data)[0][0]
            answer = data[uid]


@st.cache(allow_output_mutation=True)
def create():
    """
    Creates and caches a Streamlit application.

    Returns:
        Application
    """

    return Application()


if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # progressbar? 