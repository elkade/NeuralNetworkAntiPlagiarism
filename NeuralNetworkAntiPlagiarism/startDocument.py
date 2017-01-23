from Atomizer import Atomizer
from FeaturesExtractor import FeaturesExtractor
import pickle

a=Atomizer('test')
fp = open("test_documents\doc1.txt", 'r', encoding='utf-8')
text = fp.read()
fp.close()
paragraphs=a._GetParagraphs(text)
fe=FeaturesExtractor()
features=[]
for paragraph in paragraphs:
    features.append(fe.getFeatures(paragraph))
n = pickle.load( open( "network.bin", "rb" ) )
length=len(features)
results=[[0 for i in range(length)] for i in range(length)]
for i in range(length):
    for j in range(i):
        result=n.predict(features[j]+features[i])[0]
        results[i][j]=result
        results[j][i]=result
docFeature=1