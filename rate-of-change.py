# %%
from utils import load

import matplotlib.pyplot as plt
import pandas as pd


def ROC(data, n):
    difference = data['Close'].diff(n)
    previous = data['Close'].shift(n)
    rate_of_change = pd.Series(difference/previous, name='Rate of change')

    data = data.join(rate_of_change)
    return data


data = load('data.csv')

data_roc = ROC(data, 10)
display_roc = data_roc['Rate of change']

# %%
data.plot(title='Data', y='Close', x='Date', color='Red')
plt.xlabel('Day')
plt.ylabel('Close')

# %%
display_roc.plot(title='ROC', color='Green')
plt.xlabel('Day')
plt.ylabel('Close')

# %%
