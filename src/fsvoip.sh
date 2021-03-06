#!/bin/bash

#https://blag.felixhummel.de/admin/venv_initd.html

#when running as service (start-stop-daemon)as  another user VIRTUAL_ENV should be taken from env, but not
#/usr/bin/env | grep VIRTUAL

Now="$(date +%Y-%m-%d-%H:%M:%S)"
Msg="$Now, VIRTUAL_ENV:$VIRTUAL_ENV, PYTHON_HOME:$PYTHON_HOME, USER: $USER" 
echo $Msg
echo $Msg >> /tmp/fsvoip.sh.log

#VIRTUAL_ENV=/home/linux/virtenv/py36

source $VIRTUAL_ENV/bin/activate


#export eMAIN_PAGE='/index'
export eSECRET_KEY='ABDF1245'
export eRECORDS='./Download'
#export eDATABASE_URL="sqlite://$(pwd)/App.db"
export eDATABASE_URL='mysql://fsvoip:fsvoip2018@192.168.2.111/app_fsvoip'
#export ePORT=8877


env | grep "^e"
echo

./fsvoip.py --port=8800
