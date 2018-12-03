from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from social_blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
# this allows us to have functionality such as authenticated, active
# provide many built in attributes which can be called in views
from flask_login import UserMixin
from flask import current_app



# to get current user by pass user_id
# login_manager is defined in __init__.py
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)  # to get user object by passing user_id


# all model class inherit from db.Model
class User(db.Model, UserMixin):  # UserMixin, logging functionality(our actual model inside templates)
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    # index=True means that allows you make the column into index
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # this can be called by users blueprint, user_posts()
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        # dumps() take a object and reuturn a string
        return s.dumps({'user_id': self.id}).decode('utf-8') # this is token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            # if not expire, s.loads(token) is {'user_id': self.id}
            user_id = s.loads(token)['user_id'] 
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f'Username {self.username}'


class BlogPost(db.Model):
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    # users is tablename, id is its attribute
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f'Post ID: {self.id} -- Date : {self.date} === {self.title}'



