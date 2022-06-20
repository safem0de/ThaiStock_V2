### 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'

class MplController():

    # __daily = pd.DataFrame()

    def __init__(self) -> None:
        super().__init__()
        # # mpf.plot('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        # self.__daily = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv',index_col=0,parse_dates=True)
        # self.__daily.index.name = 'Date'
        # y = [x.replace('AAPL.','') for x in self.__daily.columns.to_list()]
        # self.__daily.columns = y

    def bind(self, view):
        self.view = view
        self.view.create_view()

    def percentB_belowzero(percentB,price):
        import numpy as np
        signal   = []
        previous = -1.0
        for date,value in percentB.iteritems():
            if value < 0 and previous >= 0:
                signal.append(price[date]*0.99)
            else:
                signal.append(np.nan)
            previous = value
        return signal