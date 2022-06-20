import pandas as pd

class ProgressController():
    def __init__(self) -> None:
        super().__init__()

    def createStock(self, st_Name) -> list:
        ls = []
        try:
            dfy = pd.read_html('https://classic.set.or.th/mkt/stockquotation.do?symbol='+ st_Name +'&ssoPageId=1&language=th&country=TH', match='เครื่องหมาย', encoding='utf8')
            df = dfy[0]
            df.fillna("-", inplace= True)
            ls.append(st_Name)
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
        except Exception as e:
            print(st_Name, e, sep='\n')
            pass

        return ls