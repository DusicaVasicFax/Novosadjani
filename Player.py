
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QGraphicsPixmapItem

PLAYER_SPEED = 3


class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("images/alien_1/alien_1_cycle_1_55x55.png"))

    # def game_update(self, keys_pressed):
    #     dx = 0
    #     dy = 0
    #     if Qt.Key_Left in keys_pressed:
    #         dx -= PLAYER_SPEED
    #     if Qt.Key_Right in keys_pressed:
    #         dx += PLAYER_SPEED
    #     if Qt.Key_Up in keys_pressed:
    #         dy -= PLAYER_SPEED
    #         print(self.y() - dy)
    #     if Qt.Key_Down in keys_pressed:
    #         dy += PLAYER_SPEED
    #     self.setPos(self.x()+dx, self.y()+dy)



