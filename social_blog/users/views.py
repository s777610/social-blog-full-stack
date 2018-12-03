from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from social_blog import db  # from __init__.py
from social_blog.models import User, BlogPost
from social_blog.users.forms import RegistrationForm, LoginForm, UpdateUserForm, RequestResetForm, ResetPasswordForm
from social_blog.users.utils import add_profile_pic, send_reset_email
from werkzeug.security import generate_password_hash


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.info'))
    form = RegistrationForm()
    # form itself is going to check if email or username has already been taken
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.info'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Log in Success!')
            # if user was trying to reach other web page which required login,
            # if so, next is that page
            next = request.args.get('next')
            # if next == None, just go to home page
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))  # core blueprint


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        # this will be activated if form.picture.data has image data
        if form.picture.data:
            username = current_user.username
            # pic is "username.png"...and so on..
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    # rendering template for user's account page
    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image) 
    return render_template('account.html', profile_image=profile_image, form=form)


@users.route("/<username>")
def user_posts(username):
    # grab whatever page you are currently on, ...
    page = request.args.get('page', 1, type=int)
    # get user by passing username
    user = User.query.filter_by(username=username).first_or_404()
    # User class has posts
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    # make sure users are logout in order to make a request to reset password
    if current_user.is_authenticated:
        return redirect(url_for('core.info'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info') # info is boostrap class
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


# click this link from email in order to reset email
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('core.info'))
    user = User.verify_reset_token(token)
    if user is None: # expire or invalid
        flash('That is an invalid or expired token', 'warning') # warning is boostrap class
        return redirect(url_for('users.reset_request'))
    # token is valid
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)




