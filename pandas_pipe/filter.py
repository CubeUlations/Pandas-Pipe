
class Filter:

    def __init__(self):
        pass

    def filter(self, df):
        return df

    def __call__(self, df):
        return self.filter(df)
