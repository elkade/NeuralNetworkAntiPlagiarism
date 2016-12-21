from InputDataReader import InputDataReader
from InputDataProcessor import InputDataProcessor
from Tester import Tester
from Atomizer import Atomizer
from sklearn.neural_network.multilayer_perceptron import MLPClassifier
from FeaturesExtractor import FeaturesExtractor
from DocumentReader import DocumentReader

a = Atomizer('learn')
e = FeaturesExtractor()

p = InputDataProcessor(a, e, (0.2, 0.8))
r = InputDataReader(p)

#(X, y) = r.read(1, 1, 10)
(X, y) = r.read_features(1)
#n = NetworkMock()
n = MLPClassifier(solver='lbfgs', alpha=1e-5,  hidden_layer_sizes=(5,), random_state=1)

n.fit(X, y)

a = Atomizer('test')
e = FeaturesExtractor()

t = Tester(a, e, n, 0.8)

test_file = r.get_file("dataSets/part{}/suspicious-document{:05d}".format(8, 500 * (8 - 1) + 1))
b = t.is_plagiarised(test_file)
print('odpowiedz systemu: ' + str(b[0]))

print('stan rzeczywisty: ' + str(not not test_file['metadata']))