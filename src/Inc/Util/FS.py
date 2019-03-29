import os
import time


def FindFile(aDirs, aFiles, aSubDir = False):
    Result = []

    for Dir in aDirs:
        for Root, Folders, Files in os.walk(Dir):
            for File1 in aFiles:
                for File2 in Files:
                    if (File1):
                        if (File1 in File2):
                            Result.append(Root + '/' + File2)
        if (not aSubDir):
            break
    return Result


def GetCoreName(aPath):
    return os.path.splitext(os.path.basename(aPath))[0]


def GetCTime(aFile):
    Result = time.localtime(os.path.getmtime(aFile))
    #time.strftime('%Y-%m-%d %H:%M:%S', Result)
    return Result

