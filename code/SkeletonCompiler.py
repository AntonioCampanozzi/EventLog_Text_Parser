from pm4py.objects.log.obj import EventLog, Trace

from EventLog_Text_Parser.code.EventSkeleton import EventSkeleton
from EventLog_Text_Parser.code.GlobalSkeleton import GlobalSkeleton
from EventLog_Text_Parser.code.Paragraph import Paragraph
from EventLog_Text_Parser.code.Text import Text


class SkeletonCompiler:
    __skeletonGlobal: GlobalSkeleton
    __skeletonEvent: EventSkeleton
    __logToCompile: EventLog

    def __init__(self, log: EventLog, glSkeleton: GlobalSkeleton, evSkeleton: EventSkeleton):
        self.__logToCompile = log
        self.__skeletonGlobal = glSkeleton
        self.__skeletonEvent = evSkeleton

    def __compileEvent(self, traceOfTheEvent: Trace, index: int):
        # extracting values from the event
        values = []
        for nt in self.__skeletonEvent.getNonTerminals():
            values.append(traceOfTheEvent[index].get(nt.getName()))
        localSentence = self.__skeletonEvent.generateSentence(values)
        return localSentence

    def __compileGlobalTrace(self, trace: Trace):
        # extracting values from global part of the trace
        values = []
        for nt in self.__skeletonGlobal.getNonTerminals():
            values.append(trace.attributes.get(nt.getName()))
        globalSentence = self.__skeletonGlobal.generateSentence(values)
        return globalSentence

    def __compileTrace(self, index: int):
        # first, the head of the Trace
        globalSentence = self.__compileGlobalTrace(self.__logToCompile[index])
        #extracting trace label
        traceclass=self.__logToCompile[index].attributes['label']
        paragraph = Paragraph(globalSentence, traceclass)
        # then, all events
        for i in range(self.__logToCompile[index].__len__()):
            i_localSentence = self.__compileEvent(self.__logToCompile[index], i)
            paragraph.addLocalSentence(i_localSentence)
        return paragraph

    def compileText(self, supposed_maxlen: int):
        # this constructor does nothing, is needed just to initialize the variable
        text: Text = Text()
        for i in range(self.__logToCompile.__len__()):
            i_paragraph = self.__compileTrace(i)
            i_paragraph.toSubParagraphs(supposed_maxlen)
            text.add(i_paragraph)
        return text
