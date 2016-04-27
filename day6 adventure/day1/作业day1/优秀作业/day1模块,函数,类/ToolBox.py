#coding:utf-8
# ############################################
# DESC：ToolBox lib
# Create Date：2016-01-15
# Student ID：29
# Author：Knightseal
# #############################################

import os
import json
import linecache
from datetime import  datetime

class toolbox(object):
    """
    这个类，把需要作业的一和二合并，包括登录三次锁定，已经三级菜单实现
    """

    dbfile = None

    def __init__(self,dbname):
        """
        :para:dbname:数据文件名称，不需要全路径，会自动在当前目录生成
        """
        db_path = os.path.abspath(os.curdir)
        dbfile = '%s/%s' % (db_path,dbname)
        self.dbfile = dbfile
        default= { "admin":{ "password" :"admin","locked_status":False,"loced_time":False}}
        if  os.path.exists(dbfile):
            file_data = linecache.getlines(dbfile)
            if file_data:
                pass
            else:
                #初始化数据文件
                with open(dbfile,'w') as f:
                    inserter_data = "%s\n" % json.dumps(default)
                    f.write(inserter_data)

        else:
            # 初始化数据文件
            with open(dbfile,'w') as f:
                inserter_data = "%s\n" % json.dumps(default)
                f.write(inserter_data)

    def register(self,user_data):
        """
        注册模块
        :para:user_data 数据内部，用于判断是否已经注册等等操作
        """
        username = input("=====请输入您要注册的用户名:")
        password = input("=============请输入密码:")
        if username and password:
            if username in user_data.keys():
                print("用户:%s,已经存在,退出注册"%username)
                return 0
            else:
                data= { username:{ "password" :password,"locked_status":False,"loced_time":False}}
                with open(self.dbfile,'a') as f:
                    inserter_data = "%s\n" % json.dumps(data)
                    f.write(inserter_data)
                print(" %s 注册成功" % username)
                return 0

        else:
            print("用户名或者密码不可以为空,退出注册")
            return 0

    def login(self,user_data,erro_num=3):
        """
        登录模块
        :para:user_data:用户数据，用于判断登录用户信息;erro_num:允许的输错密码的错误次数
        """
        x = 0
        #user_data = self.read_the_file(self.dbfile)
        username = input("======请输入用户名:")
        if username in user_data.keys():
            #print(user_data[username]["locked_status"])
            if user_data[username]["locked_status"]:
                print("用户%s,在%s被锁定,退出登录模块"%(username,user_data[username]["locked_time"]))
                return 0
            else:
                while x < erro_num:
                    password = input("======请输入密码:")
                    if password == user_data[username]["password"]:
                        print("%s登录成功,<三级菜单选择>:" % username)
                        break
                    else:
                        print("输出错误第%s次"%(x+1))
                        x += 1
                        continue
                else:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print("用户:%s 在 %s被锁定"% (username,timestamp))
                    user_data[username]['locked_status'] = True
                    user_data[username]['locked_time'] = timestamp
                    write_back = []
                    for a in user_data.keys():
                        write_back.append(json.dumps({a:user_data[a]}))
                        write_back.append('\n')
                    with open(self.dbfile,'w') as f:
                        f.write(''.join(write_back))
                    return 3


        else:
            print("用户名不存在,退出登录模块")
            return 0


def read_the_file(filename):
        """
        读取文件
        :return: 数据文件内容
        """
        data = {}
        db_path = os.path.abspath(os.curdir)
        dbfile = '%s/%s' % (db_path,filename)

        file_data = open(dbfile,'r').readlines()

        for line in file_data:
            try:
                x = json.loads(line.replace('\n',''))
                data.update(x)
            except Exception as e:
                print(str(e))
                pass
        return data

def caidan():
    """
    三级菜单自己造点数据
    :return:
    """

    province = {"1":"河北省","2":"湖南省","3":"安徽省"}
    city = {"河北省":{"1":"唐山","2":"石家庄","3":"邯郸市"},"湖南省":{"1":"长沙市","2":"株洲市","3":"湘潭市"},"安徽省":{"1":"合肥市","2":"芜湖市","3":"蚌埠市"}}
    area = {"唐山":{"1":"路北区","2":"路南区","3":"古冶区"},"石家庄":{"1":"长安区","2":"桥西区","3":"新华区"},"邯郸市":{"1":"邯山区","2":"丛台区","3":"复兴区"},
            "长沙市":{"1":"岳麓区","2":"芙蓉区","3":"天心区"},"株洲市":{"1":"天元区","2":"荷塘区","3":"芦淞区"},"湘潭市":{"1":"雨湖区","2":"岳塘区","3":"湘乡市"},
            "合肥市":{"1":"高新区","2":"新站区","3":"经开区"},"芜湖市":{"1":"镜湖区","2":"弋江区","3":"鸠江区"},"蚌埠市":{"1":"蚌山区","2":"龙子湖区","3":"禹会区"}}
    s = 0
    while s < 1:
        # 列出省份
        for p in province.keys():
            print(p,province[p])
        # 第一次选择省份
        level1 = input("请输入省份id(输入q退出):\n")

        if level1 == 'q':
            break
            return 3
        elif level1 not in ("1","2","3"):
            print("就三个,不要闹了")
            continue
        else:
            # 得到省份名称
            province_name = province[level1]
            s1 = 0
            while s1 < 1:
                # 列出城市
                for c in city[province_name].keys():
                    print(c,city[province_name][c])
                # 第二次选择城市
                level2 = input("您选择了:%s,请选择市ID:,输入b返回,输入q退出" % province_name)
                if level2 == 'q':
                    s1 = 1

                elif level2 == 'b':
                    break
                elif level2 not in ("1","2","3"):
                    print("就三个,不要闹了")
                    continue
                else:
                    # 得到城市名称
                    city_name = city[province_name][level2]
                    s2 = 0
                    while s2 <1:
                        # 列出区域
                        for a in area[city_name].keys():
                            print(a,area[city_name][a])
                        # 得到区域名称
                        level3 = input("您选择了:%s,请选择区ID:,输入b返回,输入q退出" % city_name)
                        if level3 == 'q':
                            s2 = 1

                        elif level3 == 'b':
                            break
                        elif level3 not in ("1","2","3"):
                            print("就三个,不要闹了")
                            continue

                        else:
                            area_name = area[city_name][level3]
                            last = input("您选择了:%s,输入b返回,输入q退出,"% area_name)
                            if last == 'b':
                                break
                            if last =='q':
                                s2 = 1
                    else:
                        s = 1
                        break
            else:
                s = 1
                break
    return 0

