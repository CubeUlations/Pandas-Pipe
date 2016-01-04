import pandas as pd
from base import filter_test


def test_simple_filter():
    df = pd.DataFrame(
        {
            't1': [1, 2, 3],
            't2': [-1, -2, -3]
        }
    )
    result_df = pd.DataFrame(
        {
            't5': [0, 0],
            't4': [2, 4]
        }
    ).sort_index(axis=1)
    output_df = filter_test.process(df)['output'].sort_index(axis=1)
    assert output_df.equals(result_df)
