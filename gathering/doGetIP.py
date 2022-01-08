#codeing:utf-8

result=[]
splitcode='-—_'
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
    
    i=0
    ip_hdr=''
    while i<3:
        ip_hdr=ip_hdr+ip_section[i]+'.'
        i+=1
    ip_range=list(ip_section[i].split(ch))
    for i in range(int(ip_range[0]),int(ip_range[1])):
        fw.write("%s%d\n" %(ip_hdr,i))
    fw.write("%s%d\n" %(ip_hdr,int(ip_range[1])))

def trans_ip_netmask(ip_section):
    import ipaddress
    try:
        hosts=list(ipaddress.ip_network(ip_section).hosts())
        for ip in hosts:\
            fw.write(str(ip)+'\n')
    except:
        print("[Error] %s Wrong format!!!" %ip_section)

if __name__ == '__main__':
    fr = open('./ip.txt','r')
    fw = open('./ipp.txt','w')
    for line in fr:
        line=line.replace('\n','').replace('\r','').replace('—','-')
        line=line.replace("--",'-').replace("--",'-').replace("--",'-')
        # 10.1.1.1—10.1.2.90
        if '—' in line:
            if line.count('.') == 3:
                transfrom_ip(line,'—')
                continue
            findIPs(line,'-')
        # 10.1.1.1-10.1.2.90
        if '-' in line:
            if line.count('.') == 3:
                transfrom_ip(line,'-')
                continue
            findIPs(line,'-')
        # 192.168.1.0/24
        if '/' in line:
            trans_ip_netmask(line)
            continue
        # 192.168.1.188
        if ('—' not in line) and ('-' not in line) :
            fw.write(line+'\n')
    fw.close()
    fr.close()
    print("[+] Done <ipp.txt>\n")

