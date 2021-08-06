# coding=utf-8
import subprocess
import csv
import os
import re
import platform

def digger(domain, csv_obj):
    # China
    DNSS=["114.114.114.114","8.8.8.8","223.5.5.5"]
    # Foreign
    #DNSS=["8.8.8.8","8.8.4.4","199.85.126.10","208.67.222.222","84.200.69.80","8.26.56.26","192.95.54.3","1.1.1.1"]
    result=[]
    for DNS in DNSS:
        dig_domain(domain, DNS, csv_obj)
    print("")
    print("")
    
def dig_domain(domain, dns, csv_obj):
    if "Windows" in platform.system():
        payload="dig @%s %s any| findstr /v ;|findstr IN" %(dns, domain)
    else :
        payload="dig @%s %s any|grep -v \";\"|grep IN" %(dns, domain)
    fp = os.popen(payload)
    response=fp.read()
    print("======================================")
    record=[]
    result=response.split('\n')
    result.remove('')
    record_type="Err"
    #print(result)
    for i in result:
        responce_item=i.split('\t')
        record_domain=responce_item[0][:-1]
        if record_domain==domain:
                if "IN" in responce_item[2]:
                    record_substr=responce_item[3:]
                else:
                    record_substr=responce_item[4:]
                record_type=record_substr[0]
                #print("=>%s" %str(record_substr))
                if record_type=="CNAME":
                    record=[domain, dns, "CNAME", record_substr[1][:-1]]
                elif record_type=="MX":
                    record=[domain, dns, "MX", record_substr[1].split()[1][:-1]]
                elif record_type=="SOA":
                    SOA_record=record_substr[1].split(' ')
                    record=[domain, dns, "SOA", "%s,%s" %(SOA_record[0][:-1],SOA_record[1][:-1])]
                elif record_type=="TXT":
                    pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
                    trueIp = pattern.findall(record_substr[1])
                    if trueIp:
                        record=[domain, dns, "TXT", "%s" %','.join(trueIp)]
                    else:
                        continue
                else:
                        if record_substr[1][-1] == '.': 
                            record=[domain, dns, record_type, record_substr[1][:-1]]
                        else:
                            record=[domain, dns, record_type, record_substr[1]]
                print(record)
                csv_obj.writerow(record)
    
if __name__ == "__main__":
    file_domain = r'domain.txt'      # 输入文件
    file_nslookup = r'DNS-Result.csv'  # 输出文件
    domain_list=[]
    with open(file_domain, 'r', encoding='utf-8') as rf:
        #domain_list.append(rf.readlines().replace('\n',''))
        for line in rf.readlines():
            line=line.strip('\n')
            domain_list.append(line)
    with open(file_nslookup, 'w+', newline='', encoding='utf-8') as wf:
        csv_obj = csv.writer(wf, dialect=csv.excel)
        header = ['Domain','DNSServer','RecordType', 'Adderss']
        csv_obj.writerow(header)
        for domain in domain_list:
            digger(domain, csv_obj)
    print('执行完毕')
