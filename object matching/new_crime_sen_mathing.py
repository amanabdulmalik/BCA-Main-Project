import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QPushButton, QComboBox, QTableWidgetItem, \
    QGridLayout, QLineEdit, QPushButton, QTextEdit, QRadioButton, QFileDialog
from PyQt5 import QtWidgets
from connection import conn

import ofr_displce_sec as pg2




class add_cr_scene(QWidget) :
    def __init__(self):

        super().__init__()
        self.lst=[]
        self.showui()

    def cellClick(self,row, col):

        print("Click on " + str(row) + " " + str(col))
        print(self.lst)


        qr=""
        pt = "D:\\object matching\\crime_scene\\" + self.lst[row][0]
        print(pt)
        self.img22 = pt

        self.img = QImage(pt)

        print("jjj")
        print(self.img)

        self.p = QPixmap(self.img)
        print("k2")
        self.px = self.p.scaled(150, 150)
        self.l43.setPixmap(self.px)

        self.ksks=QPixmap(self.img)
        self.px33 = self.ksks.scaled(150, 150)
        self.l43.setPixmap(self.px33)




        #self.aks=pg.office_mgt(int(self.km[0][0]))
    def ad(self):
        print("ak")




        c = conn()
        query = "select crime.crime_name,scene_no,scene_date,scene_time,scene_file from crime_scene,crime where crime.c_id=crime_scene.cr_id"
        print(query)
        self.km = c.selectall(query)
        print("ttt=",type(self.km))
        r = c.selectall(query)
        print(r)
        l1 = len(r)
        print(str(l1))

        ii=0
        ik=0

        for i in range(0, l1):
            l2 = len(r[i])
            print(l2)
            print(r[i])
            row = r[i]
            print("m=", r[i][4])

            #algo
            import cv2
            nw_pt = "D:\\object matching\\crime_scene\\" + r[i][4]
            print(nw_pt)
            # nw_pt = "D:\\object matching\\training_set\\8#8#ov.jpg"
            original = cv2.imread(nw_pt)
            print("image_comr_fir")

            image_to_compare = cv2.imread("d://object matching//imgnew.jpg")
            print("im_crop")
            # print(image_to_compare)

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
            print("GOOD Matches:", len(good_points))
            # print("How good it's the match: ", len(good_points) / number_keypoints * 100)
            result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

            if (len(good_points) >= 25):
                ii=ii+1


                self.t1.setRowCount(ii)
                print(r[i])
                mr=0
                for j in range(0, l2):
                    if mr==4:
                        print("mr="+str(row[j]))
                        self.lst.append(row[j])


                    print("dasa=" + str(row[j]))
                    # self.t1.setItem(i, j, QTableWidgetItem(str(row[j])))
                    self.t1.setItem(ik, j, QTableWidgetItem(str(row[j])))

                    self.t1.resizeColumnsToContents()
                    self.grid_layout.addWidget(self.t1, 0, 0)
                    mr=mr+1
                ik=ik+1




                    # cv2.waitKey(0)
            # cv2.destroyAllWindows()


            #ovr




        # self.ak = pg2.add_cr_scene(self.prk,self.img22)
        # self.hide()

    def showui(self):
        QWidget.__init__(self)
        self.img=""
        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")
        self.setStyleSheet("font-size:20px;")
        self.l0 = QLabel("<b><i>CHECK MATCH</i></b>", self)
        self.l0.move(325, 100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.prk = ""
        self.img22 = ""

        self.l4 = QLabel("", self)
        self.l4.setGeometry(300, 380, 150, 150)
        self.l4.setStyleSheet("background-color:white")

        self.l43 = QLabel("", self)
        self.l43.setGeometry(700, 380, 150, 150)
        self.l43.setStyleSheet("background-color:white")

        self.b3 = QPushButton("check", self)
        self.b3.move(550, 425)
        self.b3.clicked.connect(self.ad)
        self.b3.setFixedWidth(130)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b32 = QPushButton("Brows", self)
        self.b32.move(550, 525)
        self.b32.clicked.connect(self.br)
        self.b32.setFixedWidth(130)
        self.b32.setStyleSheet("background-color:#CE4B0E; color:#000000")

        # self.l1 = QLabel("Crime Name", self)
        # self.l1.move(315, 200)
        # self.l1.setStyleSheet("color:#67AB1E")
        # qry = "select * from crime"
        # c = conn()
        # r = c.selectall(qry)
        # self.e1 = QComboBox(self)
        # self.e1.move(440, 200)
        # for i in r:
        #     self.e1.addItem(i[1], i[0])
        # self.e1.activated.connect(self.handleActivated)

        self.cr_id=""
        self.aaa=""

        ##




        ##



        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(100, 250, 650, 100)
        # self.setCentralWidget(central_widget)
        self.grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(self.grid_layout)

        self.t1 = QTableWidget(self)

        self.t1.cellClicked.connect(self.cellClick)

        self.t1.setColumnCount(5)

        self.t1.setGeometry(100, 250, 650, 100)
        self.t1.setHorizontalHeaderLabels(["crime","scene", "Date", "Time","Path"])

        c = conn()

        self.show()

    def handleActivated(self, index):
        print("kj")
        print(self.e1.itemText(index))
        print(self.e1.itemData(index))

    def br(self):
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
        self.mr.save("d://object matching//imgnew.jpg")

        self.px = self.mr.scaled(150, 150)
        self.l4.setPixmap(self.px)
        #self.aaa = self.px
        #print(pp)

    def se(self):
        c=conn()
        query="select * from officer where name='"+self.l2.text()+"'"
        self.km = c.selectall(query)
        r = c.selectall(query)
        l1 = len(r)
        self.t1.setRowCount(l1)

        for i in range(0, l1):
            l2 = len(r[i])
            print(l2)
            print(r[i])
            row = r[i]
            for j in range(0, l2):
                # self.t1.setItem(i, j, QTableWidgetItem(row[j]))
                self.t1.setItem(i, j, QTableWidgetItem(str(row[j])))
                print(row[j])
                # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
        self.t1.resizeColumnsToContents()
        #grid_layout.addWidget(self.t1, 0, 0)

        print("kk")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_cr_scene()
    sys.exit(app.exec_())