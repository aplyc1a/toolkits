# sudo               
一个用来在后渗透持久化阶段利用passwd命令偷取密码的后门脚本。               
## 原理               
很多时候通过漏洞利用，我们可以得到目标设备上的操作权限，但是管理员一旦修补了漏洞，那么就前功尽弃了。本工具用来让用户使用passwd命令时将密码自动发送到攻击者的设备上。            
这个脚本利用环境变量$PATH的优先级关系，实现优先于原来的/usr/bin/passwd加载，理论上，你也可以将脚本布到/usr/bin目录下，并将 原来的passwd程序 及 脚本内的有效passwd地址 改为更低优先级的目录。        
## 使用方法               
参见脚本内的注释说明，如果你的目标设备为英文字库环境，可以自行将文中的汉字改为对应英文。         
             