# -*- coding: utf-8 -*-

import json
import time
import requests
import pprint

APIV1_URL = "https://search.censys.io/api/v1"
APIV2_URL = "https://search.censys.io/api/v2"

# 分别填入账户及API-Key
UID = ""
SECRET = ""
QUERY_NUM = 50 # 定义请求获得的最大条目数

def censys_certificate_search(query_key):
    page = 0
    num_retries = 5
    count = 1
    while num_retries > 0:
        page = page + 1
        data = {
                "query": query_key,
                "page": page,
                "fields": [ "parsed", "ct", "raw"],
                "flatten":True
        }
        headers = {
            "accept": "application/json",
            "User-Agent":"User-Agent,Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"
        }
        try:
            fp = open('censys-apisearch.txt','a+',encoding='utf-8')
            # APIManual https://search.censys.io/api#/certificates/searchCertificates
            res = requests.post(APIV1_URL + "/search/certificates", headers=headers, data=json.dumps(data), auth=(UID, SECRET))
            result = res.json()
            if result['status'] == 'error':
                if "You have used your full quota for this billing period" in str(result):
                    print("[-]You have used your full quota for this billing period. Please see https://censys.io/account/billing or contact support@censys.io.")
                break
                
            for i in result["results"]:
                pprint.pprint(i)
                fp.write(str(i)+"\r\n")
                fp.flush()
                count+=1
                
            num_retries = 5
            if count >= QUERY_NUM:
                break
        except Exception as e:
            print(e)
            num_retries=num_retries-1
        finally:
            fp.close()

def censys_host_search(query_key):
    page = 0
    per_page_num=5
    num_retries = 3
    count = 1
    cursor_next = ""
    
    while num_retries > 0:
        page = page + 1
        try:
            fp = open('censys-apisearch.txt','a+',encoding='utf-8')
            # APIManual https://search.censys.io/api#/hosts/searchHosts
            query_url = "%s/hosts/search?q=%s&per_page=%d&cursor=%s" %(APIV2_URL,query_key,per_page_num,cursor_next)
            #print(query_url)
            headers = {
                "accept": "application/json",
                "User-Agent":"User-Agent,Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"
            }
            res = requests.get(query_url, headers=headers, auth=(UID, SECRET))
            result = res.json()
            if result['code'] != 200:
                print("[-] code:%s", str(result['code']))
                break  #
            if result['status'] == 'error':
                if "You have used your full quota for this billing period" in str(result):
                    print("[-] You have used your full quota for this billing period. Please see https://censys.io/account/billing or contact support@censys.io.")
                break
            cursor = result["result"]["links"]
            cursor_next = cursor["next"]
            for i in result["result"]["hits"]:
                pprint.pprint(i)
                fp.write(str(i)+"\r\n")
                fp.flush()
                count+=1
                
            num_retries = 5
            
            if count >= QUERY_NUM:
                break
        except Exception as e:
            print(e)
            fp.close()
            num_retries=num_retries-1
        finally:
            fp.close()
    if num_retries == 0:
        print("[-] Fetch max retries times.")

if __name__ == '__main__':

    # 查询
    with open("censys.txt", 'r', encoding='utf-8') as rf:
        for line in rf:
            query_item = line.strip('\n').strip('\r')
            print("[Censys-Query] => \"%s\"" %query_item)
            censys_certificate_search(query_item)
            #censys_host_search(query_item)
            print("-"*80)
            #time.sleep(1)
    # 提取
    with open('censys-apisearch.txt', 'r',encoding='utf-8') as f:
        data=str(f.readlines())
        for i in data.split():
            if 'cctv.com' in i:
                print(i)
