from abc import ABC, abstractmethod
from __Views.MainMenu import Form, View, Table
from __Models.Stocks import Stock
import tkinter as tk


class Controller(ABC):
    @abstractmethod
    def bind(view: View):
        raise NotImplementedError


class TableController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def bind(self, view: Table):
        self.view = view
        self.view.create_view()
        self.view.create_button()


class ButtonController(Controller):
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, view: Form, frame:tk.Frame, name: str, r:int, c:int):
        self.view = view
        self.view.create_button(frame, name, row=r, column=c)