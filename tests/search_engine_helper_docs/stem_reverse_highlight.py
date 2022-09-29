# you decide not to remove stopwords?
# it does not affect my highlighting process anyway.

import en_core_web_sm
from nltk.stem import PorterStemmer

# shall we detect the language id first?
# but this is a short excerpt. except for lingua we won't get shit.
# just english and chinese. for other languages we don't understand so much.
englishNLP = en_core_web_sm.load()
porterStemmer = PorterStemmer()


def englishTextToOriginalAndStemmedWordPairs(text):
    

import json

with open("demo_txtai_search_results",'r') as f:
    content = f.read()
    test_data = json.loads(content)

query = test_data['query']
answers = test_data['answers']

# parse and stem both query and answer, check for commondities.
# sentence -> [(original_word, stemmed_word), ...]

for answer in answers:
