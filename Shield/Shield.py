from PyQt5.QtGui import QPixmap, QPen, QColor
from PyQt5.QtWidgets import QGraphicsPixmapItem

from Constants import *


class Shield(QGraphicsPixmapItem):
    def __init__(self, i, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("images/shield/shield_132x132.png"))
        self.setPos(self.calculate_start_position_x(i), self.calculate_start_position_y())
        self.active = True,
        self.health = 6

    def calculate_start_position_x(self, x) -> float:
        return SCREEN_WIDTH - 100 - (x * 535) - self.pixmap().width()

    def calculate_start_position_y(self) -> float:
        return SCREEN_HEIGHT - self.pixmap().height() - 70

    def check_if_shield_is_destroyed(self) -> bool:
        return self.health <= 0

    def check_if_shield_is_hit(self, x, x1, y) -> bool:
        x_coordinate_in_range = (self.x() <= x <= self.x() + self.pixmap().width() - 35) or \
                                (self.x() <= x1 <= self.x() + self.pixmap().width() - 35)
        hit = x_coordinate_in_range and self.y() <= y <= self.y() + self.pixmap().height() - 35
        if hit:
            self.health -= 1
        return hit
