from nltk.corpus import wordnet as wn
var=wn.synsets('dog')[0]
print("dog synsets?" , var)

# we do not have such shit.
var=wn.synsets('狗', lang='cmn')[0]
# it is working, but we still don't get the language id firsthand.
# well that is simple. we don't have many languages.
# if no response, simply translate or query for more related info/tags on web.
print("dog2 synsets?" , var)

# then? find synonyms.
s=var.hypernyms()[0].hypernyms()
#s=var.hypernyms()[0].hypernyms()
print(s)

for l in var.lemmas("cmn"):
    # no antonym.
    print(l)
    a=l.antonyms()
    print(a)

