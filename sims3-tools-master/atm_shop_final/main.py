#!/usr/bin/env python
# -*- coding:utf-8 -*-


from atm.atm_operation import enchashment,query,repayment,transfer
from credit.credit_card import login_card,add_card,changePasswd,freeze_or_no,Credit_Line,query_all
from shopping.shopping_mall import shop_mall

flag = False
while not False:
    print("\033[34;1m\n 欢迎使用本程序!\033[0m")
    print("\033[32;1m%s\033[0m"%("-"*60))
    input_string = input("\033[34;1m\n1、在线购物\n2、信用卡操作\n3、信用卡管理\n4、退出系统\n请输入您的选择:\033[0m")
    if not input_string.isdigit():
        print("\033[31;1m请按提示输入对应选项！\033[0m")
    else:
        if input_string == "1":
            print("\033[31;1m欢迎光临oldboyPython在线商城！\033[0m")
            shop_mall()

        elif input_string == "2":
            print("\033[31;1m\n欢迎使用招行信用卡！\033[0m")
            flag1 =False
            while not flag1:

                card_number = input("\033[34;1m请按提示输入您的卡号:【默认卡号001,002,003;密码是123】\033[0m")

                if login_card(card_number):
                    print("\033[36;1m欢迎%s用户登录系统！\033[0m"%card_number)
                    while not flag:
                        print("\033[35;1m请数入您的操作:\n1、取现\n2、还款\n3、查询\n4、转账\n5、退出\033[0m")
                        input_string1 = input("\033[34;1m请输入您的选项:\033[0m")

                        if not input_string1.isdigit():
                            print("\033[31;1m请按提示输入对应选项！\033[0m")
                        else:
                            if input_string1 == "1":
                                enchashment(card_number)
                            elif input_string1 == "2":
                                repayment(card_number)
                            elif input_string1 == "3":
                                query(card_number)
                            elif input_string1 == "4":
                                transfer(card_number)
                            elif input_string1 == "5":
                                print("\033[34;1m已退出%s账号\033[0m"%card_number)
                                flag1 = True
                                break
                            elif int(input_string1) > 6 or int(input_string1) == 0:
                                print("\033[32;1m您输入的数字已超出范围,请重新输入！\033[0m")
                else:
                    print("登陆失败！")
                    break
        elif input_string == "3":
            print("\033[35;1m欢迎使用信用卡管理模块！\033[0m")
            admin_user = input("\033[30;1m您输入管理员账号【提示:管理员账号/密码为admin】:\033[0m")
            admin_pasw = input("\033[30;1m您输入管理员密码:\033[0m")
            if admin_user == "admin" and admin_pasw == "admin":
                print("\033[34;1m欢迎管理员 %s 登录系统！\033[0m"%admin_user)
                while not flag:
                    print("\033[35;1m您的操作如下:\n1、添加账户\n2、密码修改\n3、信用额度\n4、查询卡号信息\n5、冻结|解冻|删除卡号\n6、退出\033[0m")
                    input_string2 = input("\033[34;1m请输入操作选项:\033[0m")
                    if not input_string2.isdigit():
                        print("\033[31;1m请按提示输入对应选项！\033[0m")
                    else:
                        if input_string2 == "1":
                            add_card()
                        elif input_string2 == "2":
                            changePasswd()
                        elif input_string2 == "3":
                            Credit_Line()
                        elif input_string2 == "4":
                            query_all()
                        elif input_string2 == "5":
                            freeze_or_no()
                        elif input_string2 == "6":
                            break

        elif input_string == "4":
            break
            flag =True

        elif int(input_string) > 4 :
            print("\033[31;1m请输入选项范围内的数字！\033[0m")