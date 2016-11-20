from nltk.tokenize import sent_tokenize
from xml.etree import ElementTree

class Atomizer(object):
    def __init__(self, filePath):
        fp = open(filePath + ".txt")
        text = fp.read()
        fp.close()

        xmlRoot = ElementTree.parse(filePath + ".xml").getroot()
        self.metadata = []
        nodes = [child for child in xmlRoot if child.attrib['name']=='plagiarism']
        for node in nodes:
            self.metadata.append(node.attrib)

        self.text = text.replace('\n',' ')
    def GetSentences(self):
        sentences = sent_tokenize(self.text)

        #trzeba opatrzeæ zdania metadanymi, w jakim procencie s¹ splagiatowane

        sentences = self.AddMetadata(sentences)

        return sentences
    def AddMetadata(self, blocks):
        for block in blocks:
            ind = self.text.find(block)
            if ind == -1:
                raise Exception('Nie znaleziono bloku w tekscie zrodlowym')
            meta = [meta for meta in self.metadata if int(meta['this_offset']) <= ind and int(meta['this_offset']) + int(meta['this_length']) >= ind ]
            if not meta:
                yield {'text': block, 'ratio': 0, 'index': ind}
            else:

                meta = meta[0]

                start = max(int(meta['this_offset']), ind)

                end = int(meta['this_offset']) + int(meta['this_length'])

                end = min(end, ind + len(block))

                ratio = (end-start)/len(block)
                yield {'text': block, 'ratio': ratio, 'index': ind}