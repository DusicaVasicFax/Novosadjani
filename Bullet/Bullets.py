from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QLabel
from Constants import *


class Bullet(QLabel):
    def __init__(self, offset_x, offset_y, parent, enemy=False):
        QLabel.__init__(self, parent)
        if enemy:
            self.setPixmap(QPixmap("images/bullet/enemy_bullet.png"))
        else:
            self.setPixmap(QPixmap("images/bullet/bullet.png"))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.pixmap().width(), self.pixmap().height())
        # self.setStyleSheet("border: 1px solid white;")
        self.show()

    def player_game_update(self) -> bool:
        self.setGeometry(self.x(), self.y() - BULLET_SPEED, self.pixmap().width(), self.pixmap().height())
        if self.y() + self.pixmap().height() <= 0:
            self.active = False
            self.close()
            return True
        return False

    def enemy_game_update(self, enemy) -> bool:
        try:
            if not self.active:

                x = enemy.x() + enemy.width() / 2 - self.width() / 2
                y = enemy.y() + enemy.height()
                self.setGeometry(x, y, self.pixmap().width(), self.pixmap().height())
                self.active = True
            else:
                self.setGeometry(self.x(), self.y() + BULLET_SPEED, self.pixmap().width(), self.pixmap().height())

                if self.y() >= SCREEN_HEIGHT:
                    self.hit()
                    return True
                return False
        except AttributeError:
            return True

    def hit(self) -> None:
        self.active = False
        self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.pixmap().width(), self.pixmap().height())
