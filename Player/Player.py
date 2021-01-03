from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from Constants import *


class Player(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/ship/ship_55x55.png"))
        self.setGeometry((SCREEN_WIDTH - self.pixmap().width()) / 2, SCREEN_HEIGHT - self.pixmap().height(),
                         self.pixmap().width(), self.pixmap().height())
        self.setStyleSheet("border: 1px solid white;")
        self.show()

    def game_update(self, keys_pressed):
        dx = self.x()
        if Qt.Key_Left in keys_pressed and self.x() - PLAYER_SPEED > 0:
            dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed and self.x() + PLAYER_SPEED < SCREEN_WIDTH - self.pixmap().width():
            dx += PLAYER_SPEED
        self.setGeometry(dx, self.y(), self.width(), self.height())
