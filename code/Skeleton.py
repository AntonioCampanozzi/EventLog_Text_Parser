
from abc import ABC

class Skeleton(ABC):

    __skeletonForm:str
    __nonTerminals:list

    def __init__(self, form:str):
        self.__skeletonForm=form

    def getNonTerminals(self):

    def generateSentence(self, values:list):