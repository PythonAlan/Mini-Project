#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

############用户注册函数#####################
def register():
    new_username = input('请输入注册用户名:')
    new_password = input('请输入新用户密码:')
    bank_money = 0

    while True:
        new_password_again = input('请再次确认新用户密码:')    ###再次确认密码
        if new_password_again != new_password:                    ###密码错误则循环
            continue
        else:
            break                                         ###正确则跳出循环执行下一个循环
    while True:
        bank_money = input('请输入你要充值的金额:')          ###输入金额数字
        if bank_money.isdigit():                          ###判断金额是否为数字
            bank_money = int(bank_money)                  ###金额数字整数化
            break
        else:                                             ###如果金额非数字则不断循环
            print('请输入正确的金额')

    user_account = "%s %s %d" % (new_username,new_password,bank_money)
    file = open('text.txt','a+')
    save_file = file.write(user_account+'\n')
    file.close()

    print (("恭喜你注册成功:%s") % (user_account))
    # with open('buyer_account.txt','w') as file:          ###把用户信息存入文档,a+为读写追加模式
    #     file.write(user_account+'\n')                     ###写入并换行
if __name__=="__main__":
    register()



####保存上次的账户???