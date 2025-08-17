from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from .. import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET'])
def register():
    return render_template('register.html', title='Register')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        data = request.get_json()
        if not data or not 'email' in data or not 'password' in data:
            return jsonify({'error': 'Invalid input'}), 400

        user = User.query.filter_by(email=data['email']).first()

        if user is None or not user.check_password(data['password']):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('main.index'))

    return render_template('login.html', title='Login')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))