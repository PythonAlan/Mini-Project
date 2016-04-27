#!/usr/bin/env python3

#antuor:Alan







products = [
    ['iphone 6s',5400],
    ['ipad pro',5800],
    ['macbook pro',14000],
    ['macbook air',7000],
    ['apple TV',2800],
]



salary = 30000

shop_list=[]
flage = 1
######################最简单的死循环,还没写购买数量###################################

while True:
    for index,p in enumerate(products): #自动添加序号,列出产品和价格
        print (index,p[0],p[1])



    choice = input('Choose to by :').strip()

    if  choice.isdigit():     #判断是否数字
        choice = int(choice) #整数
        qty = int(qty)
        p_price = products[choice][1]*qty #商品价格

        if p_price < salary :   #判断商品价格是否小于工资
            shop_list.append(products[choice]) #商品列表添加商品
            salary -= p_price #工资扣除购买费用
            print(('Has added %s into shop list and your current balance is %s') % (products[choice][0],salary))
        else:
            print('No')  #不够钱

    elif choice =='quit':   #退出

        print ('+++shop list +++')
        for k,v in enumerate(shop_list):  #列出购物车信息
            print (k,v)
        print(("Current balance is %s") % (salary))  #显示余额
        print('------Bye------')













