from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Constants import *


class Life(QLabel):
    def __init__(self, i, parent, player):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/heart/heart.png"))
        if player == 1:
            self.setGeometry(self.calculate_start_position_x(i), self.calculate_start_position_y(),
                             self.pixmap().width(),
                             self.pixmap().height())
        elif player == 2:
            self.setGeometry(SCREEN_WIDTH - self.pixmap().width() - self.calculate_start_position_x(i),
                             self.calculate_start_position_y(),
                             self.pixmap().width(),
                             self.pixmap().height())
        self.show()

    def calculate_start_position_x(self, x) -> int:
        return SCREEN_WIDTH - 1240 - (x * 50) - self.pixmap().width()

    def calculate_start_position_y(self) -> int:
        return SCREEN_HEIGHT - 844 - self.pixmap().height() - 5
