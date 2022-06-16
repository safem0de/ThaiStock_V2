from __Views.Form import Form
from __Models.Stocks import Stock
import tkinter as tk
from tkinter import ttk

class ButtonController():
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, view: Form, frame:tk.Frame,):
        self.view = view
        self.view.create_view(frame)
        self.view.buttons["Stock_NEWS"].configure(command=self.test)

    def test(self):
        print('test')