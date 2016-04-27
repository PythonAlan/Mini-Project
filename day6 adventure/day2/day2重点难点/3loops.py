#!_*_coding:utf-8_*_


# don't make your programs have too many layers
# if you do have that many layers , try to use the function feature .

#in shell , break 2 3
break_flag = False                                                     #标记1
break_flag2 = False                                                    #标记2
break_flag3 = False                                                    #标记3
while not break_flag:                                                  #因为标记是False,所以是 not break_flag成立循环
    print("the first layer is running...")
    option=input(">>>[b:back, q:quit,c:continue]:").strip()            #让买家选择,strip()去除输入时空格
    if option == "b":
        break_flag2 = True                                             #第一层,没得退,所以break_flag2=true,不断打印'the first...'
    elif option == "q":
        break_flag = True                                              #选择退出,把循环条件改为true,就能退出循环
    else:
        break_flag3,break_flag2 = False,False                          #既不是b,也不是q,则第二三层循环条件继续成立,往下走
    while not (break_flag or break_flag2):                             #进入第二层,那么第一层循环条件必须是false,q时随时可以退出
        print("in layer two...")
        option=input(">>>[b:back, q:quit,c:continue]:").strip()
        if option == "b":
            break_flag2 = True                                         #退到第一层,因为else:break_flag3,break_flag2 = False,False
        elif option == "q":
            break_flag = True                                          #退出整个循环
        else:
            break_flag2,break_flag3 = False,False                      #这里可以实现第二层第三层的切换

        while not(break_flag or break_flag2 or break_flag3):           #与上面同理
            print("in layer three...")
            option=input(">>>[b:back, q:quit,c:continue]:").strip()
            if option == "b":
                break_flag3 = True
            elif option == "q":
                break_flag = True