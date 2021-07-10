#!/bin/bash
#owner_check.sh
find / -type f 2>/dev/null |sed 's/\\/\\\\/g'| while read f;
do
    fname=${f};
    fname=${fname// /\ };
    fdir="${fname%/*}";
    fdir="${fdir:-\"/\"}"; 
    fname_owner=`getfacl "${fname}" -d 2>/dev/null |grep " owner:"|awk '{print $3}'` ;
    fdir_owner=`getfacl "${fdir}" -d 2>/dev/null |grep " owner:"|awk '{print $3}'`;
    if [ "${fname_owner}" != "${fdir_owner}" ]; then 
        echo -ne "owner[f]:\"${fname_owner}\" [d]=\"${fdir_owner}\" ... \"${fname}\"\n";
    fi
done
