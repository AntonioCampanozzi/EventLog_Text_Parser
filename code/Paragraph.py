from Sentence import Sentence


class Paragraph:
    __globalSentence: Sentence
    __localSentences: list
    __trcClass: object
    __prefixSet: list

    def __init__(self, globalSentence: Sentence):
        self.__globalSentence = globalSentence
        self.__localSentences = []
        self.__prefixSet = []

    def getGlobalSentence(self):
        return self.__globalSentence

    def getLocalSentence(self, index: int):
        return self.__localSentences[index]

    def getPrefixSet(self):
        return self.__prefixSet

    def addLocalSentence(self, locSentence: Sentence):
        self.__localSentences.append(locSentence)

    def toSubParagraphs(self, prfxLen: int = 1):
        while prfxLen <= self.__localSentences.__len__():
            subParagraph = Paragraph(self.__globalSentence)
            for i in range(prfxLen):
                subParagraph.addLocalSentence(self.__localSentences[i])
            self.__prefixSet.append(subParagraph)
            prfxLen += 1
        return self.__prefixSet

    def __str__(self):
        paragraphstr = '***START_PRAGRAPH***\n'
        for i in self.__prefixSet:
            prefixstr = f'{i.getGlobalSentence()}\n'
            for localSentence in i.__localSentences:
                prefixstr += f'{localSentence};\n'
            prefixstr += '\n'
            paragraphstr += f'{prefixstr}\n'
        paragraphstr += '***END_PARAGRAPH***\n'
        return paragraphstr

    def __len__(self, metric: str = 'characters'):
        paragraph_length = self.__globalSentence.__len__(metric)

        for event in self.__localSentences:
            paragraph_length += event.__len__(metric)

        return paragraph_length
