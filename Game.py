from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView

from Constants import *
from Player import Player
from Bullets import Bullet
from Enemy.Enemy import Enemy


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
        enemies = []
        for j in range(3):
            for i in range(10):
                self.enemy = Enemy()
                if j == 0:
                    self.enemy.alien1()
                elif j == 1:
                    self.enemy.alien2()
                else:
                    self.enemy.alien3()
                self.enemy.setPos((SCREEN_WIDTH - self.enemy.pixmap().width()) / 5 + i * 90,
                                  ((j + 1) * self.enemy.pixmap().height()) + 20 * j)
                self.addItem(self.enemy)
                enemies.append(self.enemy)

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
