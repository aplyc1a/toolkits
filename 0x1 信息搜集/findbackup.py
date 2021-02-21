# -*- coding: utf-8 -*-

import requests
import urllib3
import ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

def get_code_status(targets):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
    }
    with open(targets, 'r', encoding='utf-8') as f1:
        urls_data = f1.readlines()
        for url in urls_data:
            url = url.strip('\r').strip('\n')
            print("[url]:"+url)
            with open("./scanbakup-dic.txt", 'r', encoding='utf-8') as f2:
                uris_data = f2.readlines()
                for uri in uris_data:
                    uri = uri.strip('\n').strip('\r')
                    send_url=url+"/"+uri
                    try:
                        code=0
                        res = requests.get(send_url, headers=header, verify=False, timeout=3)
                        
                        code = res.status_code
                        send_url=res.url
                    except Exception as error:
                        pass
                    print("{%03d:%s} %d" %(code,send_url,len(res.text)))
                    if code == 200:
                        f3 = open('200.txt',"a+",encoding="utf-8")
                        f3.write(send_url+"\n")
                        f3.close()

if __name__ == '__main__':
    get_code_status('./urls.txt')