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
    
    # Dummy data for vertical carousels
    left_sidebar_images = [
        {'url': 'https://via.placeholder.com/250x400?text=Ad+1', 'alt': 'Advertisement 1', 'link': '#'},
        {'url': 'https://via.placeholder.com/250x400?text=Ad+2', 'alt': 'Advertisement 2', 'link': '#'},
        {'url': 'https://via.placeholder.com/250x400?text=Ad+3', 'alt': 'Advertisement 3', 'link': '#'},
    ]
    right_sidebar_images = [
        {'url': 'https://via.placeholder.com/250x200?text=Right+Ad+1', 'alt': 'Right Ad 1', 'link': '#'},
        {'url': 'https://via.placeholder.com/250x200?text=Right+Ad+2', 'alt': 'Right Ad 2', 'link': '#'},
    ]

    return render_template('index.html', posts=posts, left_sidebar_images=left_sidebar_images, right_sidebar_images=right_sidebar_images)

@main_bp.route('/profile')
@login_required
def profile():
    # current_user is automatically available from Flask-Login
    return render_template('profile.html', title='Your Profile', user=current_user)

@main_bp.route('/todays_posts')
def todays_posts():
    return render_template('todays_posts.html', title='Today\'s Posts')

@main_bp.route('/real_estate')
def real_estate():
    # Query all active posts for real estate listings
    posts = Post.query.filter_by(is_active=True, category='real_estate').order_by(Post.created_at.desc()).all()
    return render_template('real_estate.html', title='Real Estate', posts=posts)

@main_bp.route('/user_forum')
def user_forum():
    return render_template('user_forum.html', title='User Forum')

@main_bp.route('/marketplace')
def marketplace():
    return render_template('marketplace.html', title='Marketplace')

@main_bp.route('/business_announcements')
def business_announcements():
    return render_template('business_announcements.html', title='Business Announcements')

@main_bp.route('/events_accommodations')
def events_accommodations():
    return render_template('events_accommodations.html', title='Events & Accommodations')

@main_bp.route('/best_of')
def best_of():
    return render_template('best_of.html', title='Best Of')

@main_bp.route('/submit-post/<category>')
@login_required
def submit_post(category):
    return render_template('post_form.html', title=f'Submit {category.replace("-", " ").title()} Post', category=category)