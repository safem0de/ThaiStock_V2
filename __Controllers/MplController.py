### 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from __Models import Stocks

class CandleController():

    def __init__(self) -> None:
        super().__init__()

    def bind(self, model:Stocks, view,):
        self.view = view
        self.view.create_view(self, model,)

    def create_graph_longterm(self, st_Name:str, period:str) -> pd.DataFrame:
        __df = pd.DataFrame()
        try:
            ### https://aroussi.com/post/python-yahoo-finance
            ### period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
            ticker = yf.Ticker(st_Name.replace('%26','&').replace(' ','-').upper())
            __df = ticker.history(period=period)
            __df.Name = st_Name.upper()
        except Exception as e:
            print('err: ',e)

        return __df

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    def create_graph_shorterm(self, st_Name:str, interval:str) -> pd.DataFrame:
        __df = pd.DataFrame()
        try:
            ### https://aroussi.com/post/python-yahoo-finance
            ### period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
            ticker = yf.Ticker(st_Name.replace('%26','&').replace(' ','-').upper())
            __df = ticker.history(period='5d', interval=interval)
            __df.Name = interval.replace('m', ' minutes')

            # __df = yf.download(tickers=st_Name.replace('%26','&').replace(' ','-').upper(), period='1d', interval='5m')
        except Exception as e:
            print('err: ',e)

        return __df