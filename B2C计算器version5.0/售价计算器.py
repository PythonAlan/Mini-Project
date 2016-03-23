#!/usr/bin/env python3
#antuor:Alan
import settings
from tkinter import *





class LoadCalculator():




    def __init__(self):
        window = Tk()
        window.title("B2C计算器version5.0 author: 吕毅")
#################################部件############################################################
        label1 = Label(window,text="售价$ :").grid(row = 1,column =1,sticky=W)
        label2 = Label(window,text="采购价$ :").grid(row =2,column=1,sticky=W)
        label3 = Label(window,text="重量g :").grid(row=3,column=1,sticky=W)

        label4 = Label(window,text="0% 利润率").grid(row=7,column=1,sticky=W)
        label5 = Label(window,text="5% 利润率").grid(row=8,column=1,sticky=W)
        label6 = Label(window,text="10% 利润率").grid(row=9,column=1,sticky=W)
        label7 = Label(window,text="15% 利润率").grid(row=10,column=1,sticky=W)
        label8 = Label(window,text="20% 利润率").grid(row=11,column=1,sticky=W)
        label9 = Label(window,text="25% 利润率").grid(row=12,column=1,sticky=W)
        label10 = Label(window,text="30% 利润率").grid(row=13,column=1,sticky=W)
        label18 = Label(window,text="总成本$ :",bg = 'red').grid(row=5,column=1,sticky=W)
        label21 = Label(window,text="当前利润率 :").grid(row=6,column=1,sticky=W)
        label_ShippingMethod = Label(window,text="物流方式:").grid(row=4,column=1,sticky=W)
        label_FBA =Label(window,text="FBA_US").grid(row=4,column=2,sticky=E)
        label_First_Class = Label(window,text='USPS_FirstClass').grid(row=4,column=3,sticky=E)
#####################################输入框#########################################
        self.SalePrice = DoubleVar()           #saleprice
        entry_a = Entry(window,textvariable = self.SalePrice,justify = RIGHT).grid(row=1,column=3)
        self.PurchasePrice = DoubleVar()    #采购价
        entry_b = Entry(window,textvariable = self.PurchasePrice,justify = RIGHT).grid(row=2,column=3)
        self.ShippingWeight = DoubleVar()  #重量g
        entry_c = Entry(window,textvariable = self.ShippingWeight,justify = RIGHT).grid(row =3,column=3)



##################################FBA显示部件###################################################
        self.ToTalCost = StringVar()
        label19 = Label(window,textvariable = self.ToTalCost).grid(row=5,column=2,sticky=E)
        self.NowProfit = StringVar()
        label20 = Label(window,textvariable = self.NowProfit).grid(row=6,column=2,sticky=E)
        self.ZeroPercent = StringVar()
        label11 = Label(window,textvariable = self.ZeroPercent).grid(row=7,column=2,sticky=E)
        self.FivePercent = StringVar()
        label12 = Label(window,textvariable = self.FivePercent).grid(row=8,column=2,sticky=E)
        self.TenPercent = StringVar()
        label13 = Label(window,textvariable = self.TenPercent).grid(row=9,column=2,sticky=E)
        self.FifteenPercent = StringVar()
        label14 = Label(window,textvariable = self.FifteenPercent).grid(row=10,column=2,sticky=E)
        self.TwentyPercent = StringVar()
        label15 = Label(window,textvariable = self.TwentyPercent).grid(row=11,column=2,sticky=E)
        self.TwentyFivePercent = StringVar()
        label16 = Label(window,textvariable = self.TwentyFivePercent).grid(row=12,column=2,sticky=E)
        self.ThirtyPercent = StringVar()
        label17 = Label(window,textvariable = self.ThirtyPercent).grid(row=13,column=2,sticky=E)
