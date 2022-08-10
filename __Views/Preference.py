import tkinter as tk

class Preference(tk.Toplevel):
    def __init__(self):
        super().__init__()

    def create_view(self):
        self.title('Preferences')
        self.geometry('+1921+10')