from Atomizer import Atomizer
from FeaturesExtractor import FeaturesExtractor
from StylesComparer import StylesComparer
import time

def prepareTraining(vec):
    for i in range(0,len(vec)):
        frag1 = vec[i]
        for j in range(i+1,len(vec)):
            frag2 = vec[j]
            if frag1['ratio'] > 0.5 or frag2['ratio'] > 0.5:
                ratio = frag1['ratio'] * frag2['ratio']
                #print("{} {}".format(i,j))
                yield ([frag1['feats'], frag2['feats']], ratio)
            pass
        pass
    
X=[]
y=[]

stop = -1
start = time.time()

#training
num = 1
for part in range(1,10):
    for x in range(1,501):
        print(num)
        print(time.time() - start)
        atomizer = Atomizer("dataSets/part{}/suspicious-document{:05d}".format(part, num))
        frags = atomizer.GetFullyPlagiarizedFragments()
        vec=[]
        for frag in frags:
            featuresExtractor = FeaturesExtractor(frag)
            vec.append({'feats': featuresExtractor.GetFeatures(), 'ratio': frag['ratio']})
            pass
        for val in prepareTraining(vec):
            (_X, _y) = val
            X.append(_X)
            y.append(_y)#zamiast przechowywać w pamięci warto zapisać listę do pliku
        num+=1
        if num == stop and stop > 0:
            end = time.time()
            print(end - start)
            time.sleep(10)
        pass
    pass
comparer = StylesComparer(0);
comparer.Train(X,y)#i teraz ją odczytać


#testing
for num in range(4501,4754):
    atomizer = Atomizer("dataSets/part{}/suspicious-document{:05d}".format(10, num))
    frags = atomizer.GetParagraphs()
    vec=[]
    for frag in frags:
        featuresExtractor = FeaturesExtractor(frag)
        vec.append({'feats': featuresExtractor.GetFeatures(), 'ratio': frag['ratio']})
        pass
    #tutaj sprwdzenie jakoś tego, co zwróci sieć
    num+=1
    pass