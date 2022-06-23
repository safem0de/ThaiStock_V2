from tkinter import *
import tkinter as tk
from tkinter.ttk import *

from matplotlib import axis
import mplfinance as mpf
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.title('Insert Slot Checking by Safem0de V 0.1.0')
        self.title('test') ## 25/02/2022
        self.geometry('+10+10')
        self.protocol("WM_DELETE_WINDOW",func=lambda: self.quit())

        self.dataframe = pd.read_csv('D:\\My Documents\\Desktop\\mplfin.csv')
        self.dataframe.index = pd.to_datetime(self.dataframe['Date'])
        self.dataframe.drop(columns=self.dataframe.columns[1])

        print(self.dataframe)

if __name__ == '__main__':
    app = App()
    app.fig = mpf.figure(style='yahoo', figsize=(15,6))
    ax1 = app.fig.add_subplot(111)
    mpf.plot(app.dataframe,
            type='hollow_candle',
            ax=ax1,)

    # mpf.plot(
    #         app.dataframe,
    #         panel_ratios=(2, 1, 3, 1),
    #         type="hollow_candle",
    #         volume=True,
    #         style='yahoo',
    #         figsize=(12.8, 10),
    #         # addplot=ap0,
    #         main_panel=2,
    #         volume_panel=3,
    #         num_panels=4,)

    canvas = FigureCanvasTkAgg(app.fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.X, padx=5, pady=5)

    toolbar = NavigationToolbar2Tk(canvas, app)
    toolbar.update()
    canvas.get_tk_widget().pack(fill=tk.X)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect("key_press_event", on_key_press)

    app.mainloop()