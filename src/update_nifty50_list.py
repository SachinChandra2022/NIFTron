import os
import requests
import pandas as pd
from fetch_ohlcv_data import fetch_ohlcv
import time

def update_nifty_list():
    print("🔄 Fetching NIFTY 50 stock list from NSE...")

    url = "https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nseindia.com"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    # Save raw CSV
    raw_csv_path = "data/nifty50_raw.csv"
    with open(raw_csv_path, "wb") as f:
        f.write(response.content)

    # Parse CSV
    df = pd.read_csv(raw_csv_path)
    symbols = df['Symbol'].apply(lambda x: x.strip() + ".NS").tolist()

    # Save cleaned list
    with open("data/nifty50_list.txt", "w") as f:
        for symbol in symbols:
            f.write(symbol + "\n")

    print("✅ NIFTY 50 stock list updated.")
    return symbols

# Auto-fetch OHLCV for all NIFTY 50 stocks
if __name__ == "__main__":
    symbols = update_nifty_list()
    os.makedirs("data/nifty50", exist_ok=True)

    for symbol in symbols:
        df = fetch_ohlcv(symbol)
        if df is not None:
            df.to_csv(f"data/nifty50/{symbol}.csv", index=False)
            print(f"✅ Saved OHLCV for {symbol}")
        time.sleep(2)  # Prevent hitting API rate limits