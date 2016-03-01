#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import pickle
bash_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bash_dir) #把当前程序的路径加入环境变量中

from credit.credit_card import card_payment
product_list = [
    ('Iphone6s平板', 3888),
    ('MacBook本', 4700),
    ('CookBook书', 50),
    ('大势力架', 30),
    ('小米笔记本', 1100),
    ('小米手机', 830),
]
user_asset = 10000

def shop_mall():
    break_flag = False
    shopping_cart = []
    paid_list = []
    print("\033[32;1m%s\033[0m"%("-"*60))
    while not break_flag:
        print("\033[34;1m序号\t商品名\t\t单价\033[0m")
        print("\033[32;1m%s\033[0m"%("-"*60))
        for index,i in enumerate(product_list,1):
            print("\033[35;1m %d %s %s\033[0m"%(index,i[0],i[1]))
        user_choice = input("\033[34;1mq:退出\nc:检查购物车\np:信用卡支付\n请选择您要购买的商品编号或选项:\033[0m").strip()
        if user_choice.isdigit():
            print("\033[34;1m%s\033[0m"%("-"*60))
            user_choice = int(user_choice)-1
            if user_choice < len(product_list) and user_choice > -1:
                shopping_cart.append(product_list[user_choice])
                print("\033[35;1m选择 [%s,%s] 商品到购物车中\033[0m" %(product_list[user_choice]))
            else:
                print("\033[31;1m您选择的[%s]商品不存在,请重新选择！\033[0m"%user_choice)
            print("\033[34;1m%s\033[0m"%("-"*60))
        elif user_choice == "c":
            print("\033[34;1m%s\033[0m"%("-"*60))
            total_price = 0
            if len(shopping_cart):
                print("\033[34;1m您购买的商品如下:\033[0m")
                for index,p in enumerate(shopping_cart,1):
                    print("\033[35;1m%d  %s  %s\033[0m" %(index,p[0],p[1]))
                    total_price += p[1]
                print("\033[31;1m总共消费:[%s]元\033[0m" % total_price)

            else:
                print("\033[31;1m购物车为空！\033[0m")
            print("\033[34;1m%s\033[0m"%("-"*60))
        elif user_choice == "p":
            total_price = 0
            print("\033[34;1m您所购买的商品如下:\033[0m")
            print("\033[32;1m%s\033[0m"%("-"*60))
            print("\033[30;1m序号\t商品名\t\t单价\033[0m")
            for index,p in enumerate(shopping_cart,1):
                print("\033[34;1m %d %s %s\033[0m"%(index,p[0],p[1]))
                total_price += p[1]
            print("\033[31;1m需要支付:[%s]\033[0m" % total_price)
            print("\033[32;1m%s\033[0m"%("-"*60))
            is_pay = input("\033[34;1m是否使用信用卡进行支付 Y/N ?\033[0m")
            if is_pay=="Y" or is_pay == "y" and total_price>0:
                card_payment(total_price)
                shopping_cart = []
            else:
                print("\033[31;1m订单为空,不能支付！\033[0m")
                print("\033[34;1m%s\033[0m"%("——"*15))
                break


        elif user_choice == "Q" or user_choice == "q":
            # if shopping_cart:
            #     print("\033[31;1m您购物车中还有商品未付款！\033[0m")
            # else:
            #     print("\033[31;1m谢谢光临！\033[0m")
            break_flag = True


