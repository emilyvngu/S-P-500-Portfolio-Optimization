import streamlit as st
from streamlit_extras.app_logo import add_logo
import plotly.express as px
from modules.data_utils import load_raw_data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set the header of the page
st.header('Portfolio Visualization: Growth of $100')

spy = load_raw_data()
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


