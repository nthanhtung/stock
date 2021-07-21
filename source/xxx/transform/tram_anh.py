import xxx.load.to_df as td
import pandas as pd
import pandas_ta as pta


class tram_anh():
    def __init__(self) -> None:
        self.custom_strategy = pta.Strategy(
            name="Momo and Volatility",
            description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
            ta=[
                {"kind": "sma", "length": 20, "append":"True"},
                {"kind": "sma", "length": 50, "append":"True"},
                {"kind": "sma", "length": 200, "append":"True"},
                {"kind": "bbands", "length": 20, "append":"True"},
                {"kind": "rsi"},
                {"kind": "macd", "fast": 8, "slow": 21},
                {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME", "append":"True"},
            ]
        )
        self.candle_pattern = ["doji", "shootingstar", "hammer", "hangingman", "eveningstar", "morningstar", "invertedhammer"]

    def to_df(self, df_source, symbol_current):
        df_current = df_source[df_source["symbol"] == symbol_current]
        df_current.head()

        df_col_list = ["open", "high", "low", "close", "volume", "adj_close"]
        df_current = df_current[df_col_list]

        # To run your "Custom Strategy"
        df_current.ta.strategy(self.custom_strategy)
        df_current.ta.cdl_pattern(name = self.candle_pattern, append = True)

        df_current["SIGNAL_SMA_20_X_SMA_50"] = df_current["SMA_20"] > df_current["SMA_50"]
        df_current["SIGNAL_PRICE_X_BBU_20_SELL"] = df_current["close"] > df_current["BBU_20_2.0"]
        df_current["SIGNAL_PRICE_X_BBL_20_BUY"] = df_current["close"] < df_current["BBL_20_2.0"]
        df_current["SIGNAL_RSI_70_SELL"] = df_current["RSI_14"] > 70
        df_current["SIGNAL_RSI_30_BUY"] = df_current["RSI_14"] < 30

        df_current.tail()
        df_current["symbol"] = symbol_current
        return df_current

    def xxx(self, symbol_list, data_path: str = "C:/stock/"):
        df = td.csv_path_to_df(data_path + 'data/stock_price')
        df["adj_close"] = df["close"]
        df.set_index(pd.DatetimeIndex(df["tradingDate"]), inplace=True)
        for i in range(len(symbol_list)):
            df_current = self.to_df(df_source=df, symbol_current=symbol_list[i])
            df_current.to_csv(data_path + f"data/stock_ta/{symbol_list[i]}.csv")
        return True


class temp(): 
    pass



# xxx_ta = tram_anh()
# xxx_ta.xxx(["HPG", "VNM"], "C:/Users/tung.nguyen/Desktop/0 Project/stock/")
