import pandas as pd
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
        self.setDetails()
        
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
        return self.Market_Stat.get('SET')

    def getMarket_Stat_mai(self):
        return self.Market_Stat.get('mai')

    #Setters
    def setData(self, param:list):
        self.__data['data'] = param

    def setLiabilities(self, param):
        self.__data['ismai'] = param

    def setEquity(self, param):
        self.__data['isSET100'] = param

    def setCapital(self, param):
        self.__data['isSET50'] = param

    def setDetails(self):
        df = pd.DataFrame()
        try :
            dfstock = pd.read_html('https://portal.settrade.com/C13_MarketSummary.jsp?detail=SET'
                       , match='ค่าสถิติสำคัญและผลการดำเนินงาน')
            df = dfstock[0]
            df = df['ค่าสถิติสำคัญและผลการดำเนินงาน']
            x = list(df.columns)
            x[0] = 'ค่าสถิติสำคัญและผลการดำเนินงาน'
            df.columns = x
            df.set_index('ค่าสถิติสำคัญและผลการดำเนินงาน', inplace=True)
            
            # print(df)
            val_set = df.loc['มูลค่าหลักทรัพย์ตามราคาตลาด. (พันล้านบาท)','SET']
            ytd_set = df.loc['อันตราหมุนเวียนปริมาณการซื้อขาย(YTD)(%)','SET']
            pe_set  = df.loc['P/E (เท่า)','SET']
            pbv_set  = df.loc['P/BV (เท่า)','SET']
            yield_set  = df.loc['อัตราเงินปันผลตอบแทน(%)','SET']
            
            self.Market_Stat.get('SET').update(
                value = val_set,
                year_to_date_perc = ytd_set,
                pe = pe_set,
                pbv = pbv_set,
                yield_perc = yield_set
            )
            # print(Market_Stat)
            val_mai = df.loc['มูลค่าหลักทรัพย์ตามราคาตลาด. (พันล้านบาท)','mai']
            ytd_mai = df.loc['อันตราหมุนเวียนปริมาณการซื้อขาย(YTD)(%)','mai']
            pe_mai  = df.loc['P/E (เท่า)','mai']
            pbv_mai  = df.loc['P/BV (เท่า)','mai']
            yield_mai  = df.loc['อัตราเงินปันผลตอบแทน(%)','mai']

            self.Market_Stat.get('mai').update(
                value = val_mai,
                year_to_date_perc = ytd_mai,
                pe = pe_mai,
                pbv = pbv_mai,
                yield_perc = yield_mai
            )
        except:
            pass