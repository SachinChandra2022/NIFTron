import pandas as pd
from momentum_strategy import run_momentum_strategy
from value_investing import value_investing_strategy
from equal_weight_strategy import get_equal_weight_portfolio

def ensemble_recommendation(data_dir="data/nifty50", top_n=10):
    # Step 1: Get individual strategy results
    momentum_df = run_momentum_strategy(data_dir=data_dir, top_n=50)
    value_df = value_investing_strategy(data_dir=data_dir, top_n=50)
    equal_df = get_equal_weight_portfolio(data_dir=data_dir)

    # Step 2: Merge all on 'Symbol'
    combined_df = pd.merge(momentum_df, value_df, on="Symbol", how="inner")
    combined_df = pd.merge(combined_df, equal_df, on="Symbol", how="inner")

    # Step 3: Normalize ranks (lower is better for momentum and value)
    combined_df["momentum_rank"] = combined_df["momentum_score"].rank(ascending=True)
    combined_df["value_rank"] = combined_df["value_score"].rank(ascending=True)

    # Step 4: Compute final ensemble score
    combined_df["ensemble_score"] = combined_df[["momentum_rank", "value_rank"]].mean(axis=1)

    # Step 5: Sort and return top_n
    final_df = combined_df.sort_values("ensemble_score").head(top_n)

    return final_df[["Symbol", "momentum_score", "value_score", "Weight", "ensemble_score"]]