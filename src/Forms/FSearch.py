from FForm import *
from flask import current_app
from mutagen.mp3 import MP3
import time
import datetime
import Inc.Util.FS as FS


class TFSearch(TForm):
    Title  = "Search"
    Phone  = StringField(description ="phone number", validators = [Required(), Length(min=1, max=16)])
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
        if (request.method == "POST"):
            if (self.validate()):
                Dir  = current_app.config.get('RECORDS')
                self.Files = self.Search(Dir, self.Phone.data)
        return self.RenderTpl()
