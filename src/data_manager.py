import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from dateutil import parser

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"✅ Data loaded successfully with shape: {self.df.shape}")
        except FileNotFoundError:
            print(f" File not found: {self.file_path}")
        return self.df

    def observe_data(self):
        if self.df is not None:
            print("\n🔍 Data Types:")
            print(self.df.dtypes)
            print("\n🔍 Missing Values:")
            print(self.df.isnull().sum())
            print("\n🔍 Descriptive Statistics (Numerical):")
            print(self.df.describe(include=[np.number]))
            print("\n🔍 Descriptive Statistics (Textual):")
            print(self.df.describe(include=[object]))
            print("\n🔍 Unique Values per Column:")
            for col in self.df.columns:
                print(f"- {col}: {self.df[col].nunique()} unique values")
            print("\n🔍 Sample Rows:")
            print(self.df.head())
        else:
            print(" DataFrame is empty. Please load the data first.")

    def plot_missing_values(self):
        if self.df is not None:
            if self.df.isnull().values.any() and self.df.shape[0] > 1 and self.df.shape[1] > 1:
                msno.heatmap(self.df)
                plt.title("Missing Values Heatmap")
                plt.show()
            else:
                print("✅ No missing values detected or insufficient data for heatmap.")
        else:
            print(" DataFrame is empty. Please load the data first.")

    def plot_headline_length_distribution(self):
        if self.df is not None and 'headline' in self.df.columns:
            self.df['headline_length'] = self.df['headline'].astype(str).apply(len)
            sns.histplot(self.df['headline_length'], bins=50)
            plt.title("Headline Length Distribution")
            plt.xlabel("Length of Headline")
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(" 'headline' column not found or DataFrame is empty.")

    def plot_top_publishers(self, n=10):
        if self.df is not None and 'publisher' in self.df.columns:
            top_publishers = self.df['publisher'].value_counts().head(n)
            sns.barplot(x=top_publishers.values, y=top_publishers.index)
            plt.title(f"Top {n} Publishers")
            plt.xlabel("Number of Articles")
            plt.ylabel("Publisher")
            plt.show()
        else:
            print(" 'publisher' column not found or DataFrame is empty.")

    def plot_top_stocks(self, n=10):
        if self.df is not None and 'stock' in self.df.columns:
            top_stocks = self.df['stock'].value_counts().head(n)
            sns.barplot(x=top_stocks.values, y=top_stocks.index)
            plt.title(f"Top {n} Stocks")
            plt.xlabel("Number of Articles")
            plt.ylabel("Stock")
            plt.show()
        else:
            print("❌ 'stock' column not found or DataFrame is empty.")

    def plot_publication_trends(self):
        if self.df is not None and 'date' in self.df.columns:
            self.df['date_parsed'] = pd.to_datetime(self.df['date'], errors='coerce')
            trend = self.df['date_parsed'].dt.date.value_counts().sort_index()
            trend.plot(figsize=(12, 6))
            plt.title("Number of Articles Over Time")
            plt.xlabel("Date")
            plt.ylabel("Number of Articles")
            plt.show()
        else:
            print(" 'date' column not found or DataFrame is empty.")

    def plot_publication_hour_distribution(self):
        if self.df is not None and 'date' in self.df.columns:
            self.df['date_parsed'] = pd.to_datetime(self.df['date'], errors='coerce')
            self.df['hour'] = self.df['date_parsed'].dt.hour
            sns.histplot(self.df['hour'].dropna(), bins=24)
            plt.title("Publication Time of Day")
            plt.xlabel("Hour")
            plt.ylabel("Number of Articles")
            plt.show()
        else:
            print(" 'date' column not found or DataFrame is empty.")
    @staticmethod
    def safe_parse_date(date_str):
        try:
            return parser.parse(date_str)
        except Exception:
            return pd.NaT
    def clean_data(self):
        if self.df is not None:
            print("\n🧹 Cleaning data...")

            self.df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)

            before = self.df.shape[0]
            self.df.drop_duplicates(subset=['headline', 'date', 'stock'], inplace=True)
            after = self.df.shape[0]
            print(f"✅ Removed {before - after} duplicate rows.")

            # Apply safe date parsing
            self.df['date'] = self.df['date'].astype(str).apply(self.safe_parse_date)

            self.df['cleaned_headline'] = self.df['headline'].astype(str).apply(
                lambda x: re.sub(r"[^a-zA-Z\s]", "", x).lower().strip()
            )

            print("✅ Cleaned headlines and parsed dates.")
            missing = self.df.isnull().sum()
            print("\n🔍 Missing Values After Cleaning:")
            print(missing)

            return self.df
        else:
            print(" DataFrame is empty. Please load the data first.")

