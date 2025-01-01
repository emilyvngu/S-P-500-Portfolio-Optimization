import pandas as pd
import os

def load_sp500_data(filepath='src/assets/sp500_data.csv'):
    """
    Load S&P 500 data from the CSV file.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        DataFrame: Cleaned DataFrame with adjusted closing prices.
    """
    try:
        data = pd.read_csv(filepath, index_col=0, parse_dates=True)
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None


def load_mu_cov_data():
    mu = pd.read_csv('app/src/assets/sp500_expected_returns.csv', index_col=0, squeeze=True)
    cov_matrix = pd.read_csv('app/src/assets/sp500_covariance_matrix.csv', index_col=0)
    return mu, cov_matrix