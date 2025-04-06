import pandas as pd
import numpy as np
import os
def normalize_column(df, column):
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df

def fill_missing(df):
    return df.fillna(method="ffill").fillna(method="bfill")

import pandas as pd

def clean_stock_data(df):
    # Drop garbage first row if it contains repeated headers or NaNs
    if df.iloc[0].isnull().any() or (df.iloc[0] == df.columns).all():
        df = df[1:]

    # Rename columns to standard format
    df.columns = ["Date", "Open", "High", "Low", "close", "Volume"]

    # Convert data types
    df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
    df["High"] = pd.to_numeric(df["High"], errors="coerce")
    df["Low"] = pd.to_numeric(df["Low"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Drop rows with any remaining NaNs
    df.dropna(inplace=True)

    # Sort by date in ascending order
    df.sort_values("Date", inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df