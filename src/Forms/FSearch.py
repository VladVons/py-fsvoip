from FForm import *
from flask import current_app
from mutagen.mp3 import MP3
import time
import datetime
import Inc.Util.FS as FS


class TFSearch(TForm):
    Title  = "Search"
    Phone  = StringField(description ="phone number", validators = [Required(), Length(min=1, max=16)])
    #Days   = StringField(description ="days", validators = [Required(), Length(min=1, max=3)])
    Submit = SubmitField("OK")

    def Search(self, aDir, aFile):
        Result = []
        Files = FS.FindFile([aDir], [aFile], True)
        Files.sort()
        for File in Files:
            Audio = MP3(File)
            AudioLen = datetime.timedelta(seconds = int(Audio.info.length))

            Result.append({
                'Duration' : AudioLen, 
                'File'  : File, 
                'Name'  : FS.GetCoreName(File), 
                'Date'  : time.strftime('%Y-%m-%d %H:%M', FS.GetCTime(File))
                })
        return Result

    def Render(self):
        Dir  = current_app.config.get('RECORDS')
        print('-----5', Dir)
        if (request.method == "POST"):
            if (self.validate()):
                self.Files = self.Search(Dir, self.Phone.data)
        elif (request.method == "GET"):
            self.Files = self.Search(Dir, request.args.get('Phone'))
        return self.RenderTpl()
