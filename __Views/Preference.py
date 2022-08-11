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
        self.ComboSET['values'] = ('YES', 'NO')
        self.ComboSET['state'] = 'readonly'
        if model.getSET_download():
            self.ComboSET.set('YES')
        else:
            self.ComboSET.set('NO')

        ######## Download mai ########

        self.LblmaiDownload = ttk.Label(self.LblframeSetting, text="Download mai : ")
        self.LblmaiDownload.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.maiDownload_var = tk.StringVar()
        self.Combomai = ttk.Combobox(self.LblframeSetting, textvariable = self.maiDownload_var)
        self.Combomai.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)
        self.Combomai['values'] = ('YES', 'NO')
        self.Combomai['state'] = 'readonly'
        if model.getmai_download():
            self.Combomai.set('YES')
        else:
            self.Combomai.set('NO')

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
        
        ######## Main Screen Position ########

        self.LblposLoad = ttk.Label(self.LblframeSetting, text="Load Progress Position (x,y) : ")
        self.LblposLoad.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)

        self.posLoad_x = tk.StringVar()
        self.Txt_Load_x = ttk.Entry(self.LblframeSetting, textvariable = self.posLoad_x)
        self.Txt_Load_x.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_Load_x.insert(tk.END, model.getload_screen_x())

        self.posLoad_y = tk.StringVar()
        self.Txt_Load_y = ttk.Entry(self.LblframeSetting, textvariable = self.posLoad_y)
        self.Txt_Load_y.grid(row=3, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Txt_Load_y.insert(tk.END, model.getload_screen_y())

        self.SavePreference = ttk.Button(self, text='Save Preference')
        self.SavePreference.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E)