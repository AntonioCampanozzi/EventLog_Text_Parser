import math
import random
from datetime import datetime

import numpy as np
import pandas
import pandas as pd
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
    def get_pos_case_length_quantile(data, quantile=0.90):
        return int(
            np.ceil(data[data['case:label'] == 'deviant'].groupby('case:concept:name').size().quantile(quantile)))
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
    def split_train_validation(evLog: EventLog, XesName, trainPrcntg: float = 0.8):
        idxs = [i for i in range(len(evLog))]
        random.seed(42)
        random.shuffle(idxs)
        stop_idx = math.floor(len(idxs) * trainPrcntg)
        idxs_train = idxs[:stop_idx]
        idxs_test = idxs[stop_idx:]
        train_EventLog = EventLog(list(), attributes=evLog.attributes, extensions=evLog.extensions,
                                  classifiers=evLog.classifiers,
                                  omni_present=evLog.omni_present, properties=evLog.properties)
        val_EventLog = EventLog(list(), attributes=evLog.attributes, extensions=evLog.extensions,
                                 classifiers=evLog.classifiers,
                                 omni_present=evLog.omni_present, properties=evLog.properties)
        for idx in idxs_train:
            train_EventLog.append(evLog[idx])
        for idx in idxs_test:
            val_EventLog.append(evLog[idx])

        pm4py.write_xes(train_EventLog, f'..\\splitted_eventlogs\\TRAIN_{XesName}.xes')

        pm4py.write_xes(val_EventLog, f'..\\splitted_eventlogs\\VALIDATION_{XesName}.xes')

        return train_EventLog,val_EventLog

    @staticmethod
    def split_train_test(data: pd.DataFrame, train_ratio, XesName, split="temporal"):
        # split into train and test using temporal split and discard events that overlap the periods
        data = data.sort_values(['time:timestamp'], ascending=True, kind='mergesort')
        grouped = data.groupby('case:concept:name')
        start_timestamps = grouped['time:timestamp'].min().reset_index()
        start_timestamps = start_timestamps.sort_values('time:timestamp', ascending=True, kind='mergesort')
        train_ids = list(start_timestamps['case:concept:name'])[:int(train_ratio * len(start_timestamps))]
        train = data[data['case:concept:name'].isin(train_ids)].sort_values(['time:timestamp'],
                                                                            ascending=True,
                                                                            kind='mergesort')
        test = data[~data['case:concept:name'].isin(train_ids)].sort_values(['time:timestamp'],
                                                                            ascending=True,
                                                                            kind='mergesort')
        split_ts = test['time:timestamp'].min()
        train = train[train['time:timestamp'] < split_ts]

        train_log = pm4py.convert_to_event_log(pm4py.format_dataframe(train))
        test_log = pm4py.convert_to_event_log(pm4py.format_dataframe(test))
        pm4py.write_xes(test_log, f'..\\splitted_eventlogs\\TEST_{XesName}.xes')
        return train_log, test_log
