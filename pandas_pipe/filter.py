import abc


class Filter:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def filter(self, df):
        pass
