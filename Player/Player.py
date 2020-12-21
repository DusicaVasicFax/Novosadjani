from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from Constants import *


class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("images/ship/ship_55x55.png"))
        self.setPos((SCREEN_WIDTH - self.pixmap().width()) / 2, SCREEN_HEIGHT - self.pixmap().height())

    def game_update(self, keys_pressed):
        dx = 0
        if Qt.Key_Left in keys_pressed and self.x() - PLAYER_SPEED > 0:
            dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed and self.x() + PLAYER_SPEED < SCREEN_WIDTH - self.pixmap().width():
            dx += PLAYER_SPEED
        self.setX(self.x() + dx)
