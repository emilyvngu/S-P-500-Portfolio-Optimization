import pandas as pd
import os
print(f"Current working directory: {os.getcwd()}")

def load_raw_data():
    raw_data = pd.read_csv(os.path.join(os.getcwd(), 'src/assets/sp500_raw_data.csv'), index_col=0, parse_dates=True)
    return raw_data

def load_mu_cov_data():
    mu = pd.read_csv('app/src/assets/sp500_expected_returns.csv', index_col=0, squeeze=True)
    cov_matrix = pd.read_csv('app/src/assets/sp500_covariance_matrix.csv', index_col=0)
    return mu, cov_matrix