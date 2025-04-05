from fetch_ohlcv_data import fetch_ohlcv
import os
import time

def fetch_and_save_all_ohlcv():
    print("📦 Fetching OHLCV for NIFTY 50")
    with open("data/nifty50_list.txt", "r") as file:
        symbols = [line.strip() for line in file]

    os.makedirs("data/nifty50", exist_ok=True)

    for symbol in symbols:
        df = fetch_ohlcv(symbol)
        if df is not None:
            df.to_csv(f"data/nifty50/{symbol}.csv", index=False)
            print(f"✅ Saved {symbol}")
        time.sleep(2)  # Avoid hitting API rate limits
if __name__ == "__main__":
    fetch_and_save_all_ohlcv()
 