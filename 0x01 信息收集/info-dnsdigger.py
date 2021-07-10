# coding=utf-8
import subprocess
import csv
import os
import re

def digger(domain, csv_obj):
    DNSS=["114.114.114.114","8.8.8.8","223.5.5.5"]
    result=[]
    for DNS in DNSS:
        dig_domain(domain, DNS, csv_obj)
    print("")
    print("")
    
def dig_domain(domain, dns, csv_obj):
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
        reponce_item=i.split('\t')
        record_domain=reponce_item[0][:-1]
        if record_domain==domain:
                record_type=reponce_item[4]
                if record_type=="CNAME":
                    record=[domain, dns, "CNAME", reponce_item[4][:-1]]
                elif record_type=="MX":
                    record=[domain, dns, "MX", reponce_item[5].split()[1][:-1]]
                elif record_type=="SOA":
                    SOA_record=reponce_item[5].split(' ')
                    record=[domain, dns, "SOA", "%s,%s" %(SOA_record[0][:-1],SOA_record[1][:-1])]
                elif record_type=="TXT":
                    #print("TXT:%s" %reponce_item[5])
                    pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
                    trueIp = pattern.findall(reponce_item[5])
                    if trueIp:
                        record=[domain, dns, "TXT", "%s" %','.join(trueIp)]
                    else:
                        continue
                else:
                    record=[domain, dns, record_type, reponce_item[5][:-1]]
                print(record)
                csv_obj.writerow(record)
    
if __name__ == "__main__":
    file_domain = r'domain.txt'      # 输入文件
    file_nslookup = r'nslookup.csv'  # 输出文件
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