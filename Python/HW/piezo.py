import RPi.GPIO as GPIO
import time
piezoPin = 13

# melody list
melody = [130,146,164,174,195,220,246,261]
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while(True):
		Buzz.start(50) # PWM 시작 :: 50%는 ON, 50%는 OFF
		for i in melody:
			Buzz.ChangeFrequency(i + 32.39 )
			time.sleep(0.2)
		Buzz.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
