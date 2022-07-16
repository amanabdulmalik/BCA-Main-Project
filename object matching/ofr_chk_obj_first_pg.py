import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTableWidget,QPushButton,QComboBox,QTableWidgetItem,QGridLayout,QLineEdit,QPushButton,QTextEdit,QRadioButton
from PyQt5 import QtWidgets
from connection import conn


import objt_ident_fir as pg2




class add_cr_scene(QWidget) :
    def __init__(self):

        super().__init__()
        self.showui()

    def cellClick(self,row, col):

        print("Click on " + str(row) + " " + str(col))
        # print(self.km)
        # print(self.km[0][4])
        print(self.km[row][1])
        self.prk = self.km[row][1]


        qr=""
        pt = "D:\\object matching\\crime_scene\\" + self.km[row][4]
        print(pt)
        self.img22 = pt

        self.img = QImage(pt)

        print("jjj")
        print(self.img)

        self.p = QPixmap(self.img)
        print("k2")
        # self.px = self.p.scaled(150, 150)
        # self.l4.setPixmap(self.px)

        self.ms=QPixmap(self.img22)
        self.px44 = self.ms.scaled(150, 150)
        self.l4.setPixmap(self.px44)


        #self.aks=pg.office_mgt(int(self.km[0][0]))
    def ad(self):
        print("ak22")



        print(self.prk)
        print(self.img22)
        print("ysss")


        self.ak = pg2.add_cr_scene(self.prk,self.img22)
        self.hide()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")

        self.l0 = QLabel("<b><i>CHECK MISSING OBJECTS</i></b>", self)
        self.l0.move(325, 100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.prk = ""
        self.img22 = ""

        self.l4 = QLabel("", self)
        self.l4.setGeometry(300, 340, 150, 150)

        self.b3 = QPushButton("check", self)
        self.b3.move(700, 460)
        self.b3.clicked.connect(self.ad)
        self.b3.setFixedWidth(125)
        self.b3.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.l1 = QLabel("Crime Name", self)
        self.l1.move(315, 185)
        self.l1.setStyleSheet("color:#67AB1E")
        qry = "select * from crime"
        c = conn()
        r = c.selectall(qry)
        self.e1 = QComboBox(self)
        self.e1.move(430, 185)
        for i in r:
            self.e1.addItem(i[1], i[0])
        self.e1.activated.connect(self.handleActivated)

        self.setStyleSheet("color: grey; font-size: 20px; ")

        self.cr_id=""
        self.aaa=""

        ##




        ##



        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(100, 220, 650, 100)
        # self.setCentralWidget(central_widget)
        self.grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(self.grid_layout)

        self.t1 = QTableWidget(self)

        self.t1.cellClicked.connect(self.cellClick)

        self.t1.setColumnCount(5)

        self.t1.setGeometry(100, 250, 650, 100)
        self.t1.setHorizontalHeaderLabels(["Id","Scene", "Date", "Time","Path"])

        c = conn()
        # query = "select scene_no,scene_date,scene_time from crime_scene "
        # print(query)
        # self.km=c.selectall(query)
        # r = c.selectall(query)
        # l1 = len(r)
        # self.t1.setRowCount(l1)
        #
        #
        # for i in range(0, l1):
        #     l2 = len(r[i])
        #     print(l2)
        #     print(r[i])
        #     row = r[i]
        #     for j in range(0, l2):
        #         # self.t1.setItem(i, j, QTableWidgetItem(row[j]))
        #         self.t1.setItem(i,j,QTableWidgetItem(str(row[j])))
        #         print(row[j])
        #         # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
        # self.t1.resizeColumnsToContents()
        # grid_layout.addWidget(self.t1, 0, 0)
        self.show()

    def handleActivated(self, index):
        print("kj")
        print(self.e1.itemText(index))
        print(self.e1.itemData(index))

        c = conn()
        query = "select cr_id,scene_no,scene_date,scene_time,scene_file from crime_scene where cr_id='"+str(self.e1.itemData(index))+"'"
        print(query)
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
                print("kk=",row[j])
                # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
        self.t1.resizeColumnsToContents()
        self.grid_layout.addWidget(self.t1, 0, 0)

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