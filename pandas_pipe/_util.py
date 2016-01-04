# -*- coding:utf-8 -*-
def match_in_dict(keys, values):
    assert len(keys) == len(values)
    return {
        keys[i]: values[i] for i in range(0, len(keys))
    }


def equals_for_dict(d1, d2):
    """
    Deep compare for two specific dict
    :param d1: Dict with string key and dataframe values
    :param d2: Dict with string key and dataframe values
    :return:
    """
    if len(d1.keys()) != len(d2.keys()):
        return False
    for key in d1.keys():
        obj1 = d1.get(key)
        obj2 = d2.get(key)
        if obj2 is None:
            return False
        if obj1.columns.tolist() == obj2.columns.tolist():
            return obj1.equals(obj2)
        return False
