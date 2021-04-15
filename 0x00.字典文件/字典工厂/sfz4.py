#!/usr/bin/python3

f3=open("sfz4.txt",'w')
num_lst=range(0,10)
last_lst = [str(i) for i in num_lst] 
last_lst.append('x')
last_lst.append('X')


count=0
prefix=0
while(prefix<1000):
    #print("%03d" %count)
    for i in last_lst:
        count+=1
        print("%03d%c" %(prefix,i))
        f3.write("%03d%c\n" %(prefix,i))
        if(count%100==0):
            f3.flush()
    prefix+=1
f3.close()
print("Total:%d lines." %count)   
