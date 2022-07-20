from tkinter import *
import tkinter as tk
from tkinter.ttk import *

import mplfinance as mpf
import matplotlib.pyplot as plt
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

def example_plot(ax, fontsize=12):
    ax.plot([1, 2])


if __name__ == '__main__':
    app = App()
    # app.fig = mpf.figure(style='yahoo', figsize=(15,6))
    plt.close('all')
    app.fig = plt.figure()

    ax1 = plt.subplot2grid((3, 3), (0, 0))
    ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
    ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

    example_plot(ax1)
    example_plot(ax2)
    example_plot(ax3)
    example_plot(ax4)

    plt.tight_layout()

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