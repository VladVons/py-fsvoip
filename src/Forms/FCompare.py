from .FForm import *
from flask import current_app
from flask_uploads import UploadSet
#
from Inc.Util import UXLS


class TFCompare(TForm):
    Title  = "Compare"
    Sheet  = StringField()
    Code   = StringField(validators=[Required()])
    Name   = StringField(validators=[Required()])
    Price  = StringField(validators=[Required()])
    File1  = FileField(validators=[Required()])
    File2  = FileField(validators=[Required()])
    Submit = SubmitField("OK")

    def Exec(self, aSheet, aCode, aName, aPrice, aFile1, aFile2):
        f1 = request.files.get('File1')
        print('---', aSheet, aCode, aName, aPrice, aFile1, aFile2, f1)
        #Xls = UXLS.TXls(aSheet = aSheet, aCode = aCode, aName = aName, aPrice = aPrice)
        #Data = Xls.Compare(aFile1, aFile2)
        Data = []
        return Data

    def Render(self):
        print('111')
        if (request.method == "POST"):
            print('222')
            #if self.validate_on_submit():
            #if (self.validate()):
            if (self.Submit.data):
              print('333')
              self.Data = self.Exec(self.Sheet.data, self.Code.data, self.Name.data, self.Price.data, self.File1.data, self.File2.data)
        #elif (request.method == "GET"):
        #    Args = request.args
        #    if Args.get('Submit'):
        #      self.Data = self.Exec(Args.get('Sheet'), Args.get('Code'), Args.get('Name'), Args.get('Price'), Args.get('File1'), Args.get('File2'))
        return self.RenderTpl()
