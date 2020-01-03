#!/usr/bin/env python
###!/home/linux/virtenv/myapp/bin/python

import prctl
import signal
#
from App import app
#from App import DbInit
from Inc.Log          import Log


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
