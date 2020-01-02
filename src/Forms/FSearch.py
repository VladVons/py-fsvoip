from .FForm import *
from flask import current_app
#
from Inc.Util import UMP3


class TFSearch(TForm):
    Title  = "Search"
    Phone  = StringField(description ="phone number", validators = [Required(), Length(min=1, max=16)])
    #Days   = StringField(description ="days", validators = [Required(), Length(min=1, max=3)])
    Submit = SubmitField("OK")

    def Exec(self, aDir, aFile):
        return UMP3.GetDirList(aDir, aFile)

    def Render(self):
        Dir  = current_app.config.get('RECORDS')
        if (request.method == "POST"):
            if (self.validate()):
                self.Data = self.Exec(Dir, self.Phone.data)
        elif (request.method == "GET"):
            self.Data = self.Exec(Dir, request.args.get('Phone'))
        return self.RenderTpl()
