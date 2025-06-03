import unittest
import pandas as pd
from src.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'headline': ['Stock soars', 'Market falls'],
            'url': ['http://a.com', 'http://b.com'],
            'publisher': ['News1', 'News2'],
            'date': ['2023-01-01 10:00:00', '2023-01-02 12:00:00'],
            'stock': ['AAPL', 'GOOG']
        })
        self.dm = DataManager(None)
        self.dm.df = self.sample_data.copy()

    def test_load_data_file_not_found(self):
        dm = DataManager("nonexistent.csv")
        self.assertIsNone(dm.load_data())

    def test_clean_data(self):
        cleaned = self.dm.clean_data()
        self.assertIn('cleaned_headline', cleaned.columns)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned['date']))

    def test_safe_parse_date(self):
        result = self.dm.safe_parse_date("2023-01-01 10:00:00")
        self.assertIsInstance(result, pd.Timestamp)
        result_invalid = self.dm.safe_parse_date("invalid date")
        self.assertTrue(pd.isna(result_invalid))
