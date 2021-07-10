#!/bin/bash
for host in `cat ./host.txt`;
do
    ping -c 1 -W 2 $host &> /dev/null
    if [ "$?" == "0" ];then
        echo $host is UP
        #break;
    else
        echo $host is DOWN
    fi
done 
