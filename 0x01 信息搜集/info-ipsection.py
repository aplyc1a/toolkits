#codeing:utf-8
result=[]
def findIPs(ip_section, ch):
    import ipaddress
    start=ipaddress.ip_address(list(ip_section.split(ch))[0])
    end=ipaddress.ip_address(list(ip_section.split(ch))[1])
    result = []
    while start <= end:
        fw.write(str(start)+'\n')
        start += 1

def transfrom_ip(ip_section,ch):
    ip_section=list(ip_section.split('.'))
    for i in ip_section:
        if ch in i:
            break
    MAX=i
    i=0
    ip_hdr=''
    while i<MAX:
        ip_hdr=ip_hdr+ip_section[i]+'.'
    ip_range=list(ip_section[i].split(ch))
    for i in range(int(ip_range[0]),int(ip_range[1])):
        fw.write("%s%d\n" %(ip_hdr,i))
        
def transformIPFrom_netmask(ip_section):
    import ipaddress
    hosts=list(ipaddress.ip_network(ip_section).hosts())
    for ip in hosts:\
        fw.write(str(ip)+'\n')
        
if __name__ == '__main__':
    
    print("[*] 用于将IP段转化为所有IP\n")
    print("    [type-1]: 10.1.1.1-10.1.2.90")
    print("    [type-2]: 10.1.1.1—10.1.2.90")
    print("    [type-3]: 192.168.1.0/24")
    print("    [type-3]: 192.168.1.188")
    print("")
    print("[*] 默认读取 ip.txt")
    print("[*] 默认输出 ip_result.txt\n")
    
    fr = open('./ip.txt')
    fw = open('./ip_result.txt','w')
    print("[+] Working...\n")
    for line in fr:
        line=line.replace('\n','').replace('\r','')
        if '-' in line:
            if line.count('.')<6:
                transfrom_ip(line,'-')
                continue
            findIPs(line,'-')
        if '—' in line:
            if line.count('.')<6:
                transfrom_ip(line,'—')
                continue
            findIPs(line,'—')
        if '/' in line:
            transformIPFrom_netmask(line)
            continue
        if ('—' not in line) and ('-' not in line) :
            fw.write(line+'\n')
    fw.close()
    fr.close()
    print("[+] Done\n")

