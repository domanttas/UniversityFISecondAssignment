#%%
from utils import load

import matplotlib.pyplot as plt
import pandas as pd


def CCI(data, ndays):
    TP = (data['High'] + data['Low'] + data['Close']) / 3

    CCI = pd.Series((TP - TP.rolling(ndays).mean()) /
                    (0.015 * TP.rolling(ndays).std()), name='CCI')
    
    data = data.join(CCI)
    return data

data = load('data.csv')

data_cci = CCI(data, 10)
display_cci = data_cci['CCI']

#%%
data.plot(title='Data', y='Close', x='Date', color='Red')
plt.xlabel('Day')
plt.ylabel('Close')

#%%
display_cci.plot(title='CCI', color='Green')
plt.xlabel('Day')
plt.ylabel('Close')

# %%
