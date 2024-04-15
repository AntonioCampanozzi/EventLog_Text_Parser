from Sentence import Sentence


class Paragraph:
    __globalSentence: Sentence
    __localSentences: list

    def __init__(self, globalSentence: Sentence):
        self.__globalSentence = globalSentence

    def getGlobalSentence(self):
        return self.__globalSentence

    def getLocalSentence(self, index: int):
        return self.__localSentences[index]

    def addLocalSentence(self, locSentence: Sentence):
        self.__localSentences.append(locSentence)

    def __str__(self):
        paragraphstr = f'{self.getGlobalSentence()}\n'
        for localSentence in self.__localSentences:
            paragraphstr += f'{localSentence};\n'
        paragraphstr += '\n'
        return paragraphstr
