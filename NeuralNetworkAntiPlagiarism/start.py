from InputDataReader import InputDataReader
from InputDataProcessor import InputDataProcessor
from Tester import Tester
from Atomizer import Atomizer
from sklearn.neural_network.multilayer_perceptron import MLPClassifier
from FeaturesExtractor import FeaturesExtractor
from DocumentReader import DocumentReader
import pickle

def save(network):
    with open('network.bin', 'wb+') as handle:
        pickle.dump(network, handle)

a = Atomizer('learn')
e = FeaturesExtractor()

p = InputDataProcessor(a, e, (0.2, 0.8))
r = InputDataReader(p)

start, end = 1, 30

#r.read(1, start, end)

(X, y) = r.read_features('part1_{}_{}.csv'.format(start, end))
n = MLPClassifier(solver='adam', hidden_layer_sizes=(200, 200),  verbose=True, activation='tanh', tol = 0.0)
#n = pickle.load( open( "network.bin", "rb" ) )
n.fit(X, y)
save(n)
a = Atomizer('test')
e = FeaturesExtractor()

t = Tester(a, e, n, 0.8)
 
test_file = r.get_file("dataSets/part{}/suspicious-document{:05d}".format(8, 500 * (8 - 1) + 1))
b = t.is_plagiarised(test_file)
print('odpowiedz systemu: ' + str(b[0]))

print('stan rzeczywisty: ' + str(not not test_file['metadata']))