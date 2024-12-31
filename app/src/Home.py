##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

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



