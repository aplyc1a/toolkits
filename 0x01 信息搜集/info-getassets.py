#codeing:utf-8

import urllib
import re
import sys
import os
import socket
import threading
import Queue
import csv

def readUrl(file):
    urllist = list()
    if os.path.exists(file):
        with open(file,'r') as f:
            for line in f:
                urllist.append(line.strip('\n'))
    return urllist

def getIPfromUrl(urllist):
    for url in urllist:
        protocol, s1 = urllib.splittype(url)
        host, s2 = urllib.splithost(s1)
        host, port = urllib.splitport(host)
        if port == None:
            port = 80
        addr = socket.getaddrinfo(host, protocol)
        ip=[]
        for i in range(len(addr)):
            if ":" not in addr[i][4][0]:
                ip.append(addr[i][4][0])
        ip=set(ip)
        if len(ip)>1:
            cdn="cdn-yes"
        else:
            cdn="cdn-no"
        ip='\n'.join(ip)
        print(">%s %s %s %s" %(url,host,ip,cdn))
        data = [url, host, ip, cdn]
        with open('assets.csv', 'ab') as f:
            write = csv.writer(f)
            write.writerow(data)

def geturls():
    datafile = 'odata.txt' # get urls from original data
    urlsfile = 'urls.txt'

    if os.path.exists(urlsfile):
        fp = open(urlsfile,"r")
        urls=[]
        for url in fp:
            urls.append(url.strip('\n'))
        fp.close()
        print(urls)
    elif os.path.exists(datafile):
        fp = open(datafile,"r")
        assets_data=fp.read()
        urls = re.findall(r'(http[s]{0,1}://[^\s]*)', assets_data, re.IGNORECASE)
        fp.close()

    return urls

if __name__ == '__main__':
    urls=geturls()
    getIPfromUrl(urls)