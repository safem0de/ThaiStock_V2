import tkinter as tk
from tkinter import ttk

import numpy as np
from matplotlib import axis
import mplfinance as mpf
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler


class Graph(tk.Tk):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.state('zoomed')
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

    

    def create_view(self, df:pd.DataFrame):

        exp12 = df['Close'].ewm(span=12, adjust=False).mean()
        exp26 = df['Close'].ewm(span=26, adjust=False).mean()

        macd = exp12 - exp26

        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        fig = mpf.figure(style='yahoo')
        fig.suptitle(df.Name)
        gs0 = fig.add_gridspec(2, 2, left=0.05, right=0.95, wspace=0.05, hspace=0.02)

        gs00 = gs0[0].subgridspec(3, 1)
        gs01 = gs0[1].subgridspec(3, 1)
        gs02 = gs0[2].subgridspec(3, 1, hspace=0.02)
        gs03 = gs0[3].subgridspec(3, 1)

        ax0 = fig.add_subplot(gs00[0:, 0])
        ax0.text(0.5, 0.5, 'Safem0de', transform=ax0.transAxes,
        fontsize=20, color='gray', alpha=0.4,
        ha='center', va='center', rotation='20')
        self.RemoveLabel(ax0)

        ax1 = fig.add_subplot(gs02[0, 0],sharex = ax0)
        ax2 = fig.add_subplot(gs02[1:, 0],sharex = ax0)

        self.RemoveLabel(ax1)

        ax4 = fig.add_subplot(gs01[0:, 0],sharey = ax0)
        ax4.text(0.5, 0.5, 'Safem0de', transform=ax4.transAxes,
        fontsize=20, color='black', alpha=0.4,
        ha='center', va='center', rotation='20')

        ap = [
            mpf.make_addplot(exp12, color='y', ax=ax0),
            mpf.make_addplot(exp26, color='c', ax=ax0),
            
            mpf.make_addplot(histogram,type='bar',
                        alpha=1,secondary_y=False,
                        color='gray', ax=ax2),
            mpf.make_addplot(macd, color='fuchsia', ax=ax2),
            mpf.make_addplot(signal, color='b', ax=ax2),
            ]

        mpf.plot(df,ax=ax0,volume=ax1,type='candle', addplot=ap, xrotation=10)
        mpf.plot(df,ax=ax4,type='renko')

        print(df)
        
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.X, padx=5, pady=5)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.X)

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)

        canvas.mpl_connect("key_press_event", on_key_press)
