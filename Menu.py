from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLabel
from PyQt5.QtCore import Qt

import sys

from PyQt5.uic.properties import QtWidgets, QtCore, QtGui


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Space invaders")
        self.setGeometry(0, 0, 1400, 900)
        self.ui_components()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ui_components(self):

        head = QLabel("Space invaders", self)
        head.setGeometry(550, 300, 300, 60)

        # font
        font = QFont('Times', 14)
        font.setBold(True)
        font.setUnderline(True)

        head.setFont(font)

        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)



def start():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())


start()
