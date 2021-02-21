for hostip in {0..210};
do
    ip="170.$hostip.3.4"
        ping -c 1 -W 2 $ip &> /dev/null
    if [ "$?" == "0" ];then
        echo $ip is UP
        #break;
    else
        echo $ip is DOWN
    fi
done
