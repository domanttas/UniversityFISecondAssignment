# %%
from utils import load

import matplotlib.pyplot as plt
import pandas as pd


def FI(data, n):
    force_index = pd.Series(data['Close'].diff(
        n) * data['Volume'], name="Force index")
    data = data.join(force_index)
    return data


data = load('data.csv')

data_fi = FI(data, 10)
display_fi = data_fi['Force index']

# %%
data.plot(title='Data', y='Close', x='Date', color='Red')
plt.xlabel('Day')
plt.ylabel('Close')

# %%
display_fi.plot(title='FI', color='Green')
plt.xlabel('Day')
plt.ylabel('Close')


# %%
