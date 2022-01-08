#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-05-08
# @Author  : aplyc1a
# @FileName: info-sfz.py
import time

def brute_8(s):
    sfz=[]
    birthh=[]
    for i in range(int(time.mktime(time.strptime(s[6:10]+'0101','%Y%m%d'))),int(time.mktime(time.strptime(s[6:10]+'1231','%Y%m%d')))+1,3600*24):
        brute_4(s.replace('****',time.strftime('%Y%m%d',time.localtime(i))[4:],1))

def brute_6(s):
    sfz=[]
    birthh=[]
    for i in range(int(time.mktime(time.strptime(s[6:10]+'0101','%Y%m%d'))),int(time.mktime(time.strptime(s[6:10]+'1231','%Y%m%d')))+1,3600*24):
        if s[10:12] == time.strftime('%Y%m%d',time.localtime(i))[4:6]:
            brute_4(s.replace('**',time.strftime('%Y%m%d',time.localtime(i))[6:8],1))


def brute_4(s):
    for i in num:
        sfz=s.replace('***',i,1)
        summ=0
        for j in range(len(weight)):
            summ+=weight[j]*int(sfz[j])
        check=summ%11
        a=sfz.replace('*',checker[check],-1)
        print(a)

def brute_m4(s):
    birthh=[]
    for i in range(int(time.mktime(time.strptime(s[6:10]+'0101','%Y%m%d'))),int(time.mktime(time.strptime(s[6:10]+'1231','%Y%m%d')))+1,3600*24):
        sfz=s.replace('****',time.strftime('%Y%m%d',time.localtime(i))[4:])
        summ=0
        for i in range(len(weight)):
            summ+=weight[i]*int(sfz[i])
        check=summ%11
        if checker[check]==sfz[-1]:
            print(sfz)

if __name__=='__main__':
    s="5132211949****5126"
    weight=[7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checker=['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    num=[str(i).zfill(3) for i in range(1,1000)]
    
    #s="51322119491001****"
    if s.index('*')==14:
        brute_4(s)

    #s="513221194910******"
    if s.index('*')==12:
        brute_6(s)

    if s.index('*')==10:
        #s="5132211949********"
        if s.count('*')==8:
            brute_8(s)
        #s="5132211949****5126"
        if s.count('*')==4:
            brute_m4(s)

