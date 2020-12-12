from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from Player import Player

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
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

        self.addItem(self.player)

        # Showing the view
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
