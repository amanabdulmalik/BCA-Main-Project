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
import ofr_add_crime_objs as pg

class add_cr_scene(QWidget) :
    def __init__(self):

        super().__init__()
        self.kk22 = 0
        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)
        self.setStyleSheet("font-size:20px;")

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")

        self.l0 = QLabel("<b><i>ADD CRIME SCENE</i></b>", self)
        self.l0.move(325, 50)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.cr_id=""
        self.aaa=""
        self.pp=""
        self.scen_id=""

        self.aa3=""
        self.aa4 = ""
        self.sceneno=""

        self.l1=QLabel("Crime Name",self)
        self.l1.move(300,100)
        self.l1.setStyleSheet("color:#67AB1E")
        qry="select * from crime"
        c=conn()
        r=c.selectall(qry)
        self.e1 = QComboBox(self)
        self.e1.move(430,100)
        for i in r:
            self.e1.addItem(i[1],i[0])
        self.e1.activated.connect(self.handleActivated)

        # self.lscene=QLabel("",self)
        # self.lscene.move(300,180)
        # self.lscene.setStyleSheet("background-color:#ffffff")

        self.l2 = QLabel("Scene number", self)
        self.l2.move(300,150)
        self.l2.setStyleSheet("color:#67AB1E")
        self.e2 = QLineEdit("", self)
        self.e2.move(430,150)

        self.l3 = QLabel("Details", self)
        self.l3.move(300, 200)
        self.l3.setStyleSheet("color:#67AB1E")
        self.e3 = QLineEdit("", self)
        self.e3.move(430, 200)

        self.l4 = QLabel("Date", self)
        self.l4.move(300, 250)
        self.l4.setStyleSheet("color:#67AB1E")
        self.e4 = QLineEdit("", self)
        self.e4.move(430, 250)

        self.l5 = QLabel("Time", self)
        self.l5.move(300, 300)
        self.l5.setStyleSheet("color:#67AB1E")
        self.e5 = QLineEdit("", self)
        self.e5.move(430, 300)
        self.l6 = QLabel("Brows", self)
        self.l6.move(300, 350)
        self.l6.setStyleSheet("color:#67AB1E")

        self.b1 = QPushButton("brows", self)
        self.b1.move(430, 350)
        self.b1.clicked.connect(self.brwse)
        self.b1.setFixedWidth(125)
        self.b1.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b3 = QPushButton("add", self)
        self.b3.move(700, 400)
        self.b3.clicked.connect(self.ad)
        self.b3.setFixedWidth(125)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.l4 = QLabel("", self)
        self.l4.setGeometry(430, 390, 150, 150)
        self.l4.setStyleSheet("background-color:#ffffff;")

        self.b2 = QPushButton("save", self)
        self.b2.move(700, 550)
        self.b2.clicked.connect(self.add_crime_scene)
        self.b2.setFixedWidth(125)
        self.b2.setStyleSheet("background-color:#CE4B0E; color:#000000")
        self.show()

    def brwse(self):
        df = QFileDialog.getOpenFileName(self, "file", "/", "")
        dff=str(df).strip("(").split(",")

        pp=str(dff[0]).strip("'")
        print("PP=",pp)
        print("tyoe  ",type(pp))
        print("ggg")
        self.img = QImage(pp)
        print("jjj")
        print("msd")
        self.p = QPixmap(self.img)
        print("k2")
        self.mr = QPixmap(self.img)

        self.px = self.mr.scaled(150, 150)
        self.l4.setPixmap(self.px)
        #self.aaa = self.px
        #print(pp)

    def handleActivated(self, index):
        print("jjj")
        print(self.e1.itemText(index))
        print(type(self.e1.itemData(index)))
        print("mm")
        self.kk22=self.e1.itemData(index)
        print("kk22=",self.kk22)
        self.cr_id=self.kk22
        # self.cr_id=self.e1.itemData(index)
        # print(self.cr)
        qry="select count(cr_id) from crime_scene where cr_id='"+str(self.kk22)+"'"
        print(qry)
        c=conn()
        r=c.mid(qry)
        print(r)
        print("mmsss")
        self.scen_id=0
        self.scen_id=str(r)
        print(type(self.scen_id))
       # self.lscene.setText(self.scen_id)
        self.aa3=self.scen_id
        self.e2.setText(self.scen_id)

    def ad(self):
        print("ak")
        self.aa3=3
        print(type(self.aa3))
        print("sen=",self.sceneno)
        print("crid=",self.cr_id)
        self.ak = pg.add_cr_scene_obj(int(self.sceneno),int(self.kk22))



    def add_crime_scene(self):
        print("mmss")
        # self.name=self.e1.text()
        self.sceneno=self.e2.text()
        self.det=self.e3.text()
        self.dat=self.e4.text()
        self.time=self.e5.text()
        c = conn()

        qry = "select max(c_id) from crime_scene"
        c = conn()
        r = c.mid(qry)

        self.cr_id=r
        print("cccc=",self.cr_id)

        self.p.save("D:\\object matching\\crime_scene\\" + str(r) + ".jpg")
        self.p.save("D:\\object matching\\im.jpg")
        self.p.save("D:\\crm\\static\\crime_scene\\" + str(r) + ".jpg")

        self.pth = str(r) + ".jpg"
        query = "insert into crime_scene(cr_id,scene_no,scene_details,scene_date,scene_time,scene_file) values('"+str(self.kk22)+"','"+self.sceneno+"','"+self.det+"','"+self.dat+"','"+self.time+"','"+self.pth+"')"
        print(query)
        c.nonreturn(query)
        print("vvv")
        # cr=add_cr_scene_obj()
        # print("kkkk")
        # cr.show()
        # self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_cr_scene()
    sys.exit(app.exec_())
