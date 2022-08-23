import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#ui 파일 연동
form_class = uic.loadUiType("QTtest01.ui")[0]

class MyWindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mywindow = MyWindowClass()
	mywindow.show()
	app.exec_()
