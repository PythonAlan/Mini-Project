#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

dic = {'f':123,'d':43,'r':'qwe'}

for k,v in enumerate(dic.items()):  #自动给键值对生成序号并打印出来

    print(k,v)
for k in enumerate(dic.keys()):  #自动给键生成序号并打印出来
    print(k)
for v in enumerate(dic.values()):  #自动给值生成序号并打印出来
    print(v)