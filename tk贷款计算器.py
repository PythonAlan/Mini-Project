#!/usr/bin/env python3
#antuor:Alan

from tkinter import *
class LoadCalculator:
    def __init__(self):
        window = Tk()
        window.title("贷款计算器")
        label1 = Label(window,text="年度利率").grid(row = 1,column =1,sticky=W)
        label2 = Label(window,text="贷款年限").grid(row =2,column=1,sticky=W)
        label3 = Label(window,text="贷款金额").grid(row=3,column=1,sticky=W)
        label4 = Label(window,text="每月还款").grid(row=4,column=1,sticky=W)
        label5 = Label(window,text="总还款金额").grid(row=5,column=1,sticky=W)
        self.annualInterestRateVar = StringVar()
        entry_a = Entry(window,textvariable = self.annualInterestRateVar,justify = RIGHT).grid(row=1,column=2)
        self.numberOfYearsVar = StringVar()
        entry_b = Entry(window,textvariable = self.numberOfYearsVar,justify = RIGHT).grid(row=2,column=2)
        self.loanAmountVar = StringVar()
        entry_c = Entry(window,textvariable = self.loanAmountVar,justify = RIGHT).grid(row=3,column=2)
        self.getMonthlyPaymentVar = StringVar()
        label6 = Label(window,textvariable = self.getMonthlyPaymentVar).grid(row=4,column=2,sticky=E)
        self.totalPaymentVar =StringVar()
        lblTotalPayment = Label(window,textvariable=self.totalPaymentVar).grid(row=5,column=2,sticky=E)
        btComputePayment = Button(window,text = "开始计算",command = self.computePayment).grid(row=6,column=2,sticky=E)

        window.mainloop()

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get())/1200,
            int(self.numberOfYearsVar.get())
        )
        self.getMonthlyPaymentVar.set(format(monthlyPayment,"10.2f"))
        totalPayment = float(self.getMonthlyPaymentVar.get())* 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment,"10.2f"))


    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberOfYears):
            monthlyPayment = loanAmount * monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))
            return monthlyPayment
LoadCalculator()


