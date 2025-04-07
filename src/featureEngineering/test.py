import os
import pandas as pd
from features import apply_all_features

# Folder containing NIFTY 50 stock CSVs
DATA_FOLDER = "data/nifty50/"

def load_csv_data(filepath):
    df = pd.read_csv(filepath)
    
    # Print column names for debugging
    print(f"[i] Columns in {os.path.basename(filepath)}: {df.columns.tolist()}")

    # Auto-detect the datetime column
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
    elif 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
    else:
        raise ValueError("No valid date column ('Date' or 'timestamp') found.")
    
    return df

def main():
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".csv"):
            filepath = os.path.join(DATA_FOLDER, filename)
            try:
                # Load the original data
                df = load_csv_data(filepath)

                # Apply feature engineering
                df_with_features = apply_all_features(df)

                # Save back to the same file (overwrite)
                df_with_features.to_csv(filepath)
                print(f"[✓] Overwritten with features: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    main()