def match_in_dict(keys, values):
    assert len(keys) == len(values)
    return {
        keys[i]: values[i] for i in range(0, len(keys))
    }
