import re

from NonTerminal import NonTerminal
from Skeleton import Skeleton


class GlobalSkeleton(Skeleton):

    def __init__(self, form: str):
        # considering only global part of the skeleton
        globalform = form.split('\n', 1)[0]
        self._skeletonForm = globalform
        # composing nonTerminals
        nonTerminalPattern = re.compile(r'<(.*?)>')
        nonTerminalsasString = re.findall(nonTerminalPattern, self._skeletonForm)
        self._nonTerminals = [NonTerminal(name=extractedString) for extractedString in nonTerminalsasString]