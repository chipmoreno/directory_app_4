from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
migrate = Migrate()

def create_app():
    app=Flask(__name__,instance_relative_config=False)
    app.config['SECRET_KEY'] = 'a_very_secret_key_that_you_should_change'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/auth_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.auth.routes import auth_bp
        from app.main.routes import main_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)
        "Here, we would import roots and blueprints"
        "from app.ABC.routes import ABC_bp"
        "app.register_blueprint(ABC_bp)"


        '''Before making the following live, define 403.html'''

        '''@app.errorhandler(403)
        def forbidden_error(error):
            return render_template('errors/403.html'), 403'''
        
        return app
        