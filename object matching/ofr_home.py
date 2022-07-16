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

import ofr_add_crim as pg1
import ofr_crime_sean_add as pg2

import ofr_chk_obj_first_pg as pg3
import ofr_view_crime as pg4
import ofr_displce_fir as pg5
import new_crime_sen_mathing as pg77
import adm_matchin_his as pg44

import ofr_add_crim as pg555
import ofr_crime_sean_add as pg666
import ofr_view_crime as pg667
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

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

        # viewStatAct = QAction('Tools identification', self)
        # viewStatAct.setStatusTip('Tools identification')
        # viewStatAct.setChecked(True)
        # viewStatAct.triggered.connect(self.mm2)
        #
        # viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Check missing object', self)
        viewStatAct.setStatusTip('Check missing object')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm3)
        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('crime scene matching', self)
        viewStatAct.setStatusTip('crime scene matching')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm4)
        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Add Crime', self)
        viewStatAct.setStatusTip('Add Crime')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mr1)

        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Add Crime seane', self)
        viewStatAct.setStatusTip('Vie22')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mr2)

        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('View crime', self)
        viewStatAct.setStatusTip('View crime')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mr3)
        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Exit', self)
        viewStatAct.setStatusTip('Exit')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm55)
        viewMenu.addAction(viewStatAct)
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    def mm(self):
        print("mm")
        self.k=pg1.add_crime()
        #self.hide()

    def mm2(self):
        print("mm")
        self.k = pg44.add_cr_scene()
        #self.hide()

    def mm3(self):
        print("mm")
        self.k = pg3.add_cr_scene()
        #self.hide()

    def mm4(self):
        print("mm4")
        self.k = pg77.add_cr_scene()
        #self.hide()

    def mr1(self):
        self.k = pg555.add_crime()

    def mr2(self):
        self.k = pg666.add_cr_scene()

    def mr3(self):
        self.k = pg667.ofr_view_cr()


    def mm55(self):
        print("mm")
        self.close()

    def mm5(self):
        print("mm")
        self.k = pg5.add_cr_scene()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())