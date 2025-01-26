from flask import render_template, url_for, flash, redirect, request
from flask_wtf import form

from Flaskblog import app, db, bcrypt
from Flaskblog.forms import RegistrationForm, LoginForm
from Flaskblog.model import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    # If the user is already logged in, redirect them to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the password before storing it in the database
        hased_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hased_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Enjoy blogs!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # If the user is already logged in, redirect them to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # Check if the user exists
        if user and bcrypt.check_password_hash(user.password, form.password.data): # Check if the password is correct
            login_user(user, remember=form.remember.data) # Log the user in

            next_page = request.args.get('next') # Get the next page the user was trying to access

            # Redirect the user to the next page if it exists, otherwise redirect them to the home page
            return redirect(next_page) if next_page else redirect(url_for('home'))
            # flash(f'Welcome {user.username}!', 'success')

        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user() # Log the user out
    return redirect(url_for('home'))

@app.route("/account")
@login_required # This decorator ensures that the user is logged in before they can access def account():
def account():
    # The user's profile picture is stored in the static folder
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


# timil1234












