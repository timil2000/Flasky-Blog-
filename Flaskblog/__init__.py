from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3307/flaskblog'

db = SQLAlchemy(app)
# we pass the app instance to the Bcrypt constructor to initialize the extension
bcrypt = Bcrypt(app) # Initialize the Bcrypt extension

login_manager = LoginManager(app)

# This is the route that users are redirected to when they try to access a login_required route
login_manager.login_view = 'login'
# This is the message category that will be used for the flashed messages
login_manager.login_message_category = 'info'

from Flaskblog import route