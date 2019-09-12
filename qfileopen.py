import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):
	def __init__(self):
		super(App, self).__init__()
		self.title = 'Italulu'
		self.width = 600
		self.height = 500
		self.initWindow()


	def initWindow(self):
		fname = QFileDialog.getOpenFileName(self, 'Abrir Arquivo','c:\\', 'Imagens (*.jpg)')




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())

