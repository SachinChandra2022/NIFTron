import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import list_stock_files, load_stock_data
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import strategy functions
from strategy_modules.momentum_strategy import run_momentum_strategy
from strategy_modules.mean_reversion_strategy import mean_reversion_strategy
from strategy_modules.equal_weight_strategy import get_equal_weight_portfolio
from strategy_modules.ensemble_recommender import ensemble_recommendation

DATA_PATH = "data/nifty50/"

st.set_page_config(page_title="Trading Bot Dashboard", layout="wide")

# Styling (as you had it)
st.markdown("<h1 style='text-align: center;'>Trading Bot Dashboard</h1>", unsafe_allow_html=True)

# --- TABS ---
tabs = st.tabs(["📈 Price Chart", "📊 Recommended Stocks"])

# --- TAB 1: Price Chart ---
with tabs[0]:
    stock_files = list_stock_files()
    selected_stock_file = st.selectbox("Select Stock CSV:", stock_files)

    if selected_stock_file:
        df = load_stock_data(selected_stock_file)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])

        fig = px.line(df, x='timestamp', y='close', title=f"{selected_stock_file} Price Chart")
        st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: Recommended Stocks ---
with tabs[1]:
    st.subheader("Strategy-Based Recommendations")

    if st.button("🔄 Run Strategy Engine"):
        with st.spinner("Running strategies..."):

            momentum_df = run_momentum_strategy(data_dir=DATA_PATH, top_n=10)
            mean_rev_df = mean_reversion_strategy(data_dir=DATA_PATH, top_n=10)
            equal_weight_df = get_equal_weight_portfolio(data_dir=DATA_PATH)
            ensemble_df = ensemble_recommendation(data_dir=DATA_PATH, top_n=10)

            st.success("Strategies executed successfully!")

            st.markdown("### Momentum Strategy (Top 10)")
            st.dataframe(momentum_df)

            st.markdown("### Mean Reversion Strategy (Top 10)")
            st.dataframe(mean_rev_df)

            st.markdown("### Equal Weight Portfolio")
            st.dataframe(equal_weight_df)

            st.markdown("### Final Ensemble Recommendation")
            st.dataframe(ensemble_df)