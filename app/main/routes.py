from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user
from ..models import Post, User
from app import db 
from datetime import datetime 

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(is_active=True).order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', posts=posts)

@main_bp.route('/profile')
@login_required
def profile():
    # current_user is automatically available from Flask-Login
    return render_template('profile.html', title='Your Profile', user=current_user)
