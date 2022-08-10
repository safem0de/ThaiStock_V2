from __Views.Preference import Preference
from __Views.Form import Form
from __Views.Analyse import StockAnalyse

from __Views.MagicFormula import magicFormula
from __Controllers.AnalyseController import AnalyseController
from __Models.Stocks import Stock

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
        self.view.buttons["Magic_Formula"].configure(command=self.Magic_Formula_Click)
        self.view.buttons["Preferences"].configure(command= self.Preference)
        self.view.buttons["Bibiology"].configure(command=self.Bibiology_Click)

    def Stock_NEWS_Click(self):
        print('test NEWS')


    def Stock_Analysis_Click(self):
        window = StockAnalyse()
        window.create_view(self.model,controller=AnalyseController)


    def Magic_Formula_Click(self):
        try:
            window = magicFormula()
            window.create_view(self.model)
            
        except:
            pass

    def Preference(self):
        try:
            window = Preference()
            window.create_view()
            
        except:
            pass
        

    def Bibiology_Click(self):
        print('test Bibiology')