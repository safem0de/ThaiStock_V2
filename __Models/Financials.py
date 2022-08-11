class Financial:

    def __init__(self):
        # Constructor
        pass

    fin = {
            'สินทรัพย์รวม' : None,
            'หนี้สินรวม' : None,
            'ส่วนของผู้ถือหุ้น' : None,
            'มูลค่าหุ้นที่เรียกชำระแล้ว' : None,
            'รายได้รวม': None,
            'กำไร (ขาดทุน) จากกิจกรรมอื่น' : None,
            'กำไรสุทธิ' : None,
            'กำไรต่อหุ้น (บาท)' : None,
            'ROA(%)' : None,
            'ROE(%)' : None,
            'อัตรากำไรสุทธิ(%)' : None,
            'ราคาล่าสุด(บาท)' : None,
            'มูลค่าหลักทรัพย์ตามราคาตลาด' : None,
            'วันที่ของงบการเงินที่ใช้คำนวณค่าสถิติ' : None,
            'P/E (เท่า)' : None,
            'P/BV (เท่า)' : None,
            'มูลค่าหุ้นทางบัญชีต่อหุ้น (บาท)' : None,
            'อัตราส่วนเงินปันผลตอบแทน(%)' : None,
        }

    #Getters
    def getAssets(self):
        return self.fin.get('สินทรัพย์รวม')

    def getLiabilities(self):
        return self.fin.get('หนี้สินรวม')

    def getEquity(self):
        return self.fin.get('ส่วนของผู้ถือหุ้น')

    def getCapital(self):
        return self.fin.get('มูลค่าหุ้นที่เรียกชำระแล้ว')

    def getRevenue(self):
        return self.fin.get('รายได้รวม')

    def getProfit_Loss(self):
        return self.fin.get('กำไร (ขาดทุน) จากกิจกรรมอื่น')

    def getNetProfit(self):
        return self.fin.get('กำไรสุทธิ')

    def getEPS(self):
        return self.fin.get('กำไรต่อหุ้น (บาท)')

    def getROA(self):
        return self.fin.get('ROA(%)')

    def getROE(self):
        return self.fin.get('ROE(%)')

    def getMargin(self):
        return self.fin.get('อัตรากำไรสุทธิ(%)')

    def getLastPrice(self):
        return self.fin.get('ราคาล่าสุด(บาท)')

    def getMarketCap(self):
        return self.fin.get('มูลค่าหลักทรัพย์ตามราคาตลาด')

    def getFSPeriod(self):
        return self.fin.get('อัตราส่วนเงินปันผลตอบแทน(%)')

    def getPE(self):
        return self.fin.get('P/E (เท่า)')

    def getPBV(self):
        return self.fin.get('P/BV (เท่า)')

    def getBookValuepershare(self):
        return self.fin.get('มูลค่าหุ้นทางบัญชีต่อหุ้น (บาท)')

    def getDvdYield(self):
        return self.fin.get('สินทรัพย์รวม')

    #Setters
    def setAssets(self, param:dict):
        self.fin['สินทรัพย์รวม'] = param

    def setLiabilities(self, param:dict):
        self.fin['หนี้สินรวม'] = param

    def setEquity(self, param:dict):
        self.fin['ส่วนของผู้ถือหุ้น'] = param

    def setCapital(self, param:dict):
        self.fin['มูลค่าหุ้นที่เรียกชำระแล้ว'] = param

    def setRevenue(self, param:dict):
        self.fin['รายได้รวม'] = param

    def setProfit_Loss(self, param:dict):
        self.fin['กำไร (ขาดทุน) จากกิจกรรมอื่น'] = param

    def setNetProfit(self, param:dict):
        self.fin['กำไรสุทธิ'] = param

    def setEPS(self, param:dict):
        self.fin['กำไรต่อหุ้น (บาท)'] = param

    def setROA(self, param:dict):
        self.fin['ROA(%)'] = param

    def setROE(self, param:dict):
        self.fin['ROE(%)'] = param

    def setMargin(self, param:dict):
        self.fin['อัตรากำไรสุทธิ(%)'] = param

    def setLastPrice(self, param:dict):
        self.fin['ราคาล่าสุด(บาท)'] = param

    def setMarketCap(self, param:dict):
        self.fin['มูลค่าหลักทรัพย์ตามราคาตลาด'] = param

    def setFSPeriod(self, param:dict):
        self.fin['วันที่ของงบการเงินที่ใช้คำนวณค่าสถิติ'] = param

    def setPE(self, param:dict):
        self.fin['P/E (เท่า)'] = param

    def setPBV(self, param:dict):
        self.fin['P/BV (เท่า)'] = param

    def setBookValuepershare(self, param:dict):
        self.fin['มูลค่าหุ้นทางบัญชีต่อหุ้น (บาท)'] = param

    def setDvdYield(self, param:dict):
        self.fin['อัตราส่วนเงินปันผลตอบแทน(%)'] = param


class FinancialGrowth:
    def __init__(self):
        pass

    __Assets = []
    __Revenue = []
    __NetProfit = []
    __ROE = []
    __PE = []
    __PBV = []
    __EPS = []