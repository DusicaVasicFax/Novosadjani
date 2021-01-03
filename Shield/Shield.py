from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Constants import *


class Shield(QLabel):
    def __init__(self, i, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/shield/test.png"))
        self.setGeometry(self.calculate_start_position_x(i), self.calculate_start_position_y(), self.pixmap().width(),
                         self.pixmap().height())
        self.setStyleSheet("border: 1px solid white;")
        self.active = True,
        self.health = 6

    def calculate_start_position_x(self, x) -> int:
        return SCREEN_WIDTH - 100 - (x * 535) - self.pixmap().width()

    def calculate_start_position_y(self) -> int:
        return SCREEN_HEIGHT - self.pixmap().height() - 70

    def check_if_shield_is_destroyed(self) -> bool:
        return self.health <= 0

    def check_if_shield_is_hit(self, bullet) -> None:
        x_coordinate_in_range = (self.x() <= bullet.x() <= self.x() + self.width()) or \
                                (self.x() <= bullet.x() + bullet.width() <= self.x() + self.width())
        y_coordinate_in_range = (self.y() <= bullet.y() <= self.y() + self.height()) or \
                                (self.y() <= bullet.y() + bullet.height() <=
                                 self.y() + self.height())

        # TODO figure out the magic number for the bullet.y() since i guess bullet.pixmap().height is not accurate
        hit = x_coordinate_in_range and y_coordinate_in_range

        if hit:
            bullet.hit()
            self.health -= 1
            if self.health == 4:
                self.setPixmap(QPixmap("images/shield/shield_108x132_cut_damage_left.png"))
            elif self.health == 2:
                self.setPixmap(QPixmap("images/shield/shield_108x132_cut_damage_both.png"))
            elif self.health <= 0:
                self.close()
