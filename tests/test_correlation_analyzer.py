import unittest
import pandas as pd
from src.correlation_analyzer import CorrelationAnalyzer

class TestCorrelationAnalyzer(unittest.TestCase):

    def setUp(self):
        data = {
            'date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'cleaned_headline': ['stock up', 'market drops', 'buy signal']
        }
        self.news_df = pd.DataFrame(data)
        self.news_df['date'] = pd.to_datetime(self.news_df['date'])

    def test_sentiment_scores(self):
        analyzer = CorrelationAnalyzer(self.news_df)
        analyzer.compute_sentiment_scores()
        self.assertIn('sentiment', analyzer.daily_sentiment.columns)
        self.assertEqual(len(analyzer.daily_sentiment), 3)

    def test_merge_and_correlate(self):
        analyzer = CorrelationAnalyzer(self.news_df)
        analyzer.compute_sentiment_scores()

        stock_data = {
            'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
            'Close': [100, 102, 101]
        }
        stock_df = pd.DataFrame(stock_data)
        stock_df['Date'] = pd.to_datetime(stock_df['Date'])

        merged, corr = analyzer.merge_and_correlate(stock_df)
        self.assertTrue('sentiment' in merged.columns)
        self.assertTrue('return' in merged.columns)
        self.assertIsInstance(corr, float)

if __name__ == '__main__':
    unittest.main()
