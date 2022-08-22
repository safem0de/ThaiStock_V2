import pandas as pd
import requests

class Stock:

    __Market = {
        'SET' : {},
        'mai' : {},
        'Crypto' : {}
    }
    __Industry = {
        'SET':{
            'AGRO': {'AGRI': {}, 'FOOD': {}},
            'CONSUMP':{'FASHION': {}, 'HOME': {}, 'PERSON': {}, },
            'FINCIAL': {'BANK': {}, 'FIN': {}, 'INSUR': {}},
            'INDUS': {'AUTO': {}, 'IMM': {}, 'PAPER': {}, 'PETRO': {}, 'PKG': {}, 'STEEL': {}},
            'PROPCON': {'CONMAT' : {}, 'PROP' : {}, 'PF&REIT' : {}, 'CONS' : {}},
            'RESOURC':{'ENERG' : {}, 'MINE' : {}},
            'SERVICE': {'COMM': {}, 'HELTH':{}, 'MEDIA':{}, 'PROF': {}, 'TOURISM':{}, 'TRANS':{}},
            'TECH': {'ETRON': {}, 'ICT': {}}
        },
        'mai':{
            'AGRO': {},
            'CONSUMP': {},
            'FINCIAL': {},
            'INDUS': {},
            'PROPCON': {},
            'RESOURC': {},
            'SERVICE': {},
            'TECH': {}
        }
    }   

    __Selected_StockName = None

    def __init__(self):
        # __prefix = ['NUMBER','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        __prefix = ['NUMBER','A']
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
        for r in x['data']:
            y = dict()
            y[r.get('symbol')] = {'data':[
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
                round(float(r.get('vwap24Hr')),4) if r.get('vwap24Hr') != None else '-',
                ]}
            self.__Market['Crypto'].update(y)

        for j in self.__Industry:
            print(j)
            if j == 'mai':
                for k in self.__Industry[j]:
                    k = k.replace('&','%26')
                    print(k)
                    print(f'https://classic.set.or.th/mkt/sectorquotation.do?market={j}&sector={k}&language=th&country=TH')
                    dfRawSector = pd.read_html(f'https://classic.set.or.th/mkt/sectorquotation.do?market={j}&sector={k}&language=th&country=TH'
                                    , match="เครื่องหมาย" ,encoding='utf8')
                    dfSector = dfRawSector[0]
                    Industry = dfSector['หลักทรัพย์'].to_list()
                    vl = dfSector["มูลค่า('000 บาท)"].to_list()
                    f_value = [float(i) if not i == '-' else 0 for i in vl]

                    data = dict(zip(Industry, f_value))
                    self.setIndustry_mai(k,data)

            else:
                for k in self.__Industry[j]:
                    print('==>',k)
                    for l in self.__Industry[j][k]:
                        l = l.replace('&','%26')
                        print(l)
                        print(f'https://classic.set.or.th/mkt/sectorquotation.do?market={j}&sector={l}&language=th&country=TH')
                        dfRawSector = pd.read_html(f'https://classic.set.or.th/mkt/sectorquotation.do?market={j}&sector={l}&language=th&country=TH'
                                        , match="เครื่องหมาย" ,encoding='utf8')
                        dfSector = dfRawSector[0]
                        Industry = dfSector['หลักทรัพย์'].to_list()
                        vl = dfSector["มูลค่า('000 บาท)"].to_list()
                        f_value = [float(i) if not i == '-' else 0 for i in vl]

                        data = dict(zip(Industry, f_value))
                        self.setIndustry_SET(k,l.replace('%26','&'),data)

        # print(self.__Industry)
        
    def getMarket(self):
        return self.__Market

    def getIndustry(self):
        return self.__Industry

    def getSelected_StockName(self):
        return self.__Selected_StockName

    def setMarket_mai(self, param:dict):
        self.__Market['mai'].update(param)

    def setMarket_SET(self, param:dict):
        self.__Market['SET'].update(param)

    def setSelected_StockName(self, param):
        self.__Selected_StockName = param

    def setIndustry_mai(self, sector, param):
        self.__Industry['mai'][sector] = param

    def setIndustry_SET(self, sector, sub_sector, param):
        self.__Industry['SET'][sector][sub_sector] = param