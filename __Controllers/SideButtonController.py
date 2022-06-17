from __Views.Form import Form
from __Views.Analyse import StockAnalyse
from __Models.Stocks import Stock
from __Controllers.MplController import MplController

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
        self.view.buttons["Candle_Stick"].configure(command=lambda: self.Candle_Stick_Click)

        self.view.buttons["Bibiology"].configure(command=self.Bibiology_Click)

    def Stock_NEWS_Click(self):
        print('test NEWS')


    def Stock_Analysis_Click(self):
        window = StockAnalyse()
        window.grab_set()


    def Candle_Stick_Click(self):
        print('test Candle_Stick')
        MplController()



    def Bibiology_Click(self):
        print('test Bibiology')