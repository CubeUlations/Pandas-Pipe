import pandas as pd
from base import simple_test, test


def test_simple_mapper():
    df = pd.DataFrame(
        {
            't1': [1, 2, 3],
            't2': [-1, -2, -3]
        }
    )
    result_df = pd.DataFrame(
        {
            't5': [0, 0, 0],
            't4': [2, 4, 6]
        }
    ).sort_index(axis=1)
    output_df = simple_test.process(df)['output'].sort_index(axis=1)
    assert output_df.equals(result_df)


def test_pipe_mapper():
    df = pd.DataFrame(
        {
            't1': [1, 2, 3],
            't2': [-1, -2, -3]
        }
    )
    result_df = pd.DataFrame(
        {
            't5': [5, 5, 5],
            't4': [4, 16, 36]
        }
    ).sort_index(axis=1)
    output_df = test.process(df)['output'].sort_index(axis=1)
    assert output_df.equals(result_df)
