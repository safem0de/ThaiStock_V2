import pandas as pd
from __Models.Financial import Financial
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
        try:
            dfSET100 = pd.read_html('https://classic.set.or.th/mkt/sectorquotation.do?sector=SET100'
                        ,match='เครื่องหมาย')
            df = dfSET100[0]
            set100_data = df['หลักทรัพย์'].to_list()

            for k,v in self.model.getMarket().get('SET').items():

                if k in set100_data:
                    self.model.getMarket().get('SET').get(k).update(isSET100=True)
                else:
                    self.model.getMarket().get('SET').get(k).update(isSET100=False)
        except:
            pass

    def checkSET50(self):
        df = pd.DataFrame()
        try:
            dfSET50 = pd.read_html('https://classic.set.or.th/mkt/sectorquotation.do?sector=SET50'
                        ,match='เครื่องหมาย')
            df = dfSET50[0]
            set50_data = df['หลักทรัพย์'].to_list()

            for k,v in self.model.getMarket().get('SET').items():

                if k in set50_data:
                    self.model.getMarket().get('SET').get(k).update(isSET50=True)
                else:
                    self.model.getMarket().get('SET').get(k).update(isSET50=False)
        except:
            pass

    
    def DataframeToModel(self,df):
        cleanDatas = {}
        for row_index,row in df.iterrows():
            m = pd.to_numeric(row[1:], errors='ignore')
            cleanDatas[row[0]] = m.to_dict() ### row[0] is column header
        return cleanDatas


    def CreateFinancial(self,Market:str):
        s : dict = self.model.getMarket().get(Market)

        for k,v in s.items():
            x = s.get(k)
            y = x.get('fin_data')
            data = self.DataframeToModel(y)
            analyseModel = Financial
            analyseModel.setAssets(self, param=data['สินทรัพย์รวม'])
            analyseModel.setLiabilities(self, param=data['หนี้สินรวม'])
            analyseModel.setEquity(self, param=data['ส่วนของผู้ถือหุ้น'])
            analyseModel.setCapital(self, param=data['มูลค่าหุ้นที่เรียกชำระแล้ว'])
            analyseModel.setRevenue(self, param=data['รายได้รวม'])
            analyseModel.setProfit_Loss(self, param=data['กำไร (ขาดทุน) จากกิจกรรมอื่น'])
            analyseModel.setNetProfit(self, param=data['กำไรสุทธิ'])
            analyseModel.setEPS(self, param=data['กำไรต่อหุ้น (บาท)'])
            analyseModel.setROA(self, param=data['ROA(%)'])
            analyseModel.setROE(self, param=data['ROE(%)'])
            analyseModel.setMargin(self, param=data['อัตรากำไรสุทธิ(%)'])
            analyseModel.setLastPrice(self, param=data['ราคาล่าสุด(บาท)'])
            analyseModel.setMarketCap(self, param=data['มูลค่าหลักทรัพย์ตามราคาตลาด'])
            analyseModel.setFSPeriod(self, param=data['วันที่ของงบการเงินที่ใช้คำนวณค่าสถิติ'])
            analyseModel.setPE(self, param=data['P/E (เท่า)'])
            analyseModel.setPBV(self, param=data['P/BV (เท่า)'])
            analyseModel.setBookValuepershare(self, param=data['มูลค่าหุ้นทางบัญชีต่อหุ้น (บาท)'])
            analyseModel.setDvdYield(self, param=data['อัตราส่วนเงินปันผลตอบแทน(%)'])
            x.update(financial=analyseModel)

    
    def deleteMinusProfit(self, Market='all'):
        cal = self.model.getMarket().get('SET').copy()
        cal.update(self.model.getMarket().get('mai'))
        print(cal)

        # for c in cal:
        #     financials:Financial = cal.get(c).get('financial')
        #     netprofit = financials.getNetProfit()
        #     print(netprofit)

