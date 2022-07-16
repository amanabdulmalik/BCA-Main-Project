import sys
import smtplib
from connection import conn
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QTextEdit
import random
from PyQt5.QtWidgets import QMessageBox

import ofr_view_crime as pg




class ofr_ed_cr(QWidget) :
    def __init__(self,output):

        super().__init__()
        self.id22=str(output)
        print("id=",self.id22)

        qq="select * from crime where c_id='"+self.id22+"'"
        c = conn()
        self.r = c.selectone(qq)

        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(400, 90, 600, 525)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(600, 525))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.setWindowTitle("OBJECT MATCHING")

        self.l0 = QLabel("<b><i>EDIT DETAILS</i></b>", self)
        self.l0.move(250, 50)
        self.l0.setStyleSheet("color:#000000; font-size: 20px;")
        self.setStyleSheet("font-size:20px;")
        self.l1=QLabel("Name",self)
        self.l1.move(150,150)
        self.l1.setStyleSheet("color:#67AB1E")
        self.e1 = QLineEdit(" ",self)
        self.e1.move(300,150)
        self.e1.setText(self.r[1])

        self.l2 = QLabel("Details",self)
        self.l2.move(150, 200)
        self.l2.setStyleSheet("color:#67AB1E")
        self.e2 = QTextEdit(" ",self)
        self.e2.move(300, 200)
        self.e2.setText(self.r[2])

        self.l5 = QPushButton("Update", self)
        self.l5.move(200, 450)
        self.l5.clicked.connect(self.updt_cr)
        self.l5.setFixedWidth(130)
        self.l5.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.l6 = QPushButton("Delete", self)
        self.l6.move(350, 450)
        self.l6.clicked.connect(self.del_cr)
        self.l6.setFixedWidth(130)
        self.l6.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.import_db()
        self.show()

    def import_db(self):
        import sequence29_db_connect
        self.connect, self.cursor = sequence29_db_connect.connection()

    def del_cr(self):
        print("jjs")
        c = conn()
        query = "delete from  crime where c_id='" + self.id22 + "'"
        c.nonreturn(query)
        self.aks=pg.ofr_view_cr()
        self.hide()

    def updt_cr(self):
        print("ms")
        self.name=self.e1.text()
        self.det=self.e2.toPlainText()
        print(self.name)
        print(self.det)
        c=conn()
        query = "update crime set crime_name='"+self.name+"',details='"+self.det+"' where  c_id='"+self.id22+"'"
        print(query)
        c.nonreturn(query)
        self.aks2 = pg.ofr_view_cr()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ofr_ed_cr()
    sys.exit(app.exec_())
