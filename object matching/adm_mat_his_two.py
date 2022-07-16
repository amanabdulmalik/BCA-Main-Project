import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QFileDialog,QComboBox
from connection import conn
from PyQt5.QtWidgets import QMessageBox
# from ofr_add_crime_objs import add_cr_scene_obj
import admin_home as pg

class add_cr_scene(QWidget) :
    def __init__(self,output):

        super().__init__()
        print("hai")
        self.am=str(output)
        print(self.am)
        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 1000, 1000)

        oImage = QImage("reg.jpg")
        sImage = oImage.scaled(QSize(800, 800))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setStyleSheet("color: grey; font-size: 20px; ")
        self.setWindowTitle("Login_form")
        self.setGeometry(0, 0, 1000,1000)
        self.l0=QLabel("CRIME SCENE",self)
        self.l0.move(300,50)

        self.cr_id=""
        self.aaa=""
        self.pp=""
        self.scen_id=""

        self.aa3=""
        self.aa4 = ""






        self.l2 = QLabel("Scene number", self)
        self.l2.move(150,200)
        self.e2 = QLineEdit("", self)
        self.e2.move(300,200)

        self.l3 = QLabel("Details", self)
        self.l3.move(150, 250)
        self.e3 = QLineEdit("", self)
        self.e3.move(300, 250)

        self.l4 = QLabel("Date", self)
        self.l4.move(150, 300)
        self.e4 = QLineEdit("", self)
        self.e4.move(300, 300)

        self.l5 = QLabel("Time", self)
        self.l5.move(150, 350)
        self.e5 = QLineEdit("", self)
        self.e5.move(300, 350)

        self.l1 = QLabel("Crime Name", self)
        self.l1.move(150, 400)

        self.e1 = QLineEdit(self)
        self.e1.move(300, 400)


        self.b3 = QPushButton("Back", self)
        self.b3.move(700, 500)
        self.b3.clicked.connect(self.ad)

        self.l4 = QLabel("", self)
        self.l4.setGeometry(300, 440, 150, 150)
        self.bb1()


        self.show()

    def bb1(self):
        c=conn()
        qry="select crime.crime_name,crime_scene.scene_no,crime_scene.scene_details,crime_scene.scene_date,crime_scene.scene_time,crime_scene.scene_file from crime_scene,crime where cr_scene_id='"+self.am+"'"
        print(qry)
        ss=c.selectone(qry)
        print(ss)
        self.e1.setText(ss[0])
        self.e2.setText(ss[1])
        self.e3.setText(ss[2])
        self.e4.setText(ss[3])
        self.e5.setText(ss[4])
        pt = "D:\\object matching\\crime_scene\\" + ss[5]
        print(pt)

        self.img = QImage(pt)

        print("jjj")
        print(self.img)

        self.p = QPixmap(self.img)
        print("k2")
        self.px = self.p.scaled(150, 150)
        self.l4.setPixmap(self.px)





    def ad(self):
        print("ak")
        self.aa3=3
        print(type(self.aa3))
        self.ak = pg.Example()
        self.hide()
        # self.ak.show()
        # self.mms = self.hide()



    # def add_crime_scene(self):
    #     # self.name=self.e1.text()
    #     self.sceneno=self.e2.text()
    #     self.det=self.e3.text()
    #     self.dat=self.e4.text()
    #     self.time=self.e5.text()
    #     c = conn()
    #
    #     qry = "select max(cr_scene_id) from crime_scene"
    #     c = conn()
    #     r = c.mid(qry)
    #     self.px.save("D:\\object matching\\crime_scene\\" + str(r) + ".jpg")
    #     self.px.save("D:\\object matching\\cri\\aa.jpg")
    #
    #     self.pth = "/static/crime_scene/" + str(r) + ".jpg"
    #     query = "insert into crime_scene(cr_id,scene_no,scene_details,scene_date,scene_time,scene_file) values('"+str(self.cr_id)+"','"+self.sceneno+"','"+self.det+"','"+self.dat+"','"+self.time+"','"+self.pth+"')"
    #     print(query)
    #     c.nonreturn(query)
    #     print("vvv")
    #     # cr=add_cr_scene_obj()
    #     # print("kkkk")
    #     # cr.show()
    #     # self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_cr_scene()
    sys.exit(app.exec_())
