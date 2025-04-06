import os
import pandas as pd

def get_equal_weight_portfolio(data_dir="data/nifty50"):
    stocks = []

    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            symbol = file.replace(".csv", "")
            stocks.append(symbol)

    if not stocks:
        raise ValueError("No stock files found in the directory.")

    weight = round(1 / len(stocks), 4)
    return pd.DataFrame({
        "Symbol": stocks,
        "Weight": [weight] * len(stocks)
    })