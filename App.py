import ast
from threading import Thread
import tkinter as tk
from __Controllers.SideButtonController import ButtonController
from __Controllers.TableController import TableController
from __Controllers.ProgressController import ProgressController
from __Views.Form import Form
from __Views.Table import Table
from __Views.Images import ICON
from __Models.Stocks import Stock
from __Models.Settings import Setting
from tkinter import Frame, Label, ttk

import importlib, os, asyncio, random
from ttkthemes import ThemedStyle
import tempfile
import cryptocode

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

class Loading(tk.Tk):

    def __init__(self, model:Setting):
        super().__init__()

        def disable_event():
            pass

        self.protocol("WM_DELETE_WINDOW", func=disable_event)
        self.geometry(f'+{model.getload_screen_x()}+{model.getload_screen_y()}')
        self.title('Download Stock Data')
        self.iconbitmap(default=ICON_PATH)
        self.resizable(0, 0)

        print('Loading...')
        self.style = ttk.Style()
        self.style.configure('big.TButton', font=('Bahnschrift SemiBold', 12), foreground = "blue4")

class Button(ttk.Button):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def add_button(self, controller:ButtonController, view:Form, frame:Frame,):
        view = view(self.master)
        controller.bind(view, frame)
        
class Application(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=1, rowspan=100, sticky=tk.N + tk.S + tk.E + tk.W)

        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Bahnschrift SemiLight Condensed', 14))

    def new_tab(self, controller:TableController, view:Table, model:Stock, name:str):
        view = view(self.master, model)
        controller.bind(model, view, name)
        self.add(view, text=name)

class LblFrame(tk.LabelFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['text'] ='Datas prepared by Safem0de '
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=10)
        [self.rowconfigure(i, weight=1) for i in range(100)]
        self.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

class App(tk.Tk):
    def __init__(self, model:Setting):
        super().__init__()

        if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
            import PyInstaller as pyi_splash
            # import pyi_splash
            pyi_splash.update_text('UI Loaded ...')
            pyi_splash.close()
        
        self.title('Safem0de Stock Version 0.3.1')
        self.iconbitmap(default=ICON_PATH)
        self.geometry(f'+{model.getstart_screen_x()}+{model.getstart_screen_y()}')

        self.style = ThemedStyle(self)
        self.style.set_theme("clearlooks")
        print('MainMenu')

