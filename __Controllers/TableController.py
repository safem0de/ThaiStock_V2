from __Models.Stocks import Stock
import datetime
import pandas as pd

class TableController():
    def __init__(self, model: Stock) -> None:
        super().__init__()
        self.model = model

    def bind(self, model:Stock, view, Market:str):
        self.view = view
        self.view.create_view(self, model, Market)

    def getStockInfo(self, x_name:str):
        try:
            dflist = pd.read_html('https://classic.set.or.th/set/companyprofile.do?symbol='+ x_name +'&country=TH'
                            , match="ชื่อบริษัท" ,encoding='utf8')
            df0 = dflist[0]
            x = df0.values.tolist()
            dict_za = ['ชื่อบริษัท',
                        'ที่อยู่',
                        'เบอร์โทรศัพท์',
                        'เว็บไซต์',
                        'กลุ่มอุตสาหกรรม',
                        'หมวดธุรกิจ',
                        'ทุนจดทะเบียน',
                        'ทุนจดทะเบียนชำระแล้ว',
                        'นโยบายเงินปันผล',
                        ]
            delete_list = ['เบอร์โทรสาร','แบบ','วันที่เริ่มต้นซื้อขาย','หุ้นบุริมสิทธิ','ข้อจำกัดหุ้นต่างด้าว','รายชื่อกรรมการล่าสุด']
            txt = ''
            index = []
            data_Info = []
            final_Info = []


            for i in range(len(x)):
                y = str(x[i][0]).strip()
                txt += y

            for key in dict_za:
                index.append(txt.find(key))
            index.append(len(txt))


            for k in range(len(index)):
                if k < len(index)-1:
                    data_Info.append(str(txt[index[k]:index[k+1]]).strip())

            for l in data_Info:
                # print(l)
                for m in delete_list:
                    # print(m)
                    if not l.find(m) == -1:
                        l = l[:l.find(m)]

                final_Info.append(str(l).strip())
        except:
            pass

        return final_Info

    def StockStatement(self, x_name) -> pd.DataFrame:
        try :
            dfstock = pd.read_html('https://classic.set.or.th/set/companyhighlight.do?symbol=' + x_name + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            df.Name = x_name
            return df
        except:
            return pd.DataFrame()

    ## Substring Technic
    ## https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    def StockStatementHeader(self, df) -> list:
        x = datetime.datetime.now()
        stockstatement = df
        listOfColumn = []
        if not stockstatement.empty:
            ls = list(stockstatement.columns)
            # print(ls)
            for i in range(len(ls)):
                if i == 0:
                    listOfColumn.append(df.Name)
                else:
                    if "Unnamed" not in str(ls[i][0]) and "Unnamed" not in str(ls[i][1]):
                        listOfColumn.append(str(ls[i][1])[-10:])
                    elif "Unnamed" in str(ls[i][0]) and "Unnamed" not in str(ls[i][1]): 
                        listOfColumn.append(str(ls[i][1])[-10:])
                    else:
                        listOfColumn.append(str(ls[i][0])[-10:])
            # print(listOfColumn)
        return listOfColumn

    def StockStatementData(self, df) -> list:
        stockstatement = df
        if not stockstatement.empty:
            stockstatement
            return stockstatement.values.tolist()
        return list()