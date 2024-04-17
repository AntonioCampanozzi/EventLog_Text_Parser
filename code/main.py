from EventLog_Text_Parser.code.EventLogProcesser import EventLogProcesser
from EventLog_Text_Parser.code.EventSkeleton import EventSkeleton
from EventLog_Text_Parser.code.GlobalSkeleton import GlobalSkeleton
from EventLog_Text_Parser.code.SkeletonCompiler import SkeletonCompiler
from EventLog_Text_Parser.code.Text import Text

if __name__ == '__main__':
    EventLog = EventLogProcesser.exportEventLog('..\\..\\BPI_Challenge_2013_incidents.xes')

    EventLogProcesser.convertTimeStamp(EventLog)

    skeleton = open('..\\..\\skeleton.txt', 'r').read()

    globalSkeleton = GlobalSkeleton(skeleton)

    eventSkeleton = EventSkeleton(skeleton)

    compiler = SkeletonCompiler(log=EventLog, glSkeleton=globalSkeleton, evSkeleton=eventSkeleton)

    text: Text = compiler.compileText()

    text.store('..\\..\\Textlog.txt')
