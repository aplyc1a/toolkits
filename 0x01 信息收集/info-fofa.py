# -*- coding: utf-8 -*-
## pip3 install urllib3

'''
pip3 install urllib3
使用前先填入自己的用户名及API-Key
'''


import base64
import json
import sys
import importlib
from urllib import request, parse
import io
import time

importlib.reload(sys)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# 分别填入账户及API-Key
uname = 
ukey  = 


def do_search(query_key):
    query_url = "https://fofa.so/api/v1/search/all?email=%s&key=%s&qbase64=%s&size=100&fields=host,title,ip,domain,port,country,city" %(uname,ukey,base64.b64encode(query_key.encode('utf8')).decode())
    req = request.Request(query_url)
    MAX_RETRIES=5
    i=0
    while i<MAX_RETRIES:
        try:
            req_obj = request.urlopen(req)
            break
        except:
            printf("Retrying...")
            i+=1
    
    req_str = req_obj.read()
    req_obj.close()
    req_dic = json.loads(req_str)
    fp = open('fofa.csv','a+',encoding='utf-8')
    Q_key = req_dic.get("query")
    Q_page = req_dic.get("page")
    Q_size = req_dic.get("size")
    
    print('[+] query_keyword:"%s" ; query_page:%d ; fetch_result num:%d' %(Q_key,Q_page,Q_size))
    fp.write('"fofa_query_key","host","ip","port","domain","subdomain","country","city","title"\n')
    res_list = req_dic.get("results")
    for res in res_list:
        subdomain = res[0].strip('http://').strip('https://').split(':')[0]
        fp.write('"%s","%s","%s","%s","%s","%s","%s","%s","%s"\n' \
            %(query_key.replace("\"","\"\""),
            res[0],
            res[2],
            res[4],
            res[3],
            subdomain,
            res[5],
            res[6],
            res[1].encode('utf-8')\
            ))
        print("%s:%s" %(res[2],res[4]))
    fp.close()
    

if __name__ == "__main__":
    print(sys.getdefaultencoding())
    with open("fofa.txt", 'r', encoding='utf-8') as rf:
        for line in rf:
            print("[Fofa-Query] => '%s'" %line.strip('\n').strip('\r'))
            do_search(line.strip('\n').strip('\r'))
            print("-"*80)
            time.sleep(1)
