from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import Post

api_bp = Blueprint('api', __name__)

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
        author=current_user
    )

    db.session.add(post)
    db.session.commit()

    return jsonify(post.to_dict()), 201