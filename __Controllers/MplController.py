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
            ticker = yf.Ticker(st_Name.upper() +'.BK')
            __df = ticker.history(period="1y")
        except Exception as e:
            print(e)
            pass

        return __df
