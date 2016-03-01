#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle
import re
import datetime

info = {"001":{"passwd":"123","credit_line":"15000","card_flag":"0"},
        "002":{"passwd":"123","credit_line":"15000","card_flag":"0"},
        "003":{"passwd":"123","credit_line":"15000","card_flag":"0"}
        }
        #卡号   密码            信用额                 冻结标识
# with open("../card_list/test_card_mes_list","wb") as w_file:
#     pickle.dump(info,w_file)

# with open("../card_mes_list","wb") as w_file:
#     pickle.dump(info,w_file)

with open("card_mes_list","rb") as r_file:
    r_data = pickle.load(r_file)

with open("atm_pikle.list","rb") as atm_file:
    atm_data = pickle.load(atm_file)

#卡号登陆
def login_card(arg):
    if arg in r_data.keys():
        if r_data[arg]["card_flag"] == "0":
            p_flag = False
            login_time = 1
            while not  p_flag:
                input_passwd = input("\033[34;1m请输入密码:\033[0m")

                if input_passwd.isdigit() and input_passwd == r_data.get(arg).get("passwd"):
                    return True
                else:

                    login_time +=1
                    if login_time>3:
                        print("\033[31;1m%s的登陆密码输出错误 3 次!\033[0m"% arg)
                        freeze(arg)
                        return False
        else:
            return False
            print("\033[31;1m该卡号已被锁定,请解锁后再登录！\033[0m")
    else:
        print("\033[31;1m没有该卡号!\033[0m")
        return False


#添加卡号
def add_card():
    # print(r_data)
    break_flag = False
    while not break_flag:
        card_number = input("\033[34;1m请输入要添加的卡号:\033[0m")

        if card_number != "":
            if not re.findall("[^0-9a-zA-Z|_]",card_number):

                if card_number not in r_data.keys():
                    card_paswd = input("\033[34;1m请输入要添加的密码:\033[0m")

                    credit_line = input("\033[34;1m请输入该卡号的信用额度:\033[0m")
                    if not credit_line.isdigit():
                        print("\033[31;1m请输出正确的整数!\033[0m")
                    else:
                        card_flag = "0"
                        r_data[card_number] = {"passwd":card_paswd,"credit_line":credit_line,"card_flag":card_flag}
                        print("\033[34;1m新卡号添加完成！信用卡的信息如下:\n卡号\t密码\t信用额度\t状态\033[0m")
                        with open("card_mes_list","wb") as w_file5:
                            pickle.dump(r_data,w_file5)
                        if card_number not in atm_data.keys():
                            atm_data[card_number] = [] #添加卡号记录
                            with open("atm_pikle.list","wb") as w_file6:
                                pickle.dump(atm_data,w_file6)
                        if card_flag == "0":
                            card_flag = "正常"
                        print("\033[31;1m%s     %s     %s     %s\033[0m"%(card_number,r_data[card_number]["passwd"],r_data[card_number]["credit_line"],card_flag))
                        break_flag = True
                else:
                    print("\033[31;1m该卡号已存在,请重新选择！\033[0m")
            else:
                print("\033[31;1m账号只允许数字、字母、下划线组成！\033[0m")
        else:
            print("\033[31;1m账号不允许为空！\033[0m")

#修改密码
def changePasswd():
    card_number = input("\033[34;1m输入您要修改的账号:\033[0m")
    if card_number not  in r_data.keys():
        print("\033[31;1m您输入的账号不存在,请重新输入:\033[0m")
    else:
        new_passwd = input("\033[34;1m输入您的新密码:\033[0m")
        re_passwd = input("\033[34;1m请确认您的新密码:\033[0m")
        if new_passwd != re_passwd:
            print("\033[34;1m请 2 次输入的密码不同,请重新输入:\033[0m")
        else:
            r_data[card_number]["passwd"] = new_passwd
            with open("card_mes_list","wb") as w_file6:
                pickle.dump(r_data,w_file6)


#冻结账号
def freeze(arg):
    # print("冻结卡号")
    r_data[arg]["card_flag"] = "1"
    with open("card_mes_list","wb") as w_file1:
        pickle.dump(r_data,w_file1)
        print("\033[34;1m已冻结了%s卡号!\033[0m"% arg)

#解冻
def unfreeze(arg):
    # print("解冻卡号")
    r_data[arg]["card_flag"] = "0"
    with open("card_mes_list","wb") as w_file2:
        pickle.dump(r_data,w_file2)
        print("\033[34;1m已解冻了%s卡号!\033[0m"% arg)
#删除卡号
def del_card(arg):
    print("\033[34;1m%s\033[0m"%("——"*15))
    r_data.pop(arg)
    with open("card_mes_list","wb") as w_file3:
        pickle.dump(r_data,w_file3)
        print("\033[31;1m已删除了%s卡号!\033[0m"% arg)
    print("\033[34;1m%s\033[0m"%("——"*15))

