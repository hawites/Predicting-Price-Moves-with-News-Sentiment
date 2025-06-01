from sklearn.preprocessing import StandardScaler
from typing import Tuple
import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess_data(self, data: pd.DataFrame, target_column: str) -> Tuple[np.ndarray, np.ndarray]:
        if data.empty:
            raise ValueError("Input data is empty.")
        if target_column not in data.columns:
            raise ValueError(f"Target column '{target_column}' not found in data.")

        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        if target_column in numeric_cols:
            numeric_cols.remove(target_column)
        if not numeric_cols:
            raise ValueError("No numeric features found for scaling.")

        X = data[numeric_cols].fillna(data[numeric_cols].mean())
        y = data[target_column].fillna(data[target_column].mean())

        X_scaled = self.scaler.fit_transform(X)
        return X_scaled, y.values

    def preprocess_new_data(self, data: pd.DataFrame) -> np.ndarray:
        if data.empty:
            raise ValueError("Input data is empty.")
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric_cols:
            raise ValueError("No numeric features found for scaling.")

        X = data[numeric_cols].fillna(data[numeric_cols].mean())
        return self.scaler.transform(X)
