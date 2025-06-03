import unittest
import pandas as pd
from src.eda_analyzer import EDAAnalyzer

class TestEDAAnalyzer(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'headline': ['Stock up', 'Market down'],
            'url': ['http://a.com', 'http://b.com'],
            'publisher': ['News1', 'News2'],
            'date': pd.to_datetime(['2023-01-01', '2023-01-02']),
            'stock': ['AAPL', 'GOOG'],
            'cleaned_headline': ['stock up', 'market down']
        })
        self.eda = EDAAnalyzer(self.df)

    def test_basic_statistics(self):
        self.eda.basic_statistics()  # Should print, no errors

    def test_publisher_analysis(self):
        self.eda.publisher_analysis(top_n=2)  # Should plot, no errors

    def test_time_series_trends(self):
        self.eda.time_series_trends()  # Should plot, no errors

    def test_headline_length_distribution(self):
        self.eda.headline_length_distribution()  # Should plot, no errors

    def test_keyword_frequencies(self):
        self.eda.keyword_frequencies(top_n=5)  # Should print + plot, no errors
