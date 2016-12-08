from Atomizer import Atomizer
from FeaturesExtractor import FeaturesExtractor
from StylesComparer import StylesComparer
import time
import pickle

def prepareTraining(vec):
    for i in range(0,len(vec)):
        frag1 = vec[i]
        for j in range(i + 1,len(vec)):
            frag2 = vec[j]
            if frag1['ratio'] > 0.5 or frag2['ratio'] > 0.5:
                ratio = frag1['ratio'] * frag2['ratio']
                #print("{} {}".format(i,j))
                yield ([frag1['feats'], frag2['feats']], ratio)
            pass
        pass
    

stop = -1
start = time.time()

startNum = 1
endNum = 3

#training
num = 1
for part in range(startNum, endNum):
    X = []
    y = []
    for x in range(1,501):
        print(num)
        print(time.time() - start)
        path = "part{}/suspicious-document{:05d}".format(part, 500 * (part-1) + x)
        atomizer = Atomizer("dataSets/" + path)
        frags = atomizer.GetFullyPlagiarizedFragments()
        vec = []
        for frag in frags:
            featuresExtractor = FeaturesExtractor(frag)
            vec.append({'feats': featuresExtractor.GetFeatures(), 'ratio': frag['ratio']})
            pass
        for val in prepareTraining(vec):
            (_X, _y) = val
            X.append(_X)
            y.append(_y)#zamiast przechowywać w pamięci warto zapisać listę do pliku
        num+=1
        #if num == stop and stop > 0:
        pass
    with open('features/part{}'.format(part), 'wb+') as handle:
        pickle.dump({'X':X,'y':y}, handle)

    print(time.time() - start)
    pass


X = []
y = []
for part in range(startNum, endNum):
    try:
        with open('features/part{}'.format(part), 'rb') as handle:
            storedFeatures = pickle.load(handle)
        X.extend(storedFeatures['X'])
        y.extend(storedFeatures['y'])
    except:
        print('błąd odczytu pliku features/part{}'.format(part))

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,  hidden_layer_sizes=(15,), random_state=1)
comparer = StylesComparer(clf)
comparer.Train(X,y)#i teraz ją odczytać


##testing
for num in range(4501,4754):
    atomizer = Atomizer("dataSets/part{}/suspicious-document{:05d}".format(10, num))
    frags = atomizer.GetParagraphs()
    vec = []
    for frag in frags:
        featuresExtractor = FeaturesExtractor(frag)
        vec.append({'feats': featuresExtractor.GetFeatures(), 'ratio': frag['ratio']})
        pass
    
    #tutaj sprwdzenie jakoś tego, co zwróci sieć
    num+=1
    pass