import tkinter as tk
from tkinter import ttk

class Progress(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.labels = {}
        self.progressbars = {}
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

    def create_progress(self, frame:tk.Frame, name: str, r:int, c:int):
        self.progressbars[name] = ttk.Progressbar(frame)
        self.progressbars[name] = ttk.Progressbar(
            self,
            orient='horizontal',
            mode='determinate',
            length=280,
            name= str(name).lower()
        )
        self.progressbars[name].grid(row=r, column=c, columnspan=5, padx=10, sticky=tk.NSEW)
        
    def create_button(self):
        frame = tk.Frame(self)
        self.button = ttk.Button(frame)
        self.button["text"] = "Finished"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.W)
        frame.grid(row=1, column=0, sticky=tk.N + tk.E + tk.W + tk.S)