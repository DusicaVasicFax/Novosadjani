from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from Constants import *


class Level(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.level = 1
        self.setGeometry((SCREEN_WIDTH - 80) / 2, 5, 85, 20)
        self.setFont(QFont('Times', 12))
        self.setStyleSheet("color: orange")

    def print_level(self):
        self.setText("Level " + str(self.level) + "  ")

    def level_up(self):
        self.level += 1

    def reset_level(self):
        self.level = 1
        self.print_level()
