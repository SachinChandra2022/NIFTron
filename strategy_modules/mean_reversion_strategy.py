import os
import pandas as pd
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.featureEngineering.mean_reversion_features import add_mean_reversion_features

def generate_mean_reversion_score(df):
    """
    Calculates how far price has deviated from the mean.
    Uses Z-score as the metric.
    """
    df = add_mean_reversion_features(df)
    last_row = df.iloc[-1]

    return {
        "z_score": last_row.get("z_score", None),
        "price": last_row.get("close", None)
    }

def mean_reversion_strategy(data_dir="data/nifty50", top_n=10):
    records = []

    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            symbol = file.replace(".csv", "")
            file_path = os.path.join(data_dir, file)

            try:
                df = pd.read_csv(file_path)
                df.columns = df.columns.str.strip()
                df['close'] = pd.to_numeric(df['close'], errors='coerce')
                df.dropna(subset=['close'], inplace=True)

                result = generate_mean_reversion_score(df)
                if result["z_score"] is not None:
                    records.append({
                        "Symbol": symbol,
                        "mean_reversion_score": abs(result["z_score"]),  # Lower = more mean reverting
                        "Signal": "Buy" if result["z_score"] < -1 else "Sell" if result["z_score"] > 1 else "Hold"
                    })

            except Exception as e:
                print(f"Skipping {symbol} due to error: {e}")

    df_result = pd.DataFrame(records)

    if df_result.empty:
        print("No valid data for mean reversion strategy.")
        return pd.DataFrame(columns=["Symbol", "mean_reversion_score"])

    df_result["mean_reversion_rank"] = df_result["mean_reversion_score"].rank(ascending=True)
    df_result = df_result.sort_values("mean_reversion_rank")

    return df_result[["Symbol", "mean_reversion_score"]].head(top_n)