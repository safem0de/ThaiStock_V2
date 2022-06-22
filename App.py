
from threading import Thread
import tkinter as tk
from __Controllers.SideButtonController import ButtonController
from __Controllers.TableController import TableController
from __Controllers.ProgressController import ProgressController
from __Views.Form import Form
from __Views.Table import Table
from __Models.Stocks import Stock
from tkinter import Frame, Label, ttk

import importlib, os, asyncio, random
from ttkthemes import ThemedStyle

class Loading(tk.Tk):

    def __init__(self):
        super().__init__()

        def disable_event():
            pass

        self.protocol("WM_DELETE_WINDOW", func=disable_event)
        self.geometry('+1921+10')
        self.title('Download Stock Data')
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
    def __init__(self):
        super().__init__()

        if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
            import PyInstaller as pyi_splash
            pyi_splash.update_text('UI Loaded ...')
            pyi_splash.close()
        
        self.title('Safem0de Stock Version 0.3')
        self.geometry(f'{int(self.winfo_screenwidth()*0.975)}x{int(self.winfo_screenheight()*0.7)}+1910+0')
        self.state('zoomed')

        self.style = ThemedStyle(self)
        self.style.set_theme("clearlooks")
        print('MainMenu')

if __name__ == "__main__":

    stock = Stock()
    load = Loading()

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
        SET_name_label.grid(column=0, row=0, columnspan=5, padx=10, pady=20, sticky=tk.NSEW)

        # progressbar
        pb_S = ttk.Progressbar(
            load,
            orient='horizontal',
            mode='determinate',
            length=280,
            name='set'
        )
        # place the progressbar
        pb_S.grid(column=0, row=1, columnspan=5, padx=10, sticky=tk.NSEW)

        # label
        value_label_SET = ttk.Label(load, text=update_progressSET_label())
        value_label_SET.grid(column=0, row=2, columnspan=5, padx=10, pady=20, sticky=tk.NSEW)
        
        def update(progressbar:ttk.Progressbar, MarketName):
            count = 0
            progress_controller = ProgressController()
            x = stock.getMarket().get(MarketName)
            for k in x:
                val = progress_controller.createStock(k)

                if MarketName == 'SET':
                    stock.setMarket_SET({k : val})
                    count += 1
                else:
                    stock.setMarket_mai({k : val})
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
        mai_name_label.grid(column=0, row=3, columnspan=5, padx=10, pady=20, sticky=tk.NSEW)

        pb_m = ttk.Progressbar(
            load,
            orient='horizontal',
            mode='determinate',
            length=280,
            name='mai'
        )
        # place the progressbar
        pb_m.grid(column=0, row=4, columnspan=5, padx=10, sticky=tk.NSEW)

        value_label_mai = ttk.Label(load, text=update_progressmai_label())
        value_label_mai.grid(column=0, row=5, columnspan=5, padx=10, pady=20, sticky=tk.NSEW)
        
        def update(progressbar:ttk.Progressbar, MarketName):
            count = 0
            progress_controller = ProgressController()
            x = stock.getMarket().get(MarketName)
            for k in x:
                val = progress_controller.createStock(k)

                if MarketName == 'SET':
                    stock.setMarket_SET({k : val})
                    count += 1
                else:
                    stock.setMarket_mai({k : val})
                    count += 1

                progress(progressbar, (count/len(x))*100, MarketName, k)
                progressbar.update_idletasks()

        Thread(update(pb_m,'mai')).start()

    async def ShowMain():
        BtnClose = ttk.Button(load, text='Close', command=lambda: load.destroy(),style='big.TButton')
        BtnClose.grid(column=0, row=6, columnspan=5, padx=10, pady=20, sticky=tk.E + tk.W)
        BtnClose.focus()

        await asyncio.sleep(delay=random.uniform(0.0001, 0.0002))
        root = App()
        root.protocol("WM_DELETE_WINDOW",func=lambda:root.quit())

        lb = Label(master=root)
        lb['text'] ='SET & mai Stock'
        lb['font'] = ("Impact", 18)
        lb.grid(row=0, column=0, padx=3, sticky=tk.N + tk.S + tk.W)
        label_frame = LblFrame(master=root)

        button = Button(master=label_frame)
        button_controller = ButtonController(stock)
        
        button.add_button(view=Form, controller=button_controller, frame=label_frame)

        app = Application(master=label_frame)
        table_controller = TableController(stock)
        app.new_tab(view=Table, controller=table_controller, model=stock, name="SET")
        app.new_tab(view=Table, controller=table_controller, model=stock, name="mai")
        app.new_tab(view=Table, controller=table_controller, model=stock, name="Crypto")

        root.mainloop()

    async def sequencial():
        task1 = asyncio.create_task(ShowLoading())
        # task2 = asyncio.create_task(ShowProgress_SET())
        # task3 = asyncio.create_task(ShowProgress_mai())
        task4 = asyncio.create_task(ShowMain())
        await task1
        # await task2
        # await task3

    asyncio.run(sequencial())