import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, QGridLayout,QTableWidget, QTableWidgetItem
from connection import conn
from PyQt5.QtWidgets import QMessageBox
from ofr_add_crime_objs import add_cr_scene_obj
import ofr_add_crime_objs as pg

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
        self.setStyleSheet("font-size:20px;")
        self.l0 = QLabel("<b><i>CHECK MATCH</i></b>", self)
        self.l0.move(360, 100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.l4 = QLabel("", self)
        self.l4.setGeometry(275, 380, 150, 150)
        self.l4.setStyleSheet("background-color:white")

        self.l55 = QLabel("", self)
        self.l55.setGeometry(490, 380, 150, 150)
        self.l55.setStyleSheet("background-color:white")

        self.l5 = QLabel("Name", self)
        self.l5.move(470, 250)
        self.l5.setStyleSheet("color:#67AB1E")
        self.e5 = QLineEdit("", self)
        self.e5.move(600, 250)

        self.l57 = QLabel("Displacement", self)
        self.l57.move(470, 300)
        self.l57.setStyleSheet("color:#67AB1E")
        self.e57 = QLineEdit("", self)
        self.e57.move(600, 300)

        self.cr_id=""
        self.aaa=""
        self.pp=""
        self.scen_id=""

        self.aa3=""
        self.aa4 = ""



        self.b1 = QPushButton("brows", self)
        self.b1.move(300, 150)
        self.b1.clicked.connect(self.brwse)
        self.b1.setFixedWidth(130)
        self.b1.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b3 = QPushButton("check", self)
        self.b3.move(450, 150)
        self.b3.clicked.connect(self.ad)
        self.b3.setFixedWidth(130)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")

        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(100, 250, 300, 100)
        # self.setCentralWidget(central_widget)
        self.grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(self.grid_layout)

        self.t1 = QTableWidget(self)

        self.t1.cellClicked.connect(self.cellClick)

        self.t1.setColumnCount(1)

        self.t1.setGeometry(100, 250, 300, 100)
        self.t1.setHorizontalHeaderLabels(["id"])
        c=conn()

        self.show()

    def cellClick(self, row, col):

        print("Click on " + str(row) + " " + str(col))
        print(self.km)

        self.item = self.t1.itemAt(row, col)
        self.ID = self.item.text()
        print("p2=", self.ID)

        self.prk = self.km[row][col]

        print("p=",self.prk)
       # self.e5.setText(self.km[row][1])

        c=conn()

        qr = "select name,path,st_pos_x,st_pos_y,end_pos_x,end_pos_y from scene_object where scene_obj_id='"+str(self.ID)+"'"
        print(qr)

        q3=c.selectone(qr)
        print(q3)
        self.e5.setText(q3[0])

        pt = "D:\\object matching\\crime_sen_obj\\" + q3[1]
        print(pt)
        self.img22 = pt

        self.img = QImage(pt)

        print("jjj")
        print(self.img)

        # self.p = QPixmap(self.img)
        # print("k2")
        # self.px = self.p.scaled(150, 150)
        # self.l55.setPixmap(self.px)
        ##algor sec chek

        from PIL import Image, ImageDraw


        im = Image.open("D:\\object matching\\chk\\bb.jpg")
        im_width, im_height = im.size
        print('im.size', im.size)
        print(q3[2])
        print(q3[3])
        print(q3[4])
        print(q3[5])
        try:


            im33 = im.crop((int(q3[2]), int(q3[3]),int(q3[4]), int(q3[5])))  # (left, upper, right, lower)-tuple.

        #im33 = im.crop((20,20,30,30))  # (left, upper, right, lower)-tuple.

            im33.save("D:\\object matching\\chk\\cr55.jpg")
            print('im.size', im.size)

            #gggggg
            self.img22 = QImage("D:\\object matching\\chk\\cr55.jpg")
            self.px33 = QPixmap(self.img)
            self.px33 = self.px33.scaled(150, 150)
            self.l55.setPixmap(self.px33)

            #chk crop with new crop

            print("crop2 check......................")

            import cv2
            import numpy as np
            original = cv2.imread(pt)
            image_to_compare = cv2.imread("D:\\object matching\\chk\\cr55.jpg")
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
            sift = cv2.xfeatures2d.SURF_create()
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
            result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
            #cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
            cv2.imwrite("feature_matching.jpg", result)
            # cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
            # cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            if len(good_points)>=10:
                print("mmmss")
                self.e57.setText("same position")
            else:
                self.e57.setText("position different")


            #

        except:
            print("wrong img size")




        ##ovr


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
        self.px = QPixmap(self.img)
        print("k2")
        # self.px = self.p.scaled(150, 150)
        # self.l4.setPixmap(self.px)
        # self.aaa = self.px
        self.px.save("D:\\object matching\\chk\\bb.jpg")
        print(pp)

        self.img22 = QImage(pp)
        self.px33=QPixmap(self.img)
        self.px33 = self.px33.scaled(150, 150)
        self.l4.setPixmap(self.px33)




    def ad(self):
        print("ak")
        qry=""

        import cv2
        import numpy as np


        ######
        #qq = "select path from scene_objects where scn_id='"+self.pk22+"'"
        qq="select scene_object.path,scene_object.scene_obj_id from scene_object,crime_scene where crime_scene.cr_id=scene_object.cr_id and crime_scene.scene_no=scene_object.scn_id and crime_scene.cr_id='"+self.pk22+"'"
        print(qq)
        new_ary = []
        c = conn()
        self.km = c.selectall(qq)
        r = c.selectall(qq)
        print(r)


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
                sift = cv2.xfeatures2d.SURF_create()
                print("kk")
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

                if (len(good_points) != 0):

                    aa = str(r[ii][1])
                    new_ary.append(aa)

                # cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
                # cv2.imwrite("feature_matching.jpg", result)
                # cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
                # cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            ###
            print("afch")
            print(new_ary)

            r1 = new_ary
            l1 = len(r1)
            self.t1.setRowCount(l1)

            for i in range(0, l1):
                l2 = len(r1[i])
                print(l2)
                print("row [i=",r1[i])
                row = r[i]
                self.t1.setItem(i,0,QTableWidgetItem(str(r1[i])))
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
