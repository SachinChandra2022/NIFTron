import pandas as pd
import os

def list_stock_files(data_dir="data/nifty50"):
    """Returns a list of CSV filenames in the data directory."""
    return [f for f in os.listdir(data_dir) if f.endswith(".csv")]

def load_stock_data(stock_file, data_dir="data/nifty50"):
    """Loads a specific stock CSV file into a DataFrame."""
    file_path = os.path.join(data_dir, stock_file)
    df = pd.read_csv(file_path)
    return df