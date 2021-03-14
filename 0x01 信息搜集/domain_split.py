

for line in file:
    domain_tree=line.split(".")
    if len(domain_tree) == 3:
        print(line.replace("\r","").replace("\n",""))
file.close()


def analysis_file(filename):
    fp = open(filename,"r")
    domain_2=[]
    domain_3=[]
    domain_4=[]
    
    for domain_item in fp:
        domain=domain_item.split(".")
        if len(domain) == 3:
            print(domain_item.replace("\r","").replace("\n",""))
            domain_2.append("%s.%s" %(domain[-2],domain[-1]))
            domain_3.append(domain_item.replace("\r","").replace("\n",""))
        if len(domain) == 4:
            print(domain_item.replace("\r","").replace("\n",""))
            domain_2.append("%s.%s" %(domain[-2],domain[-1]))
            domain_2.append("%s.%s.%s" %(domain[-3],domain[-2],domain[-1]))
            domain_4.append(domain_item.replace("\r","").replace("\n",""))
        
    fp.close()
    with open('domain2.txt', 'w') as f:
        f.write(list(set(domain_2)))
    with open('domain3.txt', 'w') as f:
        f.write(list(set(domain_3)))
    with open('domain4.txt', 'w') as f:
        f.write(list(set(domain_4)))
    print(domain_2)
    print(domain_3)
    print(domain_4)

if __name__ == "__main__":
    analysis_file(filename)
