class FinancialGrowth:

    def __init__(self):
        pass

    # Encapsulation
    __data = {
        'data' : [],
        'ismai': None,
        'isSET100': None,
        'isSET50': None,
    }

    #Getters
    def getData(self):
        return self.__data['data']

    def getismai(self):
        return self.__data['ismai']

    def getisSET100(self):
        return self.__data['isSET100']

    def getisSET50(self):
        return self.__data['isSET50']

    #Setters
    def setData(self, param:list):
        self.__data['data'] = param

    def setLiabilities(self, param):
        self.__data['ismai'] = param

    def setEquity(self, param):
        self.__data['isSET100'] = param

    def setCapital(self, param):
        self.__data['isSET50'] = param