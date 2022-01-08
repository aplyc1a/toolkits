#!/bin/bash

LOG_FILE="audit_sum.log"
#a=(`echo $PATH| tr : " "`)
a[${#a[*]}]="/usr"
a[${#a[*]}]="/sbin"
a[${#a[*]}]="/bin"
a[${#a[*]}]="~/"
a[${#a[*]}]="/var"
a[${#a[*]}]="/etc"

check_sum(){
    path_type=`ls -adl ${1}|cut -c 1`
    if [ ${path_type} != 'd' ];then
        echo "[Err]"`ls -adl ${1}`
        return
    fi

    find "${1}" -type l -o -type f |grep -v "/usr/share" | while read f;
    do
        if [ `ls -adl "${f}"|cut -c 1` != "-" ];then
            continue
        fi
        sum_value=`md5sum "${f}"`
        echo ${sum_value}
        echo ${sum_value} >> ${LOG_FILE}
    done
}


i=0
while [ $i -lt ${#a[*]} ]
do
    echo -e "[+]Entering: \033[40;32m${a[${i}]}\033[0m"
    check_sum ${a[${i}]}
    let i=i+1
    echo -ne "[-]Done\n\n"
done
