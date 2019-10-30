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

class QImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.printer = QPrinter()
        self.scaleFactor = 0.0
        self.fileName = "image.jpg"

        self.imageLabel = QLabel()
        #self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 500, 500))
        #self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #self.imageLabel.setScaledContents(True)    

        self.imgLabel = QLabel(self)
        self.imgLabel.setGeometry(QtCore.QRect(20, 60, 200, 200))
        self.imgLabel.setText("HELLO")

        self.criarTableView()
       
        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setVisible(False)

        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenus()       

        self.setWindowTitle("Image Viewer")
        self.resize(800, 600)

    def criarTableView(self):
        self.tableView = QTableView(self)
        self.tableView.setGeometry(QtCore.QRect(530, -10, 271, 571))
        self.tableView.setObjectName("tableView")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(570, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Bem Vindo ao aplicativo!")

        self.coletarAmostra = QtWidgets.QPushButton(self)
        self.coletarAmostra.setGeometry(QtCore.QRect(570, 110, 191, 23))
        self.coletarAmostra.setObjectName("coletarAmostra")
        self.coletarAmostra.setText("Coletar Amostra")
        self.coletarAmostra.clicked.connect(self.coletaAmostra)

        self.processarAmostra = QtWidgets.QPushButton(self)
        self.processarAmostra.setGeometry(QtCore.QRect(570, 140, 191, 23))
        self.processarAmostra.setObjectName("processarAmostra")
        self.processarAmostra.setText("Processar Amostra")
        self.processarAmostra.clicked.connect(self.filtroCinza)

        self.relatorioAnalise = QtWidgets.QGroupBox(self)
        self.relatorioAnalise.setGeometry(QtCore.QRect(580, 210, 181, 111))
        self.relatorioAnalise.setObjectName("relatorioAnalise")
        self.relatorioAnalise.setTitle("Relátorio de Análise")

        self.radioAmonia = QtWidgets.QRadioButton(self.relatorioAnalise)
        self.radioAmonia.setGeometry(QtCore.QRect(50, 20, 82, 17))
        self.radioAmonia.setObjectName("radioAmonia")
        self.radioAmonia.setText("Amônia")              

        self.radioNitrato = QtWidgets.QRadioButton(self.relatorioAnalise)
        self.radioNitrato.setGeometry(QtCore.QRect(50, 40, 82, 17))
        self.radioNitrato.setObjectName("radioNitrato")
        self.radioNitrato.setText("Nitrato")

        self.radioNitrito = QtWidgets.QRadioButton(self.relatorioAnalise)
        self.radioNitrito.setGeometry(QtCore.QRect(50, 60, 82, 17))
        self.radioNitrito.setObjectName("radioNitrito")
        self.radioNitrito.setText("Nitrito")

        self.avaliar = QtWidgets.QPushButton(self.relatorioAnalise)
        self.avaliar.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.avaliar.setObjectName("avaliar")
        self.avaliar.setText("Avaliar")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(550, 370, 231, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.visualizarRelatorio = QtWidgets.QRadioButton(self.groupBox)
        self.visualizarRelatorio.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.visualizarRelatorio.setObjectName("visualizarRelatorio")
        self.visualizarRelatorio.setText("Visualiar relatório")

        self.enviarSMS = QtWidgets.QRadioButton(self.groupBox)
        self.enviarSMS.setGeometry(QtCore.QRect(130, 20, 82, 17))
        self.enviarSMS.setObjectName("enviarSMS")
        self.enviarSMS.setText("Enviar SMS")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")                                

        self.armazenarColeta = QtWidgets.QPushButton(self)
        self.armazenarColeta.setGeometry(QtCore.QRect(590, 480, 131, 41))
        self.armazenarColeta.setObjectName("armazenarColeta")        
        self.armazenarColeta.setText("Armazenar coleta")       
    

    def getRGB(self):
        im = Image.open("dead_parrot.jpg")
        x = 3
        y = 4

        pix = im.load()
        print (pix[x,y])

    def filtroCinza(self):
        imagemEmTonsDeCinza = cinza.filtro(self)

        imagemEmTonsDeCinza = cv2.resize(imagemEmTonsDeCinza, (500,500))
        self.data = np.array(imagemEmTonsDeCinza).reshape(500,500).astype(np.int32)
        qimage = QtGui.QImage(self.data, self.data.shape[0], self.data.shape[1], QtGui.QImage.Format_RGB32)


        self.imageLabel.setPixmap(QPixmap.fromImage(qimage))
        self.scaleFactor = 1.0 

        self.scrollArea.setVisible(True)
        #self.fitToWindowAct.setEnabled(True)
        #self.updateActions()

        #print(type(qimage))
        #print(type(imagemEmTonsDeCinza))

    def coletaAmostra(self):
        coletarAmostra.coleta(self)

    def open(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        print (fileName)
        if fileName:
            image = QImage(fileName)
            #print(type(image))
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollArea.setVisible(True)
            self.printAct.setEnabled(True)
            #self.fitToWindowAct.setEnabled(True)
            self.updateActions()
            
            #if not self.fitToWindowAct.isChecked():
            #    self.imageLabel.adjustSize()

    def print_(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O", triggered=self.open)
        self.printAct = QAction("&Print...", self, shortcut="Ctrl+P", enabled=False, triggered=self.print_)
        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)
        self.zoomInAct = QAction("Zoom &In (25%)", self, shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
        self.zoomOutAct = QAction("Zoom &Out (25%)", self, shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)
        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+S", enabled=False, triggered=self.normalSize)
        self.fitToWindowAct = QAction("&Fit to Window", self, enabled=False, checkable=True, shortcut="Ctrl+F",
                                      triggered=self.fitToWindow)
        self.filtroCinza = QAction("&Cinza", self, triggered=self.filtroCinza)

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)
        
        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    imageViewer = QImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())
