import os
import sys

# 🔧 Add project root to Python path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backtesting.backtest_engine import BacktestEngine
from backtesting.metrics import calculate_performance_metrics
from strategy_modules.mean_reversion_strategy import mean_reversion_strategy

def main():
    DATA_DIR = "data/nifty50"       # ✅ Directory containing stock CSVs
    INITIAL_CAPITAL = 100000        # ✅ Starting portfolio capital
    TOP_N = 10                      # ✅ Number of top stocks to invest in

    print("\n🎯 Running Mean Reversion Strategy Backtest...")

    # 🚀 Initialize the backtest engine
    engine = BacktestEngine(
        data_dir=DATA_DIR,
        strategy_func=mean_reversion_strategy,
        start_cash=INITIAL_CAPITAL,
        top_n=TOP_N
    )

    # 🏁 Run the backtest and collect results
    results = engine.run_backtest()

    print("\n📈 Portfolio Summary:")
    print(f"Final Portfolio Value: ₹{results['final_value']:.2f}")
    print(f"Cash Remaining: ₹{results['cash_remaining']:.2f}")
    print(f"Positions Held: {results['positions']}")
    print("\n📜 History Columns:")
    print(results["history"])
    # 📊 Calculate performance metrics based on portfolio history
    print("\n📊 Performance Metrics:")
    metrics = calculate_performance_metrics(
        results["history"], 
        initial_capital=INITIAL_CAPITAL
    )
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    main()