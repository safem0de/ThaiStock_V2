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

    def create_graph_longterm(self, st_Name:str, period:str, interval='1d') -> pd.DataFrame:
        __df = pd.DataFrame()
        try:
            ### https://aroussi.com/post/python-yahoo-finance
            ### period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
            ticker = yf.Ticker(st_Name.replace('%26','&').replace(' ','-').upper())
            __df = ticker.history(period=period, interval=interval)
            __df.Name = st_Name.upper()
        except Exception as e:
            print('err: ',e)

        return __df

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    def create_graph_shorterm(self, st_Name:str, period='1wk', interval:str='15m') -> pd.DataFrame:
        __df = pd.DataFrame()
        try:
            ### https://aroussi.com/post/python-yahoo-finance
            ### period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
            ticker = yf.Ticker(st_Name.replace('%26','&').replace(' ','-').upper())
            __df = ticker.history(period=period, interval=interval)
            __df.Name = interval.replace('m', ' minutes')

        except Exception as e:
            print('err: ',e)

        return __df

    def Test(self):
        
        try:
            dfz = pd.read_html(
                # 'https://classic.set.or.th/mkt/sectorialindices.do?language=th&country=TH'
                # 'https://classic.set.or.th/mkt/sectorquotation.do?market=SET&sector=FOOD&language=th&country=TH'
                f'https://classic.set.or.th/mkt/sectorialindices.do?market=SET&language=th&country=TH'
                            , match=".+", encoding='utf-8')
            for i in dfz:
                print(i)
        except:
            pass