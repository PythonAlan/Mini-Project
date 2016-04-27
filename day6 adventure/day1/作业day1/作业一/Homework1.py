#!/user/bin/env python3
# -*- coding:utf-8 -*-

'''
Created on: 2015年1月16日

@author: 吕毅

Email: 371725153@qq.com

Version: 1.0

Description: 输入用户名密码，认证成功显示欢迎信息，认证失败，输错三次后锁定


'''

import sys,os,getpass


os.system('clear')                                                  #把终端代码页面清空,提供个干净的视觉
i = 0
while i < 3:                                                        #只要用户登录异常不超过3次就不断循环
    username = input("请输入用户名:")

    lock_file = open('user_lock.txt','r+')                       #当用户输入用户名后，打开LOCK 文件 以检查是否此用户已经LOCK了
    lock_list = lock_file.readlines()

    for lock_line in lock_list:                                     #循环LOCK文件
        lock_line = lock_line.strip('\n')                           #去掉换行符
        if username == lock_line:                                       #如果LOCK了就直接退出
            sys.exit('=======WARNING:该账号 %s 已经被冻结========' % username)

    user_file = open('user_id.txt','r')                             #打开帐号文件
    user_list = user_file.readlines()
    for user_line in user_list:                                     #对帐号文件进行遍历
        (user,password) = user_line.strip('\n').split()             #分别获取帐号和密码信息
        if username == user:                                            #如用户名正常匹配
            m = 0
            while m < 3:                                            #只要用户密码异常不超过3次就不断循环
                passwd = getpass.getpass('请输入密码:')              #输入密码,相对安全
                if passwd == password:                              #密码正确，提示欢迎登录
                    print('HI,%s,欢迎登录系统' % username)
                    sys.exit(0)                                     #正常退出
                else:
                    if m != 2:                                      #j=2时，是最后一次机会，不用在提示还剩余0次机会了
                        print('用户 %s 密码错误，请重新输入，还有 %d 次机会' % (username,2 - m))
                m += 1                                              #密码输入错误后，循环值增加1
            else:
                lock_file.write(username + '\n')                        #密码输入三次错误后，将该用户追加到LOCK文件
                sys.exit('用户 %s 达到最大登录次数，请联系管理员!!' % username)
        else:
            pass                                                    #当用户没匹配时，跳过并继续循环
    else:
        if i != 2:                                                  #i=2时，是最后一次机会，不用在提示还剩余0次机会了
            print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (username,2 - i))
    i += 1                                                          #当用户输入错误时，循环值增加1
else:
    sys.exit('用户 %s 不存在，退出' % username)                           #用户输入三次错误后，异常退出

lock_file.close()                                                   #关闭LOCK文件
user_file.close()                                                   #关闭帐号文件