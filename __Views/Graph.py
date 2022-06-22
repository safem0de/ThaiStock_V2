import tkinter as tk
from matplotlib import axes, axis
import mplfinance as mpf
import pandas as pd

from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class Graph(tk.Tk):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.state('zoomed')
        self.protocol("WM_DELETE_WINDOW",func=lambda: self.destroy())

        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.X)

        self.LblframePeriod = ttk.LabelFrame(self.frame, text="Period of Charts")
        self.LblframePeriod.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

        self.LblframeIndicator = ttk.LabelFrame(self.frame, text="Indicators")
        self.LblframeIndicator.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

        selected_period = tk.StringVar()
        period = (('1 Day', '1d'),
                ('5 Days', '5d'),
                ('1 Month', '1mo'),
                ('3 Months', '3mo'),
                ('6 Months', '6mo'),
                ('1 Year', '1y'),
                ('2 Year', '2y'),
                ('5 Year', '5y'))

        for p in period:
            r = ttk.Radiobutton(
                self.LblframePeriod,
                text=p[0],
                value=p[1],
                variable=selected_period
            )
            r.pack(side=tk.LEFT, padx=5, pady=5)

        indicator = (
                ('EMA 12,26', 'ema'),
                ('SMA', 'sma'),
                ('Bollinger Band', 'bol'),
                ('MACD', 'macd'),
                ('RSI', 'rsi'),
                ('Renko', 'ren'),
                )
        
        for i in indicator:
            c = ttk.Checkbutton(
                self.LblframeIndicator,
                text=i[0],
                variable=i[1],
            )
            c.pack(side=tk.LEFT, padx=5, pady=5)

    def RemoveLabel(self, ax:axis):
        ax.grid(True)
        for tick in ax.xaxis.get_major_ticks():
            tick.tick1line.set_visible(False)
            tick.tick2line.set_visible(False)
            tick.label1.set_visible(False)
            tick.label2.set_visible(False)


    def create_view(self, dataframe:pd.DataFrame):

        exp12 = dataframe['Close'].ewm(span=12, adjust=False).mean()
        exp26 = dataframe['Close'].ewm(span=26, adjust=False).mean()

        macd = exp12 - exp26

        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        self.fig = mpf.figure(style='yahoo', figsize=(15,6))
        self.fig.suptitle(dataframe.Name)
        self.fig.subplots_adjust(hspace=0.001)

        ax1 = self.fig.add_subplot(321)
        ax2 = self.fig.add_subplot(323, sharex = ax1)
        ax3 = self.fig.add_subplot(325, sharex = ax1)

        self.RemoveLabel(ax1)
        self.RemoveLabel(ax2)

        ax4 = self.fig.add_subplot(322)

        # ax1.grid(True)
        # for tick in ax1.xaxis.get_major_ticks():
        #     tick.tick1line.set_visible(False)
        #     tick.tick2line.set_visible(False)
        #     tick.label1.set_visible(False)
        #     tick.label2.set_visible(False)

        # ax2.grid(True)
        # for tick in ax2.xaxis.get_major_ticks():
        #     tick.tick1line.set_visible(False)
        #     tick.tick2line.set_visible(False)
        #     tick.label1.set_visible(False)
        #     tick.label2.set_visible(False)
        
        ap = [
            # mpf.make_addplot(exp12, color='lime', ax=ax1),
            # mpf.make_addplot(exp26, color='c', ax=ax1),
            
            mpf.make_addplot(histogram,type='bar',
                            color='dimgray', ax=ax2),#secondary_y=False,
            mpf.make_addplot(macd, color='fuchsia', ax=ax2),#secondary_y=True,
            mpf.make_addplot(signal, color='b', ax=ax2),#secondary_y=True,
            ]

        mpf.plot(dataframe, ax=ax1, volume=ax3, addplot=ap, xrotation=10, type='candle')

        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.X, padx=5, pady=5)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.X)

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)

        canvas.mpl_connect("key_press_event", on_key_press)
