from flask_login import login_user, current_user, LoginManager
from FForm import *


class TFLogin(TForm):
    Title      = "Login user"

    UserName   = StringField(description ="User", validators = [Required(), Length(min=1, max=16)])
    Password   = PasswordField(description ="Password", validators = [Length(min=1, max=16)])
    RememberMe = BooleanField('Remember me')
    Submit     = SubmitField("Log in")

    def Render(self):
        if (current_user.is_authenticated):
            return self.Redirect("/")

        if (request.method == "POST"):
            if (self.validate()):
                if (SessionUser.Connect(self.UserName.data, self.Password.data)):
                    return redirect("/user")
                else:
                    self.Error = "Username or password incorrect"
                    flash(self.Error)
        return self.RenderTpl()

