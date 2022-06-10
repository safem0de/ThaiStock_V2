from __Views.Form import Form
from __Models.Stocks import Stock
import tkinter as tk

class ButtonController():
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, view: Form, frame:tk.Frame, name: str, r:int, c:int):
        self.view = view
        self.view.create_button(frame, name, row=r, column=c)