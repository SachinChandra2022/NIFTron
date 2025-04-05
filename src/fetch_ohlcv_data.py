# import requests
# import pandas as pd
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()
# API_KEY = os.getenv("FINNHUB_API_KEY")

# def fetch_ohlcv(symbol, resolution="1"):
#     url = "https://finnhub.io/api/v1/stock/candle"
#     to_time = int(time.time())
#     from_time = to_time - 3600  # last 1 hour

#     params = {
#         "symbol": symbol,
#         "resolution": resolution,
#         "from": from_time,
#         "to": to_time,
#         "token": API_KEY
#     }

#     res = requests.get(url, params=params)
#     data = res.json()

#     if data.get("s") != "ok":
#         print(f"❌ Error fetching for {symbol}")
#         return None

#     df = pd.DataFrame({
#         "timestamp": pd.to_datetime(data["t"], unit='s'),
#         "open": data["o"],
#         "high": data["h"],
#         "low": data["l"],
#         "close": data["c"],
#         "volume": data["v"]
#     })

#     return df



import yfinance as yf
import pandas as pd

def fetch_ohlcv(symbol, interval="1m", period="1d"):
    print(f"🔄 Fetching OHLCV for {symbol} using yfinance...")

    try:
        df = yf.download(tickers=symbol, interval=interval, period=period, progress=False)

        if df.empty:
            print(f"❌ No data found for {symbol}")
            return None

        df.reset_index(inplace=True)
        df = df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
            "Datetime": "timestamp"  # Some versions of yfinance return 'Datetime'
        })

        df = df[["timestamp", "open", "high", "low", "close", "volume"]]
        return df

    except Exception as e:
        print(f"❌ Error fetching data for {symbol}: {e}")
        return None