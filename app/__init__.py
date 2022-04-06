from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "7Gfcu0daJhK9NN1sDDyX"
login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import routes