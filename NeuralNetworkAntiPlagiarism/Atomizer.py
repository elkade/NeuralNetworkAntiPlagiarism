from nltk.tokenize import sent_tokenize
from xml.etree import ElementTree

class Atomizer(object):
    def __init__(self, filePath):
        fp = open(filePath + ".txt", 'r', encoding='utf-8')
        self.text = fp.read()
        fp.close()

        xmlRoot = ElementTree.parse(filePath + ".xml").getroot()
        self.metadata = []
        nodes = [child for child in xmlRoot if child.attrib['name'] == 'plagiarism']
        for node in nodes:
            self.metadata.append(node.attrib)

    def atomize(self, type):
        if type == 'parag':
            return GetParagraphs()
        if type == 'sent':
            return GetSentences()
        if type == 'plag':
            return GetFullyPlagiarizedFragments()

    def GetParagraphs(self):
        paragraphs = self.text.split("\n\n")
        paragraphs = self.AddMetadata(paragraphs)
        return paragraphs

    def GetSentences(self):
        sentences = sent_tokenize(self.text)
        sentences = self.AddMetadata(sentences)
        return sentences

    def GetFullyPlagiarizedFragments(self):
        
        lastOffset = 0

        fragments = []

        if not self.metadata:
            fragments.append(self.text)
        else:
            for meta in self.metadata:
            
                currentOffset = int(meta['this_offset'])
                currentFragLength = int(meta['this_length'])

                if currentOffset != lastOffset:
                    frag = self.text[lastOffset:currentOffset]
                    fragments.append(frag)
                    pass

                lastOffset = currentOffset + currentFragLength
                frag = self.text[currentOffset:lastOffset]

                fragments.append(frag)
                pass


        fragments = self.AddMetadata(fragments)
        return fragments

    def AddMetadata(self, blocks):
        for block in blocks:
            ind = self.text.find(block)
            if ind == -1:
                raise Exception('Nie znaleziono bloku w tekscie zrodlowym')
            meta = [meta for meta in self.metadata if (int(meta['this_offset']) <= ind and int(meta['this_offset']) + int(meta['this_length']) >= ind) or (ind <= int(meta['this_offset']) and int(meta['this_offset']) <= ind + len(block)) ]
            if not meta:
                yield {'text': block, 'ratio': 0, 'index': ind}
            else:
                l = 0

                for m in meta:
                    start = max(int(m['this_offset']), ind)

                    end = int(m['this_offset']) + int(m['this_length'])

                    end = min(end, ind + len(block))

                    l+=end - start

                ratio = l / len(block)
                yield {'text': block, 'ratio': ratio, 'index': ind}