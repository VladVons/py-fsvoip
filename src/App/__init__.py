from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from Config import TConfRelease, TConfDebug


app = Flask(__name__, template_folder='../Templates', static_folder='../Static')
app.config.from_object(TConfDebug)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

from App import Routes, DbModel
