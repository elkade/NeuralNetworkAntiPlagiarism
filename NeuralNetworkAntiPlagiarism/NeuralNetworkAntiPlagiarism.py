from Atomizer import Atomizer
from FeaturesExtractor import FeaturesExtractor

num = 1
for part in range(1,9):
    for x in range(1,500):
        atomizer = Atomizer("dataSets/part{}/suspicious-document{:05d}".format(part, num))
        frags = atomizer.GetFullyPlagiarizedFragments()
        for frag in frags:
            featuresExtractor = FeaturesExtractor(frag)
            frag['features'] = featuresExtractor.GetFeatures()
            pass



        num+=1
        pass
pass


