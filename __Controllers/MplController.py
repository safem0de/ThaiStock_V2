import pandas as pd
import mplfinance as mpf

### 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'

class MplController():
    def __init__(self) -> None:
        super().__init__()

    def percentB_belowzero(percentB,price):
        import numpy as np
        signal   = []
        previous = -1.0
        for date,value in percentB.iteritems():
            if value < 0 and previous >= 0:
                signal.append(price[date]*0.99)
            else:
                signal.append(np.nan)
            previous = value
        return signal

    # mpf.plot('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    daily = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv',index_col=0,parse_dates=True)
    daily.index.name = 'Date'
    y = [x.replace('AAPL.','') for x in daily.columns.to_list()]
    # print(y)
    daily.columns = y
    # daily.shape
    # daily.head(3)
    # daily.tail(3)

    # print(daily.head(3))