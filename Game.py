from PyQt5.QtCore import QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget

from Constants import *
from Enemy.move_enemy import MoveEnemy
from Life.Life import Life
from Player.Player import Player
from Bullet.Bullets import Bullet
from Enemy.Enemy import Enemy
from Score.Score import Score
from Shield.Shield import Shield


class Game(QWidget):
    closeGame = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.keys_pressed = set()
        self.player_timer = QBasicTimer()
        self.move_enemy = MoveEnemy()
        self.__init__ui()

    def __init__ui(self):
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setStyleSheet("background-color: black;")

        self.player = Player(self)

        #   TODO maybe bullets should spawn when you press space?
        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0], PLAYER_BULLET_Y, self)]

        self.shields = []
        for i in range(3):
            self.shields.append(Shield(i, self))

        self.enemies = []
        for j in range(5):
            for i in range(10):
                self.enemies.append(Enemy(i, j, self))

        self.lives = []
        for i in range(3):
            self.lives.append(Life(i, self))

        # ADD SCORE
        self.score = Score(self)
        self.start_game()

    def start_game(self) -> None:
        self.player_timer.start(FRAME_TIME_PLAYER_MS, self)
        self.move_enemy.move_signal.connect(self.enemy_game_update)
        self.move_enemy.start()

    def closeEvent(self, event):
        self.closeGame.emit()

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)
        for bullet in self.bullets:
            bullet.game_update(self.keys_pressed, self.player)
            for enemy in self.enemies:
                if enemy.check_if_enemy_is_hit(bullet):
                    self.enemies.remove(enemy)
                    self.score.print_results()

            for shield in self.shields:
                if shield.check_if_shield_is_destroyed(bullet):
                    self.shields.remove(shield)

    def enemy_game_update(self):
        for enemy in self.enemies:
            enemy.game_update()

