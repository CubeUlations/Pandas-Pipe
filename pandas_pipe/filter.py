
class Filter:

    def __init__(self):
        '''(Filter) -> NoneType
        *Description*
        '''
        pass

    def filter(self, df):
        '''(Filter, type(df)) -> type(df)
        *Description*
        '''
        return df

    def __call__(self, df):
        '''(Filter, type(df)) -> ___
        *Description*
        '''
        return self.filter(df)


class NumberFilter(Filter):

    def filter(self, df):
        '''(NumberFilter, type(df)) -> type(df)
        *Description*
        '''
        index = df.dtypes.index.tolist()
        for column in index:
            if df.dtypes[column] not in ['float', 'float64', 'int', 'int64']:
                df = df.drop(column, axis=1)
        return df
