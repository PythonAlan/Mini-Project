#!/usr/bin/env python3
#antuor:Alan
import pymysql
import re
import requests
html = requests.get('http://www.cnblogs.com/alan-babyblog/')
page_code =html.text
#print(page_code)
title = re.findall('class="c_b_p_desc(.*?)<a href=',page_code) #正则表达式（）前后为内容段

conn = pymysql.connect(host ='localhost',user='root',
                               passwd='',db='ip_db',port =3306, charset ='utf8')  #链接数据库
cur = conn.cursor()  #设置游标

for t in title:
    cur.execute('insert into pachong_db(title) value(%s)',(t))  #注入sql语句
conn.commit()
cur.close()
conn.close()