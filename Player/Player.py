from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from Constants import *


class Player(QLabel):
    def __init__(self, parent, lives=3):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/ship/ship.png"))
        self.setGeometry((SCREEN_WIDTH - self.pixmap().width()) / 2, SCREEN_HEIGHT - self.pixmap().height(),
                         self.pixmap().width(), self.pixmap().height())
        # self.setStyleSheet("border: 1px solid white;")
        self.show()
        self.life = lives

    def game_update(self, keys_pressed):
        dx = self.x()
        if Qt.Key_Left in keys_pressed and self.x() - PLAYER_SPEED > 0:
            dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed and self.x() + PLAYER_SPEED < SCREEN_WIDTH - self.pixmap().width():
            dx += PLAYER_SPEED
        self.setGeometry(dx, self.y(), self.width(), self.height())

    def check_if_player_is_hit(self, bullet) -> bool:
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
            self.life -= 1
            return True
        return False
