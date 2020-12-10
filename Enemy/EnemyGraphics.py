from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QGraphicsPixmapItem


class EnemyGraphics(QGraphicsPixmapItem):

    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap("../images/alien_1/alien_1_cycle_1_11x11.png"))

    def imgShow(self, x: float, y: float):
        labelImg = QLabel(self)
        img = QPixmap("../images/alien_1/alien_1_cycle_1_11x11.png")
        labelImg.setPixmap(img)
        vbox = QVBoxLayout()
        vbox.addWidget(labelImg)
        self.setLayout(vbox)
        self.Show()

    #def moveEnemy(self, move_x: float, move_y: float):
        #self.x = self.x + move_x
        #self.y = self.y + move_y
