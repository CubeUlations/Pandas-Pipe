# -*- coding:utf-8 -*-
import inspect
import types
import pandas as pd
from _util import match_in_dict


def mapping(column=None):
    '''(type(column) or NoneType) -> type(process)
    *Description*
    '''
    if isinstance(column, types.FunctionType):
        # Process column as func
        column.is_mapping = True
        column.column = column.__name__
        return column

    def process(func):
        '''(type(func)) -> type(process)
        *Description*
        '''
        func.is_mapping = True
        if column:
            func.column = column
        else:
            func.column = func.__name__
        return func

    return process


class Mapper:
    def __init__(self):
        '''(Mapper) -> NoneType
        *Description*
        '''
        pass

    def __call__(self, df):
        '''(Mapper, type(df)) -> type(new_df)
        '''
        map_functions = inspect.getmembers(self, predicate=lambda func: isinstance(func, inspect.types.MethodType)
                                                                          and getattr(func, 'is_mapping', False))
        new_df = pd.DataFrame()
        columns = df.columns.tolist()
        for map_function in map_functions:
            # Revert args order because dataframe return revert order of series
            new_df[map_function[1].column] = map(lambda *args: map_function[1](match_in_dict(columns, args[::-1])), *(df._series.values()))
        return new_df

