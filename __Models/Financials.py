import json
import pandas as pd
from __Models.Stocks import Stock
from __Controllers.AnalyseController import AnalyseController

class FinancialGrowth:

    # Encapsulation
    DataTable = {}

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
        all_findata = controller.CreateListofFinancial()
        filtered = controller.deleteMinusProfit(all_findata)

        Ast = controller.calculateGrowth(Growth_type='assets',data=filtered)
        Rvn = controller.calculateGrowth(Growth_type='revenue',data=filtered)
        Npf = controller.calculateGrowth(Growth_type='netprofit',data=filtered)
        Roe = controller.calculateGrowth(Growth_type='roe',data=filtered)
        Yld = controller.calculateGrowth(Growth_type='yield',data=filtered)
        self.DataTable = {i:{'data':[i, Ast[i], Rvn[i], Npf[i], Roe[i], Yld[i], str(list(filtered[i]['data']['P/E (เท่า)'].values())[-1]), str(list(filtered[i]['data']['P/BV (เท่า)'].values())[-1])],
                    'ismai': filtered[i]['ismai'],
                    'isSET100': filtered[i]['isSET100'],
                    'isSET50': filtered[i]['isSET50'],}
                for i in filtered}

        json_object = json.dumps(self.DataTable, indent = 4) 
        print(json_object)
        
    #Getters
    def getDataTable(self):
        return self.DataTable

    def getMarket_Stat_SET(self):
        return self.Market_Stat.get('SET')

    def getMarket_Stat_mai(self):
        return self.Market_Stat.get('mai')

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