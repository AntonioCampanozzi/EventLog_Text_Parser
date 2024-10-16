
import pandas as pd
from EventLogProcesser import EventLogProcesser
from EventSkeleton import EventSkeleton
from GlobalSkeleton import GlobalSkeleton
from SkeletonCompiler import SkeletonCompiler


if __name__ == '__main__':

    eventlog_path = input('insert event log path: ')
    skeleton_path = input('insert skeleton path: ')
    log_name = input('insert log name: ')

    quantileprefixlen = EventLogProcesser.get_pos_case_length_quantile(pd.read_csv(eventlog_path, sep=';'))

    print('processing event log ...')

    TRAIN_log, TEST_log = EventLogProcesser.split_train_test(pd.read_csv(eventlog_path, sep=';'), train_ratio=0.8,
                                                             XesName=log_name)

    TRAIN_log, VALIDATION_log = EventLogProcesser.split_train_validation(TRAIN_log, XesName=log_name)

    EventLogProcesser.convertTimeStamp(TRAIN_log)

    EventLogProcesser.convertTimeStamp(TEST_log)

    EventLogProcesser.convertTimeStamp(VALIDATION_log)

    skeleton = open(skeleton_path, 'r').read()

    globalSkeleton = GlobalSkeleton(skeleton)

    eventSkeleton = EventSkeleton(skeleton)

    TRAIN_compiler = SkeletonCompiler(log=TRAIN_log, glSkeleton=globalSkeleton, evSkeleton=eventSkeleton)

    VALIDATION_compiler = SkeletonCompiler(log=VALIDATION_log, glSkeleton=globalSkeleton, evSkeleton=eventSkeleton)

    TEST_compiler = SkeletonCompiler(log=TEST_log, glSkeleton=globalSkeleton, evSkeleton=eventSkeleton)

    print('compiling ...')

    TRAIN_text = TRAIN_compiler.compileText(quantileprefixlen)

    VALIDATION_text = VALIDATION_compiler.compileText(quantileprefixlen)

    TEST_text = TEST_compiler.compileText(quantileprefixlen)

    print('texts generated.')

    while True:
        answer_path = input('do you want to save these textlogs in a specific directory? (y/n):')

        answer_txt = input('do you want a readable sample? (y/n):')

        if answer_path == 'y' and answer_txt == 'y':

            path = input('insert path to directory:')

            print('saving...')

            TRAIN_text.store(f'{path}/TRAIN_{log_name}_textlog')

            VALIDATION_text.store(f'{path}/VALIDATION_{log_name}_textLog')

            TEST_text.store(f'{path}/TEST_{log_name}_textLog')

            TEST_text.store(f'{path}/TEST_{log_name}_textLog', filetype='.txt')

            print('files saved.')

            break

        elif answer_path == 'y' and answer_txt == 'n':

            path = input('insert path to directory:')

            print('saving...')

            TRAIN_text.store(f'{path}/TRAIN_{log_name}_textlog')

            VALIDATION_text.store(f'{path}/VALIDATION_{log_name}_textLog')

            TEST_text.store(f'{path}/TEST_{log_name}_textLog')

            print('files saved.')

            break

        elif answer_path == 'n' and answer_txt == 'y':

            print('saving...')

            TRAIN_text.store(f'..\\textlogs\\TRAIN_{log_name}_textlog')

            VALIDATION_text.store(f'..\\textlogs\\VALIDATION_{log_name}_textLog')

            TEST_text.store(f'..\\textlogs\\TEST_{log_name}_textLog')

            TEST_text.store(f'..\\textlogs\\TEST_{log_name}_textLog', filetype='.txt')

            print('files saved in standard directory \"textlogs\".')

            break

        elif answer_path == 'n' and answer_txt == 'n':

            print('saving...')

            TRAIN_text.store(f'..\\textlogs\\TRAIN_{log_name}_textlog')

            VALIDATION_text.store(f'..\\textlogs\\VALIDATION_{log_name}_textLog')

            TEST_text.store(f'..\\textlogs\\TEST_{log_name}_textLog')

            print('files saved in standard directory \"textlogs\".')

            break

        else:

            print('error, maybe you mistyped one or both the answers.')


