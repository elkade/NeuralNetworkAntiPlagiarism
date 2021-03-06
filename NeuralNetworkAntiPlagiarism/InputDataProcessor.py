class InputDataProcessor(object):
    def __init__(self, atomizer, extractor, tresholds):
        self.atomizer = atomizer
        self.extractor = extractor
        self.tresholds = tresholds
        pass

    def get_input(self, file):
        X = []
        y = []
        fragments = list(self.atomizer.atomize(file))

        for fragment in fragments:
            features = self.extractor.getFeatures(fragment['text'])
            fragment['feats'] = features

        n = len(fragments)
        for i in range(n):
            for j in range(i,n):
                el1 = fragments[i]
                el2 = fragments[j]
                if el1['ratio'] < self.tresholds[0] and el2['ratio'] > self.tresholds[1]:
                    X.append(el1['feats'] + el2['feats'])
                    y.append(1)
                    continue
                if el1['ratio'] > self.tresholds[0] and el2['ratio'] < self.tresholds[1]:
                    X.append(el1['feats'] + el2['feats'])
                    y.append(1)
                    continue
                if el1['ratio'] < self.tresholds[1] and el2['ratio'] < self.tresholds[1]:
                    X.append(el1['feats'] + el2['feats'])
                    y.append(0)
                    continue
        return X, y
    pass
