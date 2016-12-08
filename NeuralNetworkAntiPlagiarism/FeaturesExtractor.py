from TextFeatures import TextFeatures
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
class FeaturesExtractor(object):
    def __init__(self, text):
        self.text=text['text']
    def GetFeatures(self):
        features=TextFeatures()
        wordCount=len(word_tokenize(self.text))
        features.SetDots(sum(1 for l in self.text if l=='.')/len(self.text))
        features.SetCommas(sum(1 for l in self.text if l==',')/len(self.text))
        features.SetWordsFrequency(self.GetWordsFrequency())
        features.SetWordBySent(wordCount/len(sent_tokenize(self.text)))
        features.SetLetterPerWord(len(self.text)/(wordCount))
        features.SetUpperLetter((sum(1 for l in self.text if l.isupper())-len(sent_tokenize(self.text)))/len(self.text))
        features.SetSyllablesPerWord(self.syllables()/wordCount)
        features.SetReadabilityEase(206.835 - (1.015 * features.wordBySent) - (84.6 * features.syllablesPerWord))
        return features
    def GetWordsFrequency(self):
        words=['the', 'a', 'and', 'or', 'am']
        frequency={}
        for word in words:
            frequency[word]=sum(1 for word in word_tokenize(self.text) if word.lower()==word)/len(self.text)
        return frequency
    def syllables(self):
        count = 0
        vowels = 'aeiouy'
        word = self.text.lower().strip(".:;?!")
        if word[0] in vowels:
            count +=1
        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count +=1
        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count+=1
        if count == 0:
            count +=1
        return count


