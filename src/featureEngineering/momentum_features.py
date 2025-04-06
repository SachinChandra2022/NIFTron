import pandas as pd
import numpy as np
import os

def add_price_momentum(df, window=14):
    df[f"momentum_{window}"] = df['close'] - df['close'].shift(window)
    return df

def add_roc(df, window=14):
    df[f"ROC_{window}"] = df['close'].pct_change(periods=window)
    return df

def add_obv(df):
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

    obv = [0]
    for i in range(1, len(df)):
        if df['close'][i] > df['close'][i - 1]:
            obv.append(obv[-1] + df['volume'][i])
        elif df['close'][i] < df['close'][i - 1]:
            obv.append(obv[-1] - df['volume'][i])
        else:
            obv.append(obv[-1])
    df['OBV'] = obv
    return df

def add_daily_returns(df):
    df['daily_return'] = df['close'].pct_change()
    return df

def add_returns(df, periods=[126, 63]):
    if 'close' not in df.columns:
        raise ValueError("The DataFrame must contain a 'close' column.")

    for period in periods:
        col_name = f"{int(period / 21)}M_Return"
        df[col_name] = df['close'].pct_change(period)
    return df

def add_volatility(df, window=14):
    df['daily_return'] = df['close'].pct_change()
    df[f'volatility_{window}'] = df['daily_return'].rolling(window=window).std()
    return df

def add_momentum_score(df):
    df = df.copy()
    df = add_price_momentum(df, window=126)
    df = add_price_momentum(df, window=63)
    df = add_roc(df, window=126)
    df = add_roc(df, window=63)
    df = add_obv(df)
    df = add_daily_returns(df)
    df = add_returns(df)
    df = add_volatility(df, window=14)
    return df

def calculate_momentum_score(df):
    df = df.copy()
    df = add_daily_returns(df)
    df = add_returns(df, periods=[126, 63])
    df = add_volatility(df, window=20)

    # Ensure required columns exist
    if '6M_Return' not in df.columns or '3M_Return' not in df.columns:
        raise ValueError("Missing '6M_Return' or '3M_Return' in DataFrame")

    df = df.dropna(subset=['close', '6M_Return', '3M_Return'])
    return df