import pandas as pd
from src.technical_indicators import TechnicalIndicators

def test_indicators():
    data = {
        'Open': [1, 2, 3, 4, 5] * 10,
        'High': [2, 3, 4, 5, 6] * 10,
        'Low': [1, 1, 2, 3, 4] * 10,
        'Close': [2, 2, 3, 4, 5] * 10,
        'Volume': [1000, 1000, 1000, 1000, 1000] * 10
    }
    df = pd.DataFrame(data)

    ti = TechnicalIndicators(df)
    df_with_indicators = ti.add_all_indicators()

    assert 'RSI' in df_with_indicators.columns
    assert 'MACD' in df_with_indicators.columns
    assert 'SMA_10' in df_with_indicators.columns
