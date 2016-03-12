#!/usr/bin/env python3
#antuor:Alan
import settings
from tkinter import *





class LoadCalculator():




    def __init__(self):
        window = Tk()
        window.title("FBA售价计算器")
#################################部件############################################################
        label1 = Label(window,text="售价$ :",bg = 'blue').grid(row = 1,column =1,sticky=W)
        label2 = Label(window,text="采购价¥ :",bg = 'yellow').grid(row =2,column=1,sticky=W)
        label3 = Label(window,text="重量g :").grid(row=3,column=1,sticky=W)
        label4 = Label(window,text="0% 利润率").grid(row=6,column=1,sticky=W)
        label5 = Label(window,text="5% 利润率").grid(row=7,column=1,sticky=W)
        label6 = Label(window,text="10% 利润率").grid(row=8,column=1,sticky=W)
        label7 = Label(window,text="15% 利润率").grid(row=9,column=1,sticky=W)
        label8 = Label(window,text="20% 利润率").grid(row=10,column=1,sticky=W)
        label9 = Label(window,text="25% 利润率").grid(row=11,column=1,sticky=W)
        label10 = Label(window,text="30% 利润率").grid(row=12,column=1,sticky=W)
        label18 = Label(window,text="总成本$ :",bg = 'red').grid(row=4,column=1,sticky=W)
        label21 = Label(window,text="当前利润率 :").grid(row=5,column=1,sticky=W)
#####################################输入框#########################################
        self.SalePrice = DoubleVar()           #saleprice
        entry_a = Entry(window,textvariable = self.SalePrice,justify = RIGHT).grid(row=1,column=2)
        self.PurchasePrice = DoubleVar()    #采购价
        entry_b = Entry(window,textvariable = self.PurchasePrice,justify = RIGHT).grid(row=2,column=2)
        self.ShippingWeight = DoubleVar()  #重量g
        entry_c = Entry(window,textvariable = self.ShippingWeight,justify = RIGHT).grid(row =3,column=2)



##################################显示部件###################################################
        self.ToTalCost = StringVar()
        label19 = Label(window,textvariable = self.ToTalCost).grid(row=4,column=2,sticky=E)
        self.NowProfit = StringVar()
        label20 = Label(window,textvariable = self.NowProfit).grid(row=5,column=2,sticky=E)
        self.ZeroPercent = StringVar()
        label11 = Label(window,textvariable = self.ZeroPercent).grid(row=6,column=2,sticky=E)
        self.FivePercent = StringVar()
        label12 = Label(window,textvariable = self.FivePercent).grid(row=7,column=2,sticky=E)
        self.TenPercent = StringVar()
        label13 = Label(window,textvariable = self.TenPercent).grid(row=8,column=2,sticky=E)
        self.FifteenPercent = StringVar()
        label14 = Label(window,textvariable = self.FifteenPercent).grid(row=9,column=2,sticky=E)
        self.TwentyPercent = StringVar()
        label15 = Label(window,textvariable = self.TwentyPercent).grid(row=10,column=2,sticky=E)
        self.TwentyFivePercent = StringVar()
        label16 = Label(window,textvariable = self.TwentyFivePercent).grid(row=11,column=2,sticky=E)
        self.ThirtyPercent = StringVar()
        label17 = Label(window,textvariable = self.ThirtyPercent).grid(row=12,column=2,sticky=E)
        btCompute = Button(window,text = "开始计算",command = self.ComputeSalePrice).grid(row=13,column=2,sticky=E)









        window.mainloop()

    def ComputeSalePrice(self):
        try:
            TotalShippingCost = self.computeshippingcost(
                float(self.PurchasePrice.get())/settings.fee_rate['exchangeRate'],    #caigou
                float(self.ShippingWeight.get())*settings.fee_rate['firstClass']/settings.fee_rate['exchangeRate'], #toucheng
                settings.fee_rate['toFba'], #ercheng
                float(self.SalePrice.get())*settings.fee_rate['damageRate'], #sunhuai
                float(self.SalePrice.get())*settings.fee_rate['commissionRate'],
                settings.fee_rate['fbaFee'],
                settings.fee_rate['packageCost']
            )
            self.ZeroPercent.set(format(TotalShippingCost,'.2f'))
            self.FivePercent.set(format(TotalShippingCost/0.95,'.2f'))
            self.TenPercent.set(format(TotalShippingCost/0.90,'.2f'))
            self.FifteenPercent.set(format(TotalShippingCost/0.85,'.2f'))
            self.TwentyPercent.set(format(TotalShippingCost/0.80,'.2f'))
            self.TwentyFivePercent.set(format(TotalShippingCost/0.75,'.2f'))
            self.ThirtyPercent.set(format(TotalShippingCost/0.70,'.2f'))
            self.ToTalCost.set(format(TotalShippingCost,'.2f'))
            self.NowProfit.set('{:.2f} %'.format((self.SalePrice.get() - TotalShippingCost)/self.SalePrice.get()*100))

        except ZeroDivisionError:

            print('销售价不能为0')









    def computeshippingcost(self,PurchasePrice,FirstShoppingCost,SecondShoppingCost,DamageCost,Commission,FbaFee,PackageCost):


        TotalShippingCost = PurchasePrice + FirstShoppingCost + SecondShoppingCost + DamageCost + Commission + FbaFee + PackageCost

        return TotalShippingCost






LoadCalculator()