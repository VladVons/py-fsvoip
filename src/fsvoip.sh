#!/bin/bash

#https://blag.felixhummel.de/admin/venv_initd.html

#when running as service (start-stop-daemon)as  another user VIRTUAL_ENV should be taken from env, but not
#/usr/bin/env | grep VIRTUAL
echo "Env: $VIRTUAL_ENV, user: $USER" >> /tmp/fvoip.log
VIRTUAL_ENV=/home/linux/virtenv/myapp

source $VIRTUAL_ENV/bin/activate


export eSECRET_KEY='ABDF1245'
export eRECORDS='./Download'
#export eDATABASE_URL="sqlite://$(pwd)/App.db"
export eDATABASE_URL='mysql://fsvoip:fsvoip2018@192.168.2.111/app_fsvoip'
#export ePORT=8877
env | grep "^e"
echo

./fsvoip.py --port=8888

