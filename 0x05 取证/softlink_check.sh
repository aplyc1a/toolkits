#!/bin/bash
#softlink_check.sh
find / -type l 2>/dev/null |sed 's/\\/\\\\/g'|grep -v "/proc\|/run"| while read f;
do
    flnk_name=${f};
    #flnk_name=/etc/alternatives/jsonschema;
    #flnk_name=/etc/xdg/menus/gnome-applications-merged;
    #flnk_name=/etc/dpkg/origins/default;
    #flnk_name=/sys/devices/pci0000:00/0000:00:18.5/pci_bus/0000:20/device;
    flnk_name=${flnk_name// /\ };
    dlnk_name="${flnk_name%/*}";
    dlnk_name="${dlnk_name:-/}";
    if [[ "${dlnk_name}" != "*/" ]] && [ -d "${dlnk_name}" ]; then 
        dlnk_name="${dlnk_name}/";
        #echo "actual_path=$dlnk_name";
    fi
    #ls -adl ${flnk_name} 2>/dev/null
    _flnk_name=`ls -adl ${flnk_name} 2>/dev/null | awk -F' ' '{print $NF}'`;
    _flnk_name=${_flnk_name// /\ }; #文件名中含有空格
    _dlnk_name="${_flnk_name%/*}";  #通过/字符截取目录名
    _dlnk_name="${_dlnk_name:-/}";  #如果目录名为空，强制赋 /
    _perfix="${_flnk_name:0:2}";
    if [ "${_perfix}" == ".." ] || [ "${_perfix}" == "./" ]; then
    #如果目录名不为绝对路径，直接将2种路径拼起来
        _dlnk_name="${dlnk_name}${_dlnk_name}";
        _flnk_name="${dlnk_name}${_flnk_name}";
    elif [ ! -d ${_dlnk_name} ]; then
    #如果目录名为文件名自身，那就用源文件的路径。
        _dlnk_name="${dlnk_name}";
        _flnk_name="${dlnk_name}${_flnk_name}";
    #else
    #如果为绝对路径，那就直接用
    fi
    
    fname_owner=`ls -dal "${flnk_name}" 2>/dev/null |awk '{print $3}'`;
    fdir_owner=`ls -dal "${dlnk_name}" 2>/dev/null |awk '{print $3}'`;
    _fname_owner=`ls -dal "${_flnk_name}" 2>/dev/null |awk '{print $3}'`;
    _fdir_owner=`ls -dal "${_dlnk_name}" 2>/dev/null |awk '{print $3}'`;
    if [ "${fname_owner}" != "${_fname_owner}" ]; then
        echo -ne "owner[f]:\"${fname_owner}\" [d]=\"${fdir_owner}\" ... [soft-link]:\"${flnk_name}\"\n";
        echo -ne "owner[f]:\"${_fname_owner}\" [d]=\"${_fdir_owner}\" ... [dest-file]:\"${_flnk_name}\"\n";
        echo "---------------------------------------------------------------------------"    
    fi
done
