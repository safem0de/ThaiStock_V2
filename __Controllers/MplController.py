### 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

class CandleController():

    def __init__(self) -> None:
        super().__init__()

    def create_graph(self, st_Name:str) -> pd.DataFrame:
        __df = pd.DataFrame()
        try:
            ### https://aroussi.com/post/python-yahoo-finance
            ### period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
            ticker = yf.Ticker(st_Name.upper() +'.BK')
            __df = ticker.history(period="1y")
            __df.Name = st_Name.upper()
        except Exception as e:
            print(e)
            pass

        return __df

    # def bind(self, view):
    #     self.view = view
    #     self.view.create_view()