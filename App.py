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
import tempfile

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x00\x00\x00\x00h\x04\x00'
b'\x00\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01'
b'\x00 \x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\xff\xff\xff\x00\x19\x19\x00\x02\x0e\x0e\x00\x1c\x00\x00'
b'\x00\x0f\x00\x00\x00\x01\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00%%\x00E9Q\x18'
b'\xb1\\\x93D\xf5q\x99T\xfePt)\xeb$-\x00\x9c\x11\x12\x00=\x00\x00\x00\x0e\xff'
b'\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff'
b'\xff\xff\x00%&\x0074G\x12\xa6V\x8a=\xf2~\xcfs\xff\xa2\xff\xa1\xff\x8e\xf0'
b'\x8b\xff\xcf\xda\xc5\xff\xff\xff\xff\xff\xd6\xe9\xcc\xff\x8d\xb3r'
b'\xfeFh\x1e\xe3"(\x00\x91\x0e\x0e\x004\x00\x00\x00\x03\xff\xff\xff\x0023'
b'\x00#h\xa7T\xff\x9b\xfa\x9a\xff\x97\xfa\x97\xff\x88\xf2\x87\xffx\xeaw'
b'\xffh\xe2h\xff\x9a\xb9\x87\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xff\xff\xfd\xfe\xfd\xff\xcb\xe2\xbf\xff=O\x15\xd7\x00\x00\x00\t'
b'\xff\xff\xff\x0045\x03U\x87\xe9\x83\xff}\xed}\xffh\xd7d\xffK\x81-\xffkW\x15'
b'\xfffT\x18\xffE\x7f>\xffj\xa4[\xff\xab\xcf\x98\xff\xf0\xf7\xed\xff\xff'
b'\xff\xff\xff\xff\xff\xff\xffPQ3\xae\xff\xff\xff\x00\xff\xff\xff\x000.'
b'\x00NK\x7f-\xffjW\x14\xff\xabg\x18\xff\xea\x8d\'\xff\xc1\x7f.\xff\xfc\xf4'
b'\xef\xff\xe7\xbd\x9e\xff\xac{I\xffPZ\x1b\xff@\x80:\xffp\xa7^\xff\xb5\xcd'
b'\xa6\xffKO*\xbf\x00\x00\x00\rP6\x03x\xa3b\x15\xfb\xe3\x89%\xff\xff\x9e/\xff'
b'\xf6\x93*\xff\xee\x88&\xff\xb1o*\xff\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xff\xff\xff\xfc\xf2\xeb\xff\xe3\xb7\x98\xff\x9am9\xffJ~J\xfc5N\x18'
b'\x9d\x00\x00\x00\x03\x86W\x10\xd5\xf7\x94+\xff\xef\x89\'\xff\xe6\x7f#'
b'\xff\xdfx\x1f\xff\xc2o\x1b\xff\xaes*\xff\x9csg\xffTL\x8e\xffHH\x92\xff\xa2'
b'\xa2\xb4\xff\xe8\xe8\xe8\xff\xd1\xc1\xae\xff!\x19\x00D\xff\xff\xff'
b'\x00\xff\xff\xff\x00\x89R\x0f\xe4\xe0x \xff\xc8r\x1d\xff\xb9y,\xff\x92hD'
b'\xffT;b\xff@=\xa8\xffqo\xe4\xffji\xcd\xff\xe4\xe4\xfa\xff\x8e\x8e\xe0\xff@?'
b'\xab\xff?;v\xff\x02\x02\x1ew\x00\x00\x00\x14\x00\x00\x00\x02_?\x06\x9c'
b'\xb6\x85A\xff\xa9{[\xff=:\xa1\xffih\xdc\xff\x9b\x99\xff\xff\x86\x84\xff'
b'\xffqp\xff\xffDD\xc8\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xdd\xdd\xf8\xff\x86\x86\xdb\xff,,\x9f\xee\x00\x00-^\xff\xff\xff'
b'\x00D2\x00-?8{\xe7\x88\x86\xff\xffsr\xff\xff^]\xff\xffRR\xff\xffZY\xea\xffOM\xbd'
b'\xff\x81\x81\xdf\xff\xd5\xd5\xf7\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xff\xff\xff\xff\xc1\xc1\xe5\xff\x00\x00:^\xff\xff\xff\x00\xff'
b'\xff\xff\x00&%\x9d\xd2PP\xff\xff\\[\xf0\xffWV\xcb\xffoo\xcf\xff~}\xee\xff{{\xff'
b'\xffss\xff\xffjj\xf8\xffcc\xdd\xff\x8e\x8e\xe3\xff\xe2\xe2\xfa\xff\xc5'
b'\xc5\xe1\xff\x00\x00\'N\xff\xff\xff\x00\xff\xff\xff\x00\x0f\x0fr\x8ccb'
b'\xc1\xff\x8a\x89\xe7\xff\x91\x91\xff\xff\x89\x89\xff\xff\x82\x82'
b'\xff\xffzz\xff\xffss\xff\xffkk\xff\xffff\xff\xffff\xff\xffdd\xf3\xff``\xca\xff'
b'\x00\x00<v\xff\xff\xff\x00\xff\xff\xff\x00\x00\x00`\x01\x00\x00`=]]\xa7'
b'\xbf\x90\x90\xe0\xfc\x92\x92\xfd\xff\x81\x81\xff\xffyy\xff\xffrr\xff'
b'\xffjj\xff\xffss\xfd\xffyy\xe0\xfcNN\xa3\xcc\x00\x00NO\x00\x00`\x01\xff\xff'
b'\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\x00\x00`\x04\t\tgLcc\xb5\xd1\x86\x86\xe7\xfe\x81\x81\xe5\xfdWW\xac'
b'\xd6\x07\x07T[\x00\x00`\x05\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff'
b'\xff\x00\x00\x00`\x03\x00\x00`\x03\xff\xff\xff\x00\xff\xff\xff\x00'
b'\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00'
b'\xff\xff\x00\x00\xfc\x1f\x00\x00\xe0\x03\x00\x00\xc0\x01\x00\x00'
b'\xc0\x01\x00\x00\xc0\x01\x00\x00\x80\x01\x00\x00\x00\x07\x00\x00'
b'\x00\x07\x00\x00\x00\x01\x00\x00\xc0\x01\x00\x00\xc0\x01\x00\x00'
b'\xc0\x01\x00\x00\xf0\x03\x00\x00\xfe\x1f\x00\x00\xff\xff\x00\x00' )

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

class Loading(tk.Tk):

    def __init__(self):
        super().__init__()

        def disable_event():
            pass

        self.protocol("WM_DELETE_WINDOW", func=disable_event)
        # self.geometry('+1921+10')
        self.geometry('+20+10')
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
    def __init__(self):
        super().__init__()

        if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
            import PyInstaller as pyi_splash
            # import pyi_splash
            pyi_splash.update_text('UI Loaded ...')
            pyi_splash.close()
        
        self.title('Safem0de Stock Version 0.3.1')
        self.geometry('+1910+0')
        self.iconbitmap(default=ICON_PATH)
        # self.state('zoomed')

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
                            }
                        })
                    count += 1

                progress(progressbar, (count/len(x))*100, MarketName, k)
                progressbar.update_idletasks()
        
        Thread(update(pb_S,'SET')).start()
    
    async def ShowProgress_mai():
        load.withdraw()
        load.update()

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
        task3 = asyncio.create_task(ShowProgress_mai())
        task4 = asyncio.create_task(ShowMain())
        await task1
        # await task2
        await task3

    asyncio.run(sequencial())