import re

from EventLog_Text_Parser.code.NonTerminal import NonTerminal
from Skeleton import Skeleton


class EventSkeleton(Skeleton):

    def __init__(self, form:str):
        # considering only local part of the skeleton
        globalform = form.split('\n', 1)[0]
        self._skeletonForm = globalform
        # composing nonTerminals
        nonTerminalPattern = re.compile(r'<(.*?)>')
        nonTerminalsasString = re.findall(nonTerminalPattern, self.__skeletonForm)
        self.__nonTerminals = [NonTerminal(name=extractedString) for extractedString in nonTerminalsasString]