from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Constants import *


class Life(QLabel):
    def __init__(self, i, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/heart/heart.png"))
        self.setGeometry(self.calculate_start_position_x(i), self.calculate_start_position_y(), self.pixmap().width(),
                         self.pixmap().height())

    def calculate_start_position_x(self, x) -> float:
        return SCREEN_WIDTH - 1240 - (x * 50) - self.pixmap().width()

    def calculate_start_position_y(self) -> float:
        return SCREEN_HEIGHT - 844 - self.pixmap().height() - 5
