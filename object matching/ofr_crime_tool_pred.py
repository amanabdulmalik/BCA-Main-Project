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

class add_cr_scene(QWidget) :
    def __init__(self):

        super().__init__()
        print("jk23")


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
        self.l4 = QLabel("", self)
        self.l4.setGeometry(500, 150, 150, 150)

        self.l55 = QLabel("", self)
        self.l55.setGeometry(600, 450, 150, 150)

        self.l5 = QLabel("Name", self)
        self.l5.move(700, 600)
        self.e5 = QLineEdit("", self)
        self.e5.move(600, 600)

        self.cr_id=""
        self.aaa=""
        self.pp=""
        self.scen_id=""

        self.aa3=""
        self.aa4 = ""

        self.l6 = QLabel("Brows", self)
        self.l6.move(150, 100)

        self.b1 = QPushButton("brows", self)
        self.b1.move(300, 100)
        self.b1.clicked.connect(self.brwse)

        self.b3 = QPushButton("check", self)
        self.b3.move(400, 100)
        self.b3.clicked.connect(self.ad)


        c=conn()

        self.show()

    def cellClick(self, row, col):

        print("Click on " + str(row) + " " + str(col))
        print(self.km)

        self.prk = self.km[row][col]
        print("p=",self.prk)
       # self.e5.setText(self.km[row][1])

        c=conn()

        qr = "select name from scene_objects where scene_obj_id='"+str(self.km[row][1])+"'"

        q3=c.selectone(qr)
        self.e5.setText(q3[0])

        pt = "D:\\object matching\\crime_sen_obj\\" + self.km[row][0]
        print(pt)
        self.img22 = pt

        self.img = QImage(pt)

        print("jjj")
        print(self.img)

        self.p = QPixmap(self.img)
        print("k2")
        self.px = self.p.scaled(150, 150)
        self.l55.setPixmap(self.px)

        # self.aks=pg.office_mgt(int(self.km[0][0]))
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
        self.px = self.p.scaled(150, 150)
        self.l4.setPixmap(self.px)
        self.aaa = self.px
        self.px.save("D:\\object matching\\chk\\cc.jpg")
        print(pp)



    def ad(self):
        print("ak")
        qry=""

        import cv2
        import numpy as np


        ######
        #qq = "select path from scene_objects where scn_id='"+self.pk22+"'"
        qq="select file from training_set"
        print(qq)
        new_ary = []
        c = conn()
        self.km = c.selectall(qq)
        r = c.selectall(qq)


        if len(r) != 0:
            for ii in range(0, len(r)):
                # print(r[ii])
                aa = str(r[ii][0])
                aa1 = aa.replace("(", "")
                aa2 = aa1.replace(")", "")
                aa3 = aa2.replace("'", "")
                aa4 = aa3.replace(",", "")
                aa4 = aa4.replace("/", "\\")
                # print(aa4)

                nw_pt = "D:\\object matching\\training_set\\" + aa4
                print(nw_pt)
                original = cv2.imread(nw_pt)
                image_to_compare = cv2.imread("D:\\object matching\\chk\\cc.jpg")
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
                # print("ll")
                sift = cv2.xfeatures2d.SURF_create()
                # print("kk")
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
                # print("Keypoints 1ST Image: " + str(len(kp_1)))
                # print("Keypoints 2ND Image: " + str(len(kp_2)))
                print("GOOD Matches:", len(good_points))
                # print("How good it's the match: ", len(good_points) / number_keypoints * 100)
                print("--------------------")
                result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

                # if (len(good_points) == 0):
                #
                #     aa = str(r[ii][1])
                #     new_ary.append(aa)

                # cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
                # cv2.imwrite("feature_matching.jpg", result)
                # cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
                # cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            ###
            print("afch")
            # print(new_ary)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_cr_scene()
    sys.exit(app.exec_())
