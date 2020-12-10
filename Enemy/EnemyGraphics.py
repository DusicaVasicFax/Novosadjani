from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout


class EnemyGraphics:
    def __init__(self, x: float =0, y:float =0, img: str = ''):
        super().__init__()

        self.x = x
        self.y = y
        self.img = img

