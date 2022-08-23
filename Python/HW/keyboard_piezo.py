import RPi.GPIO as GPIO
import time

piezoPin = 13

melody=[130,146,164,174,195,220,246,261]
scales= ["도","레","미","파","솔","라","시","도"]
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin,GPIO.OUT)

Buzz=GPIO.PWM(piezoPin,262)

try:
	while(True):
		scale =int(input("press the key board(0~7)"))
		if (scale>7):
			print("Wrong")
			Buzz.stop()
			continue
		print(scales[scale]) 
		Buzz.start(50)
		Buzz.ChangeFrequency(melody[scale]) 
		time.sleep(0.5)
		Buzz.stop()
#		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
