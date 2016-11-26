#import nltk.data

#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#fp = open("dataSets/part1/suspicious-document00001.txt")
#data = fp.read()
#print('\n-----\n'.join(tokenizer.tokenize(data)))

from nltk.tokenize import sent_tokenize
from Atomizer import Atomizer
atomizer = Atomizer("dataSets/part1/suspicious-document00001");

list = atomizer.GetParagraphs()
for sent in list:
    print(sent)
    print("\n\n\n")
    pass
    



