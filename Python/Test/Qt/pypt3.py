import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Test2.ui")[0]

class MyAppClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.btnCallBack)
		self.pushButton_2.clicked.connect(self.btn2CallBack)

	def btnCallBack(self):
		print("btn ON")
		self.textEdit.append("btn_ON")

	def btn2CallBack(self):
		print("btn2 OFF")
		self.textEdit.append("btn2_OFF")

if __name__=="__main__":
	app=QApplication(sys.argv)
	myWindow = MyAppClass()
	myWindow.show()
	sys.exit(app.exec_())
