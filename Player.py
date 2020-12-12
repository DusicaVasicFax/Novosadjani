from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QGraphicsPixmapItem

PLAYER_SPEED = 10
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900


class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("images/ship/ship_55x55.png"))

    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed and self.x() - PLAYER_SPEED > 0:
            dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed and self.x() + PLAYER_SPEED < SCREEN_WIDTH - self.pixmap().width():
            dx += PLAYER_SPEED
        if Qt.Key_Up in keys_pressed and self.y() - PLAYER_SPEED > 0:
            dy -= PLAYER_SPEED
        if Qt.Key_Down in keys_pressed and self.y() + PLAYER_SPEED < SCREEN_HEIGHT - self.pixmap().height():
            dy += PLAYER_SPEED
        self.setPos(self.x() + dx, self.y() + dy)
