from flask import Flask, render_template, redirect, request, jsonify, flash
from app.models import User, Password
from app import app, db, bcrypt
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
	if request.method == "GET":
		return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	forms = R

	



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