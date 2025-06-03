import pandas as pd
import numpy as np
import talib

class TechnicalIndicators:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self._validate_data()

    def _validate_data(self):
        required_cols = {'Open', 'High', 'Low', 'Close', 'Volume'}
        if not required_cols.issubset(self.df.columns):
            raise ValueError(f"Missing columns. Required: {required_cols}")

    def add_moving_averages(self, periods=[10, 20, 50]):
        for period in periods:
            self.df[f"SMA_{period}"] = talib.SMA(self.df['Close'], timeperiod=period)
        return self.df

    def add_rsi(self, period=14):
        self.df["RSI"] = talib.RSI(self.df['Close'], timeperiod=period)
        return self.df

    def add_macd(self):
        macd, signal, hist = talib.MACD(self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        self.df["MACD"] = macd
        self.df["MACD_Signal"] = signal
        self.df["MACD_Hist"] = hist
        return self.df

    def add_all_indicators(self):
        self.add_moving_averages()
        self.add_rsi()
        self.add_macd()
        return self.df
