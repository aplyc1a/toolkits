# -*- coding: utf-8 -*-

import requests
import urllib3
import ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

def get_code_status(targets):
    """
    检测urls状态码
    :param targets: 目标文件
    :return: 状态码
    allow_redirects: 拒绝默认的301/302重定向从而可以通过 html.headers[‘Location’] 拿到重定向的 URL。
    verify: 取消证书认证
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
    }
    f2 = open('urls.txt', 'w+')
    with open(targets, 'r', encoding='utf-8') as f:
        urls_data = f.readlines()
        for url in urls_data:
            url = url.strip('\n').strip('\r')
            url="http://"+url
            try:
                res = requests.get(url, headers=header, verify=False, allow_redirects=False)
            except Exception as error:
                print("")
                continue
            code = res.status_code
            if code == 200:
                print(url)
            if code == 301 or code == 302:
                if "http" in res.headers['location']:
                    print(res.headers['location'])
                    url=res.headers['location']
                else:
                    print(url+'/'+res.headers['location'])
                    url=url+'/'+res.headers['location']
            f2.write(url+'\n')
    f2.close()
    return code

if __name__ == '__main__':
    get_code_status('./targets.txt')