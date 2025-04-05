def add_price_momentum(df, window=14):
    df[f"momentum_{window}"] = df['close'] - df['close'].shift(window)
    return df

def add_roc(df, window=14):
    df[f"ROC_{window}"] = df['close'].pct_change(periods=window)
    return df

def add_obv(df):
    obv = [0]
    for i in range(1, len(df)):
        if df['close'][i] > df['close'][i-1]:
            obv.append(obv[-1] + df['volume'][i])
        elif df['close'][i] < df['close'][i-1]:
            obv.append(obv[-1] - df['volume'][i])
        else:
            obv.append(obv[-1])
    df['OBV'] = obv
    return df