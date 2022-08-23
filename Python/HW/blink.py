import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while(True):
	GPIO.output(21, True)
	GPIO.output(18, False)
	time.sleep(1)
	GPIO.output(21, False)
	GPIO.output(18, True)
	time.sleep(1)
	
