from abc import ABC, abstractmethod
import re

from EventLog_Text_Parser.code.NonTerminal import NonTerminal
from EventLog_Text_Parser.code.Sentence import Sentence


class Skeleton(ABC):
    _skeletonForm: str
    _nonTerminals: list

    @abstractmethod
    def __init__(self, form: str):
        pass

    def getNonTerminals(self):
        return self._nonTerminals

    def generateSentence(self, values: list):
        sentence = self._skeletonForm
        for i in range(self._nonTerminals.__len__()):
            sentence = sentence.replace(f'<{self._nonTerminals[i].getName()}>', str(values[i]))
        # post-processing(removing skeleton parts with null datas)
        voidDataPattern = re.compile(r'\([a-z\s]*None[a-z\s]*\)', re.IGNORECASE)
        voidParts = re.findall(voidDataPattern, sentence)
        print(voidParts)
        for i in voidParts:
            sentence = sentence.replace(i, '')
        # regardless, we are removing all ()
        sentence = sentence.replace('(', '').replace(')', '')
        completeSentence = Sentence(sentence)
        return completeSentence
