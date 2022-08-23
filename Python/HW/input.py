import RPi.GPIO as GPIO
import time

switchPin1 = 11
switchPin2 = 21
LED = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(switchPin1 ,GPIO.IN)
GPIO.setup(switchPin2 ,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

try:
	while True:
		if (GPIO.input(switchPin1) == True)&(GPIO.input(switchPin2)==False):
			print("ON")
			GPIO.output(18, True)
			
		if GPIO.input(switchPin2) == True:
			print("OFF")
			GPIO.output(18,False)

except KeyboardInterrupt:
	GPIO.cleanup()
