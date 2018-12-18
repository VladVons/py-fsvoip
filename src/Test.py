#!/usr/bin/env python

import os
import time, datetime
from mutagen.mp3 import MP3
import Inc.Util.FS as FS

File='/mnt/share/work/recordings/call/2018-12-17/145339_532_532_0681477055_0681477055.mp3'
audio = MP3(File)
#print (audio.info.length)

#Msg = time.strftime('%Y-%m-%d %H:%M', FS.GetCTime(File))
Msg = time.localtime(os.path.getmtime(File))
#print(time.strftime('%m-%d-%Y', time.gmtime(Time)))
print(Msg)

#print str(datetime.timedelta(seconds=666))
#print datetime.timedelta(666)