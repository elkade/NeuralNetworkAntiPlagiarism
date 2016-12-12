from xml.etree import ElementTree
import pickle

class InputDataReader(object):
    def __init__(self, processor):
        self.processor = processor

    def read(self, partInd, startInd, endInd, serialize = True):
        X = []
        y = []
        for ind in range(startInd, endInd):
            print('file index: ' + str(ind))
            path = "dataSets/part{}/suspicious-document{:05d}".format(partInd, 500 * (partInd - 1) + ind)
            file = self.get_file(path)
            (_X, _y) = self.processor.get_input(file)
            X.extend(_X)
            y.extend(_y)
            pass
        if serialize:
            with open('features/part{}'.format(partInd), 'wb+') as handle:
                pickle.dump({'X':X,'y':y}, handle)

        return (X, y)

    def get_file(self, path):
        fp = open(path + ".txt", 'r', encoding='utf-8')
        text = fp.read()
        fp.close()

        xmlRoot = ElementTree.parse(path + ".xml").getroot()
        metadata = []
        nodes = [child for child in xmlRoot if child.attrib['name'] == 'plagiarism']
        for node in nodes:
            metadata.append(node.attrib)

        return {'text':text, 'metadata': metadata}
