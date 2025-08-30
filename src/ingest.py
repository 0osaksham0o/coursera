import pandas as pd

def load_data(path="data/input.csv"):
    return pd.read_csv(path)
