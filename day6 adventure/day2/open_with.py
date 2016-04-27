#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan


def open_with():
    with (open('nba_list.txt','w')) as f:   # 等价于f = open('nba_list.txt','w')

        txt_contents = f.write('fuck man')
"""
with等价于f = open('nba_list.txt','w')
     f.close()
"""

if __name__ == '__main__':   #因为要单独调用脚本,所以要加这句,python3 open_with.py  ,if下的才执行
    open_with()