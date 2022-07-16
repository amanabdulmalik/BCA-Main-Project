import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap


from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QFileDialog,QComboBox
from connection import conn
from PyQt5.QtWidgets import QMessageBox
import adm_matchin_his as pg4
import new_crime_sen_mathing as pg77
import adm_add_training_set as pg2
import adm_view_training_set as pg99
import ofr_displce_fir as pg39

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        print("ad")

        self.initUI()

    def initUI(self):

        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr2.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setStyleSheet("color: grey; font-size: 20px; ")
        self.setWindowTitle("OBJECT MATCHING")

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('File')

        # viewStatAct = QAction('Crime seane matching', self)
        # viewStatAct.setStatusTip('Crime seane matching')
        # viewStatAct.setChecked(True)
        # viewStatAct.triggered.connect(self.mm)
        #
        # viewMenu.addAction(viewStatAct)

        # viewStatAct = QAction('View offier', self)
        # viewStatAct.setStatusTip('Vie22')
        # viewStatAct.setChecked(True)
        # viewStatAct.triggered.connect(self.xx)
        #
        # viewMenu.addAction(viewStatAct)
        #
        viewStatAct = QAction('Crime tool add', self)
        viewStatAct.setStatusTip('Crime tool add')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm1)
        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Crime tool view', self)
        viewStatAct.setStatusTip('Crime tool view')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm4)
        viewMenu.addAction(viewStatAct)


        #
        # viewStatAct = QAction('Displacement', self)
        # viewStatAct.setStatusTip('Displacement')
        # viewStatAct.setChecked(True)
        # viewStatAct.triggered.connect(self.mm39)
        # viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Exit', self)
        viewStatAct.setStatusTip('Exit')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm2)
        viewMenu.addAction(viewStatAct)


        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    # def mm(self):
    #     print("mm")
    #     self.k = pg77.add_cr_scene()

    def xx(self):
        print("xx")
        self.ks=pg1.add_cr_scene()

    def mm1(self):
        print("mm1")
        self.k = pg2.add_trainset()

    def mm2(self):
        print("mm2")
        self.close()

    def mm3(self):
        print("mm2")
        self.k = pg4.add_cr_scene()

    def mm39(self):
        print("mm2")
        self.k = pg39.add_cr_scene()

    def mm4(self):
        print("mm2")
        self.k =pg99.adm_view_tr()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())