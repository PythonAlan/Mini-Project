#!/usr/bin/env python3
#antuor:Alan




from urllib.request import urlopen

import requests
import json


url = "http://apis.baidu.com/txapi/mvtp/meinv"         #API
req = requests.get(url)
headers= {'apikey':'自己的apikey'}  #自己的apikey
params = {'num':'5'}                                    #请求参数(urlParam) :
r = requests.get(url,params=params,headers=headers)
print(r)

print(r)
def SaveImage(ImageUrl,ImgName= 'default.jpg'):
    response = requests.get(ImageUrl,stream = True)
    image = response.content

    dst = '/Users/Alan/desktop/BaiDUImages/'
    path  = dst+ImgName
    print('Save the file:',path)
    with open(path,'wb') as img:
        img.write(image)
def run():
    for line in r['newslist']:
        title = line['title']
        picUrl = line['picUrl']
        SaveImage(picUrl,ImgName=title+'.jpg')
run()

