import pandas as pd
import mplfinance as mpf

### 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'

class MplController():
    def __init__(self) -> None:
        super().__init__()

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

    mpf.plot(daily,type='candle',mav=(3,6,9),volume=True,style='yahoo',title='\nSafem0de')
    mpf.plot(daily,type='renko',volume=True,style='yahoo',title='\nSafem0de')