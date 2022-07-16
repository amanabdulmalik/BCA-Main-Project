import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('File')

        viewStatAct = QAction('Officer add', self)
        viewStatAct.setStatusTip('Officer add')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.mm)

        viewMenu.addAction(viewStatAct)

        viewStatAct = QAction('View22', self)
        viewStatAct.setStatusTip('Vie22')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.xx)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    def mm(self):
        print("mm")
    def xx(self):
        print("xx")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())