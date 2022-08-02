import tkinter as tk
from tkinter import ttk

import numpy as np
from matplotlib import axis

import mplfinance as mpf
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

from __Controllers.MplController import CandleController
from __Models import Stocks

class Graph(tk.Tk):

    def __init__(self, model:Stocks):
        super().__init__()
        self.model = model
        n = self.model.getSelected_StockName().replace('%26','&').replace('+',' ').replace('.BK','')
        self.title(f'Candle Stick : {n}')

    def create_view(self):

        def RemoveLabel(ax:axis):
            ax.grid(True)
            for tick in ax.xaxis.get_major_ticks():
                tick.tick1line.set_visible(False)
                tick.tick2line.set_visible(False)
                tick.label1.set_visible(False)
                tick.label2.set_visible(False)

        def rma(x, n, y0):
            a = (n-1) / n
            ak = a**np.arange(len(x)-1, -1, -1)
            return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]

        def relative_strength(df:pd.DataFrame, dfName ,n = 14):
            try:
                df['change'] = df[dfName].diff() # Calculate change
                df['gain'] = df.change.mask(df.change < 0, 0.0)
                df['loss'] = -df.change.mask(df.change > 0, -0.0)
                df['avg_gain'] = rma(df.gain[n+1:].to_numpy(), n, np.nansum(df.gain.to_numpy()[:n+1])/n)
                df['avg_loss'] = rma(df.loss[n+1:].to_numpy(), n, np.nansum(df.loss.to_numpy()[:n+1])/n)
                df['rs'] = df.avg_gain / df.avg_loss
                df['rsi_14'] = 100 - (100 / (1 + df.rs))
                return df['rsi_14'].squeeze()
            except:
                pass

        def create_candle(df:pd.DataFrame):

            exp12 = df['Close'].ewm(span=12, adjust=False).mean() ## pd.Series
            exp26 = df['Close'].ewm(span=26, adjust=False).mean()

            macd = exp12 - exp26

            signal = macd.ewm(span=9, adjust=False).mean()
            histogram = macd - signal

            rsi = relative_strength(df,'Close')
            rsi_upper = pd.Series(70, index=df.index)
            rsi_lower = pd.Series(30, index=df.index)

            fig = mpf.figure(style='yahoo', figsize=(9, 8))
            fig.suptitle(name.replace('.BK',''))
            gs0 = fig.add_gridspec(2, 2, left=0.05, right=0.95, wspace=0.05, hspace=0.02)

            gs00 = gs0[0].subgridspec(3, 1)
            gs01 = gs0[1].subgridspec(3, 1)
            gs02 = gs0[2].subgridspec(3, 1, hspace=0.02)
            gs03 = gs0[3].subgridspec(3, 1)

            ax0 = fig.add_subplot(gs00[0:, 0])
            ax0.text(0.5, 0.5, 'Safem0de\ncandle stick', transform=ax0.transAxes,
            fontsize=20, color='gray', alpha=0.4,
            ha='center', va='center', rotation='20')
            RemoveLabel(ax0)

            ax1 = fig.add_subplot(gs02[0, 0],sharex = ax0)
            ax2 = fig.add_subplot(gs02[1, 0],sharex = ax0)
            ax3 = fig.add_subplot(gs02[2, 0],sharex = ax0)

            RemoveLabel(ax1)
            RemoveLabel(ax2)

            ax4 = fig.add_subplot(gs01[0:, 0], sharey=ax0)
            ax4.text(0.5, 0.5, 'Safem0de\nrenko (movement)', transform=ax4.transAxes,
            fontsize=20, color='gray', alpha=0.4,
            ha='center', va='center', rotation='20')

            try:
                ax0.annotate(
                    f'Open  : {round(df["Open"].iloc[-1],2)}\nClose : {round(df["Close"].iloc[-1],2)}\nHigh  : {round(df["High"].iloc[-1],2)}\nLow   : {round(df["Low"].iloc[-1],2)}',
                    xy=(0.02,0.8),
                    xycoords='axes fraction',
                    size=8,
                    bbox=dict(boxstyle="round", fc=(0.9, 0.9, 0.9, 0.4), ec="none"))

                ax2.annotate(f'MACD = {round(macd.values[-1],2)}',xy=(0.02,0.8),
                xycoords='axes fraction',
                size=8,
                bbox=dict(boxstyle="round", fc=(0.9, 0.9, 0.9, 0.4), ec="none"))

                ax3.annotate(f'RSI = {round(rsi.values[-1],2)}',xy=(0.02,0.8),
                    xycoords='axes fraction',
                    size=8,
                    bbox=dict(boxstyle="round", fc=(0.9, 0.9, 0.9, 0.4), ec="none"))

                ap = [
                    mpf.make_addplot(exp12, color='y', ax=ax0),
                    mpf.make_addplot(exp26, color='c', ax=ax0),
                    
                    mpf.make_addplot(histogram,type='bar',
                                alpha=1,secondary_y=False,
                                color='black', ax=ax2),
                    mpf.make_addplot(macd, color='fuchsia', ax=ax2),
                    mpf.make_addplot(signal, color='b', ax=ax2),

                    mpf.make_addplot(rsi_upper, color='mediumvioletred', ax=ax3),
                    mpf.make_addplot(rsi_lower, color='deeppink', ax=ax3),
                    mpf.make_addplot(rsi, color='indigo', ax=ax3),
                ]

                mpf.plot(df,ax=ax0,volume=ax1,type='candle', addplot=ap, xrotation=10)
                mpf.plot(df,ax=ax4,type='renko')
                
                canvas = FigureCanvasTkAgg(fig, master=self.frameChart)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.Y, expand=1, padx=5, pady=5)

                toolbar = NavigationToolbar2Tk(canvas, self.frameChart)
                toolbar.update()
                canvas.get_tk_widget().pack(fill=tk.X)

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)
            except:
                pass


        def radioButton_selected(p):
            for widgets in self.frameChart.winfo_children():
                widgets.destroy()
            a = CandleController.create_graph(self, st_Name=name, period=p)
            # print(a)
            # print(p)
            create_candle(a)

        name = str(self.model.getSelected_StockName().replace('%26','&').replace('+',' '))

        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.LblframePeriod = ttk.LabelFrame(self.frame, text="Period of Charts")
        self.LblframePeriod.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)

        ### https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/
        selected_period = tk.StringVar(self,'1y')
        period = (
                # ('1 Day', '1d'),
                # ('5 Days', '5d'),
                ('1 Month', '1mo'),
                ('3 Months', '3mo'),
                ('6 Months', '6mo'),
                ('1 Year', '1y'),
                ('2 Year', '2y'),
                # ('5 Year', '5y'),
                )

        for p in period:
            r = ttk.Radiobutton(
                self.LblframePeriod,
                text=p[0],
                value=p[1],
                variable=selected_period,
                command = lambda : radioButton_selected(selected_period.get())
            )
            r.pack(side=tk.LEFT, padx=5, pady=5)

        self.frameChart = ttk.Frame(self.frame)
        self.frameChart.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)
        radioButton_selected('1y')