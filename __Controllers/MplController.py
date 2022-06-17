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
    print(y)
    daily.columns = y
    daily.shape
    daily.head(3)
    daily.tail(3)

    print(daily.head(3))

    exp12 = daily['Close'].ewm(span=12, adjust=False).mean()
    exp26 = daily['Close'].ewm(span=26, adjust=False).mean()

    macd = exp12 - exp26

    signal    = macd.ewm(span=9, adjust=False).mean()
    histogram = macd - signal

    apds = [mpf.make_addplot(exp12,color='lime'),
        mpf.make_addplot(exp26,color='c'),
        mpf.make_addplot(histogram,type='bar',width=0.7,panel=1,
                         color='dimgray',alpha=1,secondary_y=False),
        mpf.make_addplot(macd,panel=1,color='fuchsia',secondary_y=True),
        mpf.make_addplot(signal,panel=1,color='b',secondary_y=True),

        mpf.make_addplot(signal,panel=1,type='scatter',markersize=100,marker='^')
       ]

    mpf.plot(daily,type='candle',mav=(3,6,9),
            volume=True, volume_panel=2, panel_ratios=(6,3,2), 
            style='yahoo', title='\nSafem0de', 
            addplot=apds, figscale=1.0, figratio=(10,5))
    mpf.plot(daily,type='renko',volume=True,style='yahoo',title='\nSafem0de')