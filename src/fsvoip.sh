#!/bin/bash

#https://blag.felixhummel.de/admin/venv_initd.html

#when running as service (start-stop-daemon)as  another user VIRTUAL_ENV should be taken from env, but not
#/usr/bin/env | grep VIRTUAL
echo "Env: $VIRTUAL_ENV, user: $USER" >> /tmp/fvoip.log
VIRTUAL_ENV=/home/linux/virtenv/myapp

source $VIRTUAL_ENV/bin/activate

export SECRET_KEY='ABDF1245'
export DATABASE_URL='mysql://grafana:grafana2018@192.168.2.111/3w_grafana'
#export PORT=8877
./fsvoip.py --port=8888
