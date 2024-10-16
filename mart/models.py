from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__='user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(255), nullable=False)
    secondName = db.Column(db.String(255), nullable=False)
    userName = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    isProvider = db.Column(db.Boolean, nullable=False, default=False)
    isVisitor = db.Column(db.Boolean, nullable=False, default=False)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)

    def get_id(self):
        return self.id
    

