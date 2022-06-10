import tkinter as tk
from __Controllers.SideButtonController import ButtonController
from __Controllers.TableController import TableController
from __Views.Form import Form
from __Views.Table import Table
from __Models.Stocks import *
from tkinter import Frame, ttk

import importlib, os, asyncio

from ttkthemes import ThemedStyle

class Loading(tk.Toplevel):

    def __init__(self,parent):
        super().__init__(parent)

        self.geometry('+20+10')
        self.title('Download Stock Data')

    

    async def createStockCoroutine(MarketType):
        pass
        # mktCtrl = MarketController()
        # mkt = MarketDetail()
                
        # x = mkt.getMarket()
        # y = x.get(MarketType)
        
        # coru = []
        # for i in y:
        #     await asyncio.sleep(delay=random.uniform(0, 0.0001))
        #     coru.append(await mktCtrl.createStock(i))

        #     if MarketType == 'SET':
        #         progress(pb_S,(len(coru)/len(y))*100,MarketType,i)
        #         pb_S.update_idletasks()
        #     elif MarketType == 'mai':
        #         progress(pb_m,(len(coru)/len(y))*100,MarketType,i)
        #         pb_m.update_idletasks()

        # print(y)
        # return coru


class Button(tk.Button):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def add_button(self, controller:ButtonController, view:Form, frame:Frame, name:str, row:int, col:int):
        view = view(self.master)
        controller.bind(view,frame, name, row, col)
        
class Application(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=1, rowspan=100, sticky=tk.N + tk.S + tk.E + tk.W)

        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Bahnschrift SemiLight Condensed', 14))

    def new_tab(self, controller: TableController, view: Table, name: str):
        view = view(self.master)
        controller.bind(view)
        self.add(view, text=name)

class Lbl(tk.Label):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['text'] ='SET & mai Stock'
        self['font'] = ("Impact", 18)
        self.grid(row=0, column=0, padx=3, sticky=tk.N + tk.S + tk.W)

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


if __name__ == "__main__":

    root = App()

    lb = Lbl(master=root)
    label_frame = LblFrame(master=root)
    button = Button(master=label_frame)

    stock = Stock()
    button_controller = ButtonController(stock)
    
    button.add_button(view=Form, controller=button_controller, frame=label_frame, name="Stock NEWS", row=0, col=0)
    button.add_button(view=Form, controller=button_controller, frame=label_frame, name="Stock Analysis", row=1, col=0)
    button.add_button(view=Form, controller=button_controller, frame=label_frame, name="Candle Stick", row=2, col=0)

    app = Application(master=label_frame)
    table_controller = TableController()
    app.new_tab(view=Table, controller=table_controller, name="SET")
    app.new_tab(view=Table, controller=table_controller, name="mai")

    root.mainloop()