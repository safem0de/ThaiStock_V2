import tkinter as tk
from tkinter import ttk
from abc import abstractmethod

class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError

class Table(View):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        
    def create_view(self):
        frame = tk.Frame(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        columns = ('ชื่อย่อหลักทรัพย์','เครื่องหมาย','ล่าสุด','เปลี่ยนแปลง','%เปลี่ยนแปลง','วันก่อนหน้า','เปิด','สูงสุด','ต่ำสุด','ปริมาณ(หุ้น)',"มูลค่า ('000 บาท)",'ราคาเฉลี่ย **')
        tree = ttk.Treeview(frame,columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, minwidth=0, width=90, stretch=False, anchor=tk.E)

        tree.grid(row=0, column=0, pady=3, sticky=tk.N + tk.W)

    def create_button(self):
        frame = tk.Frame(self)
        self.button = tk.Button(frame)
        self.button["text"] = "refresh"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.W)
        frame.grid(row=1, column=0, sticky=tk.N + tk.E + tk.W + tk.S)


class Form(View):
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

    