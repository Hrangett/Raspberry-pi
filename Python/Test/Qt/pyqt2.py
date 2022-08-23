import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("QTtest01.ui")[0]

class MyApp(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn1.clicked.connect(self.btn1_clicked)
		self.btn2.clicked.connect(self.btn2_clicked)
	
	def btn1_clicked(self):
		print("btn_ON Clicked")
	def btn2_clicked(self):
		print("btn_OFF Clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = MyApp()
	myWindow.show()
	sys.exit(app.exec_())
