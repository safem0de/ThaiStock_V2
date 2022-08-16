from threading import Thread
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from __Models.Stocks import Stock
from __Models.Settings import Setting
from __Models.Financials import FinancialGrowth
from __Controllers.AnalyseController import AnalyseController

class StockAnalyse(tk.Toplevel):

    __stateOfFilter = []

    def __init__(self):
        super().__init__()

    def create_view(self, setting:Setting, finance:FinancialGrowth, controller:AnalyseController):

        self.geometry(f'+{str(setting.getanalyse_screen_x())}+{str(setting.getanalyse_screen_y())}')

        def analyseTable(stk):
            columns = ('หลักทรัพย์', '(สินทรัพย์)เฉลี่ย','(รายได้)เฉลี่ย','(กำไร)เฉลี่ย','(%ROE)เฉลี่ย','(%ปันผล)เฉลี่ย','(P/E)ล่าสุด','(P/BV)ล่าสุด')
            tree = ttk.Treeview(self, columns=columns, show='headings', name='analyse', height=25)

            # define headings
            for col in columns:
                tree.heading(col, text = col)
                tree.column(col, minwidth=0, width=100, stretch=True, anchor=tk.CENTER)

            for s in stk:
                tree.insert('', tk.END, values=s)

            tree.grid(row=1, column=1, rowspan=20, pady=3, sticky=tk.NS)
            scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=1, column=2, rowspan=20, pady=3, sticky=tk.NS)

            labelfooter = ttk.Label(self, text = f'**ในตารางไม่นำ "หุ้น" ที่มีการขาดทุนในงบฯย้อนหลัง 3-5 ปี มาพิจารณา {len(stk)} ตัว', foreground='red')
            labelfooter.grid(row=40, column=0, columnspan=3, pady=3, sticky=tk.SE)


        # print(model.getMarket())
        # controller = AnalyseController(model)
        # market_stat = controller.setDetails()
        pe_set = finance.getMarket_Stat_SET().get('pe')
        pe_mai = finance.getMarket_Stat_mai().get('pe')
        pbv_set = finance.getMarket_Stat_SET().get('pbv')
        pbv_mai = finance.getMarket_Stat_mai().get('pbv')

        # controller.checkSET100()
        # controller.checkSET50()
        # Table = controller.InitialTable()
        analyseTable(stk=[]) ## Table[i]['data'] for i in Table

        self.labelheader = ttk.Label(self, text = 'Analyse')
        self.labelheader['font'] = ("Impact", 16)
        self.labelheader.grid(row=0, column=0, sticky=tk.W+tk.N)

        self.LblframeMarket = ttk.LabelFrame(self, text="Market")
        self.LblframeMarket.grid(row=1, column=0, sticky=tk.N + tk.E + tk.W)

        selected_Market = tk.StringVar()
        mkt = (('SET & mai', 'all'),
                ('SET', 'set'),
                ('SET100', 'set100'),
                ('SET50', 'set50'),
                ('mai', 'mai'),)

        mkt_count = 0
        for p in mkt:
            # print(p)
            r = ttk.Radiobutton(
                self.LblframeMarket,
                text=p[0],
                value=p[1],
                variable=selected_Market,
                command = lambda : print(selected_Market.get())
            )
            r.grid(row=0, column=mkt_count, sticky=tk.W + tk.E)
            mkt_count += 1
            # print(mkt_count)

        selected_Market.set('all')

        # https://www.pythontutorial.net/tkinter/tkinter-checkbox/
        self.checkbox_asset_var = tk.StringVar()
        self.checkbox_asset = ttk.Checkbutton(
        self,
        text=f'อัตราการเติบโตของสินทรัพย์สูงกว่าค่าเฉลี่ย (Asset Growth) >> {None}',
        # command = lambda:checkbox_assetSelected(self.checkbox_asset_var.get()),
        variable=self.checkbox_asset_var,
        onvalue='asset',
        offvalue='rm_asset')
        self.checkbox_asset.grid(row=2, column=0, padx=3, sticky=tk.W)

        self.checkbox_revenue_var = tk.StringVar()
        self.checkbox_revenue = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของรายได้สูงกว่าค่าเฉลี่ย (Revenue Growth) >> {None}',
        # command=lambda:checkbox_revenueSelected(self.checkbox_revenue_var.get()),
        variable=self.checkbox_revenue_var,
        onvalue='revenue',
        offvalue='rm_revenue')
        self.checkbox_revenue.grid(row=3, column=0, padx=3, sticky=tk.W)

        self.checkbox_netprofit_var = tk.StringVar()
        self.checkbox_netprofit = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของกำไรสูงกว่าค่าเฉลี่ย (NetProfit Growth) >> {None}',
        # command=lambda:checkbox_netprofitSelected(self.checkbox_netprofit_var.get()),
        variable=self.checkbox_netprofit_var,
        onvalue='netprofit',
        offvalue='rm_netprofit')
        self.checkbox_netprofit.grid(row=4, column=0, padx=3, sticky=tk.W)

        self.checkbox_ROE_var = tk.StringVar()
        self.checkbox_ROE = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของ ROE สูงกว่าค่าเฉลี่ย (ROE Growth) >> {None}',
        # command=lambda:checkbox_roeSelected(self.checkbox_ROE_var.get()),
        variable=self.checkbox_ROE_var,
        onvalue='roe',
        offvalue='rm_roe')
        self.checkbox_ROE.grid(row=5, column=0, padx=3, sticky=tk.W)

        self.checkbox_Yield_var = tk.StringVar()
        self.checkbox_Yield = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของเงินปันผลสูงกว่าค่าเฉลี่ย (Yield Growth) >> {None}',
        # command=lambda:checkbox_roeSelected(self.checkbox_ROE_var.get()),
        variable=self.checkbox_Yield_var,
        onvalue='yield',
        offvalue='rm_yield')
        self.checkbox_Yield.grid(row=6, column=0, padx=3, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text=f'ค่า P/E ต่ำกว่าตลาด\n>> SET : {pe_set}, mai : {pe_mai}',
        # command=lambda:checkbox_peSelected(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='rm_pe')
        self.checkbox_PE.grid(row=7, column=0, padx=3, sticky=tk.W)

        self.checkbox_PBV_var = tk.StringVar()
        self.checkbox_PBV = ttk.Checkbutton(self,
        text=f'ค่า P/BV ต่ำกว่าตลาด\n>> SET : {pbv_set}, mai : {pbv_mai}',
        # command=lambda:checkbox_pbvSelected(self.checkbox_PBV_var.get()),
        variable=self.checkbox_PBV_var,
        onvalue='pbv',
        offvalue='rm_pbv')
        self.checkbox_PBV.grid(row=8, column=0, padx=3, sticky=tk.W)