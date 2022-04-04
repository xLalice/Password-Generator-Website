from app import db


class User(db.Model):
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
		return f"User('{self.application}', '{self.password}')"