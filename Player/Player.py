from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Bullet.Bullets import Bullet
from Constants import *


class Player(QLabel):
    def __init__(self, parent, player, lives=3):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/ship/ship.png"))
        if player == 1:
            self.setGeometry(10, SCREEN_HEIGHT - self.pixmap().height() - 20,
                             self.pixmap().width(), self.pixmap().height())
            self.setPixmap(QPixmap("images/ship/ship.png"))
        elif player == 2:
            self.setGeometry(SCREEN_WIDTH - self.pixmap().width() - 10, SCREEN_HEIGHT - self.pixmap().height() - 20,
                             self.pixmap().width(), self.pixmap().height())
            self.setPixmap(QPixmap("images/ship/ship2.png"))
        self.player = player

        # self.setStyleSheet("border: 1px solid white;")
        self.life = lives
        self.show()

    def game_update(self, key, bullets_length, level) -> Bullet or None:
        dx = self.x()

        if self.player == 1:
            if Qt.Key_Left == key and self.x() - PLAYER_SPEED > 0:
                dx -= PLAYER_SPEED
                self.setGeometry(dx, self.y(), self.width(), self.height())
            elif Qt.Key_Right == key and self.x() + PLAYER_SPEED < SCREEN_WIDTH - self.pixmap().width():
                dx += PLAYER_SPEED
                self.setGeometry(dx, self.y(), self.width(), self.height())
            elif Qt.Key_Space == key and bullets_length < level:
                bullet = Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y, self.parent())
                bullet.active = True
                bullet.setGeometry(int(self.x() + self.width() / 2 - bullet.width() / 2),
                                   self.y() - self.height() + bullet.offset_y,
                                   bullet.pixmap().width(), bullet.pixmap().height())
                return bullet
            return None
        elif self.player == 2:
            if Qt.Key_A == key and self.x() - PLAYER_SPEED > 0:
                dx -= PLAYER_SPEED
                self.setGeometry(dx, self.y(), self.width(), self.height())
            elif Qt.Key_D == key and self.x() + PLAYER_SPEED < SCREEN_WIDTH - self.pixmap().width():
                dx += PLAYER_SPEED
                self.setGeometry(dx, self.y(), self.width(), self.height())
            elif Qt.Key_S == key and bullets_length < level:
                bullet = Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y, self.parent())
                bullet.active = True
                bullet.setGeometry(int(self.x() + self.width() / 2 - bullet.width() / 2),
                                   self.y() - self.height() + bullet.offset_y,
                                   bullet.pixmap().width(), bullet.pixmap().height())
                return bullet
            return None

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

    def reset_lives(self):
        self.life = 3
