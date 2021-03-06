﻿class TextFeatures(object):
    def SetDots(self, dots):
        self.dots = dots
    def SetCommas(self, commas):
        self.commas = commas
    def SetWordPerSent(self, count):
        self.wordPerSent = count
    def SetLetterPerWord(self, count):
        self.letterPerWord = count
    def SetUpperLetter(self, count):
        self.upperLetters = count
    def SetReadabilityEase(self, coef):
        self.readabilityEase = coef
    def SetSyllablesPerWord(self, coef):
        self.syllablesPerWord = coef
    def SetWordsFrequency(self, frequency):
        self.wordsFrequency = frequency
    def SetFOG(self, index):
        self.FOG=index
    def SetTextLength(self, length):
        self.length=length
    def SetHonoreRMeasure(self, coeff):
        self.HonoreRMeasure=coeff
    def SetYuleKMeasure(self, coeff):
        self.YuleKMeasure=coeff
    def toFeatureList(self):
        featureList = [self.dots, self.commas, self.wordPerSent, self.letterPerWord, self.upperLetters, self.readabilityEase, self.syllablesPerWord \
            , self.HonoreRMeasure, self.YuleKMeasure]
        for (word) in self.wordsFrequency:
            featureList.append(self.wordsFrequency[word])
        return featureList
    def __str__(self):
        return 'dots ' + str(self.dots) + ' commas ' + str(self.commas) + ' wordBySent '\
            + str(self.wordBySent) + ' letterByWord ' + str(self.letterByWord) + ' upperLetters '\
            + str(self.upperLetters) + ' syllablesPerWord ' + str(self.syllablesPerWord) + ' RE ' + str(self.readabilityEase)\
            + ' FOG '+str(self.FOG)