import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
wnl = WordNetLemmatizer()

file = open('input.txt', 'r', encoding='utf-8')
text = file.read().split()

t = 'he was learning how to drive'.split()
print(type(t))
t = nltk.pos_tag(t)

mappedtags = {'NN': 'n', 'NNS': 'n', 'NNPS': 'n', 'NNP': 'n',
              'JJ': 'a', 'JJS': 's', 'JJR': 's',
              'RB': 'r', 'RBS': 's',
              'VB': 'v', 'VBD': 'v', 'VDN': 'v', 'VBP': 'v', 'VBZ': 'v', 'VBG': 'v'}

for el in t:
    print(el)
    if el[1] in mappedtags:
        pos = mappedtags[el[1]]
        print(wnl.lemmatize(el[0], pos))
    else:
        print(wnl.lemmatize(el[0]))




#print(wnl.lemmatize('touching', pos='n'))

#nltk.help.upenn_tagset()






'''
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
print(morph.parse('dogs'))
'''




