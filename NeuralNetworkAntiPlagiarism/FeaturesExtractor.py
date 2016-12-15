from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from TextFeatures import TextFeatures
class FeaturesExtractor(object):

    def getFeatures(self, text):
        features=TextFeatures()
        wordCount=len(word_tokenize(text))
        sentCount=len(sent_tokenize(text))
        features.SetDots(sum(1 for l in text if l=='.')/len(text))
        features.SetCommas(sum(1 for l in text if l==',')/len(text))
        features.SetWordsFrequency(self.GetWordsFrequency(text))
        features.SetWordPerSent(wordCount/sentCount)
        features.SetLetterPerWord(len(text)/(wordCount))
        features.SetUpperLetter((sum(1 for l in text if l.isupper())-len(sent_tokenize(text)))/len(text))
        features.SetSyllablesPerWord(self.syllables(text)/wordCount)
        features.SetReadabilityEase(206.835 - (1.015 * features.wordPerSent) - (84.6 * features.syllablesPerWord))
        features.SetFOG(0.4*(wordCount/sentCount+100*sum(1 for w in word_tokenize(text) if self.syllables(w)>=3)/wordCount))
        return features.toFeatureList()
    def GetWordsFrequency(self, text):
        words=['the', 'a', 'and', 'or', 'am', 'of', 'is']
        frequency={}
        for word in words:
            frequency[word]=sum(1 for word in word_tokenize(text) if word.lower()==word)/len(text)
        return frequency
    def syllables(self, text):
        count = 0
        vowels = 'aeiouy'
        word = text.lower().strip(".:;?!")
        if len(word)==0 :
           return 0
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


