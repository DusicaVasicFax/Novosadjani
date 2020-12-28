from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QPushButton

from Constants import *
from Player.Player import Player
from Bullet.Bullets import Bullet
from Enemy.Enemy import Enemy
from Shield.Shield import Shield
from Life.Life import Life


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
        self.addItem(self.player)
        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y),
                        Bullet(PLAYER_BULLET_X_OFFSETS[1], PLAYER_BULLET_Y)]
        self.addItem(self.bullets[0])
        self.addItem(self.bullets[1])

        self.enemies = []
        for j in range(5):
            for i in range(10):
                enemy = None
                if j == 0:
                    enemy = Enemy(i, j, '1')
                elif 0 < j <= 2:
                    enemy = Enemy(i, j, '2')
                else:
                    enemy = Enemy(i, j, '3')
                self.addItem(enemy)
                self.enemies.append(enemy)

        self.shields = []

        # ADD SHIELDS
        for i in range(3):
            shield = Shield(i)
            self.addItem(shield)
            self.shields.append(shield)

        # ADD LIFE
        for i in range(3):
            life = Life(i)
            self.addItem(life)

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
            shields = []

            for shield in self.shields:
                shield.check_if_shield_is_hit(b)
                if not shield.check_if_shield_is_destroyed():
                    shields.append(shield)
                else:
                    self.removeItem(shield)

                for enemy in self.enemies:
                    if (enemy.y() + enemy.pixmap().height()) > (shield.y()-10):
                        self.enemy_timer.stop()
            self.shields = shields

    def enemy_game_update(self):
        for b in self.bullets:
            enemies = []
            b.game_update(self.keys_pressed, self.player)
            for enemy in self.enemies:
                enemy.game_update()
                if not enemy.check_if_enemy_is_hit(b):
                    enemies.append(enemy)
                else:
                    self.removeItem(enemy)
            self.enemies = enemies
