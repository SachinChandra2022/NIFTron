# backtesting/metrics.py

import pandas as pd
import numpy as np

def calculate_performance_metrics(portfolio_history, initial_capital):
    df = pd.DataFrame(portfolio_history)
    df['timestamp'] = pd.to_datetime(df['timestamp']) 
    df = df.sort_values('timestamp')

    # Calculate returns
    df["Returns"] = df["Portfolio Value"].pct_change().fillna(0)

    # Total Return
    total_return = (df["Portfolio Value"].iloc[-1] / initial_capital) - 1

    # CAGR
    days = (df.index[-1] - df.index[0]).days
    cagr = (df["Portfolio Value"].iloc[-1] / initial_capital) ** (365.0 / days) - 1

    # Volatility (Standard deviation of daily returns)
    volatility = df["Returns"].std() * np.sqrt(252)

    # Sharpe Ratio (assuming risk-free rate = 0 for simplicity)
    sharpe_ratio = df["Returns"].mean() / df["Returns"].std() * np.sqrt(252)

    # Maximum Drawdown
    cumulative = df["Portfolio Value"].cummax()
    drawdown = (df["Portfolio Value"] - cumulative) / cumulative
    max_drawdown = drawdown.min()

    return {
        "Total Return": total_return * 100,
        "CAGR": cagr * 100,
        "Volatility": volatility * 100,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown * 100
    }