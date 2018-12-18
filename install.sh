#!/bin/bash
# Created: 28.09.2016
# Vladimir Vons, VladVons@gmail.com


Install()
{
  Installed=$(pip list | grep Flask)
  if [ ! "$Installed" ]; then
    apt-get install python-pip
    #
    pip install Flask
    pip install Flask-WTF
    pip install Session
    pip install mutagen

    #pip install webhelpers
    #pip install flask_sqlalchemy 
    #pip install flask-migrate
    #pip install sqlalchemy_utils

    #apt-get install python-sqlalchemy-doc
    #cd /usr/share/doc/python-sqlalchemy-doc
  fi
}


ServiceRun()
{
  Name="fsvoip"

  cp -R deb/etc -T /etc
  find /etc | grep $Name

  update-rc.d $Name defaults
  update-rc.d $Name enable
  systemctl daemon-reload
  service $Name start

  echo "Check server running"
  service $Name status
  ps aux | grep -iv "grep" | egrep -i $Name
}

ServiceTest()
{
  USER=linux
  WORKDIR=/home/linux/py-fsvoip/src
  DAEMON=$WORKDIR/fsvoip.sh
  #start-stop-daemon --start --background  --user $USER --chuid $USER --chdir $WORKDIR --exec $DAEMON
  start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $USER --chuid $USER --chdir $WORKDIR --exec $DAEMON -- $ARGS
}


clear
case $1 in
    Install)        "$1"        "$2" "$3" ;;
    ServiceRun)     "$1"        "$2" "$3" ;;
esac

