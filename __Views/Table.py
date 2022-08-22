from statistics import mode
import tkinter as tk
from tkinter import DISABLED, ttk
from tkinter.messagebox import showinfo,showerror
import webbrowser
from __Models.Stocks import Stock
from __Models.Settings import Setting
from __Controllers.TableController import TableController
from __Views.Graph import Graph
from sys import platform

class Table(tk.Frame):

    def __init__(self, controller:TableController, model:Stock, setting:Setting):#master=None
        super().__init__()#master
        # self.master = master
        self.model = model
        self.controller = controller
        self.setting = setting
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        # self.create_button()
        
    def create_view(self, controller:TableController, model:Stock, Market):

        def do_popup(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        def right_click_copy_text():
            self.clipboard_clear()
            self.clipboard_append(str(list(self.tree['columns']))+'\n')
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']
                self.clipboard_append(str(record)+'\n')

            self.update()


        def CandleStick():
            name = self.model.getSelected_StockName()
            if not name == None:
                try:
                    window = Graph(self.model, self.setting)
                    window.create_view()
                    window.protocol('WM_DELETE_WINDOW',func=lambda: window.destroy())
                except Exception as e:
                    print('error : ',e)
                
            else:
                showerror(
                    'Please select stock',
                    'to show the Graphs please select\nกรุณาเลือกหุ้นที่ต้องการ เพื่อแสดงกราฟ 📈📊!!')
                return


        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']
                
                try:
                    if Market != 'Crypto':
                        x = record[0].replace(' ','+').replace('&','%26')
                        financialTable(x)
                        model.setSelected_StockName(record[0].replace(' ','-')+'.BK')
                    else:
                        model.setSelected_StockName(record[1]+'-USD')
                except:
                    pass


        def financialTable(record):

            lf = ttk.Labelframe(frame, text=str(record).replace('%26','&').replace('+',' '))
            lf.grid(row=1, column=0, pady=3, sticky=tk.EW)

            alignments = controller.getStockInfo(record)

            grid_row = 0
            for alignment in alignments:
                if not 'www' in alignment:
                    lbl = ttk.Label(lf, text=alignment)
                    lbl.grid(column=0, row = grid_row, padx=3, sticky=tk.W)
                else:
                    x = alignment.split()
                    lbl = ttk.Label(lf, text=str(x[1]), foreground='blue',cursor="hand2")
                    lbl.grid(column=0, row=grid_row, padx=3, sticky=tk.W)
                    lbl.bind("<Button-1>",lambda e : webbrowser.open_new_tab(x[1]))

                grid_row += 1

            fin_header:list = list(model.getMarket().get(Market).get(record).get('fin_data').columns)
            fin_data:list = model.getMarket().get(Market).get(record).get('fin_data').values.tolist()

            columns2 = fin_header

            tree2 = ttk.Treeview(frame, columns=columns2, show='headings', name='financial')
            
            for col2 in columns2:
                tree2.heading(col2, text = col2)
                tree2.column(col2, minwidth=0, width=180, stretch=False)

            for data in fin_data:
                tree2.insert('', tk.END, values=data)

            tree2.grid(row=2, column=0, sticky=tk.NSEW)

            scrollbar2 = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree2.yview)
            tree2.configure(yscroll=scrollbar2.set)
            scrollbar2.grid(row=2, column=1, sticky=tk.NS + tk.W)
        

        frame = tk.Frame(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        columns = ('ชื่อย่อหลักทรัพย์','เครื่องหมาย','ล่าสุด','เปลี่ยนแปลง','%เปลี่ยนแปลง','วันก่อนหน้า','เปิด','สูงสุด','ต่ำสุด','ปริมาณ(หุ้น)',"มูลค่า ('000 บาท)",'ราคาเฉลี่ย **')
        self.tree = ttk.Treeview(frame,columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=0, width=90, stretch=False, anchor=tk.E)

        try:
            for data in model.getMarket().get(Market).values():
                if not data.get('data') == None:
                    self.tree.insert('', tk.END, values=data.get('data'))
        except:
            pass
        
        self.tree.bind('<<TreeviewSelect>>', item_selected)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        if platform == "linux" or platform == "linux2":
            # linux
            self.tree.bind("<Button-3>", lambda e : do_popup(e))
        elif platform == "darwin":
            # OS X
            self.tree.bind("<Button-2>", lambda e : do_popup(e))
        elif platform == "win32":
            # windows
            self.tree.bind("<Button-3>", lambda e : do_popup(e))

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS + tk.W)

        m = tk.Menu(self.tree, tearoff = 0, activebackground='SteelBlue1',)
        m.add_command(label ="Copy as text", command=right_click_copy_text)
        m.add_command(label ="Export excel file", command=lambda :showinfo('Please wait','Developer will release on V0.4'))
        m.add_separator()
        m.add_command(label='Open Stock Realtime Chart',state=DISABLED)
        m.add_command(label='Open Stock CandleStick History', command=lambda: CandleStick())
        

    def create_button(self):
        frame = tk.Frame(self)
        self.button = ttk.Button(frame)
        self.button["text"] = "refresh"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.W)
        frame.grid(row=99, column=0, sticky=tk.N + tk.E + tk.W + tk.S)