###First class显示部分
        self.ToTalCost_US = StringVar()
        label30 = Label(window,textvariable = self.ToTalCost_US).grid(row=5,column=3,sticky=E)
        self.NowProfit_US = StringVar()
        label31 = Label(window,textvariable = self.NowProfit_US).grid(row=6,column=3,sticky=E)
        self.ZeroPercent_US = StringVar()
        label32 = Label(window,textvariable = self.ZeroPercent_US).grid(row=7,column=3,sticky=E)
        self.FivePercent_US = StringVar()
        label33 = Label(window,textvariable = self.FivePercent_US).grid(row=8,column=3,sticky=E)
        self.TenPercent_US = StringVar()
        label34 = Label(window,textvariable = self.TenPercent_US).grid(row=9,column=3,sticky=E)
        self.FifteenPercent_US = StringVar()
        label35 = Label(window,textvariable = self.FifteenPercent_US).grid(row=10,column=3,sticky=E)
        self.TwentyPercent_US = StringVar()
        label36 = Label(window,textvariable = self.TwentyPercent_US).grid(row=11,column=3,sticky=E)
        self.TwentyFivePercent_US = StringVar()
        label37 = Label(window,textvariable = self.TwentyFivePercent_US).grid(row=12,column=3,sticky=E)
        self.ThirtyPercent_US = StringVar()
        label38 = Label(window,textvariable = self.ThirtyPercent_US).grid(row=13,column=3,sticky=E)









        ###########选择fba重量段######1组#######
        self.v1 = StringVar()
        btSelectOne = Radiobutton(window,text='0～1lb',variable = self.v1,value = '1lb',command = self.selectLevel)
        btSelectTwo = Radiobutton(window,text='1～2lb',variable = self.v1,value = '2lb',command = self.selectLevel)
        btSelectOver2lb = Radiobutton(window,text='2~20lb',variable = self.v1,value = 'Over 2lb',command=self.selectLevel)

        btSelectOne.grid(row = 14,column=1,sticky=W)
        btSelectTwo.grid(row = 15,column=1,sticky=W)
        btSelectOver2lb.grid(row = 16,column=1,sticky=W)
        ##########选则尺寸Large or Small Std Size########2组########
        self.v2 = StringVar()
        btSelectSmall = Radiobutton(window,text='Small Std Size',variable = self.v2,bg='yellow',value = 'Small Std Size',command=self.selectLevel)
        btSelectLarge = Radiobutton(window,text='Large Std Size',variable = self.v2,bg='yellow',value = 'Large Std Size',command=self.selectLevel)
        btSelectSmall.grid(row = 17,column=1,sticky=W)
        btSelectLarge.grid(row = 18,column=1,sticky=W)
        btExit = Button(window,text="退出程序",command = window.quit).grid(row=20,column=3,sticky=E)
        btCompute = Button(window,text = "开始计算",command = self.ComputeSalePrice).grid(row=19,column=3,sticky=E)
        label22 = Label(window,text='* Small Std Size :38.1cm X 30.48cm X 1.9cm').grid(row=21,column=1,sticky=W)
        label23 = Label(window,text='* Large Std Size :45.72cm X 35.56cm X 20.32cm').grid(row=22,column=1,sticky=W)


        window.mainloop()
