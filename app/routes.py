from flask import Flask, render_template, redirect, request, jsonify, flash, url_for
from app.models import User, Password
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
import string
import random



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.json

        length = int(data.get("length"))
        symbols = bool(data.get("symbols"))
        numbers = bool(data.get("numbers"))
        lowercase = bool(data.get("lowercase"))
        uppercase = bool(data.get("uppercase"))
        excludeSimilar = bool(data.get("excludeSimilar"))
        excludeAmbiguous = bool(data.get("excludeAmbiguous"))

        if not symbols and not numbers and not lowercase and not uppercase:
        	return "Empty fields"


        password = generate_pass(length, symbols, numbers, uppercase, lowercase, excludeSimilar, excludeAmbiguous)
        return password
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get("next")
			if next_page:
				return redirect(next_page)
			return redirect("/")
			flash("Login Successful")
		else:
			flash("Login Unsuccessful. Incorrect email/password")

	return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = RegistrationForm()
	if form.validate_on_submit(): 
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user = User(username=form.username.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("Account created successfully", "success")
		return redirect(url_for("login"))

		return redirect(url_for('login'))
	return render_template("register.html",form=form) 

@app.route("/logout",)
def logout():
	logout_user()
	return redirect(url_for("index"))

@app.route("/manager", methods = ["GET", "POST"])
@login_required
def manager():
	if request.method == "GET":
		return render_template("manager.html")
	

	



def generate_pass(length, symbols, numbers, uppercase, lowercase, similar, ambiguous):
	password = []
	conditions = []
	if symbols == True:
		conditions.append("symbols")
	if uppercase == True:
		conditions.append("uppercase")
	if lowercase == True:
		conditions.append("lowercase")
	if numbers == True:
		conditions.append("numbers")
	if len(conditions) <= 0:
		return None
	else:
		while len(password) < length:
			generate_random = random.choice(conditions)
			# Symbol random
			if generate_random == "symbols":
				symbol_characters = ["!", "#", 	"$", "%", "&", "*", "+", "-", ",", ".", "/", ":", ";", "=", "?", "@"]
				password.append(random.choice(symbol_characters))

			# Uppercase characters random
			if generate_random == "uppercase":
				password.append(chr(random.randint(65,90)))

			# Lowercase characters random
			if generate_random == "lowercase":
				password.append(chr(random.randint(97,122)))

			# Numbers random
			if generate_random == "numbers":
				password.append(str(chr(random.randint(48,57))))

			#If similar characters are excluded
			if similar == True:
				for i in password:
					if i in ["i","l", "1", "L", "o", "0", "O"]:
						password.remove(i)

			#If ambiguous characters are exluded
			if ambiguous == True:
				for i in password:
					if i in ["{", "}", "[", "]", "(", ")", "/", chr(92), "~", ",", ";", ":", ".", "<", ">", chr(39), chr(34)]:
						password.remove(i)
		
		return "".join(password)