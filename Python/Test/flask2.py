from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return 'hello,home'

@app.route('/user')
def user():
	return 'hello,user'

if __name__ == '__main__':
	app.run(debug=True)
