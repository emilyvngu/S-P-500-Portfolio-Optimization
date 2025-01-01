import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from modules.data_utils import load_sp500_data  # Assuming this loads SPY data
import os

st.write("Current Working Directory:", os.getcwd())

# Set page title
st.title("Portfolio Visualization")

# Set the header for SPY visualization
st.header("SPY: Growth of $100 Investment")

# Load SPY data

st.write("Current Working Directory:", os.getcwd())

csv_file_path = os.path.abspath("appcode/assets/sp500_raw_data.csv")

try:
    spy = pd.read_csv(csv_file_path, index_col=0, parse_dates=True)
    st.write("Successfully loaded data.")
except FileNotFoundError:
    st.error(f"File not found: {csv_file_path}")
    st.stop()


# Calculate Log Returns, Cumulative Log Returns, Compounded Returns, and Investment Value
spy['Log Returns'] = np.log(spy['Adj Close'] / spy['Adj Close'].shift(1))
spy['Cumulative Log Returns'] = spy['Log Returns'].cumsum()
spy['Compounded Return'] = np.exp(spy['Cumulative Log Returns'])
initial_investment = 100
spy['Investment Value'] = initial_investment * spy['Compounded Return']

# Plot the Investment Value over time using Plotly
fig_spy = go.Figure()
fig_spy.add_trace(go.Scatter(x=spy.index, y=spy['Investment Value'], mode='lines', name='SPY Investment'))
fig_spy.update_layout(
    title="Principal Growth over Time for SPY ($100 Investment)",
    xaxis_title="Time",
    yaxis_title="Investment Value ($)",
    template="plotly_white"
)
st.plotly_chart(fig_spy)

# Set the header for the Equal-Weighted Portfolio visualization
st.header("Magnificent 7: Equal-Weighted Portfolio")

# Define the tickers for the "Magnificent 7"
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA']

# Fetch Adjusted Close prices
data = yf.download(tickers, start='2019-10-01', end='2024-10-01')['Adj Close']

# Calculate Log Returns
log_returns = np.log(data / data.shift(1))

# Define equal weights for the portfolio
weights = np.array([1 / len(tickers)] * len(tickers))

# Calculate weighted log returns for the portfolio
weighted_log_returns = log_returns.dot(weights)

# Calculate cumulative weighted log returns and convert to actual returns
cumulative_weighted_log_returns = weighted_log_returns.cumsum()
compounded_returns = np.exp(cumulative_weighted_log_returns)

# Calculate Investment Value
investment_values = initial_investment * compounded_returns

# Plot the growth of the $100 investment using Plotly
fig_portfolio = go.Figure()
fig_portfolio.add_trace(go.Scatter(x=data.index, y=investment_values, mode='lines', name='Equal-Weighted Portfolio'))
fig_portfolio.update_layout(
    title="Principal Growth: Magnificent 7 Equal-Weighted Portfolio ($100 Investment)",
    xaxis_title="Time",
    yaxis_title="Investment Value ($)",
    template="plotly_white"
)
st.plotly_chart(fig_portfolio)
