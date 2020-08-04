from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home_screen():
	return render_template('index.html')


@app.route('/capture')
def camera():
	return render_template('capture.html')