def freeze_or_no():
    break_flag =False
    print("\033[31;1m卡号列表:\033[0m")
    for card_list in r_data.keys():
        print("\033[31;1m%s\033[0m"%card_list)

    while not break_flag:
        print("\033[34;1m1:冻结卡号\t2:解冻卡号\t3:删除卡号\t4:返回\033[0m")
        ask = input("\033[34;1m请问您选择是:\033[0m")

        if not ask.isdigit():
            print("\033[31;1m请正确选择数字选项！\033[0m")
        else:
            if ask == "1":
                card_number1 = input("\033[34;1m请输入您要冻结的卡号:\033[0m")
                if card_number1 not in r_data.keys():
                    print("\033[31;1m您输入的卡号不存在,请重新输入!\033[0m")
                else:
                    freeze(card_number1)
                    break_flag = True
            elif ask == "2":
                card_number2 = input("\033[34;1m请输入您要冻结的账号:\033[0m")
                if card_number2 not in r_data.keys():
                    print("\033[31;1m您输入的账号不存在,请重新输入!\033[0m")
                else:
                    unfreeze(card_number2)
                    break_flag = True
            elif ask == "3":
                card_number3 = input("\033[34;1m请输入您要冻结的卡号:\033[0m")
                if card_number3 not in r_data.keys():
                    print("\033[31;1m您输入的账号不存在,请重新输入!\033[0m")
                else:
                    del_card(card_number3)
                    break_flag = True
            elif ask == "4":
                break
            elif int(ask) > 3:
                print("\033[31;1m请正确选择 1 到 3 选项,\033[0m")

#信用额度修改
def Credit_Line():
    print("\033[34;1m%s\033[0m"%("——"*15))
    credit_number = input("\033[34;1m请输入您要设置的卡号:\033[0m")
    if credit_number not  in r_data.keys():
        print("\033[31;1m您输入的卡号不存在,请重新输入:\033[0m")
    else:
        set_credit_line = input("\033[34;1m请为这张卡号设置信用额:\033[0m")
        if not set_credit_line.isdigit():
            print("\033[31;1m请输入正确的数字\033[0m")
        else:
            if int(set_credit_line) >15000:
                print("\033[31;1m该卡的信用额上限为15000!请重输入!\033[0m")
            else:
                r_data[credit_number]["credit_line"] = set_credit_line
                with open("card_mes_list","wb") as w_file4:
                    pickle.dump(r_data,w_file4)
                    print("\033[31;1m卡号 %s 的信用额度已变更为:%s!\033[0m"% (credit_number,set_credit_line))
                    print("\033[34;1m%s\033[0m"%("——"*15))
#查询所有卡号的信息
def query_all():
    print("\033[34;1m%s\033[0m"%("——"*17))
    print("\033[34;1m卡号\t信用额度\t状态\t交易额\t总利息\033[0m")
    deal = 0.0
    nterest = 0.0
    for c,v in r_data.items():
        result = "正常" if v["card_flag"] =="0" else "锁定"
        for i in atm_data[c]:
            deal += float(i[2])
            nterest += float(i[3])
        # print(c,v["credit_line"],result,deal,nterest)
        print("\033[34;1m%s   %s     %s    %s    %s \033[0m"%(c,v["credit_line"],result,deal,nterest))
    print("\033[34;1m%s\033[0m"%("——"*17))
#商城登陆验证
def login(func):
    def inner(*args,**kwargs):
        flag = False
        while not flag:
            c_number = input("\033[34;1m请输入您的信用卡号:\033[0m")
            if login_card(c_number):

                credit_line = float(r_data[c_number].get("credit_line"))
                get_totle = 0.0
                for tm in atm_data[c_number]:
                    if not str(tm[2]).startswith("-"):
                        get_totle += float(tm[2])
                canuser = credit_line - get_totle #计算可用余额
                print("\033[34;1m当前卡信用的可用余额为%s\033[0m"% canuser)
                if canuser < args[0]:
                    print("\033[34;1m当前信用卡的可用余额不足！\033[0m")
                else:

                    describe = "网购"
                    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #还款时间
                    atm_data[c_number].append([now_date,describe,str(args[0]),'0'])
                    with open("atm_pikle.list","wb") as w_file8:
                        pickle.dump(atm_data,w_file8)

                    print("\033[34;1m当前交易完成！\033[0m")
                    return func(*args,**kwargs)

            else:
                print("\033[31;1m输入的卡号不存在或是被冻结！请重新输入!\033[0m")
    return inner

#商城支付
@login
def card_payment(arg):
    print("\033[36;1m本次服务完成,欢迎下次光临！\033[0m")

