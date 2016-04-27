2#!/use/bin/env python
#coding: utf-8

# ############################################
# DESC：Day1 的需求作业一和作业二
# Create Date：2016-01-15
# Student ID：29
# Author：Knightseal
# #############################################

from ToolBox import toolbox,read_the_file,caidan

# 定义错误次数
erro_count = 3

# 定义数据文件名称
dbfile = 'test.log'


#主程序
toolbox = toolbox(dbfile)

while True:
  
    c_type = input("=====欢迎使用ToolBOX,请选择操作:\n如要注册请输入: 1\n如要登录请输入: 2\n如要退出请输入: 3\n请选择选择:")
    user_data = read_the_file(dbfile)
    
    if c_type == '3':
        break

    if c_type == '2':
        y = toolbox.login(user_data,erro_num=erro_count,)
        if y == 0 or y == 3:
            continue
        else:
            x = caidan()
            if x == 0:
                continue

    if c_type == '1':
        x = toolbox.register(user_data)
        continue
    else:
        print("不要闹了,好好选")
        continue

