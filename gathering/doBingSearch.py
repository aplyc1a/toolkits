# -*- coding: utf-8 -*-

'''
@Time         : 2021 08/18
@Author       : aplyc1a
@Repositories : https://github.com/aplyc1a/toolkits
'''

import requests
from bs4 import BeautifulSoup
import time
import pprint
import random

def bing_search(keywords):
    i = 0
    duplicate_counter = 0
    urls=[]
    subdomains=[]
    fp_u = open("bing_urls.txt","a+")
    fp_d = open("bing_domains.txt","a+")
    while True:
        i+=1
        j=i*10
        UA_headers=[
                {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
                {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
                {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'},
                {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
                {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
                {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
                {'User-Agent':'Mozilla/5.0(Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'},
                {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/17D50 UCBrowser/12.8.2.1268 Mobile AliApp(TUnionSDK/0.1.20.3)'},
                {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; OPPO R11t Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.1.0)'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 SP-engine/2.14.0 main%2F1.0 baiduboxapp/11.18.0.16 (Baidu; P2 13.3.1) NABar/0.0'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.10(0x17000a21) NetType/4G Language/zh_CN'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
        ]
        url='https://cn.bing.com/search?q='+keywords+'&qs=n&form=QBRE&sp=-1&sc=2-11&sk=&cvid=C1A7FC61462345B1A71F431E60467C43&toHttps=1&redig=3FEC4F2BE86247E8AE3BB965A62CD454&pn=2&first={}&FROM=PERE'.format(j)
        html=requests.get(url, headers=random.choice(UA_headers))
        soup=BeautifulSoup(html.content, 'html.parser')
        soup_bt=soup.findAll('h2')
        for k in soup_bt:
            try:
                item=k.a.get('href')
                if item in urls:
                    duplicate_counter+=1
                    continue
                else:
                    urls.append(item)
                    if item.split('/')[2] not in subdomains:
                        subdomains.append(item.split('/')[2])
                        fp_d.write(item.split('/')[2]+"\n")
                        fp_d.flush()
                    fp_u.write(item+"\n")
                    fp_u.flush()
                    print(item)
                    duplicate_counter = 0
            except Exception as e:
                #print("error :%s", e)
                continue
        # 获取500条记录，共50次查询。
        if i >= 50:
            print("[-] records>500")
            break
        # 默认连续出现100次重复记录则退出。
        if duplicate_counter >= 100:
            print("[-] duplicate_counter>20")
            break
        time.sleep(random.random()*5+1)
    fp_u.close()
    fp_d.close()
    print("[+] Totaly %d records,go check `bing_search.txt` for details." %len(urls))

if __name__ == '__main__':
    with open("keywords.txt", 'r', encoding='utf-8') as rf:
        for line in rf:
            keywords = line.strip('\n').strip('\r')
            bing_search(keywords)
            print("-"*80)