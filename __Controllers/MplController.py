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

    # def create_graph(self, st_Name:str,period="1y") -> pd.DataFrame:
    #     __df = pd.DataFrame()
    #     try:
    #         ### https://aroussi.com/post/python-yahoo-finance
    #         ### period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    #         ticker = yf.Ticker(st_Name.upper())
    #         __df = ticker.history(period=period)
    #         __df.Name = st_Name.upper()
    #     except Exception as e:
    #         print(e)
    #         pass

    #     return __df