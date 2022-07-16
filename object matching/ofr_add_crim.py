import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTextEdit
from connection import conn
from PyQt5.QtWidgets import QMessageBox

import ofr_home as pg




class add_crime(QWidget) :
    def __init__(self):

        super().__init__()
        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.setStyleSheet("font-size: 20px;")

        self.setWindowTitle("OBJECT MATCHING")

        self.l0=QLabel("<b><i>ADD CRIME</i></b>",self)
        self.l0.move(350,100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.l1=QLabel("Name",self)
        self.l1.move(315,200)
        self.l1.setStyleSheet("color:#67AB1E")
        self.l2 = QLineEdit(" ", self)
        self.l2.move(380,200)

        self.l3 = QLabel("Details", self)
        self.l3.move(315,250)
        self.l3.setStyleSheet("color:#67AB1E")
        self.l4 = QTextEdit("", self)
        self.l4.move(380,250)


        # self.l4.setEchoMode(QLineEdit.Password)
        self.l5 = QPushButton("save", self)
        self.l5.move(375, 500)
        self.l5.clicked.connect(self.login)
        self.l5.setFixedWidth(150)
        self.l5.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.import_db()
        self.show()

    def import_db(self):
        import sequence29_db_connect
        self.connect, self.cursor = sequence29_db_connect.connection()



    def login(self):
        self.nm=self.l2.text()
        self.dt=self.l4.toPlainText()
        query="insert into crime(crime_name,details) values('"+self.nm+"','"+self.dt+"')"
        c=conn()
        c.nonreturn(query)
        self.kk = pg.Example()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_crime()
    sys.exit(app.exec_())
