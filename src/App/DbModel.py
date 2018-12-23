from datetime import datetime
from flask_login import UserMixin
from App import db, login


@login.user_loader
def load_user(aId):
    print('---------41', aId)
    return TDUser.query.get(int(aId))


class TDUser(UserMixin, db.Model):
    __tablename__ = 'user'

    id      = db.Column(db.Integer,    primary_key=True)
    enabled = db.Column(db.Boolean(),  default=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow, doc='creation date')
    email   = db.Column(db.String(32), index=True, unique=True)
    passw   = db.Column(db.String(16))
    name    = db.Column(db.String(40))

    def __repr__(self):
        return 'id:%d, email:%s, enabled:%s' % (self.id, self.email, self.enabled)
