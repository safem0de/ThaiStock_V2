class StockDetail:

    def __init__(self):
        pass

    #private members
    __StockName = ""
    __Remark = ""
    __OpenPrice = 0.00
    __HighPrice = 0.00
    __LowPrice = 0.00
    __CurrentPrice = 0.00
    __Change = 0.00
    __PercentChange = 0.00
    __OfferPrice = 0.00
    __SalePrice = 0.00
    __Volume = 0.00
    __Value = 0.00
    __Message = ""

    #Getters
    def getStockName(self):
        return self.__StockName

    def getRemark(self):
        return self.__Remark

    def getOpenPrice(self):
        return self.__OpenPrice

    def getHighPrice(self):
        return self.__HighPrice

    def getLowPrice(self):
        return self.__LowPrice

    def getCurrentPrice(self):
        return self.__CurrentPrice

    def getChage(self):
        return self.__Change

    def getPercenChange(self):
        return self.__PercentChange

    def getOfferPrice(self):
        return self.__OfferPrice

    def getSalePrice(self):
        return self.__SalePrice

    def getVolume(self):
        return self.__Volume

    def getValue(self):
        return self.__Value

    def getMessage(self):
        return self.__Message

    #setter
    def setStockName(self, param):
        self.__StockName = param

    def setRemark(self, param):
        self.__Remark = param
    
    def setOpenPrice(self, param):
        self.__OpenPrice = param

    def setHighPrice(self, param):
        self.__HighPrice = param

    def setLowPrice(self, param):
        self.__LowPrice = param

    def setCurrentPrice(self, param):
        self.__CurrentPrice = param

    def setChange(self, param):
        self.__Change = param

    def setPercentChange(self, param):
        self.__PercentChange = param

    def setOfferPrice(self, param):
        self.__OfferPrice = param

    def setSalePrice(self, param):
        self.__SalePrice = param

    def setVolume(self, param):
        self.__Volume = param

    def setValue(self, param):
        self.__Volume = param

    def setMessage(self, param):
        self.__Message = param