if __name__ == "__main__":

    setting = Setting()
    try:
        f = open("App_Safem0de.config", "r")
        str_decoded = cryptocode.decrypt(f.read(), 'S@fem0de')
        res = ast.literal_eval(str_decoded)

        print(res)

        if res:
            setting.setSET_download(res['SET_download'])
            setting.setmai_download(res['mai_download'])
            setting.setload_screen_x(res['load_screen_x'])
            setting.setload_screen_y(res['load_screen_y'])
            setting.setstart_screen_x(res['start_screen_x'])
            setting.setstart_screen_y(res['start_screen_y'])
            setting.setanalyse_screen_x(res['analyse_screen_x'])
            setting.setanalyse_screen_y(res['analyse_screen_y'])
        else:
            pass
    except Exception as e:
        print(e)

    stock = Stock()
    load = Loading(setting)

    async def ShowLoading():
        await asyncio.sleep(delay=random.uniform(0, 0.0001))
        load.mainloop()

    async def ShowProgress_SET():

        def update_progressSET_label():
            return f"Current Progress: {round(pb_S['value'],1)}%"

        def update_SETname_label(name):
            return f"SET : {name}"

        def progress(pb: ttk.Progressbar, val ,Market, name):
            if pb['value'] < 100:
                pb['value'] = val
                if Market == 'SET':
                    SET_name_label['text'] = ""
                    value_label_SET['text'] = ""
                    SET_name_label['text'] = update_SETname_label(name)
                    value_label_SET['text'] = update_progressSET_label()
            else:
                pass

        SET_name_label = ttk.Label(load, text="")
        SET_name_label.grid(column=0, row=0, columnspan=5, padx=10, pady=20, sticky=tk.N+ tk.S+ tk.E+ tk.W)

        # progressbar
        pb_S = ttk.Progressbar(
            load,
            orient='horizontal',
            mode='determinate',
            length=280,
            name='set'
        )
        # place the progressbar
        pb_S.grid(column=0, row=1, columnspan=5, padx=10, sticky=tk.N+ tk.S+ tk.E+ tk.W)

        # label
        value_label_SET = ttk.Label(load, text=update_progressSET_label())
        value_label_SET.grid(column=0, row=2, columnspan=5, padx=10, pady=20, sticky=tk.N+ tk.S+ tk.E+ tk.W)
        
        def update(progressbar:ttk.Progressbar, MarketName):

            count = 0
            progress_controller = ProgressController()
            x = stock.getMarket().get(MarketName)
            for k in x:
                val = progress_controller.createStock(k)
                fin = progress_controller.Fin_Dataframe(k)

                if MarketName == 'SET':
                    stock.setMarket_SET({
                        k : {
                            'data':val,
                            'fin_data': fin,
                            'isSET50': None,
                            'isSET100': None,
                            'ismai': False,
                            }
                        })
                    count += 1
                else:
                    stock.setMarket_mai({
                        k : {
                            'data':val,
                            'fin_data': fin,
                            'isSET50': False,
                            'isSET100': False,
                            'ismai': True,
                            }
                        })
                    count += 1

                progress(progressbar, (count/len(x))*100, MarketName, k)
                progressbar.update_idletasks()
        
        Thread(update(pb_S,'SET')).start()
    
    async def ShowProgress_mai():

        def update_progressmai_label():
            return f"Current Progress: {round(pb_m['value'],1)}%"

        def update_mainame_label(name):
            return f"mai : {name}"

        def progress(pb: ttk.Progressbar, val ,Market, name):
            if pb['value'] < 100:
                pb['value'] = val
                if Market == 'mai':
                    mai_name_label['text'] = ""
                    value_label_mai['text'] = ""
                    mai_name_label['text'] = update_mainame_label(name)
                    value_label_mai['text'] = update_progressmai_label()
            else:
                pass

        mai_name_label = ttk.Label(load, text="")
        mai_name_label.grid(column=0, row=3, columnspan=5, padx=10, pady=20, sticky=tk.N+ tk.S+ tk.E+ tk.W)

        pb_m = ttk.Progressbar(
            load,
            orient='horizontal',
            mode='determinate',
            length=280,
            name='mai'
        )
        # place the progressbar
        pb_m.grid(column=0, row=4, columnspan=5, padx=10, sticky=tk.N+ tk.S+ tk.E+ tk.W)

        value_label_mai = ttk.Label(load, text=update_progressmai_label())
        value_label_mai.grid(column=0, row=5, columnspan=5, padx=10, pady=20, sticky=tk.N+ tk.S+ tk.E+ tk.W)
        
        def update(progressbar:ttk.Progressbar, MarketName):

            count = 0
            progress_controller = ProgressController()
            x = stock.getMarket().get(MarketName)
            for k in x:
                val = progress_controller.createStock(k)
                fin = progress_controller.Fin_Dataframe(k)
                if MarketName == 'SET':
                    stock.setMarket_SET({
                        k : {
                            'data':val,
                            'fin_data': fin,
                            'isSET50': None,
                            'isSET100': None,
                            'ismai': False,
                            }
                        })
                    count += 1
                else:
                    stock.setMarket_mai({
                        k : {
                            'data':val,
                            'fin_data': fin,
                            'isSET50': False,
                            'isSET100': False,
                            'ismai': True,
                            }
                        })
                    count += 1

                progress(progressbar, (count/len(x))*100, MarketName, k)
                progressbar.update_idletasks()

        Thread(update(pb_m,'mai')).start()

    async def ShowMain():
        BtnClose = ttk.Button(load, text='Close', command=lambda: load.destroy(),style='big.TButton')
        BtnClose.grid(column=0, row=6, columnspan=5, padx=10, pady=20, sticky=tk.E + tk.W)
        BtnClose.focus()

        await asyncio.sleep(delay=random.uniform(0.0001, 0.0002))
        root = App(setting)
        root.protocol("WM_DELETE_WINDOW",func=lambda:root.quit())

        lb = Label(master=root)
        lb['text'] ='SET, mai Stock and CryptoCurrency'
        lb['font'] = ("Impact", 18)
        lb.grid(row=0, column=0, padx=3, sticky=tk.N + tk.S + tk.W)
        label_frame = LblFrame(master=root)

        button = Button(master=label_frame)
        button_controller = ButtonController(stock, setting)
        
        button.add_button(view=Form, controller=button_controller, frame=label_frame)

        app = Application(master=label_frame)
        table_controller = TableController(stock)
        app.new_tab(view=Table, controller=table_controller, model=stock, name="SET")
        app.new_tab(view=Table, controller=table_controller, model=stock, name="mai")
        app.new_tab(view=Table, controller=table_controller, model=stock, name="Crypto")

        root.mainloop()

    async def sequencial():

        task1 = asyncio.create_task(ShowLoading())

        if bool(setting.getSET_download()):
            task2 = asyncio.create_task(ShowProgress_SET())
            await task2
        else:
            pass

        if bool(setting.getmai_download()):
            task3 = asyncio.create_task(ShowProgress_mai())
            await task3
        else:
            pass

        task4 = asyncio.create_task(ShowMain())

        await task1

    asyncio.run(sequencial())