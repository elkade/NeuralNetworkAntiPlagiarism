#import nltk.data
import sys

#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#fp = open("dataSets/part1/suspicious-document00001.txt")
#data = fp.read()
#print('\n-----\n'.join(tokenizer.tokenize(data)))
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize 
from Atomizer import Atomizer
from FeaturesExtractor import FeaturesExtractor
import nltk
atomizer = Atomizer("dataSets/part1/suspicious-document00005");
import sklearn
list = atomizer.GetParagraphs()
for sent in list:
    if len(sent['text'])==0:
        print("end")
        continue
    #print(str(sent).encode(sys.stdout.encoding, errors='replace'))
    print("\n\n\n")
    e=FeaturesExtractor(sent)
    g=e.GetFeatures()
    print(g)
    pass
    

    



