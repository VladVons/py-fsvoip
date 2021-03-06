import os
import tempfile

from .FForm import *
from flask import current_app
#from flask_uploads import UploadSet
#
from Inc.Log import Log
from Inc.Util import UXLS


class TFCompare(TForm):
    Title  = "Compare"

    Sheet1 = StringField()
    Sheet2 = StringField()
    Code1  = StringField(validators=[DataRequired()])
    Code2  = StringField()
    Name1  = StringField(validators=[DataRequired()])
    Name2  = StringField()
    Price1 = StringField(validators=[DataRequired()])
    Price2 = StringField()
    File1  = FileField(validators=[DataRequired()])
    File2  = FileField()
    Download = BooleanField(label="DoesntWork")
    Submit = SubmitField(label="OK")

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
        self.HData = {}
        self.HDownloadFile = ""

        if (request.method == "POST"):
            if (request.files) and (self.Submit.data):
                Fields = {
                    'Sheet': [self.Sheet1, self.Sheet2],
                    'Code':  [self.Code1,  self.Code2],
                    'Name':  [self.Name1,  self.Name2],
                    'Price': [self.Price1, self.Price2]
                }

                for Field in Fields:
                    if (not Fields[Field][1].data):
                        #Fields[Field][1].data = Fields[Field][0].data
                        pass

                self.HInfo = []
                Xls  = [None, None]
                File = [request.files.get('File1'), request.files.get('File2')]
                for i in range(2):
                    Xls[i] = UXLS.TXls()
                    if (File[i].filename):
                        Xls[i].LoadFields(Fields['Sheet'][i].data, Fields['Code'][i].data, Fields['Name'][i].data, Fields['Price'][i].data)
                        FileName = tempfile.mktemp() + '_' + File[i].filename
                        File[i].save(FileName)
                        Xls[i].LoadFile(FileName)
                        self.HInfo += Xls[i].Info
                        os.remove(FileName)
                self.HData = Xls[0].Compare(Xls[1])

                if (self.Download.data):
                    FileName = 'Compare.xlsx'
                    FilePath = current_app.root_path.replace('App', '') + 'Download/' + FileName
                    self.HDownloadFile = "Download/" + FileName
                    Xls[0].Export(self.HData, FilePath)

                Log.Print(1, 'w', 'Addr: %s, File1 %s, File2 %s' % (request.remote_addr, File[0].filename, File[1].filename))
        return self.RenderTpl()
