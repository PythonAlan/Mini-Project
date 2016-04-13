#!/usr/bin/env python3
#antuor:Alan

import pymysql
conn = pymysql.connect(           #Connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息
    host = 'localhost',           #这只是连接到了数据库，要想操作数据库需要创建游标
    port = 3306,
    user = 'root',
    password = '',
    db = 'samp_db',
)
cur = conn.cursor()               #通过获取到的数据库连接conn下的cursor()方法来创建游标

sqli = 'insert into projectorlamps values(%s,%s,%s)'

cur.executemany(sqli,[            #executemany()方法可以一次插入多条值，执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
                (15,'gg',45),
                (12,'fg',18),
                (13,'ty',33),
                (14,'uy',20),


                ])
aa = cur.execute('select * from projectorlamps')   #通过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作
print (aa)

info = cur.fetchmany(aa)
for ii in info:
    print (ii)

#fetchone()方法可以帮助我们获得表中的数据，可是每次执行cur.fetchone() 获得的数据都不一样，
# 换句话说我没执行一次，游标会从表中的第一条数据移动到下一条数据的位置，
# 所以，我再次执行的时候得到的是第二条数据。

#fetchmany()方法可以获得多条数据，但需要指定数据的条数，通过一个for循环就可以把多条数据打印出啦！



conn.commit()        #conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入
cur.close()          #关闭游标
conn.close()         #关闭数据库连接