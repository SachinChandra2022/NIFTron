import os
import pandas as pd
import sys

# Add project root to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import strategy modules
from strategy_modules.momentum_strategy import run_momentum_strategy
from strategy_modules.value_investing import value_investing_strategy
from strategy_modules.equal_weight_strategy import get_equal_weight_portfolio
from strategy_modules.ensemble_recommender import ensemble_recommendation

# Optional: Path to your data
DATA_PATH = "data/nifty50/"

def load_stock_data(symbol):
    file_path = os.path.join(DATA_PATH, f"{symbol}.csv")
    return pd.read_csv(file_path)

def test_all_strategies(stock_symbol=None):
    print(f"\n🔎 Running Strategy Analysis...\n")

    if stock_symbol:
        # Test a single symbol if provided
        try:
            df = load_stock_data(stock_symbol)
            print(f"--- Data Loaded for {stock_symbol} ---")
            print(df.head())
        except Exception as e:
            print(f"⚠️ Error loading {stock_symbol}: {e}")
        return

    # Run each full strategy across all NIFTY50 stocks
    print("🚀 Momentum Strategy Results:")
    momentum = run_momentum_strategy(data_dir=DATA_PATH, top_n=10)
    print(momentum)

    print("\n💰 Value Investing Strategy Results:")
    value = value_investing_strategy(data_dir=DATA_PATH, top_n=10)
    print(value)

    print("\n⚖️ Equal Weight Portfolio:")
    weights = get_equal_weight_portfolio(data_dir=DATA_PATH)
    print(weights)

    print("\n📊 Final Ensemble Recommendation:")
    ensemble = ensemble_recommendation(data_dir=DATA_PATH, top_n=10)
    print(ensemble)

if __name__ == "__main__":
    # Pass stock_symbol="RELIANCE.NS" to test a single stock CSV
    test_all_strategies()  # Run full strategy test on all stocks