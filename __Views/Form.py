import tkinter as tk
from tkinter import ttk

class Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}

    def create_entry(self, frame, label, row, column, textvar):
        label_frame = tk.LabelFrame(frame, text=label)
        self.entries[label] = tk.Entry(label_frame, textvariable=textvar)
        self.entries[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)

    def create_button(self, frame, name, row, column):
        self.buttons[name] = tk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name]["anchor"] = tk.W
        self.buttons[name]["font"] = ('Bahnschrift SemiLight Condensed', 12)
        self.buttons[name]["foreground"] = "blue4"
        self.buttons[name].grid(row=row, column=column, padx=3, sticky=tk.NW + tk.E)

    def create_combobox(self, frame, label, values, row, column):
        label_frame = tk.LabelFrame(frame, text=label)
        self.comboboxes[label] = ttk.Combobox(label_frame, values=values)
        self.comboboxes[label].grid(row=1, column=1)
        label_frame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)