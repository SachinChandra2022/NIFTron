# backtesting/backtest_engine.py

import os
import pandas as pd
from backtesting.portfolio import Portfolio

class BacktestEngine:
    def __init__(self, data_dir, strategy_func, start_cash=100000, top_n=10):
        self.data_dir = data_dir
        self.strategy_func = strategy_func
        self.top_n = top_n
        self.portfolio = Portfolio(initial_capital=start_cash)
        self.trades = []

    def load_data(self, symbol):
        file_path = os.path.join(self.data_dir, f"{symbol}.csv")
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.lower()
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.sort_values('timestamp')
        return df

    def run_backtest(self):
        # Get buy signals from the strategy
        signals = self.strategy_func(data_dir=self.data_dir, top_n=self.top_n)

        for _, row in signals.iterrows():
            symbol = row["Symbol"]
            signal_type = row.get("Mean_Reversion_Signal", "Hold")  # e.g., Buy, Sell, Hold

            try:
                df = self.load_data(symbol)
                price = df['close'].iloc[-1]  # Most recent close price

                if signal_type == "Buy":
                    quantity = int(self.portfolio.cash / (self.top_n * price))  # Equal allocation
                    self.portfolio.buy(symbol, price, quantity)

                elif signal_type == "Sell":
                    quantity = self.portfolio.positions.get(symbol, 0)
                    if quantity > 0:
                        self.portfolio.sell(symbol, price, quantity)

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        total_value = self.portfolio.get_total_value(self.get_current_prices(signals))
        return {
            "final_value": total_value,
            "cash_remaining": self.portfolio.cash,
            "positions": self.portfolio.positions,
            "history": self.portfolio.get_history()
        }

    def get_current_prices(self, signals):
        prices = {}
        for _, row in signals.iterrows():
            symbol = row["Symbol"]
            try:
                df = self.load_data(symbol)
                prices[symbol] = df['close'].iloc[-1]
            except:
                prices[symbol] = 0
        return prices