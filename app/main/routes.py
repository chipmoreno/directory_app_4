from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from ..models import Post, User
from app import db 
from datetime import datetime 

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('base.html')

@main_bp.route('/profile')
@login_required
def profile():
    # current_user is automatically available from Flask-Login
    return render_template('profile.html', title='Your Profile', user=current_user)

def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)