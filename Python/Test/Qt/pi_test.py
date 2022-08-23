import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

form_class = uic.loadUiType("Test2.ui")[0]

LED_PIN = 26
peizo = 19
dht = 21
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(peizo, GPIO.OUT)
#GPIO.setup(dht, GPIO.OUT)

Buzz = GPIO.PWM(peizo,444)
melody = [130,146,164,174,195,220,246,261]

class MyAppClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.btnCallBack)
		self.pushButton_2.clicked.connect(self.btn2CallBack)
		self.pushButton_3.clicked.connect(self.buzz01CallBack)
		self.pushButton_4.clicked.connect(self.dth01CallBack)

	def btnCallBack(self):
		print("btn ON")
		self.textEdit.append("btn_ON")
		GPIO.output(LED_PIN,True)

	def btn2CallBack(self):
		print("btn2 OFF")
		self.textEdit.append("btn2_OFF")
		GPIO.output(LED_PIN,False)

	def buzz01CallBack(self):
		self.textEdit.append("buzzzzz")
		Buzz.start(50)
		for i in melody:
			Buzz.ChangeFrequency(i)
			time.sleep(0.2)
		Buzz.stop()

	def dth01CallBack(self):
		h,t = Adafruit_DHT.read_retry(sensor,dht)
		
		if h is not None and t is not None:
			self.textEdit.append("Temp = {0:0.1f}*C Humi = {1:0.1f}%".format(t,h))
			print("Temp = {0:0.1f}*C Humi = {1:0.1f}%".format(t,h))
		else:	
			self.textEdit.append("Failed to get reading")
if __name__=="__main__":
	app=QApplication(sys.argv)
	myWindow = MyAppClass()
	myWindow.show()
	sys.exit(app.exec_())
