import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(triggerPin,True)
	time.sleep(0.0001) #10us의 어쩌구저쩌구,,
	GPIO.output(triggerPin,False)
	start = time.time()
	
	while GPIO.input(echoPin) == False:
		start = time.time()
	while GPIO.input(echoPin) == True:
		stop =  time.time()
	
	elapsed = stop - start
	distance = (elapsed * 38000)/2 #거 = 속*시
	
	return distance

def Buzz_sound():
	Buzz.start(50)
	Buzz.ChangeFrequency(246)


triggerPin = 26
echoPin = 21
piezoPin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin,440)

try:
	while True:
		distance = measure()
		if distance < 3.5:
			print("STOP")
			Buzz.start(50)
			Buzz.ChangeFrequency(246)
			continue
		Buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()

