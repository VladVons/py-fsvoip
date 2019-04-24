#!/usr/bin/env python

from Inc.Util import FS

#aDirs = ['./Download']
#FS.FindFile(aDirs, '0', True)


import urllib
queryStr = '%E2%80%8E0963352402'
t1 = urllib.unquote(queryStr)
print(t1)
