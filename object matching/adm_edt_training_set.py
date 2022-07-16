import sys
import smtplib
from connection import conn
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QTextEdit, QFileDialog
import random
from PyQt5.QtWidgets import QMessageBox

import adm_view_training_set as pg
import cv2



class adm_edt_tr(QWidget) :
    def __init__(self,output):

        super().__init__()
        self.id22=str(output)
        print("id=",self.id22)

        qq="select * from training_set where tr_set_id='"+self.id22+"'"
        c = conn()
        self.r=c.selectone(qq)
        print(self.r)
        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.aaa=""
        self.setGeometry(400, 80, 600, 575)
        self.setStyleSheet("font-size:20px;")
        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(600, 575))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")
        self.setStyleSheet("font-size:20px;")

        self.l0 = QLabel("<b><i>EDIT TRAINING SET</i></b>", self)
        self.l0.move(250, 30)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.l1 = QLabel("Name", self)
        self.l1.move(160, 305)
        self.l1.setStyleSheet("color:#67AB1E")
        self.e1 = QLineEdit(" ", self)
        self.e1.move(240, 305)
        self.e1.setText(self.r[1])

        self.l2 = QLabel("Details", self)
        self.l2.move(160, 355)
        self.l2.setStyleSheet("color:#67AB1E")
        self.e2 = QTextEdit(" ", self)
        self.e2.setGeometry(240, 355,200,150)
        self.e2.setText(self.r[2])

        self.l3 = QLabel("File", self)
        self.l3.move(160, 95)
        self.l3.setStyleSheet("color:#67AB1E")
        self.b1 = QPushButton("BROWSE", self)
        self.b1.move(215, 95)
        self.b1.clicked.connect(self.brwse)
        self.b1.setFixedWidth(150)
        self.b1.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b2 = QPushButton("CROP", self)
        self.b2.move(395, 95)
        self.b2.clicked.connect(self.abc)
        self.b2.setFixedWidth(150)
        self.b2.setStyleSheet("background-color:#CE4B0E; color:#000000")
        self.lci = QLabel("", self)
        self.lci.setGeometry(395, 135, 150, 150)

        self.l4 = QLabel("", self)
        self.l4.setGeometry(215, 135, 150, 150)
        self.l4.setStyleSheet("background-color:white")
        path = "D:\\object matching\\training_set\\" + self.r[3]
        print(path)
        self.img = QImage(path)
        self.p = QPixmap(self.img)
        self.px = self.p.scaled(150, 150)
        self.l4.setPixmap(self.px)
        print("k2")


        self.l5 = QPushButton("Update", self)
        self.l5.move(200, 520)
        self.l5.clicked.connect(self.updt_cr)
        self.l5.setFixedWidth(120)
        self.l5.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.l6 = QPushButton("Delete", self)
        self.l6.move(350, 520)
        self.l6.clicked.connect(self.del_tr)
        self.l6.setFixedWidth(120)
        self.l6.setStyleSheet("background-color:#CE4B0E; color:#000000")
        self.ppath=""
        self.import_db()
        self.show()

    def import_db(self):
        import sequence29_db_connect
        self.connect, self.cursor = sequence29_db_connect.connection()

    def del_tr(self):
        print("jjs")
        c = conn()
        query = "delete from  training_set where tr_set_id='" + self.id22 + "'"
        c.nonreturn(query)
        self.aks=pg.adm_view_tr()
        self.hide()

    def updt_cr(self):
        print("AAA====",self.aaa)
        self.name = self.e1.text()
        self.det = self.e2.toPlainText()
        c = conn()
        if self.aaa=="":
            query = "update training_set set name='"+self.name+"',details='"+self.det+"' where tr_set_id='"+self.id22+"'"
        else:
            # self.px.save("D:\\object matching\\training_set\\" + str(self.id22) + ".jpg")
            self.pth = str(self.id22) + ".jpg"
            query = "update training_set set name='" + self.name + "',details='" + self.det + "',file='"+self.pth+"' where tr_set_id='" + self.id22 + "'"
        print(query)
        c.nonreturn(query)
        self.aks2 = pg.adm_view_tr()
        self.hide()

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
        self.aaa=self.px
        self.pq = QPixmap(self.img)
        self.pq.save("im.jpg")

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

                self.ppath="D:\\object matching\\training_set\\"+str(self.id22)+".jpg"
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
        self.lci.setPixmap(self.px)

        print("ovr")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = adm_edt_tr()
    sys.exit(app.exec_())