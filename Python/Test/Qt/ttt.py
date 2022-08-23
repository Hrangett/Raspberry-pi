
#rsap_test.py
#created : 2022. 7. 29
#Author : 오소라

import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
import Adafruit_DHT

dremi = [130, 146, 164, 174, 195, 220, 246, 261]

led = 26
piezo = 19
temp = 6
trigger = 8
echo = 13
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(piezo, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

buzz = GPIO.PWM(piezo, 440)

form_class = uic.loadUiType("Test2.ui")[0]

#초음파 거리 측정
def measure() : 
	GPIO.output(trigger, True)
	time.sleep(0.0001)
	GPIO.output(trigger, False)
	start = time.time()

	while GPIO.input(echo) == False :
		start = time.time()
	while GPIO.input(echo) == True :
		stop = time.time()

	dis = stop - start
	distance = (dis * 19000) /2

	return distance

#PIEZO
def doremi(a) : 
	buzz.start(90)
	buzz.ChangeFrequency(dremi[a])
	time.sleep(0.3)
	buzz.stop()

class MyAppClass (QMainWindow, form_class):
	def __init__(self) :
		super().__init__()
		self.setupUi(self)
		#led 켜기
		self.pushButton.clicked.connect(self.turnOn)
		#led 끄기
		self.pushButton_2.clicked.connect(self.turnOff)
		#온습도 측정
		#self.btn3.clicked.connect(self.DHT)
		#거리 측정
		#self.btn4.clicked.connect(self.Distance)
		#음계 출력
		self.pushButton_3.clicked.connect(self.doremi_do)
		#self.btnRe.clicked.connect(self.doremi_re)
		#self.btnMi.clicked.connect(self.doremi_mi)
		#self.btnPa.clicked.connect(self.doremi_pa)
		#self.btnSol.clicked.connect(self.doremi_sol)
		#self.btnLa.clicked.connect(self.doremi_la)
		#self.btnSi.clicked.connect(self.doremi_si)

	def turnOn(self) :
#		self.led_text.clear()
#		self.led_text.append("TURN ON")
		GPIO.output(led, True)

	def turnOff(self) :
#		self.led_text.clear()
#		self.led_text.append("TURN OFF")
		GPIO.output(led, False)

	def DHT(self) :
		h, t = Adafruit_DHT.read_retry(sensor, temp)
		if h is not None and t is not None :
			self.textEdit.clear()
			self.textEdit.append("온도 : {0:0.1f}C, 습도 : {1:0.1f}%".format(t, h))
		else :
			self.textEdit.append("다시 시도해주세요")

	def Distance(self) :
		distance = measure()
		self.dis_text.clear()
		self.dis_text.append("거리 : %.2fcm" % distance)

	def doremi_do(self) :
		doremi(0)
	def doremi_re(self) :
		doremi(1)
	def doremi_mi(self) :
		doremi(2)
	def doremi_pa(self) :
		doremi(3)
	def doremi_sol(self) :
		doremi(4)
	def doremi_la(self) :
		doremi(5)
	def doremi_si(self) :
		doremi(6)

if __name__ == "__main__" :
	app = QApplication(sys.argv)
	myWindow = MyAppClass()
	myWindow.show()
	sys.exit(app.exec_())

