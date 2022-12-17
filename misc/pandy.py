import pandas as pd
import numpy as np


def main():
    df = pd.DataFrame(
        {
            'cat': ['tom', 'dick', 'harry', 'tom'],
            'blah': ['a', 'b', 'c', 'd'],
            'blow': [1, 2, 3, 4],
            'num': [10, 15, 20, 100]
        }
    )

    df1 = pd.DataFrame(
        {
            'cat': ['tom', 'dick', 'harry'],
            'colour': ['red', 'green', 'blue']
        }
    )

    print(df)
    print('*' * 50)
    g = df.groupby(['cat']).mean()
    print(g)
    print('*' * 50)

    print(df1.join(g, on=['cat']))

    df = pd.DataFrame([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [np.nan, np.nan, np.nan]],
                      columns=['A', 'B', 'C'])

    print(df)
    print(df.agg("mean", axis="rows"))

    print(df.index)
    print(df.iloc[1].T)


if __name__ == '__main__':
    main()
