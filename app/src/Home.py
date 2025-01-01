##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

st.title("Portfolio Optimization and Backtesting Project")
st.write("""
Welcome to this interactive app showcasing portfolio optimization and backtesting techniques.
- **Goal**: Compare SPY vs. an optimized portfolio.
- **Methods**: Data analysis, financial modeling, and optimization.
- **Tools**: Python, Streamlit, financial APIs, CVXPY.
Explore the sections below to see visualizations, results, and more!
""")

if st.sidebar.button("Get Random Ticker"):
    st.write("5")

import nav
page = nav.navigation()
if page == "Visualization":
    import pages.01_Portfolio_Visualization
elif page == "Backtesting":
    import pages.03_Backtesting
