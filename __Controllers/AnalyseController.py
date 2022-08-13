import pandas as pd
from __Models.Stocks import Stock
from __Models.Financials import Financial

class AnalyseController():

    all_findata = {}

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


    def CreateListofFinancial(self):
        Datas = {}
        cal:dict = self.model.getMarket().get('SET').copy()
        cal.update(self.model.getMarket().get('mai'))

        for k in cal:
            try:
                x : pd.DataFrame = cal.get(k).get('fin_data')
                ismai = cal.get(k).get('ismai')
                isSET50 = cal.get(k).get('isSET50')
                isSET100 = cal.get(k).get('isSET100')
            
                Year = [str(i)[-2:] for i in x.columns.to_list()[1:]]
                Assets  = x.iloc[0].tolist()[1:]
                Liabilities = x.iloc[1].tolist()[1:]
                Equity = x.iloc[2].tolist()[1:]
                Capital = x.iloc[3].tolist()[1:]
                Revenue = x.iloc[4].tolist()[1:]
                Profit_Loss = x.iloc[5].tolist()[1:]
                NetProfit = x.iloc[6].tolist()[1:]
                EPS = x.iloc[7].tolist()[1:]
                ROA = x.iloc[8].tolist()[1:]
                ROE = x.iloc[9].tolist()[1:]
                Margin = x.iloc[10].tolist()[1:]
                LastPrice = x.iloc[12].tolist()[1:]
                MarketCap = x.iloc[13].tolist()[1:]
                FSPeriod = x.iloc[14].tolist()[1:]
                PE = x.iloc[15].tolist()[1:]
                PBV = x.iloc[16].tolist()[1:]
                BookValuepershare = x.iloc[17].tolist()[1:]
                DvdYield = x.iloc[18].tolist()[1:]

                f = {}

                f['สินทรัพย์รวม'] = dict(zip(Year, Assets))
                f['หนี้สินรวม'] = dict(zip(Year, Liabilities))
                f['ส่วนของผู้ถือหุ้น'] = dict(zip(Year, Equity))
                f['มูลค่าหุ้นที่เรียกชำระแล้ว'] = dict(zip(Year, Capital))
                f['รายได้รวม'] = dict(zip(Year, Revenue))
                f['กำไร (ขาดทุน) จากกิจกรรมอื่น'] = dict(zip(Year, Profit_Loss))
                f['กำไรสุทธิ'] = dict(zip(Year, NetProfit))
                f['กำไรต่อหุ้น (บาท)'] = dict(zip(Year, EPS))
                f['ROA(%)'] = dict(zip(Year, ROA))
                f['ROE(%)'] = dict(zip(Year, ROE))
                f['อัตรากำไรสุทธิ(%)'] = dict(zip(Year, Margin))
                f['ราคาล่าสุด(บาท)'] = dict(zip(Year, LastPrice))
                f['มูลค่าหลักทรัพย์ตามราคาตลาด'] = dict(zip(Year, MarketCap))
                f['วันที่ของงบการเงินที่ใช้คำนวณค่าสถิติ'] = dict(zip(Year, FSPeriod))
                f['P/E (เท่า)'] = dict(zip(Year, PE))
                f['P/BV (เท่า)'] = dict(zip(Year, PBV))
                f['มูลค่าหุ้นทางบัญชีต่อหุ้น (บาท)'] = dict(zip(Year, BookValuepershare))
                f['อัตราส่วนเงินปันผลตอบแทน(%)'] = dict(zip(Year, DvdYield))

                Datas[k] = {
                            'data': f,
                            'ismai': ismai,
                            'isSET100':isSET100,
                            'isSET50':isSET50
                        }

            except Exception as e:
                print(e)

        self.all_findata = Datas
        # print(Datas)

    def deleteMinusProfit(self):
        raw = self.all_findata.copy()
        # print(len(raw))
        removal_list = []
        for k0, v0 in raw.items():
            netProfits = v0.get('data').get('กำไรสุทธิ')
            # print(netProfits)
            for k1, v1 in netProfits.items():
                if (str(v1) == '-' or float(v1) < 0) and not k0 in removal_list:
                    removal_list.append(k0)

        for i in removal_list:
            raw.pop(i)

        return raw


    def calculateGrowth(self, Growth_type:str, data:dict):
        
        for k, v in data.items():
            x = None
            result_growth = []
            y = []
            if Growth_type == 'assets':
                x = v.get('data').get('สินทรัพย์รวม')
            elif Growth_type == 'revenue':
                x = v.get('data').get('รายได้รวม')
                print(Growth_type, x)
            elif Growth_type == 'netprofit':
                x = v.get('data').get('กำไรสุทธิ')
                print(Growth_type, x)
            elif Growth_type == 'roe':
                x = v.get('data').get('ROE(%)')
                print(Growth_type, )
            elif Growth_type == 'yield':
                x = v.get('data').get('อัตราส่วนเงินปันผลตอบแทน(%)')
                print(Growth_type, x)
            else:
                pass

            for i in x:
                try:
                    y.append(float(x[i]))
                except ValueError:
                    y.append(float(0))
                z = y[::-1]
                print(z)
                for i in range(len(z)):
                    # print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
                    # print("อัตราการเติบโตของทรัพย์สิน (ต่อปี)")
                    if (i+1) < len(z):
                        # print((i+1), len(z))
                        try:
                            a = ((z[i]-z[i+1])/z[i+1])*100
                            # print(f'({z[i]}-{z[i+1]}/{z[i+1]})*100')
                        except ZeroDivisionError:
                            a = 0

                        if len(result_growth) < 3:
                            result_growth.append(round(a,3))

            print(result_growth)
            # return result_growth

    def InitialTable(self):
        self.CreateListofFinancial()
        data = self.deleteMinusProfit()
        self.calculateGrowth(Growth_type='assets',data=data)


