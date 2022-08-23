from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return "<h1> Web Control page <h1>"

@app.route('/get')
def get():
	return render_template('default.html')

if __name__=="__main__":
	app.run(host="0.0.0.0")

