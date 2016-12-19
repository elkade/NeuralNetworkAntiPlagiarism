from nltk.tokenize import sent_tokenize
from xml.etree import ElementTree

class Atomizer(object):
    def __init__(self, type):
        self.type = type

    def atomize(self, file):
        text = file['text']
        metadata = file['metadata']

        if self.type == 'learn':

            fragments = []
            plag_frags = self.GetFullyPlagiarizedFragments(text, metadata)
            for frag in plag_frags:
                paragraphs = self._GetParagraphs(frag)
                for parag in paragraphs:
                    if len(parag) > 100:
                        fragments.append(parag)
            fragments = self.AddMetadata(fragments, text, metadata)
            return fragments
        if self.type == 'test':
            return self.GetParagraphs(text, metadata)

    def _GetParagraphs(self, text):
        paragraphs = text.split("\n\n")
        return paragraphs
    def GetParagraphs(self, text, metadata):
        paragraphs = text.split("\n\n")
        paragraphs = [p for p in paragraphs if len(p)>100]
        paragraphs = self.AddMetadata(paragraphs, text, metadata)
        return paragraphs
    def GetSentences(self, text, metadata):
        sentences = sent_tokenize(text)
        sentences = self.AddMetadata(sentences, text, metadata)
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