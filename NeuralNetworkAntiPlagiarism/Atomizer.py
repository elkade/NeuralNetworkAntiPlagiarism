from nltk.tokenize import sent_tokenize
from xml.etree import ElementTree

class Atomizer(object):
    def __init__(self, type):
        self.type = type

    def atomize(self, file):

        text = file['text']
        metadata = file['metadata']

        if self.type == 'parag':
            return self.GetParagraphs(text, metadata)
        if self.type == 'sent':
            return self.GetSentences(text, metadata)
        if self.type == 'plag':
            return self.GetFullyPlagiarizedFragments(text, metadata)

    def GetParagraphs(self, text, metadata):
        paragraphs = text.split("\n\n")
        paragraphs = self.AddMetadata(paragraphs, metadata)
        return paragraphs

    def GetSentences(self, text, metadata):
        sentences = sent_tokenize(text)
        sentences = self.AddMetadata(sentences)
        return sentences

    def GetFullyPlagiarizedFragments(self, text, metadata):
        
        lastOffset = 0

        fragments = []

        if not metadata:
            fragments.append(text)
        else:
            for meta in metadata:
            
                currentOffset = int(meta['this_offset'])
                currentFragLength = int(meta['this_length'])

                if currentOffset != lastOffset:
                    frag = text[lastOffset:currentOffset]
                    fragments.append(frag)
                    pass

                lastOffset = currentOffset + currentFragLength
                frag = text[currentOffset:lastOffset]

                fragments.append(frag)
                pass


        fragments = self.AddMetadata(fragments, text, metadata)
        return fragments

    def AddMetadata(self, blocks, text, metadata):
        for block in blocks:
            ind = text.find(block)
            if ind == -1:
                raise Exception('Nie znaleziono bloku w tekscie zrodlowym')
            meta = [meta for meta in metadata if (int(meta['this_offset']) <= ind and int(meta['this_offset']) + int(meta['this_length']) >= ind) or (ind <= int(meta['this_offset']) and int(meta['this_offset']) <= ind + len(block)) ]
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