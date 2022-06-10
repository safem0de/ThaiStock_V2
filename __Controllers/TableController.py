from __Views.Table import Table
from __Models.Stocks import Stock

class TableController():
    def __init__(self) -> None:
        super().__init__()

    def bind(self, view: Table):
        self.view = view
        self.view.create_view()
        self.view.create_button()