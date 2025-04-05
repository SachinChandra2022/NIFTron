import time
from api.finnhub_client import client

def get_realtime_quote(ticker):
    quote = client.quote(ticker)
    return {
        "current_price": quote['c'],
        "high": quote['h'],
        "low": quote['l'],
        "open": quote['o'],
        "prev_close": quote['pc'],
        "timestamp": quote['t']
    }

def get_basic_fundamentals(ticker):
    metrics = client.company_basic_financials(ticker, 'all')
    return metrics.get("metric", {})

def get_ohlcv(ticker, resolution="M", _from="1700000000", _to="1705000000"):
    return client.stock_candles(ticker, resolution, int(_from), int(_to))

ticker = "AAPL"

while True:
    print("Realtime Quote:")
    print(get_realtime_quote(ticker))
    print("\nBasic Fundamentals:")
    print(get_basic_fundamentals(ticker))
    time.sleep(5)  # Wait for 5 seconds before the next update