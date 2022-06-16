import tkinter as tk
from tkinter import ttk
import webbrowser
from __Models.Stocks import Stock
from __Controllers.TableController import TableController

class Table(tk.Frame):

    def __init__(self, controller:TableController, model:Stock, master=None):
        super().__init__(master)
        self.master = master
        self.model = model
        self.controller = controller
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.create_button()
        
    def create_view(self, controller:TableController, model:Stock, Market):

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']

                print(record)
                x = record[0]
                financialTable(x)

        def financialTable(record):

            lf = ttk.Labelframe(frame, text=record)
            lf.grid(row=1, column=0, pady=3, sticky=tk.EW)

            alignments = controller.getStockInfo(record)

            grid_row = 0
            for alignment in alignments:
                if not 'www' in alignment:
                    lbl = ttk.Label(lf, text=alignment)
                    lbl.grid(column=0, row = grid_row, padx=3, sticky=tk.W)
                else:
                    x = alignment.split()
                    lbl = ttk.Label(lf, text=x[1], foreground='blue',cursor="hand2")
                    lbl.grid(column=0, row=grid_row, padx=3, sticky=tk.W)
                    lbl.bind("<Button-1>",lambda e : webbrowser.open_new_tab(x[1]))

                grid_row += 1

            financial = controller.StockStatement(record)
            fin_header = controller.StockStatementHeader(financial)
            fin_data = controller.StockStatementData(financial)

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

        for data in model.getMarket().get(Market).values():
            try:
                self.tree.insert('', tk.END, values=data)
            except:
                pass
        
        self.tree.bind('<<TreeviewSelect>>', item_selected)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS + tk.W)


    def create_button(self):
        frame = tk.Frame(self)
        self.button = ttk.Button(frame)
        self.button["text"] = "refresh"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.W)
        frame.grid(row=99, column=0, sticky=tk.N + tk.E + tk.W + tk.S)