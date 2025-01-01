import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import plotly.express as px

# set the header of the page
st.header('Portfolio Visualization: Growth of $100')

# Example data
data = {
    "Date": ["2020-01-01", "2020-02-01", "2020-03-01"],
    "SPY": [100, 110, 105],
    "Optimized Portfolio": [100, 112, 108]
}
df = pd.DataFrame(data)

st.header("Portfolio Growth Over Time")
fig = px.line(df, x="Date", y=["SPY", "Optimized Portfolio"], title="Portfolio Growth")
st.plotly_chart(fig)

