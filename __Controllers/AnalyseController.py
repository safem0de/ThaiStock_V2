from pyexpat import model
import pandas as pd
from __Models.Stocks import Stock

class AnalyseController():

    def __init__(self, model:Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, model:Stock, view):
        self.view = view
        self.view.create_view(self, model,)

    def setDetails(self):
        df = pd.DataFrame()
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
            },
        }
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
            
            Market_Stat.get('SET').update(
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

            Market_Stat.get('mai').update(
                value = val_mai,
                year_to_date_perc = ytd_mai,
                pe = pe_mai,
                pbv = pbv_mai,
                yield_perc = yield_mai
            )
            return Market_Stat

        except:
            return Market_Stat

    def checkSET100(self):
        df = pd.DataFrame()
        dfSET100 = pd.read_html('https://classic.set.or.th/mkt/sectorquotation.do?sector=SET100'
                    ,match='เครื่องหมาย')
        df = dfSET100[0]
        set100_data = df['หลักทรัพย์'].to_list()
        # print(set100_data)
        for k,v in self.model.getMarket().get('SET').items():
            print(k,v)
            if k in set100_data:
                # print(k,v)
                self.model.getMarket().get('SET').get(k).update(isSET100=True)
            else:
                self.model.getMarket().get('SET').get(k).update(isSET100=False)

        print(self.model.getMarket())

    def checkSET50(self):
        df = pd.DataFrame()
        dfSET50 = pd.read_html('https://classic.set.or.th/mkt/sectorquotation.do?sector=SET50'
                    ,match='เครื่องหมาย')
        df = dfSET50[0]
        set50_data = df['หลักทรัพย์'].to_list()
        # print(set100_data)
        for k,v in self.model.getMarket().get('SET').items():
            print(k,v)
            if k in set50_data:
                # print(k,v)
                self.model.getMarket().get('SET').get(k).update(isSET50=True)
            else:
                self.model.getMarket().get('SET').get(k).update(isSET50=False)

        print(self.model.getMarket())