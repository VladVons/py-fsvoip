Process=fsvoip

#/etc/init.d/fsvoip restart
#sleep 1
ps aux | grep -v grep | egrep -iw $Process | awk '{ print $1, $2, $11, $12 }' | egrep -i $Process --color=auto
