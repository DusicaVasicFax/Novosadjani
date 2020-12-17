from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView

from Constants import *
from Player import Player
from Bullets import Bullet
from Enemy.Enemy import Enemy
from Shield.Shield import Shield


class Game(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent=parent)

        self.keys_pressed = set()
        self.player_timer = QBasicTimer()
        self.enemy_timer = QBasicTimer()
        self.player_timer.start(FRAME_TIME_PLAYER_MS, self)
        self.enemy_timer.start(FRAME_TIME_ENEMY_MS, self)

        # ADDING THE PLAYER (Current support is for only one player)
        self.player = Player()
        self.player.setPos((SCREEN_WIDTH - self.player.pixmap().width()) / 2,
                           SCREEN_HEIGHT - self.player.pixmap().height())

        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y),
                        Bullet(PLAYER_BULLET_X_OFFSETS[1], PLAYER_BULLET_Y)]

        for b in self.bullets:
            b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.addItem(b)

        self.addItem(self.player)
        self.enemies = []
        for j in range(5):
            for i in range(10):
                self.enemy = Enemy()
                if j == 0:
                    self.enemy.alien1()
                elif 0 < j <= 2:
                    self.enemy.alien2()
                else:
                    self.enemy.alien3()
                self.enemy.setPos((SCREEN_WIDTH - self.enemy.pixmap().width()) / 5 + i * 90,
                                  ((j + 1) * self.enemy.pixmap().height()) + 20 * j)
                self.addItem(self.enemy)
                self.enemies.append(self.enemy)

        self.shields = []
        for i in range(3):
            self.shield = Shield()
            if i == 0:
                self.shield.fullshield()
                self.shield.setPos((SCREEN_WIDTH - self.shield.pixmap().width()) / 5 - 70 + i * 90,
                                  (self.shield.pixmap().height()) + 20 + 500)
            elif i == 1:
                self.shield.fullshield()
                self.shield.setPos((SCREEN_WIDTH - self.shield.pixmap().width()) / 5 - 70 + i * 90+400,
                                   (self.shield.pixmap().height()) + 20 + 500)
            else:
                self.shield.fullshield()
                self.shield.setPos((SCREEN_WIDTH - self.shield.pixmap().width()) / 5 -70 + i * 90 + 800,
                                   (self.shield.pixmap().height()) + 20 + 500)
            self.addItem(self.shield)
            self.shields.append(self.shield)

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
        if event.timerId() == self.enemy_timer.timerId():
            self.enemy_game_update()
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)
        for b in self.bullets:
            b.game_update(self.keys_pressed, self.player)
        # call every enemy check if it's hit or not

    def enemy_game_update(self):
        for i in range(len(self.enemies)):
            self.enemies[i].game_update()
