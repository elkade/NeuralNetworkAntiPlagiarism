from Mocks.FeaturesExtractorMock import FeaturesExtractorMock
from Mocks.NetworkMock import NetworkMock
from InputDataReader import InputDataReader
from InputDataProcessor import InputDataProcessor
from Tester import Tester
from Atomizer import Atomizer

a = Atomizer('plag')
e = FeaturesExtractorMock()

p = InputDataProcessor(a, e, (0.2, 0.8))
r = InputDataReader(p)

(X, y) = r.read(1, 1, 4)

n = NetworkMock()
n.fit(X, y)

t = Tester(a, e, n, 0.8)

test_file = r.get_file("dataSets/part{}/suspicious-document{:05d}".format(8, 500 * (8 - 1) + 1))
b = t.is_plagiarised(test_file)
print('odpowiedz systemu: ' + str(b))

print('stan rzeczywisty: ' + str(not test_file['metadata']))