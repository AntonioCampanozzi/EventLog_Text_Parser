from pm4py.objects.log.obj import EventLog, Trace

from EventSkeleton import EventSkeleton
from GlobalSkeleton import GlobalSkeleton


class SkeletonCompiler:


    __skeletonGlobal:GlobalSkeleton
    __skeletonEvent:EventSkeleton
    __logToCompile:EventLog

    def __init__(self, log:EventLog, glSkeleton:GlobalSkeleton, evSkeleton:EventSkeleton):

    def __compileEvent(self, index:int):

    def __compileGlobalTrace(self, trace:Trace):

    def __compileTrace(self, index:int):

    def compileText(self):
