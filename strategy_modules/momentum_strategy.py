import os
import pandas as pd
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.featureEngineering.momentum_features import calculate_momentum_score

def run_momentum_strategy(symbol=None, data_dir="data/nifty50", top_n=10):
    records = []

    # If a single stock is passed (e.g., "RELIANCE.NS")
    if symbol:
        file_path = os.path.join(data_dir, f"{symbol}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found.")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()  # Clean up any leading/trailing whitespace
        if 'close' not in df.columns:
            raise KeyError(f"'close' column not found in {file_path}")
        df['close'] = pd.to_numeric(df['close'], errors='coerce')
        df.dropna(subset=['close'], inplace=True)
        features = calculate_momentum_score(df)
        return pd.DataFrame([{
            "Symbol": symbol,
            "momentum_score": (features["return_126"] + features["return_63"]) / 2  # or any logic
        }])

    # Else: loop through all CSVs in directory
    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            symbol = file.replace(".csv", "")
            file_path = os.path.join(data_dir, file)

            try:
                df = pd.read_csv(file_path)
                df.columns = df.columns.str.strip()
                if 'close' not in df.columns:
                    raise KeyError(f"'close' column not found in {symbol}")
                df['close'] = pd.to_numeric(df['close'], errors='coerce')
                df.dropna(subset=['close'], inplace=True)

                if len(df) >= 130:
                    features = calculate_momentum_score(df)
                    records.append({
                        "Symbol": symbol,
                        "6M_Return": features["6M_Return"].iloc[-1],
                        "3M_Return": features["3M_Return"].iloc[-1],
                        "Volatility": features["volatility_20"].iloc[-1]
                    })
            except Exception as e:
                print(f"Skipping {symbol} due to error: {e}")

    result_df = pd.DataFrame(records).dropna()

    result_df["return_score"] = result_df[["6M_Return", "3M_Return"]].mean(axis=1)
    result_df["volatility_rank"] = result_df["Volatility"].rank(ascending=True)
    result_df["momentum_rank"] = result_df["return_score"].rank(ascending=False)
    result_df["momentum_score"] = result_df[["momentum_rank", "volatility_rank"]].mean(axis=1)

    top_stocks = result_df.sort_values("momentum_score").head(top_n)
    return top_stocks[["Symbol", "momentum_score"]]