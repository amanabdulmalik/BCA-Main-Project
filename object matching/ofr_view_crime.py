import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTableWidget,QPushButton,QComboBox,QTableWidgetItem,QGridLayout,QLineEdit,QPushButton,QTextEdit,QRadioButton
from PyQt5 import QtWidgets
from connection import conn
import ofr_edit_crime as pg




class ofr_view_cr(QWidget) :
    def __init__(self):

        super().__init__()
        self.showui()

    def cellClick(self,row, col):

        print("Click on " + str(row) + " " + str(col))
        print(self.km)
        print("ID=====",self.km[row][2])
        self.aks=pg.ofr_ed_cr(int(self.km[row][2]))


    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)

        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setWindowTitle("OBJECT MATCHING")

        self.l0 = QLabel("<b><i>VIEW CRIME</i></b>", self)
        self.l0.move(350, 100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.l1 = QLabel("Search", self)
        self.l1.move(170, 200)
        self.l1.setStyleSheet("color:#67AB1E")
        self.l2 = QLineEdit(" ", self)
        self.l2.move(250, 200)

        self.l66 = QPushButton("search", self)
        self.l66.move(460, 200)
        self.l66.clicked.connect(self.se)
        self.l66.setFixedWidth(200)
        self.l66.setStyleSheet("background-color:#CE4B0E; color:#000000")

        self.setStyleSheet("color: grey; font-size: 20px; ")

        self.cr_id=""
        self.aaa=""

        ##




        ##



        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(230,250,300,200)
        # self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)

        self.t1 = QTableWidget(self)

        self.t1.cellClicked.connect(self.cellClick)

        self.t1.setColumnCount(2)

        self.t1.setGeometry(100, 250, 650, 300)
        self.t1.setHorizontalHeaderLabels(["Crime Name","Details"])

        c = conn()
        print("pp")
        query = "select crime_name,details,c_id from crime"
        print(query)
        self.km=c.selectall(query)
        r = c.selectall(query)
        print(r)
        l1 = len(r)
        self.t1.setRowCount(l1)
        for i in range(0, l1):
            print("mri")
            l2 = len(r[i])

            print("i2=",l2)
            print("r[i]=",r[i])
            row = r[i]
            for j in range(0, l2):
                print("j==",j)
                self.t1.setItem(i,j,QTableWidgetItem(str(row[j])))
                print(row[j])
        self.t1.resizeColumnsToContents()
        grid_layout.addWidget(self.t1, 0, 0)
        self.show()

    def se(self):
        c=conn()
        query="select crime_name,details,c_id from crime where crime_name like '%"+self.l2.text()+"%'"
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
                print(row[j])
                # print(self.t1.setItem(i,j-1,QTableWidgetItem(row[j])))
        self.t1.resizeColumnsToContents()
        #grid_layout.addWidget(self.t1, 0, 0)

        print("kk")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ofr_view_cr()
    sys.exit(app.exec_())