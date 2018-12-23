from DbModel import TDUser
from App import db


def CreateDemoDb():
    print('--------------1')
    db.create_all()

    db.session.add(TDUser(id = 1, email = 'user1@example.com', passw = '1abcd'))
    db.session.add(TDUser(id = 3, email = 'user3@example.com', passw = '2abcd'))
    db.session.add(TDUser(id = 2, email = 'user2@example.com', passw = '3abcd'))
    db.session.add(TDUser(id = 4, email = 'user4@example.com', passw = '4abcd'))

    db.session.commit()
