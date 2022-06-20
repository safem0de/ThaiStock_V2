import tkinter as tk
from matplotlib.figure import Figure
import mplfinance as mpf
import pandas as pd
import numpy as np

from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure

class Graph(tk.Tk):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.protocol("WM_DELETE_WINDOW",func=lambda: self.destroy())

    def create_view(self, dataframe:pd.DataFrame):

        exp12 = dataframe['Close'].ewm(span=12, adjust=False).mean()
        exp26 = dataframe['Close'].ewm(span=26, adjust=False).mean()

        macd = exp12 - exp26

        signal    = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        self.fig = mpf.figure(style='yahoo', figsize=(6,7))
        ax1 = self.fig.add_subplot(3,1,1)
        ax2 = self.fig.add_subplot(3,1,2, sharex=ax1)
        ax3 = self.fig.add_subplot(3,1,3)

        ap = [
            # mpf.make_addplot(exp12, color='lime', ax=ax1),
            # mpf.make_addplot(exp26, color='c', ax=ax1),
            
            mpf.make_addplot(histogram,type='bar',width=0.7,panel=1,
                            color='dimgray',alpha=1,secondary_y=False, ax=ax2),
            mpf.make_addplot(macd,panel=1,color='fuchsia',secondary_y=True, ax=ax2),
            mpf.make_addplot(signal,panel=1,color='b',secondary_y=True, ax=ax2),
            ]

        mpf.plot(dataframe, ax=ax1, volume=ax3, addplot=ap, xrotation=10, type='candle')

        # self.fig = Figure(figsize=(5, 4), dpi=100)
        # t = np.arange(0, 3, .01)
        # self.fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)

        canvas.mpl_connect("key_press_event", on_key_press)

    # def add_window(self, controller):
    #     view = view(self.master)
    #     controller.bind(view)
