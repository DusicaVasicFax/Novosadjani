from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QGraphicsPixmapItem


class Enemy(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

    def draw(self):
        self.setPixmap(QPixmap("../images/alien_1/alien_1_cycle_1_11x11.png"))

    def move(self, vel):
        self.y += vel


