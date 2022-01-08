# -*- coding: utf-8 -*-

def analysis_file(filename):
    fp = open(filename,"r")
    domain1=[]
    domain2=[]
    domain3=[]
    
    with open(filename, 'r', encoding='utf-8') as fp:
        for item in fp:
            domain=item.replace("\n","").replace("\r","").split(".")
            print(domain)
            if len(domain) == 3:
                # 360.cn
                domain1.append("%s.%s" %(domain[-2],domain[-1]))
                # ti.360.cn
                domain2.append("%s.%s.%s" %(domain[-3],domain[-2],domain[-1]))
            if len(domain) == 4:
                # 360.cn
                domain1.append("%s.%s" %(domain[-2],domain[-1]))
                # ti.360.cn
                domain2.append("%s.%s.%s" %(domain[-3],domain[-2],domain[-1]))
                # x.ti.360.cn
                domain3.append("%s.%s.%s.%s" %(domain[-4],domain[-3],domain[-2],domain[-1]))
    #print(domain1)
    #print(domain2)
    #print(domain3)
    with open('domain1.txt', 'w') as f:
        for i in list(set(domain1)):
            f.write(i+"\n")
    with open('domain2.txt', 'w') as f:
        for i in list(set(domain2)):
            f.write(i+"\n")
    with open('domain3.txt', 'w') as f:
        for i in list(set(domain3)):
            f.write(i+"\n")
if __name__ == "__main__":
    analysis_file("domain.txt")
