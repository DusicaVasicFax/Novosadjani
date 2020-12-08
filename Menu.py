
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QLabel, QDesktopWidget

import sys



class Menu(QWidget) :
    def __init__(self):
        super().__init__()

        # x,y from left top corner of the screen and width and height of screen
        self.setGeometry(0, 0, 650, 400)
        self.setWindowTitle("Space invaders")
        self.initUI()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        # grid = QGridLayout()
        # self.setLayout(grid)
        #
        # names = ['.', '.', '.', '.', '.',
        #          '.', '.', '.', '.', '.',
        #          '.', '.', 'New Game', '.', '.',
        #          '.', '.', 'EXIT', '.', '.',
        #          '.', '.', '.', '.', '.']
        #
        # positions = [(i, j) for i in range(5) for j in range(5)]
        #
        # for positions,name in zip(positions,names):
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *positions)
        #
        # self.show()

        label = QLabel('New game',self)

        # print(label.geometry().width())
        # width = (self.geometry().width() / 2) - (label.geometry().width() /4)
        # height = (self.geometry().height() / 2) - (label.geometry().height() /4)
        # label.move(int(width),int(height))
        # print(width, height)

        qr = label.geometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        label.move(qr.topLeft())



def start():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())

start()