from xml.etree import ElementTree
import pickle
import threading

class InputDataReader(object):
    def __init__(self, processor):
        self.processor = processor
        self.lock = threading.Lock()
    def run(self, path):
        print("start: "+path)
        fp = open(path + ".txt", 'r', encoding='utf-8')
        text = fp.read()
        fp.close()

        xmlRoot = ElementTree.parse(path + ".xml").getroot()
        metadata = []
        nodes = [child for child in xmlRoot if child.attrib['name'] == 'plagiarism']
        for node in nodes:
            metadata.append(node.attrib)

        (x, y) = self.processor.get_input({'text':text, 'metadata': metadata})
        self.lock.acquire()
        self.X.extend(x)
        self.Y.extend(y)
        self.lock.release()
        print("end: "+path)
    def read(self, partInd, startInd, endInd, serialize = True):
        self.X = []
        self.Y = []
        threads=[]
        for ind in range(startInd, endInd):
            print('file index: ' + str(ind))
            path = "dataSets/part{}/suspicious-document{:05d}".format(partInd, 500 * (partInd - 1) + ind)
            thread=threading.Thread(target=self.run, args=([path]))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
            #X.extend(reader.X)
            #y.extend(reader.Y)
            pass
        if serialize:
            with open('features/part{}_{}_{}'.format(partInd, startInd, endInd), 'wb+') as handle:
                pickle.dump({'X':self.X,'y':self.Y}, handle)

        return (self.X, self.Y)
    def read_features(self, filename):
        X, y = [], []
        try:
            with open('features/{}'.format(filename), 'rb') as handle:
                storedFeatures = pickle.load(handle)
            X.extend(storedFeatures['X'])
            y.extend(storedFeatures['y'])
        except:
            print('błąd odczytu pliku features/{}'.format(filename))

        return X, y

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