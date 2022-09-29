# you decide not to remove stopwords?
# it does not affect my highlighting process anyway.

import en_core_web_sm
from nltk.stem import PorterStemmer

# shall we detect the language id first?
# but this is a short excerpt. except for lingua we won't get shit.
englishNLP = 

with open(".json",'r') as f:
    content = f.read()
    test_data = json.loads(content)