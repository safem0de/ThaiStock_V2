import pandas as pd
import threading as Thread
class Stock:

    __Market = {
        'SET' : {},
        'mai' : {},
    }

    def __init__(self):
        __prefix = ['NUMBER','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in __prefix:
            dflist = pd.read_html('https://classic.set.or.th/set/commonslookup.do?language=th&country=TH&prefix='+i
                        , match="ชื่อย่อหลักทรัพย์" ,encoding='utf8')
            df0 = dflist[0]
            df0 = df0[['ชื่อย่อหลักทรัพย์','ตลาด']]

            for r_i,r in df0.iterrows():
                x = dict()
                if df0.iloc[r_i,1] == 'mai':
                    x[str(df0.iloc[r_i,0]).replace('&','%26').replace(' ','+')] = None
                    self.__Market['mai'].update(x)
                    # print(x)
                else:
                    x[str(df0.iloc[r_i,0]).replace('&','%26').replace(' ','+')] = None
                    self.__Market['SET'].update(x)
                    # print(x)

    def getMarket(self):
        return self.__Market

    def setMarket_mai(self, param:dict):
        self.__Market['mai'].update(param)

    def setMarket_SET(self, param:dict):
        self.__Market['SET'].update(param)