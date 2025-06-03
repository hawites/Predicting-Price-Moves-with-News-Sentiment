import pandas as pd
import pandas_ta as ta

class TechnicalIndicators:
    def __init__(self, df):
        self.df = df

    def add_moving_average(self, window=14):
        self.df[f"MA_{window}"] = ta.SMA(self.df['Close'], timeperiod=window)
        return self.df

    def add_rsi(self):
        self.df['RSI'] = ta.RSI(self.df['Close'], timeperiod=14)
        return self.df

    def add_macd(self):
        macd, macdsignal, macdhist = ta.MACD(self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        self.df['MACD'] = macd
        self.df['MACD_Signal'] = macdsignal
        self.df['MACD_Hist'] = macdhist
        return self.df
