def normalize_column(df, column):
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df

def fill_missing(df):
    return df.fillna(method="ffill").fillna(method="bfill")