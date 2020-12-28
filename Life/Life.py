from PyQt5.QtGui import QPixmap, QPen, QColor
from PyQt5.QtWidgets import QGraphicsPixmapItem

from Constants import *


class Life(QGraphicsPixmapItem):
    def __init__(self, i, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("images/heart/cesr.png"))
        self.setPos(self.calculate_start_position_x(i), self.calculate_start_position_y())

    def calculate_start_position_x(self, x) -> float:
        return SCREEN_WIDTH - 1240 - (x * 50) - self.pixmap().width()

    def calculate_start_position_y(self) -> float:
        return SCREEN_HEIGHT - 844 - self.pixmap().height() - 5
