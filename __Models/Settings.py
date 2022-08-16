
class Setting:

    setting = {
        'SET_download' : False,
        'mai_download' : True,
        'load_screen_x' : 1925,
        'load_screen_y' : 0,
        'start_screen_x' : 1925,
        'start_screen_y' : 0,
        'analyse_screen_x' : 1925,
        'analyse_screen_y' : 0,
        'BNB_API': '',
        'BNB_Secret_key': '',
    }

    #Getter
    def getSET_download(self):
        return self.setting.get('SET_download')
        
    def getmai_download(self):
        return self.setting.get('mai_download')

    def getload_screen_x(self):
        return str(self.setting.get('load_screen_x'))

    def getload_screen_y(self):
        return str(self.setting.get('load_screen_y'))

    def getstart_screen_x(self):
        return str(self.setting.get('start_screen_x'))

    def getstart_screen_y(self):
        return str(self.setting.get('start_screen_y'))

    def getanalyse_screen_x(self):
        return str(self.setting.get('analyse_screen_x'))

    def getanalyse_screen_y(self):
        return str(self.setting.get('analyse_screen_y'))

    def getsettingModel(self):
        return self.setting

    #Setter
    def setSET_download(self, param):
        self.setting.update({'SET_download':param})

    def setmai_download(self, param):
        self.setting.update({'mai_download':param})

    def setload_screen_x(self, param):
        self.setting.update({'load_screen_x':param})

    def setload_screen_y(self, param):
        self.setting.update({'load_screen_y':param})

    def setstart_screen_x(self, param):
        self.setting.update({'start_screen_x':param})

    def setstart_screen_y(self, param):
        self.setting.update({'start_screen_y':param})

    def setanalyse_screen_x(self, param):
        self.setting.update({'start_screen_x':param})

    def setanalyse_screen_y(self, param):
        self.setting.update({'start_screen_y':param})