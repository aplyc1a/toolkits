# -*- coding: utf-8 -*-

import requests
import urllib3
import ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

def check_alive(hosts):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
    }
    with open(hosts, 'r', encoding='utf-8') as f:
        urls_data = f.readlines()
        for url in urls_data:
            url = url.strip('\n').strip('\r')
            try:
                res = requests.get(url, headers=header, verify=False,timeout=2)
            except Exception as error:
                print("")
                continue
            print(res.url)

if __name__ == '__main__':
    check_alive('./check_urls.txt')