import pandas as pd
import os

class StockDataCleaner:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load_file(self, filename):
        file_path = os.path.join(self.folder_path, filename)
        try:
            df = pd.read_csv(file_path)
            print(f"✅ Loaded {filename} successfully.")
            return df
        except FileNotFoundError:
            print(f" File not found: {filename}")
            return None
        except pd.errors.EmptyDataError:
            print(f" Empty file: {filename}")
            return None
        except pd.errors.ParserError:
            print(f" Parser error in file: {filename}")
            return None
        except Exception as e:
            print(f" Unexpected error loading {filename}: {e}")
            return None

    def observe_data(self):
        files = [f for f in os.listdir(self.folder_path) if f.endswith('.csv')]
        for file in files:
            df = self.load_file(file)
            if df is None:
                continue

            print(f"\n📊 Observing {file}...")
            print(df.info())
            print(df.head())
            print(df.describe())

            # Check for missing values
            missing = df.isnull().sum()
            print(f"🔍 Missing Values:\n{missing}")

            # Check for duplicate rows
            duplicates = df.duplicated(subset='Date').sum()
            if duplicates > 0:
                print(f" Found {duplicates} duplicate rows based on 'Date'.")
            else:
                print("✅ No duplicate rows based on 'Date'.")

            print("-" * 50)

   