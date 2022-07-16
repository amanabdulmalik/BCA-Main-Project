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

#import ci_home as pg99



from flask import session,Flask
app=Flask(__name__)
app.secret_key="hi"




# from ofr_crime_sean_add import add_cr_scene


class add_cr_scene_obj(QWidget) :
    def __init__(self,output=1,output2=2):
        super().__init__()
        print("hell")
        self.scn1 = str(output)
        self.crim2 = str(output2)

        self.showui()

    def showui(self):
        QWidget.__init__(self)
        print("ms")

        print("self22")
        print(self.scn1)
        print(self.crim2)

        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")
        self.setStyleSheet("font-size:20px;")
        self.l0 = QLabel("<b><i>ADD CRIME OBJECTS</i></b>", self)
        self.l0.move(325, 75)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.cr_id=""
        self.aaa=""
        self.pt=""
        self.pt1=""
        self.va1=""
        self.va2 = ""
        self.va3 = ""
        self.va4 = ""


        # self.lmain = QLabel("", self)  #main image
        # self.lmain.setGeometry(80, 130, 500, 400)
        # self.lmain.setStyleSheet('background-color:#ffffff;')
        # self.img = QImage("D:\object matching\cri\aa.jpg")
        # self.p = QPixmap(self.img)
        # # self.px = self.p.scaled(250, 250)
        # self.lmain.setPixmap(self.p)

        self.lname = QLabel("Name", self)
        self.lname.move(75, 550)
        self.lname.setStyleSheet("color:#67AB1E")

        self.ed=QLineEdit("",self)
        self.ed.move(155,550)

        # self.b_crop = QPushButton("crop", self)
        # self.b_crop.move(675, 325)
        # # self.b_crop.clicked.connect(self.brwse)
        #
        #
        self.l4 = QLabel("", self)
        self.l4.setGeometry(450, 250, 250, 250)
        self.l4.setStyleSheet('background-color:#ffffff;')


        self.b2 = QPushButton("Save", self)
        self.b2.move(425, 550)
        self.b2.clicked.connect(self.add_crime_scene)
        self.b2.setFixedWidth(130)
        self.b2.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b3 = QPushButton("Crop", self)
        self.b3.move(590, 550)
        self.b3.clicked.connect(self.abc)
        self.b3.setFixedWidth(130)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.b9 = QPushButton("Finish", self)
        self.b9.move(750, 550)
        self.b9.clicked.connect(self.ad)
        self.b9.setFixedWidth(130)
        self.b9.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.show()

    def brwse(self):
        df = QFileDialog.getOpenFileName(self, "file", "/", "")
        dff=str(df).strip("(").split(",")
        print(dff[0])
        pp=str(dff[0]).strip("'")
        self.img = QImage(pp)
        print("msd")
        self.p = QPixmap(self.img)
        print("k2")
        self.px = self.p.scaled(150, 150)
        self.l4.setPixmap(self.px)
        self.aaa = self.px
        print(pp)

    def ad(self):
        print("ak")
        QMessageBox.about(self, "Title", "Success")



    def handleActivated(self, index):
        print(self.e1.itemText(index))
        print(self.e1.itemData(index))
        self.cr_id=self.e1.itemData(index)


    def add_crime_scene(self):
        # self.name=self.e1.text()
        c = conn()
        query = "insert into scene_object(cr_id,scn_id,name,details,st_pos_x,st_pos_y,end_pos_x,end_pos_y,path) values('"+self.crim2+"','"+self.scn1+"','"+self.ed.text()+"','detlis','"+str(self.va1)+"','"+str(self.va2)+"','"+str(self.va3)+"','"+str(self.va4)+"','"+self.pt1+"')"
        print(query)
        c.nonreturn(query)

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

            self.mm=self.crim2+"#"+self.scn1+"#"+self.ed.text()+".jpg"
            self.pt="D:\\object matching\\crime_sen_obj\\"+self.mm
            self.pt1=self.mm
            cropped_image.save(self.pt)
            cropped_image.save("D:\\crm\\static\\crime_sen_obj\\" + self.mm)

            self.img = QImage(self.pt)
            self.p = QPixmap(self.img)
            self.px = self.p.scaled(250, 250)
            self.l4.setPixmap(self.px)
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
    ex = add_cr_scene_obj()
    sys.exit(app.exec_())