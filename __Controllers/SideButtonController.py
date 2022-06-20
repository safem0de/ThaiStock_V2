from __Views.Form import Form
from __Views.Analyse import StockAnalyse
from __Views.Graph import Graph
from __Models.Stocks import Stock
from __Controllers.MplController import MplController

import pandas as pd

import tkinter as tk

class ButtonController():
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, view: Form, frame:tk.Frame):
        self.view = view
        self.view.create_view(frame)
        self.view.buttons["Stock_NEWS"].configure(command=self.Stock_NEWS_Click)
        self.view.buttons["Stock_Analysis"].configure(command=self.Stock_Analysis_Click)
        self.view.buttons["Candle_Stick"].configure(command=self.Candle_Stick_Click)

        self.view.buttons["Bibiology"].configure(command=self.Bibiology_Click)

    def Stock_NEWS_Click(self):
        print('test NEWS')


    def Stock_Analysis_Click(self):
        window = StockAnalyse()
        window.grab_set()


    def Candle_Stick_Click(self):

        daily = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv',index_col=0,parse_dates=True)
        daily.index.name = 'Date'
        y = [x.replace('AAPL.','') for x in daily.columns.to_list()]
        # print(y)
        daily.columns = y

        window = Graph()
        window.geometry('+1921+10')
        window.title('Candle Stick')
        window.create_Graph(daily)
        window.grab_set()
        window.update()

        x = window.winfo_toplevel().winfo_reqwidth()

        window2 = Graph()
        window2.geometry(f'+{1921+x+10}+10')
        window2.title('Renko')
        window2.grab_set()

    def Bibiology_Click(self):
        print('test Bibiology')