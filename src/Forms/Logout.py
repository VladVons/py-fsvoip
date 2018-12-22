from flask_login import logout_user
#
from FForm import *


class TFLogout(TForm):
    Title    = "Logout user"

    def Render(self):
        logout_user()
        self.Redirect('/')
