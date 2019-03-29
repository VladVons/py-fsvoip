from datetime import datetime
from flask_login import UserMixin
from App import db, login


@login.user_loader
def load_user(aId):
    return TDUser.query.get(int(aId))


class TDbUser(UserMixin, db.Model):
    __tablename__ = 'rUser'

    ID      = db.Column(db.Integer,    primary_key=True)
    Name    = db.Column(db.Text())
    Enabled = db.Column(db.Boolean(),  default=True)
    Created = db.Column(db.DateTime(), default=datetime.utcnow, doc='creation date')
    EMail   = db.Column(db.String(32), index=True, unique=True)
    Passw   = db.Column(db.String(16))

    def __repr__(self):
        return 'ID:%d, EMail:%s, Enabled:%s' % (self.ID, self.EMail, self.Enabled)

#--- Additions

class TDbUserGroup(db.Model):
    __tablename__ = 'rUserGroup'

    ID        = db.Column(db.Integer(), primary_key=True)
    User_ID   = db.Column(db.Integer(), db.ForeignKey('rUser.ID'))
    Users_ID  = db.Column(db.Integer(), db.ForeignKey('rUser.ID'))


class TDbSeat(db.Model):
    __tablename__ = 'rSeat'

    ID       = db.Column(db.Integer(),  primary_key=True)
    Created  = db.Column(db.DateTime(), default=datetime.utcnow)
    Name     = db.Column(db.Text())


class TDbCompany(db.Model):
    __tablename__ = 'rCompany'

    ID       = db.Column(db.Integer(),  primary_key=True)
    Created  = db.Column(db.DateTime(), default=datetime.utcnow)
    Name     = db.Column(db.Text())
    Site     = db.Column(db.Text())
    Comment  = db.Column(db.Text())

    def __repr__(self):
        return 'ID:%d, Name:%s, Site:%s, Comment:%s' % (self.ID, self.Name, self.Site, self.Comment)


class TDbEmployee(db.Model):
    __tablename__ = 'rEmployee'

    ID         = db.Column(db.Integer(),  primary_key=True)
    Created    = db.Column(db.DateTime(), default=datetime.utcnow)
    Name       = db.Column(db.Text())
    EMail      = db.Column(db.String(32))
    Phone      = db.Column(db.String(32))
    Address    = db.Column(db.Text())
    Company_ID = db.Column(db.Integer(), db.ForeignKey('rCompany.ID'))
    Seat_ID    = db.Column(db.Integer(), db.ForeignKey('rSeat.ID'))

    def __repr__(self):
        return 'ID:%d, Name:%s, EMail:%s, Phone:%s, Company_id:%d' % (self.ID, self.Name, self.EMail, self.Phone, self.Company_ID)


class TDbUserCompany(db.Model):
    __tablename__ = 'rUserCompany'

    ID          = db.Column(db.Integer(), primary_key=True)
    User_ID     = db.Column(db.Integer(), db.ForeignKey('rUser.ID'))
    Company_ID  = db.Column(db.Integer(), db.ForeignKey('rCompany.ID'))


class TDbAction(db.Model):
    __tablename__ = 'rAction'

    ID       = db.Column(db.Integer(),  primary_key=True)
    Created  = db.Column(db.DateTime(), default=datetime.utcnow)
    Name     = db.Column(db.Text())

    def __repr__(self):
        return 'ID:%d, Name:%s' % (self.ID, self.Name)


class TDbProject(db.Model):
    __tablename__ = 'rProject'

    ID       = db.Column(db.Integer(),  primary_key=True)
    Created  = db.Column(db.DateTime(), default=datetime.utcnow)
    Name     = db.Column(db.Text())

    def __repr__(self):
        return 'ID:%d, Name:%s' % (self.ID, self.Name)


class TDbTask(db.Model):
    __tablename__ = 'dTask'

    ID          = db.Column(db.Integer(),  primary_key=True)
    Created     = db.Column(db.DateTime(), default=datetime.utcnow)
    Remind      = db.Column(db.DateTime())
    Result      = db.Column(db.Text())
    User_ID     = db.Column(db.Integer(), db.ForeignKey('rUser.ID'), nullable=False)
    Action_ID   = db.Column(db.Integer(), db.ForeignKey('rAction.ID'))
    Project_ID  = db.Column(db.Integer(), db.ForeignKey('rProject.ID'))
    Employee_ID = db.Column(db.Integer(), db.ForeignKey('rEmployee.ID'), nullable=False)

    def __repr__(self):
        return 'ID:%d, User_ID:%d, Employee_ID:%d, Result:%s' % (self.ID, self.User_ID, self.Employee_ID, self.Result)
