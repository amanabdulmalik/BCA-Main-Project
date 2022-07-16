import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, QGridLayout, \
    QTableWidget, QTableWidgetItem
from connection import conn
from PyQt5.QtWidgets import QMessageBox
# import ofr_add_crime_objs as pg

class add_cr_scene(QWidget) :
    def __init__(self,output,output2):

        super().__init__()
        print("jk23")
        self.pk22 = str(output)
        self.img22 = output2
        print(self.pk22)
        print(self.img22)


        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")

        self.l0 = QLabel("<b><i>CRIME SCENE</i></b>", self)
        self.l0.move(325, 100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")
        self.l4 = QLabel("", self)
        self.l4.setGeometry(100, 500, 150, 150)
        self.l4.setStyleSheet("bakground-color:white")
        self.setStyleSheet("font-size:20px;")
        self.l55 = QLabel("", self)
        self.l55.setGeometry(250, 500, 150, 150)
        #self.l55.move(300,300)

        self.l5 = QLabel("Name", self)
        self.l5.move(550, 250)

        self.l5.setStyleSheet("color:#67AB1E")
        self.e5 = QLineEdit("", self)
        self.e5.move(610, 250)

        self.cr_id=""
        self.aaa=""
        self.pp=""
        self.scen_id=""

        self.aa3=""
        self.aa4 = ""


        self.b1 = QPushButton("brows", self)
        self.b1.move(300, 170)
        self.b1.clicked.connect(self.brwse)
        self.b1.setFixedWidth(125)
        self.b1.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b3 = QPushButton("check", self)
        self.b3.move(450, 170)
        self.b3.clicked.connect(self.ad)
        self.b3.setFixedWidth(125)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")

        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(100, 220, 300, 100)
        # self.setCentralWidget(central_widget)
        self.grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(self.grid_layout)

        self.t1 = QTableWidget(self)

        self.t1.cellClicked.connect(self.cellClick)

        self.t1.setColumnCount(1)

        self.t1.setGeometry(100, 220, 300, 100)
        self.t1.setHorizontalHeaderLabels(["id"])
        c=conn()

        self.new_ary = []

        self.show()

    def cellClick(self, row, col):

        print("Click on " + str(row) + " " + str(col))
        print(self.km)

        self.prk =self.new_ary[row][col]
        print("p=",self.prk)
        print("ss=",self.new_ary[row][col])


       # self.e5.setText(self.km[row][1])

        c=conn()

        qr = "select name,path from scene_object where scene_obj_id='"+str(self.prk)+"'"
        print(qr)

        q3=c.selectone(qr)
        print(q3)
        print("pppppppp")
        print(q3[0])
        asdf=str(q3[1])

        self.e5.setText(q3[0])

        pt = "D:\\object matching\\crime_sen_obj\\" + asdf
        print(pt)
        self.img22 = pt

        self.img = QImage(pt)

        print("jjj")
        print(self.img)

        self.p = QPixmap(self.img)
        print("k2")
        self.px = self.p.scaled(150, 150)
        self.l55.setPixmap(self.px)


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
        # self.px = self.p.scaled(150, 150)
        # self.l4.setPixmap(self.px)
        #self.aaa = self.px
        self.p.save("D:\\object matching\\chk\\bb.jpg")
        print(pp)

        self.pm=QPixmap(self.img)
        self.px22 = self.pm.scaled(150, 150)
        self.l4.setPixmap(self.px22)




    def ad(self):
        print("ak")
        qry=""

        import cv2
        import numpy as np


        ######
        #qq = "select path from scene_objects where scn_id='"+self.pk22+"'"
        qq="select scene_object.path,scene_object.scene_obj_id from scene_object,crime_scene where crime_scene.cr_id=scene_object.cr_id and crime_scene.scene_no=scene_object.scn_id and crime_scene.scene_no='"+self.pk22+"'"
        print(qq)
        # new_ary = []
        c = conn()
        self.km = c.selectall(qq)
        r = c.selectall(qq)
        print(r)
        print("len(r)=",len(r))


        if len(r) != 0:
            for ii in range(0, len(r)):
                print("pppppp")
                aa = str(r[ii][0])
                aa1 = aa.replace("(", "")
                aa2 = aa1.replace(")", "")
                aa3 = aa2.replace("'", "")
                aa4 = aa3.replace(",", "")
                aa4 = aa4.replace("/", "\\")
                # print(aa4)

                nw_pt = "D:\\object matching\\crime_sen_obj\\" + aa4
                print(nw_pt)
                original = cv2.imread(nw_pt)
                image_to_compare = cv2.imread("D:\\object matching\\chk\\bb.jpg")
                print("zz")

                # 1) Check if 2 images are equals
                if original.shape == image_to_compare.shape:
                    print("The images have same size and channels")
                    difference = cv2.subtract(original, image_to_compare)
                    b, g, r = cv2.split(difference)
                    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                        print("The images are completely Equal")
                    else:
                        print("The images are NOT equal")
                # 2) Check for similarities between the 2 images
                print("ll")
                import cv2



                sift = cv2.xfeatures2d.SURF_create()

                print("kk")
                # print("orgi=",original)
                # print("imgcmp=",image_to_compare)
                kp_1, desc_1 = sift.detectAndCompute(original, None)
                kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
                index_params = dict(algorithm=0, trees=5)
                search_params = dict()
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                matches = flann.knnMatch(desc_1, desc_2, k=2)
                good_points = []

                for m, n in matches:
                    if m.distance < 0.6 * n.distance:
                        good_points.append(m)
                # Define how similar they are
                number_keypoints = 0
                if len(kp_1) <= len(kp_2):
                    number_keypoints = len(kp_1)
                else:
                    number_keypoints = len(kp_2)
                print("Keypoints 1ST Image: " + str(len(kp_1)))
                print("Keypoints 2ND Image: " + str(len(kp_2)))
                print("GOOD Matches:", len(good_points))
                print("How good it's the match: ", len(good_points) / number_keypoints * 100)
                print("--------------------")
                result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

                print("ln=",len(good_points))

                if (len(good_points) == 0):
                    print("hai")

                    aa = str(r[ii][1])
                    self.new_ary.append(aa)


            ###
            print("afch")
            print(self.new_ary)

            r = self.new_ary
            l1 = len(r)
            self.t1.setRowCount(l1)

            for i in range(0, l1):
                l2 = len(r[i])
                print(l2)
                print("row [i=",r[i])
                row = r[i]
                self.t1.setItem(i,0,QTableWidgetItem(str(r[i])))
                #for j in range(0, l2):
                    # self.t1.setItem(i, j, QTableWidgetItem(row[j]))
                    # self.t1.setItem(i, j, QTableWidgetItem(str(row[i])))
                    # print("row[j=",row[j])
                    # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
            self.t1.resizeColumnsToContents()
            self.grid_layout.addWidget(self.t1, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_cr_scene()
    sys.exit(app.exec_())
