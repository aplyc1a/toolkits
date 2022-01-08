from pwn import *
prefix = ""
ip = "172.19.2.246"
port = 32013
f = open(sys.argv[1])
w = open(sys.argv[2],"a+")
count = 0
for line in f:
    payload = prefix + line.replace('\n','')
    p = remote(ip,port)
    p.send(payload)
    try:
        a = "Recv:%s    <---- %s"  % (p.recv(timeout =0.01),payload)
        print a
        w.write(a+"\n")
    except EOFError:
        p.close()
        a = "Recv: EOFError    <----%s" % (payload)
        w.write(a+"\n")
        continue
    p.close()
    count +=1
    if count % 10 ==0 :
        w.flush
        print "Count:%d" %count
w.close()