import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
#from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
#    qApp, QFileDialog, QTableView, QTableWidget, QTableWidgetItem, QWidget
from PyQt5.QtWidgets import *
import coletarAmostra, cinza
import os, sys
from PIL import Image

app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(0, 0, 400, 200)

btn = QPushButton(window)

pic = QLabel(window)
pic.setGeometry(10, 10, 400, 100)
#use full ABSOLUTE path to the image, not relative
pic.setPixmap(QPixmap(os.getcwd() + "/logo.png"))

window.show()
sys.exit(app.exec_())