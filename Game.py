from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem
from Player import Player
from Bullets import Bullet

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
PLAYER_BULLET_X_OFFSETS = [-15, 15]
PLAYER_BULLET_Y = 15
FRAME_TIME_MS = 16  # TODO change this later


class Game(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent=parent)

        self.keys_pressed = set()
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        # ADDING THE PLAYER (Current support is for only one player)
        self.player = Player()
        self.player.setPos((SCREEN_WIDTH - self.player.pixmap().width()) / 2,
                           (SCREEN_HEIGHT - self.player.pixmap().height()) / 2)

        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y),
                        Bullet(PLAYER_BULLET_X_OFFSETS[1], PLAYER_BULLET_Y)]

        for b in self.bullets:
            b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.addItem(b)

        self.addItem(self.player)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.view.setStyleSheet("background-color: black;")
        self.view.show()
        self.setSceneRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)
        for b in self.bullets:
            b.game_update(self.keys_pressed, self.player)
