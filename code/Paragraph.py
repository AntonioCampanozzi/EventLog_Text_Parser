from EventLog_Text_Parser.code.Sentence import Sentence


class Paragraph:
    __globalSentence: Sentence
    __localSentences: list
    __trcClass: object
    __prefixSet: list

    def __init__(self, globalSentence: Sentence, trclass: object):
        self.__globalSentence = globalSentence
        self.__localSentences = []
        self.__prefixSet = []
        self.__trcClass = trclass

    def getGlobalSentence(self):
        return self.__globalSentence

    def getSentenceset(self):
        return self.__localSentences

    def getLocalSentence(self, index: int):
        return self.__localSentences[index]

    def getPrefixSet(self):
        return self.__prefixSet

    def getClass(self):
        return self.__trcClass

    def addLocalSentence(self, locSentence: Sentence):
        self.__localSentences.append(locSentence)

    def toSubParagraphs(self, supposed_maxlen: int, prfxLen: int = 1):
        max_prefix_length = min(40, supposed_maxlen)
        while prfxLen <= min(max_prefix_length, self.__localSentences.__len__()):
            subParagraph = Paragraph(self.__globalSentence, self.__trcClass)
            for i in range(prfxLen):
                subParagraph.addLocalSentence(self.getLocalSentence(i))
            self.__prefixSet.append(subParagraph)
            prfxLen += 1

    def formatParagraph(self):
        paragraphstr = ''
        for i in self.__prefixSet:
            prefixstr = ''
            for localSentence in i.__localSentences:
                prefixstr += f'{localSentence}\n'
            prefixstr += f'{i.getGlobalSentence()}\n'
            paragraphstr += f'{prefixstr}\n'
        return paragraphstr

    def formatPrefix(self):
        prefixstr = ''
        for localSentence in self.__localSentences:
            prefixstr += f'{localSentence}; '
        prefixstr += f'{self.getGlobalSentence()}   '
        return prefixstr

    def __str__(self):
        formattedString = ''
        # check if the paragraph is a prefix or not
        if len(self.__prefixSet) == 0:
            formattedString = self.formatPrefix()
        else:
            formattedString = self.formatParagraph()
        return formattedString

    def Paragraphlen(self, metric: str = 'characters'):
        paragraph_length = 0
        for prfx in self.__prefixSet:
            prefix_length = prfx.__globalSentence.__len__(metric)
            for event in prfx.__localSentences:
                prefix_length += event.__len__(metric)
            paragraph_length += prefix_length
        return paragraph_length
