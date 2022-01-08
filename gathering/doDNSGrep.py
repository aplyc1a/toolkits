#pip3 install bs4
import requests
from bs4 import BeautifulSoup
import time
import sys

def get_subdomain(domain):
    fp = open("dnsgrep.txt","a+")
    heads={
        'User-Agent': 'Mozilla/5.0(Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    }
    url='https://www.dnsgrep.cn/subdomain/'+domain
    html=requests.get(url,headers=heads)
    soup=BeautifulSoup(html.content,'html.parser')
    job_tr=soup.findAll('tr')
    for i in job_tr:
        if not i:
            continue
        job_td=i.findAll('td')
        if job_td:
            subdomain = job_td[0].get('data')
            record = job_td[1].get('data')
            record_type = job_td[2].get('data')
            line = "%s %s %s\n" %(subdomain,record,record_type)
            print(line)
            fp.write(line)
            fp.flush()
    fp.close()
    '''
        <tr>
            <td data="zhongan.com">
                <a href='/subdomain/zhongan.com'>zhongan.com</a>
            </td>
            <td data="47.98.84.224">
                <a href="/ip/47.98.84.224">47.98.84.224 (浙江省杭州市/阿里云)</a>
            </td>
            <td data="A">A</td>
            <td data="2021-06-27" class="date">2021-06-27</td>
        </tr>
    '''
if __name__ == "__main__":
    print(sys.getdefaultencoding())
    with open("domain.txt", 'r', encoding='utf-8') as rf:
        for line in rf:
            print("[+] dnsgrep.cn > domain = \"%s\"" %line.strip('\n').strip('\r'))
            get_subdomain(line.strip('\n').strip('\r'))
            print("-"*80)
            time.sleep(1)