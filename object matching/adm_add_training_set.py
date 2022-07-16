import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QFileDialog
from connection import conn

# import  admin_home as ad

import cv2

class add_trainset(QWidget) :
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
        self.l0=QLabel("<b><i>ADD TRAINING SET</i></b>",self)
        self.l0.move(325,100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.l1=QLabel("Name",self)
        self.l1.move(315,420)
        self.l1.setStyleSheet("color:#67AB1E")
        self.e1 = QLineEdit(" ",self)
        self.e1.move(380,420)

        self.l2 = QLabel("Details",self)
        self.l2.move(315, 470)
        self.l2.setStyleSheet("color:#67AB1E")
        self.e2 = QLineEdit(" ",self)
        self.e2.move(380, 470)

        self.l3 = QLabel("File",self)
        self.l3.move(315, 150)
        self.l3.setStyleSheet("color:#67AB1E")
        self.b1 = QPushButton("BROWSE", self)
        self.b1.move(360, 150)
        self.b1.clicked.connect(self.brwse)
        self.b1.setFixedWidth(150)
        self.b1.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b2 = QPushButton("CROP", self)
        self.b2.move(540, 150)
        self.b2.clicked.connect(self.abc)
        self.b2.setFixedWidth(150)
        self.b2.setStyleSheet("background-color:#CE4B0E; color:#000000")
        self.l4=QLabel("",self)
        self.l4.setGeometry(360,190,150,150)
        self.l4.setStyleSheet("background-color:#ffffff")
        self.loi = QLabel("ORIGINAL IMAGE", self)
        self.loi.move(380, 345)
        self.loi.setStyleSheet("color:#ffffff;font-size:14px;")
        self.l5 = QLabel("", self)
        self.l5.setGeometry(540, 190, 150, 150)
        self.l5.setStyleSheet("background-color:#ffffff")
        self.lci = QLabel("CROPPED IMAGE", self)
        self.lci.move(560, 345)
        self.lci.setStyleSheet("color:#ffffff;font-size:14px;")

        self.b2 = QPushButton("REGISTER", self)
        self.b2.move(350, 525)
        self.b2.clicked.connect(self.add_train)
        self.b2.setFixedWidth(200)
        self.b2.setStyleSheet("background-color:#CE4B0E; color:#000000")
        self.aaa=""
        self.ppath=""
        self.show()

    def brwse(self):
        print("kkk")
        df = QFileDialog.getOpenFileName(self, "file", "/", "")
        dff=str(df).strip("(").split(",")
        print(dff[0])
        pp=str(dff[0].strip("'"))
        print("pp=",pp)
        print("t",type(pp))
        print("kkkk")
        self.img = QImage(pp)
        print("msd")

        self.p = QPixmap(self.img)
        print("k2")
        self.px=self.p.scaled(150,150)
        self.l4.setPixmap(self.px)
        print("ii")

        self.pq=QPixmap(self.img)
        self.pq.save("im.jpg")

        self.aaa=self.pq


    def add_train(self):
        self.nm=self.e1.text()
        self.dt=self.e2.text()
        c=conn()
        image = cv2.imread("cropped.jpg")
        qry = "select max(tr_set_id) from training_set"
        c = conn()
        r = c.mid(qry)
        #self.aaa.save("D:\\object matching\\training_set\\"+str(r)+".jpg")

        self.pth = str(r) + ".jpg"
        query="insert into training_set(name,details,file) values('"+self.nm+"','"+self.dt+"','"+self.pth+"')"
        c.nonreturn(query)
        # self.ks = ad.Example()
        self.hide()

    def abc(self):

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
                #chk
                qry="select max(tr_set_id) from training_set"
                c=conn()
                r=c.mid(qry)
                self.ppath="D:\\object matching\\training_set\\"+str(r)+".jpg"
                #ovr

                crop(images, (int(ar[0]), int(ar[1]), int(ar2[0]), int(ar2[1])), self.ppath)

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

        self.img = QImage(self.ppath)
        self.p = QPixmap(self.img)
        self.px = self.p.scaled(150, 150)
        self.l5.setPixmap(self.px)

        print("ovr")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_trainset()
    sys.exit(app.exec_())
