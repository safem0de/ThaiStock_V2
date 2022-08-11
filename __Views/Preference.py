import tkinter as tk
from tkinter import ttk
from __Models.Settings import Setting

class Preference(tk.Toplevel):
    def __init__(self):
        super().__init__()

    def create_view(self, model:Setting):
        self.title('Preferences')
        self.geometry(f'+{str(model.getstart_screen_x())}+{str(model.getstart_screen_y())}')

        self.LblframeSetting = ttk.LabelFrame(self, text="Setting Windows Position")
        self.LblframeSetting.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

        ######## Download SET ########

        self.LblSETDownload = ttk.Label(self.LblframeSetting, text="Download SET : ")
        self.LblSETDownload.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.SETDownload_var = tk.StringVar()
        self.ComboSET = ttk.Combobox(self.LblframeSetting, textvariable = self.SETDownload_var)
        self.ComboSET.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)
        self.ComboSET['values'] = ('✔ YES', '❌ NO')
        self.ComboSET['state'] = 'readonly'
        if model.getSET_download():
            self.ComboSET.set('✔ YES')
        else:
            self.ComboSET.set('❌ NO')

        ######## Download mai ########

        self.LblmaiDownload = ttk.Label(self.LblframeSetting, text="Download mai : ")
        self.LblmaiDownload.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.maiDownload_var = tk.StringVar()
        self.Combomai = ttk.Combobox(self.LblframeSetting, textvariable = self.maiDownload_var)
        self.Combomai.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)
        self.Combomai['values'] = ('✔ YES', '❌ NO')
        self.Combomai['state'] = 'readonly'
        if model.getmai_download():
            self.Combomai.set('✔ YES')
        else:
            self.Combomai.set('❌ NO')

        ######## Main Screen Position ########

        self.LblposMain = ttk.Label(self.LblframeSetting, text="Main Menu Position (x,y) : ")
        self.LblposMain.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.posMain_x = tk.StringVar()
        self.Txt_main_x = ttk.Entry(self.LblframeSetting, textvariable = self.posMain_x)
        self.Txt_main_x.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_main_x.insert(tk.END, model.getstart_screen_x())

        self.posMain_y = tk.StringVar()
        self.Txt_main_y = ttk.Entry(self.LblframeSetting, textvariable = self.posMain_y)
        self.Txt_main_y.grid(row=2, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_main_y.insert(tk.END, model.getstart_screen_y())

        self.LblposMainalert = ttk.Label(self.LblframeSetting, text="")
        self.LblposMainalert.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)
        
        ######## Main Screen Position ########

        self.LblposLoad = ttk.Label(self.LblframeSetting, text="Load Progress Position (x,y) : ")
        self.LblposLoad.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.posLoad_x = tk.StringVar()
        self.Txt_Load_x = ttk.Entry(self.LblframeSetting, textvariable = self.posLoad_x)
        self.Txt_Load_x.grid(row=4, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_Load_x.insert(tk.END, model.getload_screen_x())

        self.posLoad_y = tk.StringVar()
        self.Txt_Load_y = ttk.Entry(self.LblframeSetting, textvariable = self.posLoad_y)
        self.Txt_Load_y.grid(row=4, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_Load_y.insert(tk.END, model.getload_screen_y())

        self.LblposLoadalert = ttk.Label(self.LblframeSetting, text="")
        self.LblposLoadalert.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        ######## BNB APi ########

        self.LblBNB_APi = ttk.Label(self.LblframeSetting, text="Binance Api : ")
        self.LblBNB_APi.grid(row=6, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.BNB_APi = tk.StringVar()
        self.Txt_BNB_APi = ttk.Entry(self.LblframeSetting, textvariable = self.BNB_APi)
        self.Txt_BNB_APi.grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_BNB_APi.insert(tk.END, '')
        self.Txt_BNB_APi.config(show="*")

        ######## BNB Secret ########

        self.LblBNB_Secret = ttk.Label(self.LblframeSetting, text="Secret key : ")
        self.LblBNB_Secret.grid(row=7, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.BNB_Secret = tk.StringVar()
        self.Txt_BNB_Secret = ttk.Entry(self.LblframeSetting, textvariable = self.BNB_Secret)
        self.Txt_BNB_Secret.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_BNB_Secret.insert(tk.END, '')
        self.Txt_BNB_Secret.config(show="*")

        ####### Main Screen Position ########

        self.SavePreference = ttk.Button(self, text='Save Preference')
        self.SavePreference.grid(row=1, column=0, padx=5, pady=5, sticky=tk.S + tk.E)