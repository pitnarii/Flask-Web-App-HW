from datetime import datetime
from flask_login import UserMixin
from blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

#Create post models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    title = db.Column(db.String(255))#db.Text, nullable=False
    content = db.Column(db.Text)#nullable=False
    author = db.Column(db.String(255))
    image_file = db.Column(db.String(40), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    slug = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='post') 

    def __repr__(self):
        return f"Post('{self.date}', '{self.title}', '{self.content}')"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user')
    
    def __repr__(self):
        return f"User('{self.username}')"
    
    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)
    date =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    # posts = db.relationship('Post', backref='comment', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

