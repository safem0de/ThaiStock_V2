import tkinter as tk
from tkinter import ttk

class Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}

    def create_view(self, frame):
        self.create_button(frame, name="Stock_NEWS", row=0, column=0)
        self.create_button(frame, name="Stock_Analysis", row=1, column=0)
        self.create_button(frame, name="Candle_Stick", row=2, column=0)
        self.create_button(frame, name="Magic_Formula", row=3, column=0)

        self.create_button(frame, name="Preferences", row=98, column=0)
        self.create_button(frame, name="Bibiology", row=99, column=0)

    def create_entry(self, frame, label, row, column, textvar):
        label_frame = tk.LabelFrame(frame, text=label)
        self.entries[label] = tk.Entry(label_frame, textvariable=textvar)
        self.entries[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)

    def create_button(self, frame, name, row, column):
        self.style = ttk.Style()
        self.style.configure('big.TButton', font=('Bahnschrift SemiBold', 12), foreground = "blue4")

        self.buttons[name] = ttk.Button(frame)
        self.buttons[name]["text"] = str(name).replace("_"," ")
        self.buttons[name]["style"] = "big.TButton"
        self.buttons[name].grid(row=row, column=column, padx=3, sticky=tk.NW + tk.E)

    def create_combobox(self, frame, label, values, row, column):
        label_frame = tk.LabelFrame(frame, text=label)
        self.comboboxes[label] = ttk.Combobox(label_frame, values=values)
        self.comboboxes[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)

