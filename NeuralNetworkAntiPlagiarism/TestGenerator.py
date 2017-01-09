from Atomizer import Atomizer
from FeaturesExtractor import FeaturesExtractor
from InputDataProcessor import InputDataProcessor
from InputDataReader import InputDataReader
from sklearn.neural_network.multilayer_perceptron import MLPClassifier
import csv
from Tester import Tester


class TestGenerator(object):
    def runTest(self, trainingFilename, startIndex, endIndex):
        
        a = Atomizer('learn')
        e = FeaturesExtractor()
        
        p = InputDataProcessor(a, e, (0.2, 0.8))
        r = InputDataReader(p)
        (X, y) = r.read_features(trainingFilename)

        
        n = MLPClassifier(solver='sgd', alpha=1e-5,  hidden_layer_sizes=(20,), random_state=1, verbose=True)

        n.fit(X, y)

        a = Atomizer('test')
        e = FeaturesExtractor()
        
        t = Tester(a, e, n, 0.9)
        
        for i in range(startIndex, endIndex):
            testFilename="suspicious-document{:05d}".format(i)
            test_file = r.get_file("dataSets/part{}/{}".format(1, testFilename))
            b = t.is_plagiarised(test_file)
            if b==False:
                continue
            print('odpowiedz systemu: ' + str(b[0]))

            print('stan rzeczywisty: ' + str(not not test_file['metadata']))
            csv_file=open("wyniki.csv",'a')
            wr = csv.writer(csv_file)
            list=[trainingFilename , testFilename, str(b[0]), str(not not test_file['metadata'])]
            wr.writerows([list])
        