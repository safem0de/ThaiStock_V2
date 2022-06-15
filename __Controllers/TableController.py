from __Views.Table import Table
from __Models.Stocks import Stock

class TableController():
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, model:Stock, view:Table, Market:str):
        self.view = view
        self.view.create_view(model, Market)