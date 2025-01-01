import streamlit as st
import numpy as np

st.title('Optimization: User-Defined Constraints')

st.header("Portfolio Optimization")
max_weight = st.slider("Maximum Weight per Asset (%)", 0, 100, 20) / 100
expected_return = st.number_input("Minimum Expected Return (%)", value=5) / 100

# Perform optimization (mock example)
optimized_weights = np.random.dirichlet(np.ones(5), size=1)[0] * max_weight
st.write("Optimized Weights:", optimized_weights)
