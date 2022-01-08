# -*- coding: utf-8 -*-
import json
import optparse
import pprint
COUNTER=1
SIMPLE=2
NORMAL=3
DEBUG=4
VERBOSE=5

def analysis(data,level=SIMPLE):
    Event={
        "Channel":"",
        "Computer":"",
        "EventID":"",
        "EventRecordID":"",
        "ProcessID":"",
        "TimeCreated":"",
        "System":"",
        "AuthenticationPackageName":"",
        "CertIssuerName":"",
        "CertSerialNumber":"",
        "CertThumbprint":"",
        "FailureReason":"",
        "IpAddress":"",
        "IpPort":"",
        "LogonGuid":"",
        "LogonProcessName":"",
        "LogonType":"",
        "PreAuthType":"",
        "ProcessName":"",
        "ServiceName":"",
        "ServiceSid":"",
        "Status":"",
        "SubjectDomainName":"",
        "SubjectLogonId":"",
        "SubjectUserName":"",
        "SubjectUserSid":"",
        "TargetDomainName":"",
        "TargetInfo":"",
        "TargetLogonGuid":"",
        "TargetServerName":"",
        "TargetSid":"",
        "TargetUserName":"",
        "TicketEncryptionType":"",
        "TicketOptions":"",
        "TransmittedServices":"",
        "WorkstationName":"",
        "EventData":""
    }
    SimpleEvent=""
    if data['Event']['System']['EventID']==4624:
        Event['TimeCreated']=data['Event']['System']['TimeCreated']['#attributes']['SystemTime']
        Event['Computer']=data['Event']['System']['Computer']
        Event['Channel']=data['Event']['System']['Channel']
        Event['EventRecordID']=data['Event']['System']['EventRecordID']
        Event['EventID']=data['Event']['System']['EventID']
        Event['ProcessID']=data['Event']['System']['Execution']['#attributes']['ProcessID']
        Event['System']=data['Event']['System']
        
        Event['ProcessName']=data['Event']['EventData']['ProcessName']
        Event['LogonProcessName']=data['Event']['EventData']['LogonProcessName']
        Event['AuthenticationPackageName']=data['Event']['EventData']['AuthenticationPackageName']
        Event['IpAddress']=data['Event']['EventData']['IpAddress']
        Event['IpPort']=data['Event']['EventData']['IpPort']
        Event['LogonGuid']=data['Event']['EventData']['LogonGuid']
        Event['LogonType']=data['Event']['EventData']['LogonType']
        Event['SubjectDomainName']=data['Event']['EventData']['SubjectDomainName']
        Event['SubjectUserName']=data['Event']['EventData']['SubjectUserName']
        Event['SubjectUserSid']=data['Event']['EventData']['SubjectUserSid']
        Event['TargetDomainName']=data['Event']['EventData']['TargetDomainName']
        Event['TargetUserName']=data['Event']['EventData']['TargetUserName']
        Event['TargetUserSid']=data['Event']['EventData']['TargetUserSid']
        Event['EventData']=data['Event']['EventData']
        
        SimpleEvent = "\t[登录成功] %s:%s   %s(%s:%s:%s)  %s/%s==>%s/%s" %(
                    Event['IpAddress'],
                    Event['IpPort'],
                    Event['LogonType'],
                    Event['LogonProcessName'],
                    Event['AuthenticationPackageName'],
                    Event['ProcessName'],
                    Event['SubjectDomainName'],
                    Event['SubjectUserName'],
                    Event['TargetDomainName'],
                    Event['TargetUserName']
                    )
    elif data['Event']['System']['EventID']==4625:
        Event['TimeCreated']=data['Event']['System']['TimeCreated']['#attributes']['SystemTime']
        Event['Computer']=data['Event']['System']['Computer']
        Event['Channel']=data['Event']['System']['Channel']
        Event['EventRecordID']=data['Event']['System']['EventRecordID']
        Event['EventID']=data['Event']['System']['EventID']
        Event['ProcessID']=data['Event']['System']['Execution']['#attributes']['ProcessID']
        Event['System']=data['Event']['System']
        
        Event['ProcessName']=data['Event']['EventData']['ProcessName']
        Event['LogonProcessName']=data['Event']['EventData']['LogonProcessName']
        Event['AuthenticationPackageName']=data['Event']['EventData']['AuthenticationPackageName']
        Event['IpAddress']=data['Event']['EventData']['IpAddress']
        Event['IpPort']=data['Event']['EventData']['IpPort']
        Event['LogonType']=data['Event']['EventData']['LogonType']
        Event['FailureReason']=data['Event']['EventData']['FailureReason']
        Event['SubjectDomainName']=data['Event']['EventData']['SubjectDomainName']
        Event['SubjectUserName']=data['Event']['EventData']['SubjectUserName']
        Event['SubjectUserSid']=data['Event']['EventData']['SubjectUserSid']
        Event['TargetDomainName']=data['Event']['EventData']['TargetDomainName']
        Event['TargetUserName']=data['Event']['EventData']['TargetUserName']
        Event['WorkstationName']=data['Event']['EventData']['WorkstationName']
        Event['EventData']=data['Event']['EventData']
        
        SimpleEvent = "\t[登录失败] %s:%s   %s:%s(%s:%s:%s)  %s:%s/%s==>%s/%s" %(
                    Event['IpAddress'],
                    Event['IpPort'],
                    Event['LogonType'],
                    Event['AuthenticationPackageName'],
                    Event['LogonProcessName'],
                    Event['ProcessName'],
                    Event['FailureReason'],
                    Event['WorkstationName'],
                    Event['SubjectDomainName'],
                    Event['SubjectUserName'],
                    Event['TargetDomainName'],
                    Event['TargetUserName']
                    )
    elif data['Event']['System']['EventID']==4648:
        Event['TimeCreated']=data['Event']['System']['TimeCreated']['#attributes']['SystemTime']
        Event['Computer']=data['Event']['System']['Computer']
        Event['Channel']=data['Event']['System']['Channel']
        Event['EventRecordID']=data['Event']['System']['EventRecordID']
        Event['EventID']=data['Event']['System']['EventID']
        Event['ProcessID']=data['Event']['System']['Execution']['#attributes']['ProcessID']
        Event['System']=data['Event']['System']
        
        Event['ProcessName']=data['Event']['EventData']['ProcessName']
        Event['IpAddress']=data['Event']['EventData']['IpAddress']
        Event['IpPort']=data['Event']['EventData']['IpPort']
        Event['LogonGuid']=data['Event']['EventData']['LogonGuid']
        Event['SubjectDomainName']=data['Event']['EventData']['SubjectDomainName']
        Event['SubjectUserName']=data['Event']['EventData']['SubjectUserName']
        Event['SubjectLogonId']=data['Event']['EventData']['SubjectLogonId']
        Event['SubjectUserSid']=data['Event']['EventData']['SubjectUserSid']
        Event['TargetDomainName']=data['Event']['EventData']['TargetDomainName']
        Event['TargetUserName']=data['Event']['EventData']['TargetUserName']
        Event['TargetServerName']=data['Event']['EventData']['TargetServerName']
        Event['TargetLogonGuid']=data['Event']['EventData']['TargetLogonGuid']
        Event['TargetInfo']=data['Event']['EventData']['TargetInfo']
        Event['EventData']=data['Event']['EventData']
        
        SimpleEvent = "\t[登录尝试] %s:%s   (%s)  %s/%s==>%s/%s(%s)" %(
                    Event['IpAddress'],
                    Event['IpPort'],
                    Event['ProcessName'],
                    Event['SubjectDomainName'],
                    Event['SubjectUserName'],
                    Event['TargetDomainName'],
                    Event['TargetUserName'],
                    Event['TargetServerName']
                    )
    elif data['Event']['System']['EventID']==4768:
        Event['TimeCreated']=data['Event']['System']['TimeCreated']['#attributes']['SystemTime']
        Event['Computer']=data['Event']['System']['Computer']
        Event['Channel']=data['Event']['System']['Channel']
        Event['EventRecordID']=data['Event']['System']['EventRecordID']
        Event['EventID']=data['Event']['System']['EventID']
        Event['ProcessID']=data['Event']['System']['Execution']['#attributes']['ProcessID']
        Event['System']=data['Event']['System']
        
        Event['IpAddress']=data['Event']['EventData']['IpAddress']
        Event['IpPort']=data['Event']['EventData']['IpPort']
        Event['TargetDomainName']=data['Event']['EventData']['TargetDomainName']
        Event['TargetUserName']=data['Event']['EventData']['TargetUserName']
        Event['TicketEncryptionType']=data['Event']['EventData']['TicketEncryptionType']
        Event['TicketOptions']=data['Event']['EventData']['TicketOptions']
        Event['TargetSid']=data['Event']['EventData']['TargetSid']
        Event['PreAuthType']=data['Event']['EventData']['PreAuthType']
        Event['ServiceName']=data['Event']['EventData']['ServiceName']
        Event['ServiceSid']=data['Event']['EventData']['ServiceSid']
        Event['Status']=data['Event']['EventData']['Status']
        Event['CertIssuerName']=data['Event']['EventData']['CertIssuerName']
        Event['CertSerialNumber']=data['Event']['EventData']['CertSerialNumber']
        Event['CertThumbprint']=data['Event']['EventData']['CertThumbprint']
        Event['EventData']=data['Event']['EventData']
        
        SimpleEvent = "\t[Kbs认证] %s:%s  %s(%s:%s)   ==>%s/%s(%s)" %(
                    Event['IpAddress'],
                    Event['IpPort'],
                    Event['ServiceName'],
                    Event['PreAuthType'],
                    Event['TicketEncryptionType'],
                    Event['TargetDomainName'],
                    Event['TargetUserName'],
                    Event['TargetServerName']
                    ) 
    elif data['Event']['System']['EventID']==4769:
        Event['TimeCreated']=data['Event']['System']['TimeCreated']['#attributes']['SystemTime']
        Event['Computer']=data['Event']['System']['Computer']
        Event['Channel']=data['Event']['System']['Channel']
        Event['EventRecordID']=data['Event']['System']['EventRecordID']
        Event['EventID']=data['Event']['System']['EventID']
        Event['ProcessID']=data['Event']['System']['Execution']['#attributes']['ProcessID']
        Event['System']=data['Event']['System']
        
        Event['IpAddress']=data['Event']['EventData']['IpAddress']
        Event['IpPort']=data['Event']['EventData']['IpPort']
        Event['LogonGuid']=data['Event']['EventData']['LogonGuid']
        Event['TargetDomainName']=data['Event']['EventData']['TargetDomainName']
        Event['TargetUserName']=data['Event']['EventData']['TargetUserName']
        Event['ServiceName']=data['Event']['EventData']['ServiceName']
        Event['ServiceSid']=data['Event']['EventData']['ServiceSid']
        Event['Status']=data['Event']['EventData']['Status']
        Event['TicketEncryptionType']=data['Event']['EventData']['TicketEncryptionType']
        Event['TicketOptions']=data['Event']['EventData']['TicketOptions']
        Event['TransmittedServices']=data['Event']['EventData']['TransmittedServices']
        Event['EventData']=data['Event']['EventData']
        
        SimpleEvent = "\t[Kbs票据] %s:%s  %s %s %s" %(
                    Event['IpAddress'],
                    Event['IpPort'],
                    Event['TicketEncryptionType'],
                    Event['TargetUserName'],
                    Event['TargetDomainName']
                    )
    else:
        Event['TimeCreated']=data['Event']['System']['TimeCreated']['#attributes']['SystemTime']
        Event['Computer']=data['Event']['System']['Computer']
        Event['Channel']=data['Event']['System']['Channel']
        Event['EventRecordID']=data['Event']['System']['EventRecordID']
        Event['EventID']=data['Event']['System']['EventID']
        Event['ProcessID']=data['Event']['System']['Execution']['#attributes']['ProcessID']
        Event['System']=data['Event']['System']
        
        SimpleEvent = "\t[其他事件] "
        
    if level==VERBOSE:
        print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(
        Event['TimeCreated'],
        Event['Computer'],
        Event['Channel'],
        Event['EventRecordID'],
        Event['EventID'],
        Event['ProcessID'],
        "",
        "",
        Event['IpAddress'],
        Event['IpPort'],
        Event['ProcessName'],
        Event['LogonProcessName'],
        Event['LogonType'],
        Event['LogonGuid'],
        Event['AuthenticationPackageName'],
        Event['FailureReason'],
        Event['PreAuthType'],
        Event['SubjectDomainName'],
        Event['SubjectLogonId'],
        Event['SubjectUserName'],
        Event['SubjectUserSid'],
        Event['TargetDomainName'],
        Event['TargetInfo'],
        Event['TargetLogonGuid'],
        Event['TargetServerName'],
        Event['TargetSid'],
        Event['TargetUserName'],
        Event['WorkstationName'],
        Event['ServiceName'],
        Event['ServiceSid'],
        Event['Status'],
        Event['CertIssuerName'],
        Event['CertSerialNumber'],
        Event['CertThumbprint'],
        Event['TicketEncryptionType'],
        Event['TicketOptions'],
        Event['TransmittedServices'],
        Event['System'],
        Event['EventData']
        ))
        return
    if level==COUNTER:
        print("%s,%s,%s,%s,%s,%s" %(
        Event['TimeCreated'],
        Event['Computer'],
        Event['Channel'],
        Event['EventRecordID'],
        Event['EventID'],
        Event['ProcessID']
        ))
    if level==SIMPLE:
        if "::1" in SimpleEvent: return
        if "127.0.0.1"  in SimpleEvent: return
        if "其他" in SimpleEvent: return
        if "fe80::" in SimpleEvent: return
        
        print(u"%s,%s,%s" %(
        Event['TimeCreated'],
        Event['EventID'],
        SimpleEvent
        ))

if __name__ == "__main__":
    parser = optparse.OptionParser('')
    parser.add_option('-i', '--input', dest = 'import_file', type = 'string', default="NULL",help = '输入事件文件名')
    parser.add_option('-l', '--level', dest = 'level', type = 'string', default="SIMPLE",help = '输入事件文件名')
    (options,args) = parser.parse_args()

    if options.import_file == "NULL":
        print("--------------------------------------------------------------")
        print("wget https://github.com/omerbenamram/evtx/releases/download/v0.7.2/evtx_dump-v0.7.2.exe")
        print(".\evtx_dump-v0.7.2.exe security.evtx -o jsonl -f domain.json")
        print("--------------------------------------------------------------")
        print("usage: python evtx.py -i domain.json -l COUNTER/SIMPLE/VERBOSE")
        exit(1)

    mode = NORMAL
    with open(options.import_file, 'r') as f:
        count=0
        while 1:
            line = f.readline().replace('\r','').replace('\n','')
            if not line:
                break
            data = json.loads(line)
            count+=1
            try:
                analysis(data,level)
            except Exception as e:
                print("=======================")
                print(e)
                break