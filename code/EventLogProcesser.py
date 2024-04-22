from datetime import datetime

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
        for trc in eventLog:
            timestampOfFirstEvent = int(datetime.timestamp(trc[0].get('time:timestamp')))
            for e in trc:
                e['time:timestamp'] = int(datetime.timestamp(e.get('time:timestamp')) - timestampOfFirstEvent)

    @staticmethod
    def sortEventLog(elog: EventLog, timestampLabel: str = 'time:timestamp'):
        listofTrcaes: list = []
        timeStampkey = lambda t: t[0][timestampLabel]
        for i in elog:
            listofTrcaes.append(i)
        listofTrcaes.sort(key=timeStampkey)
        sortedEventLog = EventLog(listofTrcaes)
        return sortedEventLog

    @staticmethod
    def train_test_Split(evLog: EventLog, xesDestinationpath: str, originalXesName: str, trainPrcntg: float = 0.8):
        train_test_EventLogs = pm4py.objects.log.util.split_train_test.split(evLog, trainPrcntg)
        trainEventLog = train_test_EventLogs[0]
        testEventLog = train_test_EventLogs[1]
        # writing a new .xes with only train part
        pm4py.write_xes(trainEventLog, f'{xesDestinationpath}\\TRAIN_{originalXesName}')
        # writing a new .xes with only test part
        pm4py.write_xes(testEventLog, f'{xesDestinationpath}\\TEST_{originalXesName}')
