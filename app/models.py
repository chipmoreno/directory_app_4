from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    return db.session.get(User, int(user_id))

'''# Many-to-many association table for Users and Roles
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

# Many-to-many association table for Listings and Tags
listing_tags = db.Table('listing_tags',
    db.Column('listing_id', db.Integer, db.ForeignKey('listings.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)'''



class User(db.Model, UserMixin, SerializerMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)
    '''roles = db.relationship('Role', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))'''
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'
    

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    contact_info = db.Column(db.Text, nullable=False)
    image_urls = db.Column(db.JSON)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': str(self.price),
            'location': self.location,
            'contact_info': self.contact_info,
            'image_urls': self.image_urls,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }

    
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Message {self.id}>'

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    def __repr__(self):
        return f'<Comment {self.id}>'
    