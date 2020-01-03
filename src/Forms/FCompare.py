import os
import tempfile

from .FForm import *
from flask import current_app
from flask_uploads import UploadSet
#
from Inc.Util import UXLS


class TFCompare(TForm):
    Title  = "Compare"
    Sheet  = StringField()
    Code   = StringField(validators=[DataRequired()])
    Name   = StringField(validators=[DataRequired()])
    Price  = StringField(validators=[DataRequired()])
    File1  = FileField(validators=[DataRequired()])
    File2  = FileField(validators=[DataRequired()])
    Submit = SubmitField("OK")

    def Exec(self, aSheet, aCode, aName, aPrice, aFile1, aFile2):
        FileName1 = tempfile.mktemp() + '_' + aFile1.filename
        FileName2 = tempfile.mktemp() + '_' + aFile2.filename
        aFile1.save(FileName1)
        aFile2.save(FileName2)

        Xls = UXLS.TXls(aSheet = aSheet.data, aCode = aCode.data, aName = aName.data, aPrice = aPrice.data)
        Result = Xls.Compare(FileName1, FileName2)

        os.remove(FileName1)
        os.remove(FileName2)

        return Result

    def Render(self):
        if (request.method == "POST"):
            if (request.files) and (self.Submit.data):
                File1 = request.files.get('File1')
                File2 = request.files.get('File2')
                self.Data = self.Exec(self.Sheet, self.Code, self.Name, self.Price, File1, File2)
        return self.RenderTpl()
