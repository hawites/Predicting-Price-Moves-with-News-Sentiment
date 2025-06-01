import pandas as pd
import os

class LoadData:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        df = pd.read_csv(self.file_path)
        if df.empty:
            raise ValueError("Loaded data is empty.")
        return df

