from Sentence import Sentence


class Paragraph:
    __globalSentence: Sentence
    localSentences: list

    def __init__(self, globalSentence: Sentence):
        self.__globalSentence = globalSentence
        self.localSentences=[]

    def getGlobalSentence(self):
        return self.__globalSentence

    def getLocalSentence(self, index: int):
        return self.localSentences[index]

    def addLocalSentence(self, locSentence: Sentence):
        self.localSentences.append(locSentence)

    def __str__(self):
        paragraphstr = f'{self.getGlobalSentence()}\n'
        for localSentence in self.localSentences:
            paragraphstr += f'{localSentence};\n'
        paragraphstr += '\n'
        return paragraphstr
