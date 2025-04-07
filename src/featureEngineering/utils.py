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


def add_technical_indicators(df):
    
    df.set_index('timestamp', inplace=True)
    df['SMA_10'] = df['close'].rolling(window=10).mean()
    df['SMA_20'] = df['close'].rolling(window=20).mean()

    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    exp1 = df['close'].ewm(span=12, adjust=False).mean()
    exp2 = df['close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

    df['Daily_Return'] = df['close'].pct_change()
    df['ROC'] = df['close'].pct_change(periods=10)

    df['Volatility_10'] = df['close'].rolling(window=10).std()

    sma_20 = df['close'].rolling(window=20).mean()
    std_20 = df['close'].rolling(window=20).std()
    df['BB_Upper'] = sma_20 + (2 * std_20)
    df['BB_Lower'] = sma_20 - (2 * std_20)

    return df