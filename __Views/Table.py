import tkinter as tk
from tkinter import ttk

class Table(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.create_button()
        
    def create_view(self):
        frame = tk.Frame(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        columns = ('ชื่อย่อหลักทรัพย์','เครื่องหมาย','ล่าสุด','เปลี่ยนแปลง','%เปลี่ยนแปลง','วันก่อนหน้า','เปิด','สูงสุด','ต่ำสุด','ปริมาณ(หุ้น)',"มูลค่า ('000 บาท)",'ราคาเฉลี่ย **')
        tree = ttk.Treeview(frame,columns=columns, show='headings', height=15)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, minwidth=0, width=90, stretch=False, anchor=tk.E)

        tree.grid(row=0, column=0, pady=3, sticky=tk.N + tk.W)

    def create_button(self):
        frame = tk.Frame(self)
        self.button = ttk.Button(frame)
        self.button["text"] = "refresh"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.W)
        frame.grid(row=1, column=0, sticky=tk.N + tk.E + tk.W + tk.S)