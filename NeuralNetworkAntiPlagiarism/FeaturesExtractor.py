from TextFeatures import TextFeatures
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
class FeaturesExtractor(object):
    def __init__(self, text):
        self.text=text['text']
    def GetFeatures(self):
        features=TextFeatures()
        features.SetDots(sum(1 for l in self.text if l=='.')/len(self.text))
        features.SetCommas(sum(1 for l in self.text if l==',')/len(self.text))
        features.SetWordsFrequency(self.GetWordsFrequency())
        features.SetWordBySent(len(word_tokenize(self.text))/len(sent_tokenize(self.text)))
        features.SetLetterByWord(len(self.text)/(len(word_tokenize(self.text))))
        features.SetUpperLetter((sum(1 for l in self.text if l.isupper())-len(sent_tokenize(self.text)))/len(self.text))
        return features
    def GetWordsFrequency(self):
        words=['the', 'a', 'and', 'or', 'am']
        frequency={}
        for word in words:
            frequency[word]=sum(1 for word in word_tokenize(self.text) if word.lower()==word)/len(self.text)
        return frequency
            


