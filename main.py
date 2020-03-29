#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, request
from flask_prometheus import monitor
import re, time

app = Flask(__name__)

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
			return render_template('login.html', error=error), 401
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/notfound')
def notfound():
	return 'Not Found',404

@app.route('/delay')
def delay():
	time.sleep(10)
	return 'Delay Airline', 200
@app.route('/home')
def home():
	return 'Welcome Home', 200

@app.route('/calculator', methods=['GET','POST'])
def calculator():
	if request.method == 'GET':
		return render_template('calculator.html')
	elif request.method == 'POST':
		expression = request.form.get('expression')
		result = eval(expression)
		return render_template('calculator.html', result=result)

monitor(app, port=8000)
app.run()
