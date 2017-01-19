from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from math import log10
from TextFeatures import TextFeatures
class FeaturesExtractor(object):

    def getFeatures(self, text):
        features=TextFeatures()
        words=word_tokenize(text)
        wordCount=len(words)
        sentCount=len(sent_tokenize(text))
        frequency=self.GetTotalWordFrequency(words)
        features.SetTextLength(len(text))
        features.SetDots(sum(1 for l in text if l=='.')/len(text))
        features.SetCommas(sum(1 for l in text if l==',')/len(text))
        features.SetWordsFrequency(self.GetWordsFrequency(frequency, words, len(text)))
        features.SetWordPerSent(wordCount/sentCount)
        features.SetLetterPerWord(len(text)/(wordCount))
        features.SetUpperLetter((sum(1 for l in text if l.isupper())-sentCount)/len(text))
        features.SetSyllablesPerWord(self.syllables(text)/wordCount)
        features.SetReadabilityEase(206.835 - (1.015 * features.wordPerSent) - (84.6 * features.syllablesPerWord))
        features.SetFOG(0.4*(wordCount/sentCount+100*sum(1 for w in words if self.syllables(w)>=3)/wordCount))
        features.SetHonoreRMeasure(self.GetRMeasure(frequency, wordCount))
        features.SetYuleKMeasure(self.GetKMeasure(frequency, wordCount))
        return features.toFeatureList()
    def GetKMeasure(self, frequency, wordCount):
        V={}
        for (word, count) in frequency.items():
            if count not in V:
                V[count]=0
            V[count]=V[count]+1
        K=0
        for (i, count) in V.items():
            K=K+i*i*count
        K=K-len(V)*wordCount
        K=10000*K/(wordCount*wordCount)
        return K
    def GetRMeasure(self, frequency, wordCount):
        return 100*log10(wordCount)*(1-self.V1(frequency)/len(frequency))
    def V1(self, frequency):
        totalCount=0
        for (word, count) in frequency.items():
            if count==1:
                totalCount=totalCount+1
        return totalCount
    def GetWordsFrequency(self, frequency, words, textLength):
        smallWords=['the', 'a', 'and', 'or', 'am', 'of', 'is']
        smallFrequency={}
        for word in smallWords:
            if word not in frequency:
                smallFrequency[word]=0
            else:
                smallFrequency[word]=frequency[word]/textLength
        return smallFrequency
    def GetTotalWordFrequency(self, words):
        frequency={}
        for word in words:
            wl=word.lower()
            if wl not in frequency:
                frequency[wl]=0
            frequency[wl]=frequency[wl]+1
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


