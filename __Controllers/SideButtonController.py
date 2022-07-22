from __Views.Form import Form
from __Views.Analyse import StockAnalyse
from __Views.Graph import Graph
from __Models.Stocks import Stock
from __Controllers.MplController import CandleController

import pandas as pd

import tkinter as tk

class ButtonController():
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, view:Form, frame:tk.Frame):
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
        data = CandleController()
        a = data.create_graph('PTG','1y')

        window = Graph()
        # window.geometry('+1921+10')
        window.title('Candle Stick')
        window.create_view(a)
        # window.protocol('WM_DELETE_WINDOW',func=lambda: window.destroy())

    def Bibiology_Click(self):
        print('test Bibiology')