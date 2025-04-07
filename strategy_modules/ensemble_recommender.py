import pandas as pd
from strategy_modules.momentum_strategy import run_momentum_strategy
from strategy_modules.mean_reversion_strategy import mean_reversion_strategy
from strategy_modules.equal_weight_strategy import get_equal_weight_portfolio

def ensemble_recommendation(data_dir="data/nifty50", top_n=10):
    # Step 1: Get individual strategy results
    momentum_df = run_momentum_strategy(data_dir=data_dir, top_n=50)
    mean_reversion_df = mean_reversion_strategy(data_dir=data_dir, top_n=50)
    equal_df = get_equal_weight_portfolio(data_dir=data_dir)

    # Step 2: Merge all on 'Symbol'
    combined_df = pd.merge(momentum_df, mean_reversion_df, on="Symbol", how="inner")
    combined_df = pd.merge(combined_df, equal_df, on="Symbol", how="inner")

    # Step 3: Normalize ranks (lower is better for both strategies)
    combined_df["momentum_rank"] = combined_df["momentum_score"].rank(ascending=True)
    combined_df["mean_reversion_rank"] = combined_df["mean_reversion_score"].rank(ascending=True)

    # Step 4: Compute final ensemble score
    combined_df["ensemble_score"] = combined_df[["momentum_rank", "mean_reversion_rank"]].mean(axis=1)

    # Step 5: Sort and return top_n
    final_df = combined_df.sort_values("ensemble_score").head(top_n)

    return final_df[["Symbol", "momentum_score", "mean_reversion_score", "Weight", "ensemble_score"]]