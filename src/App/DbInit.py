from DbModel import *
from App import db


def CreateDemoDb():
    db.create_all()

    db.session.add(TDbUser(ID = 1, EMail = 'user1@example.com', Passw = '1abcd'))
    db.session.add(TDbUser(ID = 3, EMail = 'user3@example.com', Passw = '2abcd'))
    db.session.add(TDbUser(ID = 2, EMail = 'user2@example.com', Passw = '3abcd'))

    db.session.commit()


def DeleteDb():
    db.drop_all()
