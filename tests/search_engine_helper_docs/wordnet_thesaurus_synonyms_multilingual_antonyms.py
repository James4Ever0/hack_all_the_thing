from nltk.corpus import wordnet as wn
var=wn.synsets('dog')[0]
print("dog synsets?" , var)

var=wn.synsets('狗')[0]
print("dog2 synsets?" , var)
