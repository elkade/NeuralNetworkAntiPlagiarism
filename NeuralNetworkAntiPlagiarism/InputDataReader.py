from xml.etree import ElementTree
import pickle
import threading
import csv
import ast

class InputDataReader(object):
    def __init__(self, processor):
        self.processor = processor
        self.lock = threading.Lock()
    def run(self, path, output_path, serialize):
        try:
            print("start: "+path)
            fp = open(path + ".txt", 'r', encoding='utf-8')
            text = fp.read()
            fp.close()

            xmlRoot = ElementTree.parse(path + ".xml").getroot()
            metadata = []
            nodes = [child for child in xmlRoot if child.attrib['name'] == 'plagiarism']
            for node in nodes:
                metadata.append(node.attrib)

            (X, Y) = self.processor.get_input({'text':text, 'metadata': metadata})
            self.lock.acquire()
            #self.X.extend(x)
            #self.Y.extend(y)
            if serialize:
                with open(output_path, 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, delimiter=';', quoting=csv.QUOTE_NONE, fieldnames=['x', 'y'])
                    for i in range(0,len(X)):
                        writer.writerow({'x':X[i], 'y':Y[i]})
            self.lock.release()
            print("end: "+path)
        except Exception as ex:
            print(ex.args)
    def read(self, partInd, startInd, endInd, serialize = True):
        self.X = []
        self.Y = []
        threads=[]
        output_path = 'features/part{}_{}_{}.csv'.format(partInd, startInd, endInd)
        with open(output_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', quoting=csv.QUOTE_NONE, fieldnames=['x', 'y'])
            writer.writeheader()
        for ind in range(startInd, endInd):
            print('file index: ' + str(ind))
            path = "dataSets/part{}/suspicious-document{:05d}".format(partInd, 500 * (partInd - 1) + ind)
            thread=threading.Thread(target=self.run, args=([path, output_path, serialize]))
            threads.append(thread)
            thread.start()
            
            #with open('features/part{}_{}_{}'.format(partInd, startInd, endInd), 'wb+') as handle:
            #    pickle.dump({'X':self.X,'y':self.Y}, handle)
        for thread in threads:
            thread.join()
            #X.extend(reader.X)
            #y.extend(reader.Y)
            pass
        return (self.X, self.Y)
    def read_features(self, filename):
        X, y = [], []
        buf = []
        try:
            with open('features/{}'.format(filename), 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
                for row in reader:
                    y.append(float(row['y']))
                    x = ast.literal_eval(row['x'])
                    X.append(x)
        except Exception as ex:
            print('błąd odczytu pliku features/{}'.format(filename), ex.args)

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