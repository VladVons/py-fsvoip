from flask   import render_template, request, redirect, flash, url_for
from wtforms import Form, StringField, SubmitField, PasswordField, BooleanField, FileField, validators
from wtforms.validators import Required, Length


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
