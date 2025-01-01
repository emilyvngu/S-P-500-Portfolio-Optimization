##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# Title and Introduction
st.title("Portfolio Optimization and Backtesting")
st.write("""
This app processes S&P 500 stock data, calculates portfolio metrics, and provides visualizations for portfolio analysis.
""")

# Fixed date range for simplicity
start_date = '2020-01-01'
end_date = '2023-01-01'

# Step 1: Fetch S&P 500 Tickers
st.write("Fetching S&P 500 tickers...")
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_table = pd.read_html(url)[0]
tickers = sp500_table['Symbol'].to_list()
st.success(f"Successfully fetched {len(tickers)} tickers.")

# Step 2: Download Adjusted Close Prices
st.write(f"Downloading stock data from {start_date} to {end_date}...")
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

if data.empty:
    st.error("No data fetched. Please check the tickers or internet connection.")
else:
    st.success("Data downloaded successfully.")

    # Step 3: Clean Data
    st.write("Cleaning data...")
    failed_tickers = data.columns[data.isna().mean() > 0.5].tolist()
    data = data.drop(columns=failed_tickers)
    data = data.ffill().bfill().dropna()

    st.write(f"Removed {len(failed_tickers)} tickers with more than 50% missing data.")
    st.success("Data cleaned successfully.")

    # Step 4: Compute Log Returns, mu, and Covariance Matrix
    st.write("Calculating log returns and portfolio metrics...")
    log_returns = np.log(data / data.shift(1)).dropna()
    mu = log_returns.mean()
    cov_matrix = log_returns.cov()
    st.success("Metrics calculated successfully!")

    # Step 5: Visualize Results
    st.write("## Visualizations")

    # Stock Prices Visualization
    st.write("### Stock Prices Over Time")
    st.line_chart(data)

    # Portfolio Expected Returns
    st.write("### Expected Returns (mu)")
    st.dataframe(mu)

    # Covariance Matrix
    st.write("### Covariance Matrix Sample")
    st.dataframe(cov_matrix.iloc[:5, :5])

    # Portfolio Growth Simulation
    st.write("### Simulated Portfolio Growth")
    initial_investment = 100
    cumulative_returns = (np.exp(log_returns.cumsum()) * initial_investment).dropna()
    st.line_chart(cumulative_returns)