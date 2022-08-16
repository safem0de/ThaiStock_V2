import json
from statistics import mean
import pandas as pd
from __Models.Stocks import Stock

class AnalyseController():

    def __init__(self, model:Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, model:Stock, view):
        self.view = view
        self.view.create_view(self, model)

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

        return Datas

    def deleteMinusProfit(self,data):
        raw = data.copy()
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


    def calculateGrowth(self, Growth_type:str,data):
        calculated = {}

        for k, v in data.items():
            x = None
            y = []
            if Growth_type == 'assets':
                x = v.get('data').get('สินทรัพย์รวม')
            elif Growth_type == 'revenue':
                x = v.get('data').get('รายได้รวม')
            elif Growth_type == 'netprofit':
                x = v.get('data').get('กำไรสุทธิ')
            elif Growth_type == 'roe':
                x = v.get('data').get('ROE(%)')
            elif Growth_type == 'yield':
                x = v.get('data').get('อัตราส่วนเงินปันผลตอบแทน(%)')
            else:
                pass

            for i in x:
                try:
                    y.append(float(x[i]))
                except ValueError:
                    y.append(float(0))
                
                z = y[::-1]
                result_growth = []
                for i in range(len(z)):
                    # print(f"((สินทรัพย์ปี {year_asset[i][0]} - สินทรัพย์ปี {year_asset[i+1][0]})/ สินทรัพย์ปี {year_asset[i+1][0]})*100")
                    if (i+1) < len(z):
                        # print((i+1), len(z))
                        a = 0
                        try:
                            a = ((z[i]-z[i+1])*100)/z[i+1]
                        except ZeroDivisionError:
                            a = 0

                        result_growth.append(round(a,3))

                try:
                    if len(result_growth) >= 1:
                        calculated[k] = round(mean(result_growth[:3]),3)
                except:
                    pass

        print(calculated)
        return calculated    

    # def InitialTable(self):
    #     self.CreateListofFinancial()
    #     self.deleteMinusProfit()

    #     json_object = json.dumps(self.filtered, indent = 4) 
    #     print(json_object)

    #     Ast = self.__calculateGrowth(Growth_type='assets')
    #     Rvn = self.__calculateGrowth(Growth_type='revenue')
    #     Npf = self.__calculateGrowth(Growth_type='netprofit')
    #     Roe = self.__calculateGrowth(Growth_type='roe')
    #     Yld = self.__calculateGrowth(Growth_type='yield')
    #     dataTable = {i:{'data':[i, Ast[i], Rvn[i], Npf[i], Roe[i], Yld[i], str(list(self.filtered[i]['data']['P/E (เท่า)'].values())[-1]), str(list(self.filtered[i]['data']['P/BV (เท่า)'].values())[-1])],
    #                 'ismai': self.filtered[i]['ismai'],
    #                 'isSET100': self.filtered[i]['isSET100'],
    #                 'isSET50': self.filtered[i]['isSET50'],}
    #             for i in self.filtered}

    #     json_object = json.dumps(dataTable, indent = 4) 
    #     print(json_object)

    #     return dataTable