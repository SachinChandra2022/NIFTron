import os
import pandas as pd
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.featureEngineering.value_features import add_value_features

def calculate_value_score(df):
    """
    Adds value-based metrics and returns the final row's value indicators.
    Skips if any required column is missing.
    """
    required_cols = ['eps', 'book_value']
    if not all(col in df.columns for col in required_cols):
        raise KeyError("Missing one or more required columns: 'eps', 'book_value'")

    df = add_value_features(df)
    last_row = df.iloc[-1]

    return {
        "PE": last_row.get("pe_ratio", None),
        "PB": last_row.get("pb_ratio", None),
        "EY": last_row.get("earnings_yield", None)
    }



def value_investing_strategy(data_dir="data/nifty50", top_n=10):
    records = []

    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            symbol = file.replace(".csv", "")
            file_path = os.path.join(data_dir, file)

            try:
                df = pd.read_csv(file_path)
                df.columns = df.columns.str.strip()
                if 'close' not in df.columns:
                    raise KeyError(f"'close' column missing in {symbol}")
                df['close'] = pd.to_numeric(df['close'], errors='coerce')
                df.dropna(subset=['close'], inplace=True)

                value_scores = calculate_value_score(df)

                records.append({
                    "Symbol": symbol,
                    "PE": value_scores["PE"],
                    "PB": value_scores["PB"],
                    "EY": value_scores["EY"]
                })

            except Exception as e:
                print(f"⚠️ Skipping {symbol} due to error: {e}")

    result_df = pd.DataFrame(records).dropna(subset=["PE", "PB", "EY"])

    if result_df.empty:
        print("🚫 No valid data for value investing strategy.")
        return pd.DataFrame(columns=["Symbol", "value_score"])

    # Invert EY
    result_df["inv_EY"] = 1 / result_df["EY"]
    result_df["value_score"] = result_df[["PE", "PB", "inv_EY"]].mean(axis=1)
    result_df["value_rank"] = result_df["value_score"].rank(ascending=True)

    top_stocks = result_df.sort_values("value_rank").head(top_n)

    return top_stocks[["Symbol", "value_score"]]