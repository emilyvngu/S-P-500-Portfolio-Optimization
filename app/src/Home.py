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
