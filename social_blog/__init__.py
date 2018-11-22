import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from social_blog.config import Config



"""
We want extension objects be created outside of create_app func, 
but we still want to initialize those extensions inside func with "app"
Therefore, one extension object could be used for multiple apps
"""
# create extensions
db = SQLAlchemy()

login_manager = LoginManager()
# in order to tell users what view to go to when they log in
login_manager.login_view = 'users.login'  # blueprint of users
mail = Mail()



# it allow us to have different instance with different config
def create_App_Db(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    Migrate(app,db)

    from social_blog.core.views import core
    from social_blog.users.views import users
    from social_blog.blog_posts.views import blog_posts
    from social_blog.error_pages.handlers import error_pages
    app.register_blueprint(core)
    app.register_blueprint(users)
    app.register_blueprint(blog_posts)
    app.register_blueprint(error_pages)

    return app, db






