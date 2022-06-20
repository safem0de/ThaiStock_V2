import tkinter as tk
import matplotlib
import mplfinance as mpf
import pandas as pd

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from __Controllers.MplController import MplController

class Graph(tk.Toplevel):

    def __init__(self):
        super().__init__()

    def create_view(self, dataframe:pd.DataFrame):

        exp12 = dataframe['Close'].ewm(span=12, adjust=False).mean()
        exp26 = dataframe['Close'].ewm(span=26, adjust=False).mean()

        macd = exp12 - exp26

        signal    = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        self.fig = mpf.figure(style='yahoo',figsize=(7,8))
        ax1 = self.fig.add_subplot(3,1,1)
        ax2 = self.fig.add_subplot(3,1,2)
        ax3 = self.fig.add_subplot(3,1,3)

        ap = [
            # mpf.make_addplot(exp12, color='lime', ax=ax1),
            # mpf.make_addplot(exp26, color='c', ax=ax1),
            
            mpf.make_addplot(histogram,type='bar',width=0.7,panel=1,
                            color='dimgray',alpha=1,secondary_y=False, ax=ax2),
            mpf.make_addplot(macd,panel=1,color='fuchsia',secondary_y=True, ax=ax2),
            mpf.make_addplot(signal,panel=1,color='b',secondary_y=True, ax=ax2),
            ]

        mpf.plot(dataframe, ax=ax1, volume=ax3, addplot=ap, xrotation=0, type='candle')

        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
