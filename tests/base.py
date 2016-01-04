# -*- coding:utf-8 -*-
from pandas_pipe import *

simple_test = Pipeline('Simple Test Pipeline')
filter_test = Pipeline('Simple Filter Pipeline')
test = Pipeline('Test Pipeline')


@test(outchannel='temp')
@simple_test
@filter_test
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


@filter_test(outchannel='root')
class F1(Filter):
    def filter(self, df):
        return df[df.t1 // 3 == 0]
