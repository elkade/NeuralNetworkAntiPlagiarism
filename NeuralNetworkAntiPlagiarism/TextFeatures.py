class TextFeatures(object):
    def SetDots(self, dots):
        self.dots=dots
    def SetCommas(self, commas):
        self.commas=commas
    def SetTheWords(self, words):
        self.theWords=words
    def SetAWords(self, words):
        self.aWords=words
    def SetWordBySent(self, count):
        self.wordBySent=count
    def SetLetterByWord(self, count):
        self.letterByWord=count
    def SetWordsFrequency(self, frequency):
        self.wordsFrequency=frequency
    def SetUpperLetter(self, count):
        self.upperLetters=count
    def __str__(self):
        return 'dots ' + str(self.dots) + ' commas ' + str(self.commas) + ' wordBySent ' + str(self.wordBySent) + ' letterByWord ' + str(self.letterByWord)

