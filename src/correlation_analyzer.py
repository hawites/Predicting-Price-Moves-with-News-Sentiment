import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from dateutil import parser

class CorrelationAnalyzer:
    def __init__(self, news_df: pd.DataFrame):
        self.news_df = news_df.copy()
        self.daily_sentiment = None
        self._setup_vader()

    def _setup_vader(self):
        """Ensure VADER lexicon is downloaded and initialize analyzer."""
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except LookupError:
            nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()

    def safe_parse_date(self, date_str):
        try:
            return parser.parse(str(date_str)).date()
        except Exception:
            return None

    def compute_sentiment_scores(self):
        """Compute sentiment score for each cleaned headline and aggregate daily average."""
        self.news_df['sentiment'] = self.news_df['cleaned_headline'].apply(
            lambda text: self.analyzer.polarity_scores(str(text))['compound']
        )
        self.news_df['date'] = self.news_df['date'].apply(self.safe_parse_date)
        self.news_df.dropna(subset=['date'], inplace=True)

        self.daily_sentiment = (
            self.news_df.groupby('date')['sentiment'].mean().reset_index()
        )

    def merge_and_correlate(self, stock_df: pd.DataFrame):
        """Merge daily sentiment scores with daily stock returns and compute correlation."""
        stock_df = stock_df.copy()
        stock_df['date'] = pd.to_datetime(stock_df['Date']).dt.date
        stock_df['return'] = stock_df['Close'].pct_change()

        merged_df = pd.merge(stock_df, self.daily_sentiment, on='date', how='inner')
        corr = merged_df[['sentiment', 'return']].corr().iloc[0, 1]
        return merged_df, corr