####运费逻辑运算
    def ComputeSalePrice(self):
        try:
            #计算FBA
            TotalShippingCost = self.computeshippingcost(
                float(self.PurchasePrice.get()),    #采购价
                float(self.ShippingWeight.get())*settings.fee_rate['firstClass']/settings.fee_rate['exchangeRate'], #头程
                settings.fee_rate['toFba'], #二程
                float(self.SalePrice.get())*settings.fee_rate['damageRate'], #售后
                float(self.SalePrice.get())*settings.fee_rate['commissionRate'],#平台费
                self.selectLevel(),  #   调用选择FBA的重量级别的函数
                settings.fee_rate['packageCost']
            )
            # print('采购价：',float(self.PurchasePrice.get()))
            # print('头程：',float(self.ShippingWeight.get())*settings.fee_rate['firstClass']/settings.fee_rate['exchangeRate'])
            # print('二程：',settings.fee_rate['toFba'])
            # print('售后退货：',float(self.SalePrice.get())*settings.fee_rate['damageRate'])
            # print('平台费：',float(self.SalePrice.get())*settings.fee_rate['commissionRate'])
            # print('FBA费用：',self.selectLevel())
            # print('包装费：',settings.fee_rate['packageCost'])



            self.ZeroPercent.set(format(TotalShippingCost,'.2f'))
            self.FivePercent.set(format(TotalShippingCost/0.95,'.2f'))
            self.TenPercent.set(format(TotalShippingCost/0.90,'.2f'))
            self.FifteenPercent.set(format(TotalShippingCost/0.85,'.2f'))
            self.TwentyPercent.set(format(TotalShippingCost/0.80,'.2f'))
            self.TwentyFivePercent.set(format(TotalShippingCost/0.75,'.2f'))
            self.ThirtyPercent.set(format(TotalShippingCost/0.70,'.2f'))
            self.ToTalCost.set(format(TotalShippingCost,'.2f'))
            self.NowProfit.set('{:.2f} %'.format((self.SalePrice.get() - TotalShippingCost)/self.SalePrice.get()*100))

            #计算first class
            oz_to_g = 28.4           # 盎司转化为克
            if self.ShippingWeight.get()/oz_to_g > 16:     #判断重量是否超过16oz，是则不适用first_class
                self.ToTalCost_US.set('不适用firs class')
                self.NowProfit_US.set('不适用firs class')
                self.ZeroPercent_US.set('不适用firs class')
                self.FivePercent_US.set('不适用firs class')
                self.TenPercent_US.set('不适用firs class')
                self.FifteenPercent_US.set('不适用firs class')
                self.TwentyPercent_US.set('不适用firs class')
                self.TwentyFivePercent_US.set('不适用firs class')
                self.ThirtyPercent_US.set('不适用firs class')

            else:                                          #适用first_class
                TotalShippingCost_first_class = self.compute_usps(
                float(self.PurchasePrice.get()),    #采购价
                float(self.ShippingWeight.get())*settings.fee_rate['firstClass']/settings.fee_rate['exchangeRate'], #头程
                float(self.SalePrice.get())*settings.fee_rate['damageRate'], #售后
                float(self.SalePrice.get())*settings.fee_rate['commissionRate'],#平台费
                settings.first_class[int(self.ShippingWeight.get()/oz_to_g)],  #first class的邮费
                settings.fee_rate['packageCost']
            )
                print(settings.first_class[int(self.ShippingWeight.get()/oz_to_g)])


                self.ZeroPercent_US.set(format(TotalShippingCost_first_class,'.2f'))
                self.FivePercent_US.set(format(TotalShippingCost_first_class/0.95,'.2f'))
                self.TenPercent_US.set(format(TotalShippingCost_first_class/0.90,'.2f'))
                self.FifteenPercent_US.set(format(TotalShippingCost_first_class/0.85,'.2f'))
                self.TwentyPercent_US.set(format(TotalShippingCost_first_class/0.80,'.2f'))
                self.TwentyFivePercent_US.set(format(TotalShippingCost_first_class/0.75,'.2f'))
                self.ThirtyPercent_US.set(format(TotalShippingCost_first_class/0.70,'.2f'))
                self.ToTalCost_US.set(format(TotalShippingCost_first_class,'.2f'))
                self.NowProfit_US.set('{:.2f} %'.format((self.SalePrice.get() - TotalShippingCost_first_class)/self.SalePrice.get()*100))
        except ZeroDivisionError:
            print('售价不能为0')









#计算FBA，总成本函数
    def computeshippingcost(self,PurchasePrice,FirstShoppingCost,SecondShoppingCost,DamageCost,Commission,FbaFee,PackageCost):


        TotalShippingCost = PurchasePrice + FirstShoppingCost + SecondShoppingCost + DamageCost + Commission + FbaFee + PackageCost


        return TotalShippingCost

#计算first,总成本函数
    def compute_usps(self,PurchasePrice,FirstShoppingCost,DamageCost,Commission,Usps_Fee,PackageCost):


        TotalShippingCost_b = PurchasePrice+FirstShoppingCost+DamageCost+Commission+Usps_Fee+PackageCost

        return TotalShippingCost_b







##选择FBA重量段函数
    def selectLevel(self):
        fbaFee = 3.02
        if self.v1.get() == '1lb' and self.v2 == 'Small Std Size':   #1lb内 且尺寸为small Std Size ，= $2.56
            fbaFee = settings.fee_rate['fbaFee_s_1lb']
        elif self.v1.get() == '1lb' and self.v2 == 'Large Std Size': #1lb内 且尺寸为Large Std Size ，＝ $3.02
            fbaFee = settings.fee_rate['fbaFee_l_1lb']
        elif self.v1.get() == '2lb':                                 #1-2lb内，默认尺寸为Large Std Size， =$4.01
            self.v2.set('Large Std Size')
            fbaFee = settings.fee_rate['fbaFee_l_2lb']
        elif self.v2.get() =='Small Std Size':                       #尺寸为‘small Std Size', 重量默认为1lb
            self.v1.set('1lb')
            fbaFee = settings.fee_rate['fbaFee_s_1lb']
        elif self.v1.get() == 'Over 2lb':      #Std Size超2lb ： $4.01+0.39/lb（超2lb）部份
            self.v2.set('Large Std Size')
            fbaFee = settings.fee_rate['fbaFee_l_2lb']+(self.ShippingWeight.get()/453-2)*settings.fee_rate['over 2lb']

        return fbaFee







LoadCalculator()