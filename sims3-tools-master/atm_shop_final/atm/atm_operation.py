#!/usr/bin/env python
# -*- coding:utf-8 -*-
# print("\033[34;1m\n欢迎使用招行信用卡！\033[0m")

import pickle
import datetime
import time
import logging

info = {"001":[["2016-02-10 12:10:11","取现","100","0"],["2016-02-11 11:23:12","取现","110","0"]],
        "002":[["2016-02-10 12:10:11","取现","1300","0"],],
        "003":[["2016-02-24 12:12:11","取现","100","0"],]
        }

# info = {"001":[],
#         "002":[],
#         "003":[]
#         }
        #卡号   交易日期               交易金额   本期账单  利息
# with open("../atm_pikle.list","wb") as w_file:
#     pickle.dump(info,w_file)



#创建日志
logger = logging.getLogger('card_user_log')
logger.setLevel(logging.INFO)

# 创建控制台处理程序 和设置 debug级别
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#创建文件处理程序并设置INFO级别
fh = logging.FileHandler("card_user_log.log")
fh.setLevel(logging.INFO)

# 创建格式化程序
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 格式化ch 和 fh
# ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 添加ch 和 fh 的日志记录
logger.addHandler(fh)

# # 日志记录内容
# logger.info('2、info message')

#获取atm上的信息
with open("atm_pikle.list","rb") as r_file:
    data = pickle.load(r_file)

#获取信用卡上的信息
with open("card_mes_list","rb") as cr_file:
    data_card = pickle.load(cr_file)

#取现
def enchashment(arg):
    print("\033[34;1m%s\033[0m"%("_"*60))
    print("\033[34;1m当前取款卡号是:%s\033[0m"%arg)
    get_money = input("\033[34;1m请输入取款金额:\033[0m")
    if not get_money.isdigit():
        print("\033[34;1m输入金额不对,请重新输入:\033[0m")
    else:
        if int(get_money)>=100:
            pay_money= 0.0
            for i in data[arg]:
                pay_money += float(i[2])
            credit_line = eval(data_card[arg].get("credit_line"))/2 ##获取取款的额度
            totle= float(get_money) + pay_money #总取款额数
            if totle >= credit_line: #限制取款额度不能大于信用额度
                print("\033[31;1m已超过了该卡号的取款额度啦！\033[0m")
            else:
                new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #获取交易时间hh:mm:ss
                describe = "取款"
                data[arg].append([new_date,describe,get_money,"0"])
                if int(get_money)< 100: #取款手续费计算，每一笔小于10的额度，按每次10元的手续费计算
                    handling = 10
                elif int(get_money) >= 100:
                    handling = float(get_money) * 0.1 #大于10的额度，按照取款额的10%计算手续费
                data[arg].append([new_date,"取款手续费",handling,"0"])
                with open("atm_pikle.list","wb") as w_file:
                    pickle.dump(data,w_file)
            logger.info(arg+" 取现 "+get_money) # 日志记录内容
            print("\033[34;1m本次的取款额是:%s,取款手续费是:%.3f\033[0m"%(get_money,handling))
        else:
            print("\033[31;1m取款金额要大于100的整数倍\033[0m")
    print("\033[34;1m%s\033[0m"%("="*60))


#还款
def repayment(arg):
    print("\033[34;1m%s\033[0m"%("_"*60))
    print("\033[34;1m当前还款卡号是:%s\033[0m"%arg)
    pay_money = input("\033[34;1m请输入还款金额:\033[0m")
    if not pay_money.isdigit():
        print("\033[31;1m请输入正确的金额!\033[0m")
    else:
        describe = "还款"
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #还款时间
        data[arg].append([now_date,describe,'-'+pay_money,'0'])
        with open("atm_pikle.list","wb") as w_file:
            pickle.dump(data,w_file)
        logger.info(arg+" 还款 "+pay_money)
        print("\033[31;1m本次的还款额是:%s\033[0m"%(pay_money))
    print("\033[34;1m%s\033[0m"%("="*60))

