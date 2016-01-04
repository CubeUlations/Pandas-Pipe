import inspect
import pandas as pd
from _util import match_in_dict


def mapping(column=None):

    def process(func):
        func.is_mapping = True
        if column:
            func.column = column
        else:
            func.column = func.__name__
        return func

    return process


class Mapper:
    def __init__(self):
        pass

    def map_dataframe(self, df):
        map_functions = inspect.getmembers(self, predicate=lambda func: isinstance(func, inspect.types.MethodType)
                                                                          and getattr(func, 'is_mapping', False))
        new_df = pd.DataFrame()
        columns = df.columns.tolist()
        for map_function in map_functions:
            # Revert args order because dataframe return revert order of series
            new_df[map_function[1].column] = map(lambda *args: map_function[1](match_in_dict(columns, args[::-1])), *(df._series.values()))
        return new_df

