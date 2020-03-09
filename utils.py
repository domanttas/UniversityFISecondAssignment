import pandas as pd

def load(data):
    result = pd.read_csv(data, parse_dates=['Date'])

    return pd.DataFrame(result)