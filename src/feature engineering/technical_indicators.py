import pandas as pd
import os
def add_moving_averages(df, windows=[10, 20, 50]):
    for w in windows:
        df[f"SMA_{w}"] = df['close'].rolling(window=w).mean()
    return df

def add_rsi(df, window=14):
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=window).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def add_macd(df, short_window=12, long_window=26, signal_window=9):
    short_ema = df['close'].ewm(span=short_window, adjust=False).mean()
    long_ema = df['close'].ewm(span=long_window, adjust=False).mean()
    df['MACD'] = short_ema - long_ema
    df['MACD_signal'] = df['MACD'].ewm(span=signal_window, adjust=False).mean()
    return df

def add_bollinger_bands(df, window=20):
    sma = df['close'].rolling(window).mean()
    std = df['close'].rolling(window).std()
    df['BB_upper'] = sma + (2 * std)
    df['BB_lower'] = sma - (2 * std)
    return df

def add_volatility(df, window=14):
    df[f"volatility_{window}"] = df['close'].rolling(window).std()
    return df