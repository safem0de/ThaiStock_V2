from __Models.Stocks import Stock
from __Controllers.AnalyseController import AnalyseController

class FinancialGrowth:

    # Encapsulation
    __data = {
        'data' : [],
        'ismai': None,
        'isSET100': None,
        'isSET50': None,
    }

    Market_Stat = {
            'SET': {
                'value' : 0,
                'year_to_date_perc': 0,
                'pe': 0,
                'pbv' : 0,
                'yield_perc' : 0
            },
            'mai' : {
                'value' : 0,
                'year_to_date_perc': 0,
                'pe': 0,
                'pbv' : 0,
                'yield_perc' : 0
            }
    }

    def __init__(self, model:Stock):
        self.model = model

        controller = AnalyseController(model)
        controller.checkSET100()
        controller.checkSET50()
        # print(self.model.getMarket())
        controller.CreateListofFinancial()
        controller.deleteMinusProfit()

    #Getters
    def getData(self):
        return self.__data['data']

    def getismai(self):
        return self.__data['ismai']

    def getisSET100(self):
        return self.__data['isSET100']

    def getisSET50(self):
        return self.__data['isSET50']

    def getMarket_Stat_SET(self):
        return 

    #Setters
    def setData(self, param:list):
        self.__data['data'] = param

    def setLiabilities(self, param):
        self.__data['ismai'] = param

    def setEquity(self, param):
        self.__data['isSET100'] = param

    def setCapital(self, param):
        self.__data['isSET50'] = param