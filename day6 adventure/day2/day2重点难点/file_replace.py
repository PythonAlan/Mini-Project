
import os                                                       #os操作系统模块
f = open("test.txt","r")                                        #旧文件读模式
f_new = open("text_new.txt","w")                                #新文件写模式
for line in f:                                                  #遍历旧文件
    if line.startswith("alex"):                                 #找到要替换的行
        new_line = line.replace("alex","ALEX LI....")           #替换好赋值给新行
        f_new.write(new_line)                                   #把新行写到新文件
    else:
        f_new.write(line)                                       #如果找不到,则把原文写到新文件
f.close()
f_new.close()
os.rename("test.txt","test.txt.bak")                            #把旧文件改名为back up
os.rename("text_new.txt","test.txt")                            #新文件覆盖旧文件

'''
f = open("test.txt","r+")
for line in f:
    if line.startswith("alex"):
        new_line = line.replace("alex","ALEX LI")
        print("current pos:",f.tell())                          #显示指针的位置
        f.seek(37)                                              #把指针指到该位置
        f.write(new_line)
        break
f.close()
'''