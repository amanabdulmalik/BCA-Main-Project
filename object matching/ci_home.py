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

        viewStatAct = QAction('Add Crime', self)
        viewStatAct.setStatusTip('Add Crime')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm)

        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Add Crime seane', self)
        viewStatAct.setStatusTip('Vie22')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm2)

        viewMenu.addAction(viewStatAct)


        viewStatAct = QAction('View crime', self)
        viewStatAct.setStatusTip('View crime')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm4)
        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('Exit', self)
        viewStatAct.setStatusTip('Exit')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm22)
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
        self.k = pg2.add_cr_scene()
        #self.hide()

    def mm22(self):
        print("mm")
        self.close()
        # self.hide()
    def mm3(self):
        print("mm")
        self.k = pg3.add_cr_scene()
        #self.hide()

    def mm4(self):
        print("mm4")
        self.k = pg4.ofr_view_cr()
        #self.hide()

    def mm5(self):
        print("mm")
        self.k = pg5.add_cr_scene()
        #self.hide()

    def mm5(self):
        print("mm")
        self.k = pg5.add_cr_scene()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())