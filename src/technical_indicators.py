import pandas as pd
import talib

class TechnicalIndicators:
    def __init__(self, df):
        self.df = df

    def add_moving_average(self, window=14):
        self.df[f"MA_{window}"] = talib.SMA(self.df['Close'], timeperiod=window)
        return self.df

    def add_rsi(self):
        self.df['RSI'] = talib.RSI(self.df['Close'], timeperiod=14)
        return self.df

    def add_macd(self):
        macd, macdsignal, macdhist = talib.MACD(self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        self.df['MACD'] = macd
        self.df['MACD_Signal'] = macdsignal
        self.df['MACD_Hist'] = macdhist
        return self.df
