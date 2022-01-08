#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#批量查询域名备案（工信部）
#thanks for aaron and Jik-W

import requests,sys,time
from bs4 import BeautifulSoup

def get_dingjiicp(dingjiicp):
    #UA反爬虫
    headers={'User-Agent':'Mozilla/5.0'}
    #原始接口http://icp.chinaz.com/baidu.com
    url="http://icp.chinaz.com/"+dingjiicp
    req=requests.get(url,headers=headers,timeout=10)
    soup=BeautifulSoup(req.text,"html.parser")
    #确定爬的范围
    result=soup.find("ul",attrs={"class":"bor-t1s IcpMain01"})
    #内容输出
    if result:
        print(dingjiicp,"|",result.strong.text,"|",result.a.text,"|",result.font.text)
    else:
        print(dingjiicp,"|","未查询到相关备案网站")

#多级域名到二级域名
def get_dingji(dingji):
    result=[]
    for i in dingji:
        field=i.split(".")
        dingji1=field[-2]+"."+field[-1]
        #com.cn例外处理
        if dingji1=="com.cn":
            dingji1=field[-3]+"."+dingji1
        #列表末尾追加新的二级域名    
        result.append(dingji1)
    #原列表去重并从小到大排序
    for i in list(set(result)):
        get_dingjiicp(i)
        #每隔5秒请求一次
        time.sleep(5)

#python后跟文件        
if __name__=="__main__":
    #dingjiicp为待读取文件
    dingjiicp=sys.argv[1]
    with open(dingjiicp,'r') as f:
        fin=f.read().splitlines()
    get_dingji(fin)