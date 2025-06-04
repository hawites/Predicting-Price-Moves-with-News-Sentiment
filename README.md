# 🧠 Predicting Price Moves with News Sentiment

This project explores the relationship between news headlines and stock market movements using natural language processing (NLP), time series analysis, and technical indicators.

---

## 📦 Task 1: News Data Analysis

- Load and inspect raw financial news data
- Clean and preprocess text (headlines, dates, duplicates)
- Visualize distributions, top publishers/stocks, and article frequency
- Perform basic NLP (keyword extraction, topic modeling)
- Analyze trends by publisher and time

---

## 📉 Task 2: Technical Indicators with Stock Data

- Load historical stock data for AAPL, AMZN, GOOG, META, MSFT, NVDA, and TSLA
- Clean and standardize OHLCV data
- Apply TA-Lib (or pandas-ta) indicators:
  - Moving Averages (MA)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
- Visualize and compare indicator signals

---

## 🔄 Task 3: Correlation Analysis

- Compute daily sentiment scores from news using VADER
- Calculate daily stock returns
- Align sentiment and price data by date
- Plot and calculate correlations between sentiment and returns for each stock

---

## 📁 Project Structure

```
├── data/                   # CSV files
├── notebooks/              # Task 1–3 notebooks
├── src/                    # Core Python modules (OOP style)
├── tests/                  # Unit tests
├── requirements.txt
└── README.md
```

---

## ✅ Requirements

- Python 3.10+
- Install dependencies:
```bash
pip install -r requirements.txt
```
Note: `TA-Lib` must be installed manually before running this project. See [TA-Lib installation guide](https://github.com/cgohlke/talib-build/releases).

---


