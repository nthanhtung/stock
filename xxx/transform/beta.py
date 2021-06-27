import pandas as pd
import numpy as np
import xxx.load.to_df as td


# Roll Function
# Returns groupby object ready to apply custom functions

from numpy.lib.stride_tricks import as_strided as stride
import pandas as pd

def roll(df, w, list_date_to_filter, **kwargs):
    v = df.values
    d0, d1 = v.shape
    s0, s1 = v.strides

    a = stride(v, (d0 - (w - 1), w, d1), (s0, s0, s1))

    rolled_df = pd.concat({
        row: pd.DataFrame(values, columns=df.columns)
        for row, values in zip(df.index, a)
    })  # create rolling/sliding window things

    rolled_df = rolled_df[rolled_df.index.isin(list_date_to_filter, level=0)] # filter date to avoid excess computation

    return rolled_df.groupby(level=0, **kwargs)

# Beta Function
# Use closed form solution of OLS regression
# Assume column 0 is market

def beta(df):
    # first column is the market
    X = df.values[:, [0]]
    # prepend a column of ones for the intercept
    X = np.concatenate([np.ones_like(X), X], axis=1)
    # matrix algebra
    b = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(df.values[:, 1:])
    return pd.Series(b[1], df.columns[1:], name='Beta')

# Input dataframe strucuture


#               Market     s0000     s0001     s0002     s0003     s0004     s0005     s0006     s0007     s0008     s0009  ...     s3989     s3990     s3991     s3992     s3993     s3994     s3995     s3996     s3997     s3998     s3999
# Date                                                                                                                      ...
# 1995-12-31  0.728546  0.675513  0.688173  0.072844  0.954855  0.677390  0.872082  0.121189  0.655257  0.438122  0.868818  ...  0.777193  0.438990  0.447012  0.128825  0.682321  0.057693  0.213816  0.527867  0.062187  0.561745  0.369624
# 1996-01-31  0.172022  0.107173  0.066479  0.778843  0.570779  0.659260  0.899787  0.743830  0.541568  0.769515  0.346845  ...  0.974025  0.439171  0.903383  0.251169  0.267713  0.228522  0.698496  0.367326  0.028912  0.869097  0.199463
# 1996-02-29  0.460964  0.627891  0.616278  0.260655  0.336733  0.821706  0.904124  0.442072  0.151736  0.868874  0.282638  ...  0.224187  0.939505  0.957553  0.353828  0.518734  0.110580  0.134759  0.710960  0.062588  0.339334  0.134619
# 1996-03-31  0.701750  0.537356  0.546828  0.367404  0.329619  0.520202  0.122381  0.771901  0.852561  0.236778  0.292321  ...  0.631175  0.076253  0.625307  0.837768  0.369676  0.991885  0.984995  0.725521  0.067750  0.086681  0.628215



#############

def calculate_beta(list_date_to_filter, sliding_window):
    df = td.csv_path_to_df('data\stock_price')
    df = df.pivot(index="tradingDate", columns="symbol", values="close")
    df = df[['^VNINDEX'] + list(df.columns)]
    df = df.sort_index(ascending=False)
    betas = roll(df.pct_change().fillna(0), sliding_window, list_date_to_filter).apply(beta)
    betas.head(5)
    return betas


