import streamlit as st

st.header('Backtesting Results: Performance Metrics')
 
metrics = {
    "Portfolio": ["SPY", "Optimized Portfolio"],
    "Total Return (%)": [10, 12],
    "Annualized Volatility (%)": [15, 13],
    "Sharpe Ratio": [0.67, 0.92],
    "Max Drawdown (%)": [-20, -18]
}
metrics_df = pd.DataFrame(metrics)

st.header("Backtesting Results")
st.write("Performance metrics for each portfolio:")
st.dataframe(metrics_df)
