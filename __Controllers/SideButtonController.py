from tkinter.messagebox import showerror
from __Views.Form import Form
from __Views.Analyse import StockAnalyse
from __Views.Graph import Graph
from __Views.MagicFormula import magicFormula
from __Controllers.AnalyseController import AnalyseController


from __Models.Stocks import Stock

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
        self.view.buttons["Candle_Stick"].configure(command=lambda:self.Candle_Stick_Click())
        self.view.buttons["Magic_Formula"].configure(command=self.Magic_Formula_Click)
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
            
            window.title('Analysis Mode')
            window.geometry('+21+10')
        except:
            pass

    def Candle_Stick_Click(self):
        name = self.model.getSelected_StockName()
        if not name == None:
            try:
                window = Graph(self.model)
                window.create_view()
                # window.geometry('+1921+10')
                window.geometry('+21+10')
                # window.state('zoomed')
                window.protocol('WM_DELETE_WINDOW',func=lambda: window.destroy())
            except Exception as e:
                print(e)
            
        else:
            showerror(
                'Please select stock',
                'to show the Graphs please select\nกรุณาเลือกหุ้นที่ต้องการ เพื่อแสดงกราฟ 📈📊!!')
            return

    def Bibiology_Click(self):
        print('test Bibiology')