#格式化日期(浮点数)
def format_float(arg):
    tmp = time.mktime(time.strptime(arg,'%Y-%m-%d %H:%M:%S'))
    return tmp

#查询(账单展示)
def query(arg):
    print("\033[34;1m%s\033[0m"%("_"*60))
    print("\033[34;1m所查询的用户卡号为:%s\033[0m"%(arg))
    print("\033[34;1m本期的账单区间是上个月的22号到本月的22号!\033[0m")
    print("\033[34;1m请在本月的10号之前还款,否则会产生相应是利息！\033[0m")
    last_month = (datetime.date.today().replace(day=1) - datetime.timedelta(2)).replace(day=22).strftime('%Y-%m-%d %H:%M:%S') #上个月的22号
    next_month = datetime.date.today().replace(day=22).strftime('%Y-%m-%d %H:%M:%S')
    last_pay =  datetime.date.today().replace(day=10).strftime('%Y-%m-%d %H:%M:%S') #本月10为上个周期的还款日

    payment = 0
    balance = 0
    repayment = 0 #还款
    print("\033[34;1m%s\033[0m"%("_"*60))
    print("\033[34;1m卡号 %s 的详单如下:\033[0m"%arg)
    print("\033[34;1m %s    %s  %s %s\033[0m" %("操作日期   时间","内容","金额","本次利息"))

    if data[arg]:
        for ele in data[arg]:
            if format_float(ele[0]) > format_float(last_month) or format_float(ele[0]) <= format_float(next_month):
                #利息计算
                day1 = (format_float(ele[0]) - format_float(last_pay)) / 86400 #
                if ele[1] == "还款":
                    repayment += float(ele[2])
                else:
                    payment += float(ele[2])
                balance += float(ele[2])
            print("\033[30;1m%s %s %s %s\033[0m"%(ele[0],ele[1],ele[2],ele[3]))
            nterest = float(ele[3]) * 0.0005 * day1 + (float(ele[3]) - repayment) * 0.0005 * day1
    else:
        nterest = 0.0
    print("\033[34;1m%s\033[0m"%("-"*60))
    if abs(repayment) >= payment:
        print("\033[31;1m本期最低还款金额是:%.3f\033[0m"%(0))
    else:
        print("\033[31;1m本期最低还款金额是:%.3f\033[0m"%((payment * 0.1) ))
    logger.info(arg+"进行查询操作！")
    print("\033[34;1m本期还款是￥ = 本期还款金额￥ + 本期交易金额￥ + 本期利息￥\033[0m")
    print("\033[31;1m  %.3f       %.3f       %.3f      %.3f\033[0m"%((payment+repayment+nterest),repayment,payment,nterest))
    print("\033[34;1m%s\033[0m"%("_"*60))

#转账
def transfer(arg):
    print("\033[34;1m%s\033[0m"%("_"*60))
    print("\033[34;1m转账操作进行中...\033[0m")
    account = input("\033[34;1m请输入对方的账号:\033[0m")
    if account != arg:
        if account in data.keys():
            pay_money = input("\033[34;1m请输入转账金额:\033[0m")
            if not pay_money.isdigit():
                print("\033[31;1m请输入正确的金额!\033[0m")
            else:
                print("\033[34;1m当前的转账操作是:从当前账号%s传入%s账号中...\033[0m"%(arg,account))
                describe = "转出"
                now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #还款时间
                data[arg].append([now_date,describe,pay_money,'0'])
                data[account].append([now_date,"转入",'-'+pay_money,'0'])
                logger.info(arg+"向卡号"+account+"转账 "+pay_money)
                print("\033[31;1m您已成功从当前卡号%s转出%s金额到%s账号中！\033[0m"%(arg,pay_money,account))
        else:
            print("\033[31;1m输入的账号不存在!\033[0m")
    else:
        print("\033[31;1m不能向本账号转账!\033[0m")
    print("\033[34;1m%s\033[0m"%("_"*60))
#退出
def quit():
    exit()
