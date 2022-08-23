from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
#View  함수 :: return 이 항상 존재해야함
	return "Hello, Flask"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug = True)
