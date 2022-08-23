import RPi.GPIO as GPIO
import time
from flask import Flask 

ledPin = 21

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

@app.route('/')
@app.route('/home')
def home():
	return "HOME"

@app.route('/on')
def led_on():
	GPIO.output(ledPin,True)
	return "LED ON"

@app.route('/off')
def led_off():
	GPIO.output(ledPin,False)
	return "LED OFF"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
