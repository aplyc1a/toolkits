f3=open("3.lst",'w')
count=0
for line1 in open("1.lst",'r'):
    line1=line1.strip()
    for line2 in open("2.lst",'r'):
        line2=line2.strip()
        print("%s%s" %(line1,line2))
        f3.write(line1+line2+"\n")
        count+=1
        if (count%100 ==0):
            f3.flush()
f3.close()
print("Total:%d lines." %count)   
    






