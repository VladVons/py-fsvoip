import urllib
import time
import datetime

from mutagen.mp3 import MP3
from Inc.Util import UFS 

def GetDirList(aDir, aFile):
    Result = []
    if (not aFile):
      return Result

    aFile = urllib.parse.unquote(aFile).strip()
    Files = UFS.FindFile([aDir], [aFile], True)
    Files.sort()
    for File in Files:
        Audio = MP3(File)
        AudioLen = datetime.timedelta(seconds = int(Audio.info.length))

        Result.append({
          'Duration' : AudioLen,
          'File'  : File,
          'Name'  : UFS.GetCoreName(File),
          'Date'  : time.strftime('%Y-%m-%d %H:%M', UFS.GetCTime(File))
        })
    return Result
