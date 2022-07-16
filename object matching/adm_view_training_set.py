import sys
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTableWidget,QPushButton,QComboBox,QTableWidgetItem,QGridLayout
from PyQt5 import QtWidgets
from connection import conn

from PyQt5.QtGui import QImage, QPalette, QBrush,QPixmap
import adm_edt_training_set as nxt_pg



class adm_view_tr(QWidget) :
    def __init__(self):

        super().__init__()
        self.showui()

    def showui(self):
        QWidget.__init__(self)
        self.setGeometry(200, 50, 900, 600)
        self.setStyleSheet("font-size:20px;")
        oImage = QImage("cr1.jpg")
        sImage = oImage.scaled(QSize(900, 600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.setWindowTitle("OBJECT MATCHING")

        self.l0=QLabel("<b><i>VIEW TRAINING SET</i></b>",self)
        self.l0.move(325,100)
        self.l0.setStyleSheet("color:red; font-size: 20px;")

        self.cr_id=""
        self.aaa=""
        self.r=[]


        central_widget = QWidget(self)  # Create a central widget
        central_widget.setGeometry(230, 150, 350, 200)
        # self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)
        self.t1 = QTableWidget(self)
        self.t1.setStyleSheet("font-size:20px;")

        self.t1.cellClicked.connect(self.cellClick)

        self.t1.setColumnCount(2)
        self.t1.setMinimumWidth(800)
        self.t1.setGeometry(100, 150, 950, 400)
        self.t1.setHorizontalHeaderLabels(["Name","Details"])
        grid_layout.addWidget(self.t1, 0, 0)

        c = conn()
        query = "select name,details,tr_set_id from training_set"
        print(query)
        self.r = c.selectall(query)
        l1 = len(self.r)
        self.t1.setRowCount(l1)
        for i in range(0, l1):
            l2 = len(self.r[i])
            row = self.r[i]
            for j in range(0, l2):
                self.t1.setItem(i, j, QTableWidgetItem(row[j]))
        self.t1.resizeColumnsToContents()

        self.show()

    def cellClick(self,row, col):
        print("Click on " + str(row) + " " + str(col))
        print(self.r)
        print("ID==",self.r[row][2])
        self.aks = nxt_pg.adm_edt_tr(int(self.r[row][2]))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = adm_view_tr()
    sys.exit(app.exec_())
