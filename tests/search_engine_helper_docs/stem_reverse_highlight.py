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
    global englishNLP, porterStemmer
    doc = englishNLP(text)
    originalAndStemmedWordPairs = []
    for token in doc:
        original_word = token.text
        stemmed_word= porterStemmer.stem(original_word)
        originalAndStemmedWordPairs.append((original_word, stemmed_word))
    return originalAndStemmedWordPairs

def englishTextToStemmedWords(text):
    originalAndStemmedWordPairs = englishTextToOriginalAndStemmedWordPairs(text)
    stemmedWords = [stemmed_word for original_word, stemmed_word in originalAndStemmedWordPairs]
    return stemmedWords
import json

with open("demo_txtai_search_results",'r') as f:
    content = f.read()
    test_data = json.loads(content)

query = test_data['query']
answers = test_data['answers']

queryStemmedWords = englishTextToStemmedWords(query)

# parse and stem both query and answer, check for commondities.
# sentence -> [(original_word, stemmed_word), ...]

# we need to show these highlights! fuck.
from lazero.utils.logger import sprint
sprint("QUERY:",query)
sprint('QUERY KEYWORDS STEMMED:',queryStemmedWords)


from rich.text import Text

text = Text(
    "hello world python this is python", style="green"
)  # there is no style applied.
text.on(click="view.toggle('world')") # fuck?
from rich.console import Console

console = Console()
highlighted = text.highlight_words(
    ["python"], style="yellow"
)  # but we should not highlight individual letters right?
# so we pass a list of words to be highlighted.
# just a damn number?
console.print(text)
for answer in answers:
    highlightSet = set()
    answerOriginalAndStemmedWordPairs = englishTextToOriginalAndStemmedWordPairs(answer)
    for original_word, stemmed_word in answerOriginalAndStemmedWordPairs:
        if stemmed_word in queryStemmedWords:
            highlightSet.add(original_word) # just original_word is enough. remember to deduplicate.
    highlightSet