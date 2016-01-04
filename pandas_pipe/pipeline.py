# -*- coding:utf-8 -*-
import types

import pandas as pd
from mapper import Mapper
from filter import Filter
from _util import equals_for_dict


class Pipeline:
    def __init__(self, name='Undefined Pipeline'):
        self._mappers = {}
        self._filters = {}
        self._output_channels_info = {}
        self._input_channels_info = {}
        self.name = name

    def process(self, df, channel='root'):
        df_map = {
            'root': df
        }
        updated = True
        while updated:
            next_df, updated = self._process_dataframe_map(df_map)
            df_map = next_df
        return df_map

    def append(self, cls, channel='root', output_channel='output'):
        self(channel, output_channel)(cls)

    def _process_dataframe_map(self, df_map):
        temp_df_map = {}
        for channel, df in df_map.items():
            temp_df_map.update(self._filter_dataframe(df, channel))
        is_filter_used = not equals_for_dict(df_map, temp_df_map)
        df_map.clear()
        for channel, df in temp_df_map.items():
            df_map.update(self._map_dataframe(df, channel))
        is_mapper_used = not equals_for_dict(df_map, temp_df_map)
        return df_map, is_filter_used or is_mapper_used

    def _modify_dataframe(self, df, objs):
        result_map = {}
        for obj in objs:
            output_channel = self._output_channels_info[obj]
            if result_map.get(output_channel) is None:
                result_map[output_channel] = []
            result_map[output_channel].append(obj(df))
        return self._merge_dataframes(result_map)

    def _filter_dataframe(self, df, channel):
        filters = self._filters.get(channel)
        if filters is None:
            return {
                channel: df
            }
        return self._modify_dataframe(df, filters)

    def _map_dataframe(self, df, channel):
        mappers = self._mappers.get(channel)
        if mappers is None:
            return {
                channel: df
            }
        return self._modify_dataframe(df, mappers)

    def _merge_dataframes(self, df_map):
        temp_df_map = {}
        for key, value in df_map.items():
            if len(value) == 1:
                temp_df_map[key] = value[0]
            else:
                temp_df_map[key] = pd.concat(value, axis=1, join='inner')
        df_map.clear()
        return temp_df_map

    def _process_entity(self, cls, channel, outchannel, entity_map):
        obj = cls()
        self._input_channels_info[obj] = channel
        self._output_channels_info[obj] = outchannel
        if not entity_map.get(channel):
            entity_map[channel] = []
        entity_map[channel].append(obj)
        return cls

    def __call__(self, channel='root', outchannel='output'):
        def process_function(cls):
            if issubclass(cls, Mapper):
                assert channel != 'output', 'You cannot use mapper for output chanell'
                return self._process_entity(cls, channel, outchannel, self._mappers)
            elif issubclass(cls, Filter):
                return self._process_entity(cls, channel, outchannel, self._filters)

        if isinstance(channel, types.ClassType):
            cls = channel
            channel = 'root'
            return process_function(cls)

        return process_function
