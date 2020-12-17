from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from Constants import *

class Shield(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)

    def fullshield(self):
        self.setPixmap(QPixmap("images/shield/shield_132x132.png"))
