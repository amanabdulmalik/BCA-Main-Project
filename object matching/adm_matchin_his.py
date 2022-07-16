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
# from ofr_add_crime_objs import add_cr_scene_obj
import adm_mat_his_two as pg


class add_cr_scene(QWidget) :
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

        self.setWindowTitle("OBJECT MATCHING")
        self.setStyleSheet("font-size:20px;")
        self.l0 = QLabel("<b><i>CHECK MATCH</i></b>", self)
        self.l0.move(350, 130)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.cr_id=""
        self.aaa=""
        self.pp=""
        self.scen_id=""

        self.aa3=""
        self.aa4 = ""


        self.b1 = QPushButton("BROWSE", self)
        self.b1.move(260, 210)
        self.b1.clicked.connect(self.brwse)
        self.b1.setFixedWidth(130)
        self.b1.setStyleSheet("background-color:#CE4B0E; color:#000000")


        self.l4 = QLabel("", self)
        self.l4.setGeometry(320, 270, 150, 150)
        self.l4.setStyleSheet("background-color:white")

        self.b3 = QPushButton("CHECK", self)
        self.b3.move(430, 210)
        self.b3.clicked.connect(self.ad)
        self.b3.setFixedWidth(130)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")


        # self.b4 = QPushButton("crop", self)
        # self.b4.move(380, 150)
        # self.b4.clicked.connect(self.abc)
        # self.b4.setFixedWidth(130)
        # self.b4.setStyleSheet("background-color:#CE4B0E; color:#000000")


        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(230, 350, 160, 100)
        # self.setCentralWidget(central_widget)
        # self.grid_layout = QGridLayout(self)  # Create QGridLayout
        # central_widget.setLayout(self.grid_layout)
        #
        # self.t1 = QTableWidget(self)
        #
        # self.t1.cellClicked.connect(self.cellClick)
        #
        # self.t1.setColumnCount(1)
        #
        # self.t1.setGeometry(100, 250, 650, 100)
        # self.t1.setHorizontalHeaderLabels(["cr_scene_id"])

        c = conn()
        #query = "select crime_scene.cr_scene_id,crime_scene.scene_no from crime_scene,crime where crime.cr_id=crime_scene.cr_id"
        # query="select crime_scene.cr_scene_id from crime_scene,crime where crime.cr_id=crime_scene.cr_id"
        # print(query)
        # self.km = c.selectall(query)
        # r = c.selectall(query)
        # l1 = len(r)
        # self.t1.setRowCount(l1)
        #
        # for i in range(0, l1):
        #     l2 = len(r[i])
        #     print(l2)
        #     print(r[i])
        #     row = r[i]
        #     for j in range(0, l2):
        #         # self.t1.setItem(i, j, QTableWidgetItem(row[j]))
        #         self.t1.setItem(i, j, QTableWidgetItem(str(row[j])))
        #         print(row[j])
        #         # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
        # self.t1.resizeColumnsToContents()
        # self.grid_layout.addWidget(self.t1, 0, 0)

        self.show()

    def cellClick(self,row, col):

        print("Click on " + str(row) + " " + str(col))
        print(self.km)
        print(self.km[0][0])
        self.aks=pg.add_cr_scene(int(self.km[0][1]))
        self.hide()

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
        # self.aaa = self.px
        print(pp)
        self.p.save("im.jpg")

        self.kss=QPixmap(self.img)
        self.px22 = self.kss.scaled(150, 150)
        self.l4.setPixmap(self.px22)
        self.aaa = self.px22



    def ad(self):
        print("ak")
        import cv2
        import numpy as np



