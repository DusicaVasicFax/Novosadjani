from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Constants import *


class Shield(QLabel):
    def __init__(self, i, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/shield/shield.png"))
        self.setGeometry(self.calculate_start_position_x(i), self.calculate_start_position_y(), self.pixmap().width(),
                         self.pixmap().height())
        # self.setStyleSheet("border: 1px solid white;")
        self.active = True,
        self.health = 6
        self.show()

    def calculate_start_position_x(self, x) -> int:
        return SCREEN_WIDTH - 80 - (x * 380) - self.pixmap().width()

    def calculate_start_position_y(self) -> int:
        return SCREEN_HEIGHT - self.pixmap().height() - 100

    def check_if_shield_is_destroyed(self) -> bool:
        if self.health == 4:
            self.setPixmap(QPixmap("images/shield/shield_dmg.png"))
        elif self.health == 2:
            self.setPixmap(QPixmap("images/shield/shield_dmg_2.png"))
        elif self.health <= 0:
            self.close()
            return True
        return False

    def check_if_shield_is_hit(self, bullet) -> bool:
        x = self.x()
        x1 = self.x() + self.width()

        x_coordinate_in_range = (x <= bullet.x() <= x1) or \
                                (x <= bullet.x() + bullet.width() <= x1)

        y = self.y()
        y1 = self.y() + self.height()

        y_coordinate_in_range = (y <= bullet.y() <= y1) or \
                                (y <= bullet.y() + bullet.height() <= y1)

        hit = x_coordinate_in_range and y_coordinate_in_range

        if hit:
            bullet.hit()
            self.health -= 1
            return True
        return False
