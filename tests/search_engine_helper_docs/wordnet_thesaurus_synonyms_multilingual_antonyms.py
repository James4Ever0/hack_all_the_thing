from nltk.corpus import wordnet as wn
var=wn.synsets('dog')[0]
print("dog synsets?" , var)

# we do not have such shit.
var=wn.synsets('狗', lang='cmn')[0]
# it is working, but we still don't get the language id firsthand.
print("dog2 synsets?" , var)
