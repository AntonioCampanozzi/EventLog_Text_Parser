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
        dummy_EventLog, test_EventLog = pm4py.objects.log.util.split_train_test.split(evLog, trainPrcntg)
        # splitting dummy EventLog in train and validation
        train_EventLog, validation_EventLog = pm4py.objects.log.util.split_train_test.split(dummy_EventLog, trainPrcntg)
        # writing new xes files for train and validation logs
        pm4py.write_xes(train_EventLog, f'{xesDestinationpath}\\TRAIN_{originalXesName}')
        pm4py.write_xes(validation_EventLog, f'{xesDestinationpath}\\VALIDATION_{originalXesName}')
        # writing a new .xes with only test part
        pm4py.write_xes(test_EventLog, f'{xesDestinationpath}\\TEST_{originalXesName}')
