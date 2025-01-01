import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import plotly.express as px

# set the header of the page
st.header('Portfolio Visualization: Growth of $100')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

ticker = 'SPY'
spy = yf.download(ticker, start='2019-10-01', end='2024-10-02')
print("original spy data:__________________")
print(spy.head(4))

spy['Log Returns'] = np.log(spy['Adj Close'] / spy['Adj Close'].shift(1))
print("Log Returns spy:____________________")
print(spy.head(4))

spy['Cumulative Log Returns'] = spy['Log Returns'].cumsum()
print("Cumulative Log Returns:_____________________")
print(spy.head(4))

spy['Compounded Return'] = np.exp(spy['Cumulative Log Returns'])
print("Compounded Return:_____________________")
print(spy.head(4))

initial_investment = 100
spy['Investment Value'] = initial_investment * spy['Compounded Return']
print("Investment Value:_____________________")
print(spy.head(4))

# Plot the Investment Value over time
plt.figure(figsize=(10, 6))
plt.plot(spy.index, spy['Investment Value'], label='Principal Growth (SPY)')
plt.title('Principal Growth over Time for SPY')
plt.xlabel('Time')
plt.ylabel('Principal Growth')
plt.legend()
plt.grid(True)
plt.show()

# NEXT GRAPH (1/N) Equal Weights Portfolio"____________________________________________________________________

# Download historical price data for the "Magnificent 7"
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA']
data = yf.download(tickers, start='2019-10-01', end='2024-10-01')['Adj Close']

# Calculate the logarithmic returns for each stock
log_returns = np.log(data / data.shift(1))

# Define equal weights for each stock (assuming equal weighting)
weights = np.array([1/7] * 7)  # Equal weight for each stock
print("weights:", weights)

# Calculate weighted log returns for the equal-weighted portfolio
weighted_log_returns = log_returns.dot(weights)
print("weighted log returns:_____________________")
print(weighted_log_returns.head(4))

# Calculate cumulative weighted log returns
cumulative_weighted_log_returns = weighted_log_returns.cumsum()
print("cumulative weighted log returns:_____________________")
print(cumulative_weighted_log_returns.head(4))

# Convert cumulative log returns to actual returns (compounding)
compounded_returns = np.exp(cumulative_weighted_log_returns)
print("compounded returns:_____________________")
print(compounded_returns.head(4))

# Set the initial investment = $100
initial_investment = 100
investment_values = initial_investment * compounded_returns
print("Investment Values:_____________________")
print(investment_values.head(4))

# Plot the growth of the $100 investment
plt.figure(figsize=(10, 6))
plt.plot(cumulative_weighted_log_returns.index, investment_values, label='Investment Value ($100 Initial)')
plt.title('Principal Growth: Magnificent 7 (Equal-Weighted Portfolio)')
plt.xlabel('Time')
plt.ylabel('Investment Value ($)')
plt.legend()
plt.grid(True)
plt.show()

