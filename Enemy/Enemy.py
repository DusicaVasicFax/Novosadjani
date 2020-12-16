from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from Constants import *


class Enemy(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.moves = 0
        self.direction = 1

    def alien1(self):
        self.setPixmap(QPixmap("images/alien_1/alien_1_cycle_1_55x55.png"))

    def alien2(self):
        self.setPixmap(QPixmap("images/alien_2/alien_2_cycle_1_55x55.png"))

    def alien3(self):
        self.setPixmap(QPixmap("images/alien_3/alien_3_cycle_1_55x55.png"))

    def game_update(self):

        if self.moves == 25:
            self.direction *= -1
            self.moves += 1

        if self.direction < 0:
            self.setY(self.y() + self.pixmap().height())
            if self.direction == -1:
                self.direction = 2
            else:
                self.direction = 1
            return

        if self.moves > 50:
            self.moves = 0

        if self.direction == 1:
            self.setX(self.x() + PLAYER_SPEED)
            self.moves += 1
        else:
            self.setX(self.x() - PLAYER_SPEED)
            self.moves += 1
