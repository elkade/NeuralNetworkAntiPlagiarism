from InputDataReader import InputDataReader
from InputDataProcessor import InputDataProcessor
from Tester import Tester
from Atomizer import Atomizer
from sklearn.neural_network.multilayer_perceptron import MLPClassifier
from FeaturesExtractor import FeaturesExtractor
from DocumentReader import DocumentReader
import pickle
import time
import sys
import winsound
def print_time_interval(txt):
    global start_time
    print("Time elapsed on {}:".format(txt),time.time() - start_time)
    start_time = time.time()

def save(network):
    with open('network.bin', 'wb+') as handle:
        pickle.dump(network, handle)
try:

    for i in range(1):

        part, start, end, hidden, solver = 1, 1, 2, 200, 'sgd'
        #
        sys.stdout = open('output/{}_{}x{}output{}_{}_{}.txt'.format(solver, hidden, hidden, part, start, end), 'w+', 1)
        #

        start_time = time.time()


        a = Atomizer('learn')
        e = FeaturesExtractor()

        p = InputDataProcessor(a, e, (0.2, 0.8))
        r = InputDataReader(p)


        r.read(part, start, end)
        print_time_interval("feature extraction")
        (X, y) = r.read_features('part{}_{}_{}.csv'.format(part, start, end))
        print_time_interval("reading serialized features")
        n = MLPClassifier(solver=solver, hidden_layer_sizes=(hidden, hidden),  verbose=True, activation='tanh', tol = 0.0)
        print(n)
        n = pickle.load( open( "network.bin", "rb" ) )
        n.fit(X, y)
        print_time_interval("network learning")
        save(n)
        #a = Atomizer('test')
        #e = FeaturesExtractor()

        #t = Tester(a, e, n, 0.8)
 
        #test_file = r.get_file("dataSets/part{}/suspicious-document{:05d}".format(8, 500 * (8 - 1) + 1))
        #b = t.is_plagiarised(test_file)
        #print('odpowiedz systemu: ' + str(b[0]))

        #print('stan rzeczywisty: ' + str(not not test_file['metadata']))
        #print_time_interval()
    end
finally:
    winsound.Beep(2500,1000)