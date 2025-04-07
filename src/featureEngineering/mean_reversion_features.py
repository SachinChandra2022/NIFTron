import pandas as pd
import numpy as np

def add_rolling_stats(df, window=20):
    """
    Adds rolling mean and std deviation to calculate z-score.
    """
    df = df.copy()
    df['rolling_mean'] = df['close'].rolling(window=window).mean()
    df['rolling_std'] = df['close'].rolling(window=window).std()
    df['z_score'] = (df['close'] - df['rolling_mean']) / df['rolling_std']
    return df

def add_bollinger_bands(df, window=20, num_std=2):
    """
    Adds Bollinger Bands to the DataFrame.
    """
    df = df.copy()
    rolling_mean = df['close'].rolling(window=window).mean()
    rolling_std = df['close'].rolling(window=window).std()

    df['boll_upper'] = rolling_mean + num_std * rolling_std
    df['boll_lower'] = rolling_mean - num_std * rolling_std

    return df

# mean_reversion_features.py

def add_mean_reversion_features(df, window=20):
    df["rolling_mean"] = df["close"].rolling(window=window).mean()
    df["rolling_std"] = df["close"].rolling(window=window).std()
    df["z_score"] = (df["close"] - df["rolling_mean"]) / df["rolling_std"]
    return df