from flask   import render_template, request, redirect, flash, url_for
from wtforms import Form, validators
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField, FileField
from wtforms.validators import DataRequired, Length
#
from Inc.Log          import Log

class TForm(Form):
    def RenderTpl(self):
        Template = self.__class__.__name__ + '.html'
        return render_template(Template, Form = self)

    def Render(self):
        Msg = Log.Print(1, 'e', self.__class__.__name__, 'DoParameter()', 'Not implemented')
        raise NotImplementedError(Msg)

    def Redirect(self, aUrl):
        #return redirect(url_for(aUrl))
        return redirect(aUrl)

    def Flash(self, aMsg):
        return flash(aMsg)
