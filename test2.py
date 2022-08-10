import json
import pprint
import yfinance as yf

ticker_object = yf.Ticker('AOT.BK')

analyse = ticker_object.analysis
bal_sheet = ticker_object.balancesheet
cashflow = ticker_object.cashflow
stock_news = ticker_object.get_news()


# print(analyse)
# print(bal_sheet)
# print(cashflow)
for i in stock_news:
    print(i)


# from googlefinance import getQuotes
# import json                                                                                                
# print(json.dumps(getQuotes('AAPL'), indent=2))