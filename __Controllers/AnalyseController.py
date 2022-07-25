from __Models.Stocks import Stock

class AnalyseController():

    def __init__(self, model:Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, model:Stock, view):
        self.view = view
        