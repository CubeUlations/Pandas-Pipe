
class Filter:

    def __init__(self):
        pass

    def filter(self, df):
        return df

    def __call__(self, df):
        return self.filter(df)


class NumberFilter(Filter):

    def filter(self, df):
        index = df.dtypes.index.tolist()
        for column in index:
            if df.dtypes[column] not in ['float', 'float64', 'int', 'int64']:
                df = df.drop(column, axis=1)
        return df
