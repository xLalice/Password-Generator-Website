from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=6, max=20)])
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Password", validators=[DataRequired(), EqualTo("password ")])
	submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")