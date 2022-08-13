
class Setting:

    setting = {
        'SET_download' : False,
        'mai_download' : True,
        'start_screen_x' : 0,
        'start_screen_y' : 0,
        'load_screen_x' : 0,
        'load_screen_y' : 0,
        'BNB_API': '',
        'BNB_Secret_key': '',
    }

    def getSET_download(self):
        return self.setting.get('SET_download')
        
    def getmai_download(self):
        return self.setting.get('mai_download')

    def getstart_screen_x(self):
        return str(self.setting.get('start_screen_x'))

    def getstart_screen_y(self):
        return str(self.setting.get('start_screen_y'))

    def getload_screen_x(self):
        return str(self.setting.get('load_screen_x'))

    def getload_screen_y(self):
        return str(self.setting.get('load_screen_y'))

    def getsettingModel(self):
        return self.setting

    def setSET_download(self, param):
        self.setting.update({'SET_download':param})

    def setmai_download(self, param):
        self.setting.update({'mai_download':param})

    def setstart_screen_x(self, param):
        self.setting.update({'start_screen_x':param})

    def setstart_screen_y(self, param):
        self.setting.update({'start_screen_y':param})

    def setload_screen_x(self, param):
        self.setting.update({'load_screen_x':param})

    def setload_screen_y(self, param):
        self.setting.update({'load_screen_y':param})