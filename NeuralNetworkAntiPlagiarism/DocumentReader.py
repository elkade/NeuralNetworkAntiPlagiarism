class DocumentReader(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path=path
    def run(self):
        print(path)
        print(time.time() - start)
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