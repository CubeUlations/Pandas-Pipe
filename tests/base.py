from pandas_pipe import *

simple_test = Pipeline('Simple Test Pipeline')
test = Pipeline('Test Pipeline')


@test(outchannel='temp')
@simple_test()
class T1(Mapper):
    @mapping(column='t5')
    def t3(self, record):
        return record['t1'] + record['t2']

    @mapping()
    def t4(self, record):
        return record['t1'] - record['t2']


@test(channel='temp')
class T2(Mapper):
    @mapping()
    def t5(self, record):
        return record['t5'] ** 2 + 5

    @mapping()
    def t4(self, record):
        return record['t4'] ** 2