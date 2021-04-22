# -*- coding: utf-8 -*-
# @aplyc1a。使用前先填入自己的用户名及API-Key
import json
import time
import requests
import pprint

'''
censys网上说一共有以下6种API接口：search、view、report、query、export、data。对普通用户而言，censys有查询限制。
本工具只实现了search接口。search在网页版上提供IP/certificates/website三种检索模式。
分别对应于
https://censys.io/api/v1/search/ipv4
https://censys.io/api/v1/search/certificates
https://censys.io/api/v1/search/website

下面给出一些支持使用的search关键字：
location.country_code: DE
protocols: ("23/telnet" or "21/ftp")
80.http.get.headers.server: Apache
80.http.get.status_code: 200
80.http.get.status_code:[400 TO 500]
80.http.get.headers.server：nginx
tags: scada
autonomous_system.description: University
weblogic and location.country_code: CN
23.0.0.0/8 or 8.8.8.0/24
'''

API_URL = "https://censys.io/api/v1"
UID = ""
SECRET = ""

columns = { 'ip' : 'ip', 
            'protocols' : 'protocols', 
            'country' : 'location.country',
            'city' : 'location.city', 
            'country_code' : 'location.country_code',
            'asn' : 'autonomous_system.asn',
            'name' : 'autonomous_system.name',
            'organization' : 'autonomous_system.organization'
}

def censys_search(query_key):
    page = 1
    num_retries = 5
    while num_retries > 0:
        data = {
                "query": query_key,
                "page": page,
                "fields": [columns['ip'],columns['protocols'],columns['country'],columns['city'], 
                        columns['country_code'],columns['asn'],columns['name'],columns['organization']],
                "flatten":True
        }
        try:
            res = requests.post(API_URL + "/search/ipv4", data=json.dumps(data), auth=(UID, SECRET))
            result = res.json()
            if result['status'] == 'error':
                if "You have used your full quota for this billing period" in str(result):
                    print("[-]You have used your full quota for this billing period. Please see https://censys.io/account/billing or contact support@censys.io.")
                break
                
            #print(result["results"])
            #pprint.pprint(result["results"])
            #print(result["metadata"])
            for i in result["results"]:
            
                #print(i)
                
                print("")
                pprint.pprint(i)
                
                # 打印所有的查询结果项
                #for j in i.keys():
                #    print("\"%s\"\t" %(i[j]), end=" " )
                #    print("")
                
                # 只打印 IP和协议
                #print("%s %s" %(i[columns['ip']],i[columns['protocols']]))
            num_retries = 5
            page = page + 1
        except Exception as e:
            print(e)
            num_retries=num_retries-1

if __name__ == '__main__':
    with open("censys-item.txt", 'r', encoding='utf-8') as rf:
        for line in rf:
            print("[censys-Query] => \"%s\"" %line.strip('\n').strip('\r'))
            censys_search(line.strip('\n').strip('\r'))
            print("-"*80)
            #time.sleep(1)
