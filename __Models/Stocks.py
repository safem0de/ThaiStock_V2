import pandas as pd
import requests

class Stock:

    __Market = {
        'SET' : {},
        'mai' : {},
        'Crypto' : {}
    }
    __Selected_StockName = None

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

        url = 'https://api.coincap.io/v2/assets'
        response = requests.get(url)
        x = dict(response.json())
        # y = pd.DataFrame(x['data'])
        # print(y)

        for r in x['data']:
            y = dict()
            y[r.get('symbol')] = [
                str(r.get('name')).upper(),
                r.get('symbol'),
                round(float(r.get('priceUsd')),4),
                '-',
                round(float(r.get('changePercent24Hr')),4),
                '-',
                '-',
                '-',
                '-',
                round(float(r.get('volumeUsd24Hr')),4),
                round(float(r.get('marketCapUsd'))/1000000,4),
                # round(float(r.get('vwap24Hr')),4),
                ]
            self.__Market['Crypto'].update(y)

        # print(self.__Market)


    def getMarket(self):
        return self.__Market

    def setMarket_mai(self, param:dict):
        self.__Market['mai'].update(param)

    def setMarket_SET(self, param:dict):
        self.__Market['SET'].update(param)

    def getSelected_StockName(self):
        return self.__Selected_StockName

    def setSelected_StockName(self, param):
        self.__Selected_StockName = param