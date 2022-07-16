import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton

from PyQt5.QtWidgets import QMessageBox
from connection import conn

import  ofr_home as pg
import  ci_home as pg55
#
#
import admin_home as ah




class App11(QWidget) :
    def __init__(self):

        super().__init__()
        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("crlog.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setStyleSheet("color: grey; font-size: 20px; ")
        self.setWindowTitle("OBJECT MATCHING")
        self.l0=QLabel("LOGIN PAGE",self)
        self.l0.move(400,125)
        self.l0.setStyleSheet("color: #000000; font-size: 24px;")
        self.l1=QLabel("Email ID",self)
        self.l1.move(300,265)
        self.l1.setStyleSheet("color: #000000;")
        self.l2 = QLineEdit("", self)
        self.l2.move(390,265)
        self.l3 = QLabel("Password", self)
        self.l3.move(300,315)
        self.l3.setStyleSheet("color: #000000;")
        self.l4 = QLineEdit("", self)
        self.l4.move(390,315)
        self.l4.setEchoMode(QLineEdit.Password)
        self.l5 = QPushButton("LOGIN", self)
        self.l5.move(390, 375)
        self.l5.clicked.connect(self.login)
        self.l5.setStyleSheet("background-color:#CE4B0E; color:#000000")
        self.l5.setFixedWidth(120)

        self.import_db()
        self.show()

    def import_db(self):
        import sequence29_db_connect
        self.connect, self.cursor = sequence29_db_connect.connection()



    def login(self):
        self.a=self.l2.text()
        self.b=self.l4.text()
        print(self.a)
        print(len(self.a))
        print(self.b)
        if len(self.a) == 0 or len(self.b) == 0 :
            print("asdf")
            QMessageBox.about(self, "Error", "enter your username and password")

        else:
            print("ss")

            qry="select * from login where username='"+self.l2.text()+"' and password='"+self.l4.text()+"'"
            print(qry)
            c=conn()
            r=c.selectone(qry)
            print (r)
            if r is not None:
                # if r[3]=="admin":
                #     print("jk")
                #     self.kk=ah.Example()
                #
                #
                #     #ad.show()
                #     print("s")
                #     self.hide()
                if r[3]=="police":
                    print("jk")
                    self.kk=pg.Example()


                    #ad.show()
                    print("s")
                    self.hide()
                # if r[2]=="ci":
                #     print("jk")
                #     self.kk = pg55.Example()
                #
                #     # ad.show()
                #     print("s")
                #     self.hide()
                #






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App11()
    sys.exit(app.exec_())
