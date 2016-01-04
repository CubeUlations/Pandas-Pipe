# -*- coding:utf-8 -*-
import types

import pandas as pd
from mapper import Mapper


class Pipeline:
    def __init__(self, name='Undefined Pipeline'):
        self._mappers = {}
        self._output_channels_info = {}
        self._input_channels_info = {}
        self.name = name

    def process(self, df, channel='root'):
        df_map = {
            'root': df
        }
        mappers = self._mappers[channel]
        while mappers:
            if isinstance(mappers, list):
                temp_df_map = {}
                for mapper in mappers:
                    input_df = df_map.get(self._input_channels_info[mapper])
                    if input_df is None:
                        continue
                    temp_df = mapper.map_dataframe(input_df)
                    output_channel = self._output_channels_info[mapper]
                    if not temp_df_map.get(output_channel):
                        temp_df_map[output_channel] = []
                    temp_df_map[output_channel].append(temp_df)
                df_map.clear()
                for key, value in temp_df_map.items():
                    if len(value) == 1:
                        df_map[key] = value[0]
                    else:
                        df_map[key] = pd.concat(value, axis=1, ignore_index=True)
            mappers = []
            for key in df_map.keys():
                key_mappers = self._mappers.get(key)
                if key_mappers is not None:
                    mappers.extend(key_mappers)
            if len(mappers) == 0:
                mappers = None
        return df_map

    def __call__(self, channel='root', outchannel='output', priority=1):
        def process_function(cls):
            if issubclass(cls, Mapper):
                assert channel != 'output', 'You cannot use mapper for output chanell'
                assert isinstance(priority,
                                  int) and priority == 1, 'Mapper can\'t have priority, use channel logic instead'
                obj = cls()
                self._input_channels_info[obj] = channel
                self._output_channels_info[obj] = outchannel
                if not self._mappers.get(channel):
                    self._mappers[channel] = []
                self._mappers[channel].append(obj)
                return cls

        if isinstance(channel, types.ClassType):
            cls = channel
            channel = 'root'
            return process_function(cls)

        return process_function
