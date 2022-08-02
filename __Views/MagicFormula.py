from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from __Models import Stocks

class magicFormula(tk.Toplevel):

    def __init__(self):
        super().__init__()

    def create_view(self, model:Stocks):
        self.title('Magic Formula requested by MJ & Friends')
        self.geometry('+1921+10')
        # self.state('zoomed')