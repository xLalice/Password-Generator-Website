from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.password}')"

class Password(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	application = db.Column(db.String(20), nullable=False)
	password = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return f"Password('{self.application}', '{self.password}')"