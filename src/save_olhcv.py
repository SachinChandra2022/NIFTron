import os
import pandas as pd
from fetch_ohlcv_data import fetch_ohlcv

def save_ohlcv(symbol):
    new_df = fetch_ohlcv(symbol)

    if new_df is None:
        return

    file_path = f"data/nifty50/{symbol}.csv"

    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        combined_df = pd.concat([existing_df, new_df]).drop_duplicates(subset="timestamp")
    else:
        combined_df = new_df

    combined_df.sort_values("timestamp", inplace=True)
    combined_df.to_csv(file_path, index=False)
    print(f"💾 Saved: {symbol}")