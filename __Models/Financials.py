import json
from statistics import mean
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
                'yield_perc' : 0,
                'avg_asset': 0,
                'avg_revenue': 0,
                'avg_netprofit': 0,
                'avg_roe' : 0,
                'avg_yield' : 0
            },
            'mai' : {
                'value' : 0,
                'year_to_date_perc': 0,
                'pe': 0,
                'pbv' : 0,
                'yield_perc' : 0,
                'avg_asset': 0,
                'avg_revenue': 0,
                'avg_netprofit': 0,
                'avg_roe' : 0,
                'avg_yield' : 0
            }
        }

    def __init__(self, model:Stock):
        self.model = model
        self.setDetails()
        
        controller = AnalyseController(model)
        controller.checkSET100()
        controller.checkSET50()
        
        all_findata = controller.CreateListofFinancial()
        filtered = controller.deleteMinusProfit(all_findata)

        Ast = controller.calculateGrowth(Growth_type='assets',data=filtered)
        Rvn = controller.calculateGrowth(Growth_type='revenue',data=filtered)
        Npf = controller.calculateGrowth(Growth_type='netprofit',data=filtered)
        Roe = controller.calculateGrowth(Growth_type='roe',data=filtered)
        Yld = controller.calculateGrowth(Growth_type='yield',data=filtered)
        self.DataTable = {i:{'data':
                            [   i,
                                Ast[i],
                                Rvn[i],
                                Npf[i],
                                Roe[i], 
                                Yld[i], 
                                str(list(filtered[i]['data']['P/E (เท่า)'].values())[-1]),
                                str(list(filtered[i]['data']['P/BV (เท่า)'].values())[-1])
                            ],
                    'ismai': filtered[i]['ismai'],
                    'isSET100': filtered[i]['isSET100'],
                    'isSET50': filtered[i]['isSET50'],}
                for i in filtered}

        # json_object = json.dumps(self.DataTable, indent = 4) 
        # print(json_object)
        self.setAverageValue()
        
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
                yield_perc = yield_set,
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
                yield_perc = yield_mai,
            )
        except:
            pass

    def setAverageValue(self):
        if self.DataTable:
            try:
                __assets_mai = mean([self.DataTable[j]['data'][1] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_assets_mai = round(__assets_mai,3)
                self.Market_Stat.get('mai').update(avg_asset = avg_assets_mai)

                __revenue_mai = mean([self.DataTable[j]['data'][2] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_revenue_mai = round(__revenue_mai,3)
                self.Market_Stat.get('mai').update(avg_revenue = avg_revenue_mai)

                __netprofit_mai = mean([self.DataTable[j]['data'][3] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_netprofit_mai = round(__netprofit_mai,3)
                self.Market_Stat.get('mai').update(avg_netprofit = avg_netprofit_mai)

                __roe_mai = mean([self.DataTable[j]['data'][4] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_roe_mai = round(__roe_mai,3)
                self.Market_Stat.get('mai').update(avg_roe = avg_roe_mai)

                __yield_mai = mean([self.DataTable[j]['data'][5] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_yield_mai = round(__yield_mai,3)
                self.Market_Stat.get('mai').update(avg_yield = avg_yield_mai)

                ### SET ###
                __asset_SET = mean([self.DataTable[j]['data'][1] for j in self.DataTable if not self.DataTable[j]['ismai']])
                avg_assets_SET = round(__asset_SET,3)
                self.Market_Stat.get('SET').update(avg_asset = avg_assets_SET)

                __revenue_mai = mean([self.DataTable[j]['data'][2] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_revenue_mai = round(__revenue_mai,3)
                self.Market_Stat.get('mai').update(avg_revenue = avg_revenue_mai)

                __netprofit_mai = mean([self.DataTable[j]['data'][3] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_netprofit_mai = round(__netprofit_mai,3)
                self.Market_Stat.get('mai').update(avg_netprofit = avg_netprofit_mai)

                __roe_mai = mean([self.DataTable[j]['data'][4] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_roe_mai = round(__roe_mai,3)
                self.Market_Stat.get('mai').update(avg_roe = avg_roe_mai)

                __yield_mai = mean([self.DataTable[j]['data'][5] for j in self.DataTable if self.DataTable[j]['ismai']])
                avg_yield_mai = round(__yield_mai,3)
                self.Market_Stat.get('mai').update(avg_yield = avg_yield_mai)
            except:
                pass