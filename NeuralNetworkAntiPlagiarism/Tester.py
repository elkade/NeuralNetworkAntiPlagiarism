class Tester(object):
    def __init__(self, atomizer, extractor, network, treshold):
        self.atomizer = atomizer
        self.extractor = extractor
        self.network = network
        self.treshold = treshold
        pass

    def is_plagiarised(self, file):
        fragments = list(self.atomizer.atomize(file))

        for fragment in fragments:
            features = self.extractor.getFeatures(fragment['text'])
            fragment['feats'] = features

        n = len(fragments)
        answers = [[] for i in range(n)]
        for i in range(n):
            for j in range(i,n):
                el1 = fragments[i]
                el2 = fragments[j]
                ans = self.network.predict([el1['feats'] + el2['feats']])
                answers[i].append(ans[0])
                answers[j].append(ans[0])

        b = False
        plags = []
        for i in range(n):
            s = sum(answers[i])
            if s > self.treshold * n:
                b = True
                plags.append(fragments[i]['text'])
        return (b, plags)
    pass