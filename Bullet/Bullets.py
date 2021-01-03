from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QLabel
from Constants import *


class Bullet(QLabel):
    def __init__(self, offset_x, offset_y, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/bullet/bullet.png"))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.frames = 0
        self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.pixmap().width(), self.pixmap().height())
        self.setStyleSheet("border: 1px solid white;")
        self.show()

    def game_update(self, keys_pressed, player):
        if not self.active:
            if Qt.Key_Space in keys_pressed and BULLET_SPEED < SCREEN_HEIGHT - self.pixmap().height():
                self.active = True
                self.setGeometry(player.x() + player.width() / 2 - self.width() / 2,
                                 player.y() - player.height() + self.offset_y,
                                 self.pixmap().width(), self.pixmap().height())
                self.frames = BULLET_FRAMES
        else:
            self.setGeometry(self.x(), self.y() - BULLET_SPEED, self.pixmap().width(), self.pixmap().height())
            self.frames -= 1
            if self.frames <= 0:
                self.hit()

    def hit(self) -> None:
        self.active = False
        self.frames = BULLET_FRAMES
        self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.pixmap().width(), self.pixmap().height())
