# 📊 Portfolio Optimization Dashboard

An interactive web app that visualizes and backtests portfolio strategies using historical equity data, rolling window analysis, and constrained mean–variance optimization.

## 🔍 Project Overview

This dashboard provides two key tools:

- **Portfolio Visualization**  
  Compare the growth of $100 invested in SPY (S&P 500 ETF) vs. an equal-weighted Magnificent 7 portfolio (`AAPL`, `MSFT`, `AMZN`, `GOOGL`, `META`, `TSLA`, `NVDA`) using actual market data.

- **Backtesting (Julia)**  
  A rolling-window backtest of a **constrained minimum-variance portfolio** using Julia’s `JuMP` and `COSMO`. The model enforces no short selling, full investment, and a target return constraint, rebalancing monthly and simulating wealth growth over time.

## 🛠️ Tech Stack

- **Python**: pandas, NumPy, yfinance, Plotly, Streamlit
- **Julia**: JuMP, COSMO, MosekTools, DataFrames
- **Visualization**: Streamlit dashboard with interactive charts
- **Data**: S&P 500 price data scraped from Yahoo Finance

## 📁 Key Files

- `/pages/01_Portfolio_Visualization.py`: SPY and Magnificent 7 comparison
- `/pages/03_Backtesting.py`: Julia-powered backtest engine
- `/assets/`: Preprocessed CSVs (log returns, covariances