######
        qq="select tr_set_id,file from training_set"
        new_ary=[]
        c = conn()
        self.km = c.selectall(qq)
        rk = c.selectall(qq)
        print(rk)

        try:
            if len(rk) != 0:
                for ii in range(0, len(rk)):
                    print("mr")
                    print(self.km[ii][1])



                    nw_pt = "D:\\object matching\\training_set\\" + rk[ii][1]
                    print(nw_pt)
                    #nw_pt = "D:\\object matching\\training_set\\8#8#ov.jpg"
                    original = cv2.imread(nw_pt)
                    print("image_comr_fir")

                    image_to_compare = cv2.imread("im.jpg")
                    print("im_crop")
                    #print(image_to_compare)

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
                    # print("Keypoints 1ST Image: " + str(len(kp_1)))
                    # print("Keypoints 2ND Image: " + str(len(kp_2)))
                    print("GOOD Matches:", len(good_points))
                    # print("How good it's the match: ", len(good_points) / number_keypoints * 100)
                    result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)

                    if (len(good_points) >= 15):
                        aa = str(r[ii][1])
                        new_ary.append(aa)

                    print("apn")
                    print(new_ary)
                    # cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
                    # cv2.imwrite("feature_matching.jpg", result)
                    # cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
                    # cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                ###
                print("afch")
                if len(new_ary)!=0:

                    QMessageBox.about(self, "RESULT", "Image as simlar to crime tool")

                else:
                    QMessageBox.about(self, "RESULT", "Image as Not simlar to crime tool")
                # print(new_ary)
                #
                # r = new_ary
                # l1 = len(r)
                # self.t1.setRowCount(l1)
                #
                # for i in range(0, l1):
                #     l2 = len(r[i])
                #     print(l2)
                #     print(r[i])
                #     row = r[i]
                #     for j in range(0, l2):
                #         # self.t1.setItem(i, j, QTableWidgetItem(row[j]))
                #         self.t1.setItem(i, j, QTableWidgetItem(str(row[j])))
                #         print(row[j])
                #         # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
                # self.t1.resizeColumnsToContents()
                # self.grid_layout.addWidget(self.t1, 0, 0)


        except:
            print("wrong")

    def add_crime_scene(self):


        print("vvv")

    def abc(self):
        import cv2
        print("hai22")

        # initialize the list of reference points and boolean indicating
        # whether cropping is being performed or not
        ref_point = []
        cropping = False
        ###chk2
        from PIL import Image
        def crop(image_path, coords, saved_location):
            """
            @param image_path: The path to the image to edit
            @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
            @param saved_location: Path to save the cropped image
            """
            image_obj = Image.open(image_path)
            cropped_image = image_obj.crop(coords)
            cropped_image.save(saved_location)

            # self.mm=self.crim2+"#"+self.crim2+"#"+self.ed.text()+".jpg"
            # self.pt="D:\\object matching\\crime_sen_obj\\"+self.mm
            # self.pt1=self.mm
            # cropped_image.save(self.pt)

            #cropped_image.show()
         #ov

        def shape_selection(event, x, y, flags, param):
            # grab references to the global variables

            global ref_point, cropping

            # if the left mouse button was clicked, record the starting
            # (x, y) coordinates and indicate that cropping is being
            # performed
            if event == cv2.EVENT_LBUTTONDOWN:
                # print("qq")
                ref_point = [(x, y)]
                cropping = True

            # check to see if the left mouse button was released
            elif event == cv2.EVENT_LBUTTONUP:
                # print("ms")
                # record the ending (x, y) coordinates and indicate that
                # the cropping operation is finished
                ref_point.append((x, y))
                cropping = False

                # draw a rectangle around the region of interest
                cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
                images = 'im.jpg'
                print((ref_point[0]))
                aas=str(ref_point[0])
                print("aa")
                print(aas)
                bbb=aas[1:len(aas)-1]
                print(bbb)
                ar=[]
                ar=bbb.split(",")
                self.va1=ar[0]
                self.va2 = ar[1]

                aas = str(ref_point[1])
                print("aa2")
                print(aas)
                bbb = aas[1:len(aas) - 1]
                print(bbb)
                ar2 = []
                ar2 = bbb.split(",")
                self.va3 = ar2[0]
                self.va4 = ar2[1]







                #crop(images, (161, 166, 706, 1050), 'cropped.jpg')
                crop(images, (int(ar[0]), int(ar[1]), int(ar2[0]), int(ar2[1])), 'cropped.jpg')

                print("rf=",ref_point[0])
                print("rf1=", ref_point[1])
                cv2.imshow("image", image)


        # construct the argument parser and parse the arguments
        # ap = argparse.ArgumentParser()
        # ap.add_argument("-i", "--image", required=True, help="Path to the image")
        # args = vars(ap.parse_args())

        # load the image, clone it, and setup the mouse callback function
        print("ag")


        image = cv2.imread("im.jpg")
        clone = image.copy()
        cv2.namedWindow("imageq")
        cv2.setMouseCallback("imageq", shape_selection)
        # print("rel2=", len(ref_point))

        # keep looping until the 'q' key is pressed
        while True:
            # print("jk22")
            # display the image and wait for a keypress
            cv2.imshow("imageq", image)
            key = cv2.waitKey(1) & 0xFF

            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                print("bbc2")
                image = clone.copy()

            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                print("bbc")
                break

        # if there are two reference points, then crop the region of interest
        # from teh image and display it
        if len(ref_point) == 2:
            print("qqw")
            crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
            print(crop_img)
            cv2.imshow("crop_img", crop_img)
            cv2.imwrite("d://cr24.jpg", crop_img)

            cv2.waitKey(0)

        # close all open windows
        cv2.destroyAllWindows()

        print("ovr")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_cr_scene()
    sys.exit(app.exec_())
