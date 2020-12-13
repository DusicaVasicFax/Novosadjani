from PyQt5.QtCore import Qt, QBasicTimer

from PyQt5.QtGui import QPixmap, QBrush

from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QGraphicsRectItem, QGraphicsView, QApplication

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
BULLET_SPEED = 100  # pix/frame
BULLET_FRAMES = 20
FRAME_TIME_MS = 100  # ms/frame


class Bullet(QGraphicsPixmapItem):
    def __init__(self, offset_x, offset_y, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap("images/bullet/bullet_55x55.png"))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.frames = 0

    def game_update(self, keys_pressed, player):
        if not self.active:
            if Qt.Key_Space in keys_pressed and BULLET_SPEED < SCREEN_HEIGHT - self.pixmap().height() :
                self.active = True
                self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                self.frames = BULLET_FRAMES
        else:
            self.setPos(self.x(), self.y() - BULLET_SPEED)
            self.frames -= 1
            if self.frames <= 0:
                self.active = False
                self.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
