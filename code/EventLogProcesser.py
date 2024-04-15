import pm4py
from pm4py.objects.log.obj import EventLog


class EventLogProcesser:

    @staticmethod
    def exportEventLog(filepath: str, case_id: str = 'case:concept:name'):
        eventLog = pm4py.read_xes(filepath)
        eventLog = pm4py.convert_to_event_log(eventLog, case_id)
        return eventLog

    @staticmethod
    def convertTimeStamp(eventLog: EventLog):
        print('')



