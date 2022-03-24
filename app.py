from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "GET":
		return render_template("index.html")
	else:
		# Get the input values
		length = int(request.form.get("charnum"))
		numbers = request.form.get("numbers")
		symbols = request.form.get("symbols")
		lowercase = request.form.get("lowercase")
		uppercase = request.form.get("uppercase")
		ambiguous = request.form.get("ambiguous")

		# Generate Password with the preceding conditions
		password = generate_pass(length, symbols, uppercase, lowercase, numbers, ambiguous)
		return render_template("password.html", password=password)














def generate_pass(length, symbols, uppercase, lowercase, numbers, ambiguous):
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
	while len(password) < length:
		generate_random = random.choice(conditions)
		# Symbol random
		if generate_random == "symbols":
			symbol_character = chr(random.randint(33,64))
			while symbol_character.isnumeric():
				symbol_character = chr(random.randint(33,64))
			password.append("symbol_character")

		# Uppercase characters random
		if generate_random == "uppercase":
			password.append(chr(random.randint(65,90)))

		# Lowercase characters random
		if generate_random == "lowercase":
			password.append(random.randint(97,122))

		# Numbers random
		if generate_random == "numbers":
			password.append(chr(random.randint(48,57)))
	
	return "".join(password)





