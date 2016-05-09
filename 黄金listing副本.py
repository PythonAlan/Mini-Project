#!/usr/bin/env python3
#antuor:Alan


import re
import requests

import threading
import time

import datetime
from lxml import etree




sku = {
    'B005HB7T38':'01-00247',
    'B00RMEE76K':'01-00247',
    'B005HB7WLM':'20-01032-20',
    'B00460PIAM':'ELPLP42',
    'B000P59HAO':'ELPLP42',
}


sku1 = {
    'B00J80PAZI':'20-01032-20',
    'B00795EGBS':'20-01175-20',
    'B00DUTNIK2':'VIP230W0.8E20.8',
    'B00735Z2H6':'ELPLP42',
    'B007CJQ588':'ELPLP49',
}

sku2 = {
    'B00GMV0U4C':'20-01175-20',
    'B00DTTVOYU':'20-01175-20',
    'B0067PIEPU':'ELPLP60',
    'B0041TNRYW':'ELPLP54',
    'B00FWNIJBW':'ELPLP42',
}

sku3 = {
    'B00PB4WBNE':'AN-F212LP',
    'B00QF1EHUM':'AN-K15LP',
    'B00M0ETHG2':'B00M0ETHG2',
    'B005FIVJG6':'ELPLP67',
    'B016U402WU':'ELPLP42'
}



sku4 = {
    'B00QGIDFAW':'BL-FU310B',
    'B00GB83UXO':'ET-LAB80',
    'B001AJ8YOE':'ELPLP42',
    'B00BQUWZ56':'ELPLP49',
    'B007YW40JY':'ELPLP54',

}





Re_price = '<span id="priceblock_ourprice" class="a-size-medium a-color-price">(.*?)</span>'  #不匹配货币符号，用斜杠转译

#Re_soldby = '>(.*?)</a> and'

#Re_other_price = '<span class="a-size-medium a-color-price">(.*?)</span>'

#Re_other_sellers = '<span class="a-size-small mbcMerchantName">(.*?)</span>'


headers_am = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}

def Scraper(kw):
    global other_seller_2nd
    global other_price_2nd
    for i,v in kw.items():
        try:
            product_page = 'http://www.amazon.com/dp/{}'.format(i)
            response = requests.get(product_page,headers=headers_am)
            price = re.findall(Re_price,response.text) #        搜索第1名价格 如果要找全部的话re.findall(Re_rule,response.text)
            tree = etree.HTML(response.text)
            soldby = tree.xpath('//div[2]/div[9]/div[5]/div[14]/div/a/text()') #用lxml，xpath获取节点元素
            other_price = tree.xpath('//div[2]/div[9]/div[3]/div[5]/div/div[1]/div/div[2]/div/span[2]/div/div[1]/span[1]/text()')[0].strip()
            other_seller = tree.xpath('//div[2]/div[9]/div[3]/div[5]/div/div[1]/div/div[2]/div/span[2]/div/div[2]/span[2]/text()')[0].strip()
        except AttributeError:
            print('{}查找不到'.format(i))

        try:
            other_price_2nd = tree.xpath('//div[2]/div[9]/div[3]/div[5]/div/div[1]/div/div[3]/div/span[2]/div/div[1]/span[1]/text()')[0].strip()
            other_seller_2nd = tree.xpath('//div[2]/div[9]/div[3]/div[5]/div/div[1]/div/div[3]/div/span[2]/div/div[2]/span[2]/text()')[0].strip()
        except (IndexError,NameError):
            print('其它卖家(2):没显示')
        with open('/Users/Alan/desktop/am_scraper.txt','a') as f:
            f.write('ASIN:{0} 型号:{8} 爬去完毕at{1}'
                    '\n结果:\nBuybox价:{2},Soldby:{3},'
                    '\n其它卖家(1){4} By:{5}'
                    '\n其它卖家(2){6} By:{7}\n'.format(i,time.ctime(),price,soldby,other_price,other_seller,other_price_2nd,other_seller_2nd,v))


        print('--------ASIN:{0} 型号:\033[1;36;40m{8}\033[0m爬去完毕at{1}结果:\nBuybox价:\033[1;31;40m{2}\033[0m,Soldby:\033[1;32;40m{3}\033[0m,'
              '\n\033[1;36;40m其它卖家(1)\033[0m:{4} By:{5} '
              '\n\033[1;36;40m其它卖家(2)\033[0m:{6} By:{7}'.format(i,time.ctime(),price,soldby,other_price,other_seller,other_price_2nd,other_seller_2nd,v))
    time.sleep(1)


threads = []

t1 = threading.Thread(target=Scraper,args=(sku,))
threads.append(t1)
t2 = threading.Thread(target=Scraper,args=(sku1,))
threads.append(t2)
t3 = threading.Thread(target=Scraper,args=(sku2,))
threads.append(t3)
t4 = threading.Thread(target=Scraper,args=(sku3,))
threads.append(t4)
t5 = threading.Thread(target=Scraper,args=(sku4,))
threads.append(t5)


if __name__ == '__main__':
    time_start = datetime.datetime.now()
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    time_end = datetime.datetime.now()
    print ("共耗时:",(time_end-time_start))