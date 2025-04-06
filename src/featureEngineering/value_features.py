import pandas as pd

def add_price_to_volume_ratio(df):
    """
    Adds price-to-volume ratio feature to the DataFrame.
    """
    df['price_to_volume'] = df['close'] / df['volume']
    return df

def add_value_features(df):
    """
    Adds basic value investing features to the DataFrame.
    Assumes df contains 'close', 'eps', and 'book_value' columns.

    Returns:
        DataFrame with new columns: 'pe_ratio', 'pb_ratio', 'earnings_yield'
    """
    df = df.copy()

    # Ensure numeric conversions
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df["eps"] = pd.to_numeric(df["eps"], errors="coerce")
    df["book_value"] = pd.to_numeric(df["book_value"], errors="coerce")

    # P/E Ratio: Price / Earnings Per Share
    df["pe_ratio"] = df["close"] / df["eps"]

    # P/B Ratio: Price / Book Value Per Share
    df["pb_ratio"] = df["close"] / df["book_value"]

    # Earnings Yield: EPS / Price (inverse of PE)
    df["earnings_yield"] = df["eps"] / df["close"]

    return df