samples = [
    "content: ) ○ 36 (cyan) ○ 37 (white) BUGS Presumably. Report them or discuss them at: https://github",  # conventional english
    "https://github.com/stedolan/jq/issues",  # github link
    """寻找潜在爆款话题 标签

快排参数 上首页
https://github.com/sopify-bot/seo

分为主动点击 换IP点击 
以及优化自身关键词 被动优化两种方式""",  # chinese with english
    """wordninja hit.matched_terms() from semantic_ai_search_base_conv_with_step_charbased import (
    listOfCleanedMergedConvGroupWithLineIndexMapping,
    linewise,
)

# query = "math addition operation" # strange enbedding!
# query="following examples"
from docarray import Document, DocumentArray
""",  # wordninja, glued words or code.
]

def removeDuplicates(line, chars=[" ", "\t"], maxConsecutiveLength=1):
    for char in chars:
        minUnallowedConsecutiveLength = maxConsecutiveLength + 1
        while True:
            if char * minUnallowedConsecutiveLength in line:
                line = line.replace(
                    char * minUnallowedConsecutiveLength, char * maxConsecutiveLength
                )
            else:
                break
    return line


def stripChars(line, chars=[" ", "\t"]):
    while True:
        flag = False
        for char in chars:
            if line.startswith(char) or line.endswith(char):
                line = line.strip(char)
                flag = True
        if not flag:
            break
    return line


def standardLineCleaner(line):
    line = removeDuplicates(line)
    line = stripChars(line)
    return line


import wordninja
import string
from zhon.hanzi import punctuation

chinese_and_english_punctuation = set(list(string.punctuation+punctuation))

# you also need to stem english words.

for sample in samples:
    line = sample.replace("\n"," ")
    for punctuation in chinese_and_english_punctuation: