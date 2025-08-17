from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from app import db
from app.models import Post, User

api_bp = Blueprint('api', __name__)

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not 'username' in data or not 'email' in data or not 'password' in data:
        return jsonify({'error': 'Invalid input'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    # In a real application, you would return a JWT token here.
    # For simplicity, we will return a success message.
    return jsonify({'message': 'User registered successfully'}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not 'email' in data or not 'password' in data:
        return jsonify({'error': 'Invalid input'}), 400

    user = User.query.filter_by(email=data['email']).first()

    if user is None or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    login_user(user)
    # In a real application, you would return a JWT token here.
    # For simplicity, we will return a success message.
    return jsonify({'message': 'Logged in successfully'})

@api_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

@api_bp.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    posts = Post.query.filter_by(is_active=True).order_by(Post.created_at.desc()).paginate(page=page, per_page=limit, error_out=False)
    return jsonify({
        'posts': [post.to_dict() for post in posts.items],
        'total_count': posts.total,
        'current_page': posts.page,
        'total_pages': posts.pages
    })

@api_bp.route('/posts', methods=['POST'])
@login_required
def create_post():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    required_fields = ['title', 'description', 'price', 'location', 'contact_info']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    post = Post(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        location=data['location'],
        contact_info=data['contact_info'],
        image_urls=data.get('image_urls'),
        category=data.get('category', 'general'), # Add this line
        author=current_user
    )

    db.session.add(post)
    db.session.commit()

    return jsonify(post.to_dict()), 201
