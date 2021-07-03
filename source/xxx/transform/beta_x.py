import pandas as pd
import numpy as np
import xxx.load.to_df as td
from numpy.lib.stride_tricks import as_strided as stride
import pandas as pd

def roll(df, w, list_date_to_filter, **kwargs):
    '''
    Roll Function
    Returns groupby object ready to apply custom functions
    '''
    v = df.values
    d0, d1 = v.shape
    s0, s1 = v.strides

    a = stride(v, (d0 - (w - 1), w, d1), (s0, s0, s1))

    rolled_df = pd.concat({
        row: pd.DataFrame(values, columns=df.columns)
        for row, values in zip(df.index[(w-1):], a)
    })  # create rolling/sliding window things

    rolled_df = rolled_df[rolled_df.index.isin(list_date_to_filter, level=0)] # filter date to avoid excess computation

    return rolled_df.groupby(level=0, **kwargs)


def beta(df):
    '''
    Beta Function
    Use closed form solution of OLS regression
    Assume column 0 is market
    '''    
    # first column is the market
    X = df.values[:, [0]]
    # prepend a column of ones for the intercept
    X = np.concatenate([np.ones_like(X), X], axis=1)
    # matrix algebra
    b = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(df.values[:, 1:])
    return pd.Series(b[1], df.columns[1:], name='Beta')


def calculate_beta(data_path, list_date_to_filter, sliding_window):
    df = td.csv_path_to_df(data_path + 'data\stock_price')
    df = df.pivot(index="tradingDate", columns="symbol", values="close")
    df = df[['^VNINDEX'] + list(df.columns)]
    betas = roll(df.pct_change().fillna(0), sliding_window, list_date_to_filter).apply(beta)
    betas.head(5)
    return betas


