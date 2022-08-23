from functools import reduce
from threading import Thread
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from __Models.Settings import Setting
from __Models.Financials import FinancialGrowth
from __Controllers.AnalyseController import AnalyseController

class StockAnalyse(tk.Toplevel):

    __stateOfFilter = []
    __Table = None

    def __init__(self):
        super().__init__()

    def create_view(self, setting:Setting, finance:FinancialGrowth, controller:AnalyseController):

        self.title('Growth Stock Analyse')
        self.geometry(f'+{str(setting.getanalyse_screen_x())}+{str(setting.getanalyse_screen_y())}')
        self.__Table = finance.getDataTable()

        pe_set = finance.getMarket_Stat_SET().get('pe')
        pe_mai = finance.getMarket_Stat_mai().get('pe')
        pbv_set = finance.getMarket_Stat_SET().get('pbv')
        pbv_mai = finance.getMarket_Stat_mai().get('pbv')

        avg_asset_SET = finance.getMarket_Stat_SET().get('avg_asset')
        avg_revenue_SET = finance.getMarket_Stat_SET().get('avg_revenue')
        avg_netprofit_SET = finance.getMarket_Stat_SET().get('avg_netprofit')
        avg_roe_SET = finance.getMarket_Stat_SET().get('avg_roe')
        avg_yield_SET = finance.getMarket_Stat_SET().get('avg_yield')

        avg_asset_mai = finance.getMarket_Stat_mai().get('avg_asset')
        avg_revenue_mai = finance.getMarket_Stat_mai().get('avg_revenue')
        avg_netprofit_mai = finance.getMarket_Stat_mai().get('avg_netprofit')
        avg_roe_mai = finance.getMarket_Stat_mai().get('avg_roe')
        avg_yield_mai = finance.getMarket_Stat_mai().get('avg_yield')

        def CheckCondition(data, condition_Filter:list = self.__stateOfFilter):
            Table = self.__Table.copy()
            
            dc_SET = {}
            dc_mai = {}
            if data == 'all':
                dc_SET = {i: Table[i]['data'] for i in Table if Table[i]['ismai'] == False and Table[i]['isSET100'] == False and Table[i]['isSET50'] == False}
                dc_mai = {i: Table[i]['data'] for i in Table if Table[i]['ismai'] == True}

                # print(dc_SET)
                # print(len(dc_SET))

                # print(dc_mai)
                # print(len(dc_mai))

            elif data == 'set':
                dc_SET = {
                            i: Table[i]['data'] for i in Table if Table[i]['ismai'] == False
                            and
                            Table[i]['isSET100'] == False
                            and
                            Table[i]['isSET50'] == False
                        }
            elif data == 'set100':
                dc_SET = {i: Table[i]['data'] for i in Table if Table[i]['isSET100'] == True}
            elif data == 'set50':
                dc_SET = {i: Table[i]['data'] for i in Table if Table[i]['isSET50'] == True}
            elif data == 'mai':
                dc_SET = {i: Table[i]['data'] for i in Table if Table[i]['ismai'] == True}

            try:
                dc_SET_asset = {}
                dc_mai_asset = {}
                dc_SET_revenue = {}
                dc_mai_revenue = {}
                dc_SET_netprofit = {}
                dc_mai_netprofit = {}
                dc_SET_roe = {}
                dc_mai_roe = {}
                dc_SET_yield = {}
                dc_mai_yield = {}
                dc_SET_pe = {}
                dc_mai_pe = {}
                dc_SET_pbv = {}
                dc_mai_pbv = {}

                for i in condition_Filter:
                    if i == 'asset':
                        dc_SET_asset = {i: dc_SET[i] for i in dc_SET if float(dc_SET[i][1]) > float(avg_asset_SET)}
                        dc_mai_asset = {i: dc_mai[i] for i in dc_mai if float(dc_mai[i][1]) > float(avg_asset_mai)}

                        # print(dc_SET_asset)
                        # print(len(dc_SET_asset))

                        # print(dc_mai_asset)
                        # print(len(dc_mai_asset))

                    if i == 'revenue':
                        dc_SET_revenue = {i: dc_SET[i] for i in dc_SET if float(dc_SET[i][2]) > float(avg_revenue_SET)}
                        dc_mai_revenue = {i: dc_mai[i] for i in dc_mai if float(dc_mai[i][2]) > float(avg_revenue_mai)}

                        # print(dc_SET_revenue)
                        # print(len(dc_SET_revenue))

                        # print(dc_mai_revenue)
                        # print(len(dc_mai_revenue))

                    if i == 'netprofit':
                        dc_SET_netprofit = {i: dc_SET[i] for i in dc_SET if float(dc_SET[i][3]) > float(avg_netprofit_SET)}
                        dc_mai_netprofit = {i: dc_mai[i] for i in dc_mai if float(dc_mai[i][3]) > float(avg_netprofit_mai)}

                        # print(dc_SET_netprofit)
                        # print(len(dc_SET_netprofit))

                        # print(dc_mai_netprofit)
                        # print(len(dc_mai_netprofit))

                    if i == 'roe':
                        dc_SET_roe = {i: dc_SET[i] for i in dc_SET if float(dc_SET[i][4]) > float(avg_roe_SET)}
                        dc_mai_roe = {i: dc_mai[i] for i in dc_mai if float(dc_mai[i][4]) > float(avg_roe_mai)}

                        # print(dc_SET_roe)
                        # print(len(dc_SET_roe))

                        # print(dc_mai_roe)
                        # print(len(dc_mai_roe))

                    if i == 'yield':
                        dc_SET_yield = {
                                            i: dc_SET[i] for i in dc_SET if float(dc_SET[i][5]) > float(avg_yield_SET) and
                                            float(str(dc_SET[i][5]).replace('*','').replace('-','0')) != 0
                                        }
                        dc_mai_yield = {
                                            i: dc_mai[i] for i in dc_mai if float(dc_mai[i][5]) > float(avg_yield_mai) and
                                            float(str(dc_SET[i][5]).replace('*','').replace('-','0')) != 0
                                        }

                        # print(dc_SET_yield)
                        # print(len(dc_SET_yield))

                        # print(dc_mai_yield)
                        # print(len(dc_mai_yield))

                    if i == 'pe':
                        dc_SET_pe = {
                                        i: dc_SET[i] for i in dc_SET
                                        if float(str(dc_SET[i][6]).replace('*','').replace('-','0')) < float(pe_set) and
                                        float(str(dc_SET[i][6]).replace('*','').replace('-','0')) != 0
                                    }
                        dc_mai_pe = {
                                        i: dc_mai[i] for i in dc_mai
                                        if float(str(dc_mai[i][6]).replace('*','').replace('-','0')) < float(pe_mai) and
                                        float(str(dc_mai[i][6]).replace('*','').replace('-','0')) != 0
                                    }

                        # print(dc_SET_pe)
                        # print(len(dc_SET_pe))

                        # print(dc_mai_pe)
                        # print(len(dc_mai_pe))


                    if i == 'pbv':
                        dc_SET_pbv = {
                                        i: dc_SET[i] for i in dc_SET
                                        if float(str(dc_SET[i][7]).replace('*','').replace('-','0')) < float(pbv_set) and
                                        float(str(dc_SET[i][7]).replace('*','').replace('-','0')) != 0
                                    }
                        dc_mai_pbv = {
                                        i: dc_mai[i] for i in dc_mai
                                        if float(str(dc_mai[i][7]).replace('*','').replace('-','0')) < float(pbv_mai) and
                                        float(str(dc_mai[i][7]).replace('*','').replace('-','0')) != 0
                                    }

                        # print(dc_SET_pbv)
                        # print(len(dc_SET_pbv))

                        # print(dc_mai_pbv)
                        # print(len(dc_mai_pbv))

                rawData = reduce(set.union, map(set, map(dict.keys, [dc_SET, dc_mai])))
                asset_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_asset, dc_mai_asset])))
                revenue_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_revenue, dc_mai_revenue])))
                netprofit_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_netprofit, dc_mai_netprofit])))
                roe_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_roe, dc_mai_roe])))
                yield_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_yield, dc_mai_yield])))
                pe_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_pe, dc_mai_pe])))
                pbv_union = reduce(set.union, map(set, map(dict.keys, [dc_SET_pbv, dc_mai_pbv])))

                list_of_sets = [asset_union, revenue_union, netprofit_union, roe_union, yield_union, pe_union, pbv_union]
                non_empties = [x for x in list_of_sets if x]
                solution_set = rawData.intersection(*non_empties)
                Datas = []
                #### # http://hackwrite.com/posts/intersection-of-non-empty-sets-in-python/
                for j in solution_set:
                    # print('--->',Table[j]['data'])
                    Datas.append(Table[j]['data'])

                return Datas
            except:
                pass

        def CheckBox(value:str):
            if 'rm' in value:
                self.__stateOfFilter.remove(value.replace('rm_',''))
            else:
                self.__stateOfFilter.append(value)

            RadioBtn_Selected(selected_Market.get())


        def RadioBtn_Selected(data):
            analyseTable(CheckCondition(data))

        def analyseTable(stk):

            columns = ('หลักทรัพย์', '(สินทรัพย์)เฉลี่ย','(รายได้)เฉลี่ย','(กำไร)เฉลี่ย','(%ROE)เฉลี่ย','(%ปันผล)เฉลี่ย','(P/E)ล่าสุด','(P/BV)ล่าสุด')
            tree = ttk.Treeview(self, columns=columns, show='headings', name='analyse', height=25)

            ## Clear Treeview ##
            for i in tree.get_children():
                tree.delete(i)

            # define headings
            for col in columns:
                tree.heading(col, text = col)
                tree.column(col, minwidth=0, width=100, stretch=True, anchor=tk.CENTER)

            for s in stk:
                if s:
                    tree.insert('', tk.END, values=s)

            tree.grid(row=1, column=1, rowspan=20, pady=3, sticky=tk.NS)
            scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=1, column=2, rowspan=20, pady=3, sticky=tk.NS)

            labelfooter = ttk.Label(self, text = f'**ในตารางไม่นำ "หุ้น" ที่มีการขาดทุนในงบฯย้อนหลัง 3-5 ปี มาพิจารณา {len(stk)} ตัว', foreground='red')
            labelfooter.grid(row=40, column=0, columnspan=3, pady=3, sticky=tk.SE)

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
                command = lambda : RadioBtn_Selected(selected_Market.get())
            )
            r.grid(row=0, column=mkt_count, sticky=tk.W + tk.E)
            mkt_count += 1
            # print(mkt_count)

        selected_Market.set('all')

        # https://www.pythontutorial.net/tkinter/tkinter-checkbox/
        self.checkbox_asset_var = tk.StringVar()
        self.checkbox_asset = ttk.Checkbutton(
        self,
        text=f'อัตราการเติบโตของสินทรัพย์สูงกว่าค่าเฉลี่ย (Asset Growth)\n>> SET : {avg_asset_SET}, mai : {avg_asset_mai}',
        command = lambda: CheckBox(self.checkbox_asset_var.get()),
        variable=self.checkbox_asset_var,
        onvalue='asset',
        offvalue='rm_asset')
        self.checkbox_asset.grid(row=2, column=0, padx=3, sticky=tk.W)

        self.checkbox_revenue_var = tk.StringVar()
        self.checkbox_revenue = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของรายได้สูงกว่าค่าเฉลี่ย (Revenue Growth)\n>> SET : {avg_revenue_SET}, mai : {avg_revenue_mai}',
        command = lambda: CheckBox(self.checkbox_revenue_var.get()),
        variable=self.checkbox_revenue_var,
        onvalue='revenue',
        offvalue='rm_revenue')
        self.checkbox_revenue.grid(row=3, column=0, padx=3, sticky=tk.W)

        self.checkbox_netprofit_var = tk.StringVar()
        self.checkbox_netprofit = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของกำไรสูงกว่าค่าเฉลี่ย (NetProfit Growth)\n>> SET : {avg_netprofit_SET}, mai : {avg_netprofit_mai}',
        command = lambda: CheckBox(self.checkbox_netprofit_var.get()),
        variable=self.checkbox_netprofit_var,
        onvalue='netprofit',
        offvalue='rm_netprofit')
        self.checkbox_netprofit.grid(row=4, column=0, padx=3, sticky=tk.W)

        self.checkbox_ROE_var = tk.StringVar()
        self.checkbox_ROE = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของ ROE สูงกว่าค่าเฉลี่ย (ROE Growth)\n>> SET : {avg_roe_SET}, mai : {avg_roe_mai}',
        command = lambda: CheckBox(self.checkbox_ROE_var.get()),
        variable=self.checkbox_ROE_var,
        onvalue='roe',
        offvalue='rm_roe')
        self.checkbox_ROE.grid(row=5, column=0, padx=3, sticky=tk.W)

        self.checkbox_Yield_var = tk.StringVar()
        self.checkbox_Yield = ttk.Checkbutton(self,
        text=f'อัตราการเติบโตของเงินปันผลสูงกว่าค่าเฉลี่ย (Yield Growth)\n>> SET : {avg_yield_SET}, mai : {avg_yield_mai}',
        command = lambda: CheckBox(self.checkbox_ROE_var.get()),
        variable=self.checkbox_Yield_var,
        onvalue='yield',
        offvalue='rm_yield')
        self.checkbox_Yield.grid(row=6, column=0, padx=3, sticky=tk.W)

        self.checkbox_PE_var = tk.StringVar()
        self.checkbox_PE = ttk.Checkbutton(self,
        text=f'ค่า P/E ต่ำกว่าตลาด\n>> SET : {pe_set}, mai : {pe_mai}',
        command = lambda: CheckBox(self.checkbox_PE_var.get()),
        variable=self.checkbox_PE_var,
        onvalue='pe',
        offvalue='rm_pe')
        self.checkbox_PE.grid(row=7, column=0, padx=3, sticky=tk.W)

        self.checkbox_PBV_var = tk.StringVar()
        self.checkbox_PBV = ttk.Checkbutton(self,
        text=f'ค่า P/BV ต่ำกว่าตลาด\n>> SET : {pbv_set}, mai : {pbv_mai}',
        command=lambda: CheckBox(self.checkbox_PBV_var.get()),
        variable=self.checkbox_PBV_var,
        onvalue='pbv',
        offvalue='rm_pbv')
        self.checkbox_PBV.grid(row=8, column=0, padx=3, sticky=tk.W)

        RadioBtn_Selected(selected_Market.get())