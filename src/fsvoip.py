#!/usr/bin/env python3
###!/home/linux/virtenv/myapp/bin/python

from Inc.Log import Log, TLogConsole, TLogFile
Log.AddEcho(TLogConsole())
Log.AddEcho(TLogFile('/tmp/fsvoip.py.log'))
Log.Print(1, 'i', __name__, 'starting')

try:
  import prctl
except Exception as E:
  Log.Print(1, 'e', __name__, E)
  exit()

import signal
#
from App import app
#from App import DbInit


if (__name__ == "__main__"): 
    def SetExitHandler(aFunc):
        prctl.set_name('fsvoip')
        prctl.set_pdeathsig(signal.SIGINT)
        signal.signal(signal.SIGTERM, aFunc)

    def OnExit(aSignal, func=None):
        Log.Print(1, 'i', __name__, 'OnExit()')
        sys.exit(1)

    SetExitHandler(OnExit)

    #DbInit.CreateDemoDb()
    #DbInit.DeleteDb()

    app.run(host = '0.0.0.0', port = app.config.get('PORT'))
