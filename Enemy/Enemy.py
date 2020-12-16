from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QGraphicsPixmapItem
from PyQt5.QtCore import Qt
from Constants import *


class Enemy(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)

    def alien1(self):
        self.setPixmap(QPixmap("images/alien_1/alien_1_cycle_1_55x55.png"))

    def alien2(self):
        self.setPixmap(QPixmap("images/alien_2/alien_2_cycle_1_55x55.png"))

    def alien3(self):
        self.setPixmap(QPixmap("images/alien_3/alien_3_cycle_1_55x55.png"))

    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed:
            dx -= ENEMY_SPEED
        if Qt.Key_Right in keys_pressed:
            dx += ENEMY_SPEED
        if Qt.Key_Up in keys_pressed:
            dy -= ENEMY_SPEED
        if Qt.Key_Down in keys_pressed:
            dy += ENEMY_SPEED
        self.setPos(self.x() + dx, self.y() + dy)
