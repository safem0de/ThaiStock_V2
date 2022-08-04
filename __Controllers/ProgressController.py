import pandas as pd
import datetime

class ProgressController():
    def __init__(self) -> None:
        super().__init__()

    def createStock(self, st_Name) -> list:
        ls = []
        try:
            dfy = pd.read_html('https://classic.set.or.th/mkt/stockquotation.do?symbol='+ st_Name +'&ssoPageId=1&language=th&country=TH', match='เครื่องหมาย', encoding='utf8')
            df = dfy[0]
            df.fillna("-", inplace= True)
            ls.append(str(st_Name).replace('+',' ').replace('%26','&'))
            ls.append(df.iloc[0,1])
            ls.append(df.iloc[1,1] if (df.iloc[1,1]) == '-' else float(df.iloc[1,1]))
            ls.append(df.iloc[2,1] if (df.iloc[2,1]) == '-' else float(df.iloc[2,1]))
            ls.append(df.iloc[3,1] if (df.iloc[3,1]) == '-' else float(df.iloc[3,1]))
            ls.append(df.iloc[4,1] if (df.iloc[4,1]) == '-' else float(df.iloc[4,1]))
            ls.append(df.iloc[5,1] if (df.iloc[5,1]) == '-' else float(df.iloc[5,1]))
            ls.append(df.iloc[6,1] if (df.iloc[6,1]) == '-' else float(df.iloc[6,1]))
            ls.append(df.iloc[7,1] if (df.iloc[7,1]) == '-' else float(df.iloc[7,1]))
            ls.append(df.iloc[8,1] if (df.iloc[8,1]) == '-' else float(df.iloc[8,1]))
            ls.append(df.iloc[9,1] if (df.iloc[9,1]) == '-' else float(df.iloc[9,1]))
            ls.append(df.iloc[10,1] if (df.iloc[10,1]) == '-' else float(df.iloc[10,1]))
            return ls
        except Exception as e:
            print(st_Name, e, sep='\n')
            return None


    def StockStatement(self, x_name) -> pd.DataFrame:
        df = pd.DataFrame()
        try :
            dfstock = pd.read_html('https://classic.set.or.th/set/companyhighlight.do?symbol=' + x_name + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            df.Name = x_name
            df.drop([0,9], inplace = True)
            df.reset_index()
            return df
        except:
            return df


    ## Substring Technic
    ## https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    def StockStatementHeader(self, df) -> list:
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

    def Fin_Dataframe(self, x_name):
        dfx = pd.DataFrame()
        try :
            dfstock = pd.read_html('https://classic.set.or.th/set/companyhighlight.do?symbol=' + x_name + '&language=th&country=TH'
                       , match="งวดงบการเงิน")
            df = dfstock[0]
            df.fillna('-', inplace = True)
            df.Name = str(x_name).replace('+','-').replace('%26','&')
            df.drop([0,9], inplace = True)
            df.reset_index()

            data = self.StockStatementData(df)
            col = self.StockStatementHeader(df)
            col_result  = [col[0] if i==0 else col[i][-7:] for i in range(len(col))]
            dfx = pd.DataFrame(data,columns = col_result)
            print(x_name, df.Name)
            return dfx
        except:
            return dfx