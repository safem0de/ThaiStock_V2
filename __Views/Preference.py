import tkinter as tk

class Preference(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def create_view(self):
        self.title('Preferences')
        self.geometry(f'+{str()}+{str()}')