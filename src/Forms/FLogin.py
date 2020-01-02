from flask import request
from flask_login import login_user, current_user, LoginManager
from werkzeug.urls import url_parse
#
from .FForm import *
#from App.DbModel import TDbUser
from App import login


class TFLogin(TForm):
    Title      = "Login user"

    UserName   = StringField(description ="User", validators = [Required(), Length(min=1, max=32)])
    Password   = PasswordField(description ="Password", validators = [Length(min=1, max=16)])
    RememberMe = BooleanField('Remember me')
    Submit     = SubmitField("Log in")

    def Render(self):
        if (current_user.is_authenticated):
            return self.Redirect("/")

        if (request.method == "POST"):
            if (self.validate()):
                #User = TDbUser.query.filter_by(email=self.UserName.data).first()
                User = 'user01'
                if (User) and (User.passw == self.Password.data):
                    login_user(User, remember = self.RememberMe.data)

                    NextPage = request.args.get('next')
                    if (not NextPage) or (url_parse(NextPage).netloc != ''):
                        NextPage = 'index'
                    return self.Redirect("user")
                else:
                    self.Error = "Username or password incorrect"
                    self.Flash(self.Error)

        return self.RenderTpl()
