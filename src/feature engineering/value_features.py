def add_price_to_volume_ratio(df):
    df['price_to_volume'] = df['close'] / df['volume']
    return df