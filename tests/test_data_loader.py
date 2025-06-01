import unittest
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data_success(self):
        loader = DataLoader('../data/raw_analyst_ratings.csv')
        df = loader.load_data()
        self.assertIsNotNone(df)

    def test_load_data_file_not_found(self):
        loader = DataLoader('../data/nonexistent.csv')
        with self.assertRaises(FileNotFoundError):
            loader.load_data()