#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

def open_txt():
    f = open('nba_list','+w')
    try:
        f.write('hi,2016 nba all start game')
        Post_lines = f.readlines()
        print(Post_lines)
    except:
        print ("this file can't open")
    finally:
        f.close()

    return
if __name__ == '__main__':
    open_txt()

