class Stock:

    def __init__(self):
        pass
    
    __MarketSET = {}

    def getMarketData(self):
        return self.__MarketSET

    def setMarketData_SET(self, name, data):
        self.__MarketSET[name] = data