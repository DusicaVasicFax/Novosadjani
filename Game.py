from PyQt5.QtCore import QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget

from random import seed
from random import choice
from Bullet.Bullets import Bullet
from Constants import *
from Enemy.Enemy import Enemy
from Enemy.move_enemy import MoveEnemy
from Life.Life import Life
from Player.Player import Player
from Score.Score import Score
from Shield.Shield import Shield


class Game(QWidget):
    closeGame = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.keys_pressed = set()
        self.player_timer = QBasicTimer()
        self.move_enemy = MoveEnemy()
        self.level = None
        self.__init__ui()

    def __init__ui(self):
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setStyleSheet("background-color: black;")

        self.player = Player(self)

        #   TODO maybe bullets should spawn when you press space?
        self.bullets = []

        self.shields = []
        for i in range(4):
            self.shields.append(Shield(i, self))

        self.enemies = []
        for j in range(5):
            for i in range(11):
                self.enemies.append(Enemy(i, j, self))

        self.lives = []
        for i in range(3):
            self.lives.append(Life(i, self))

        # ENEMY_BULLETS
        self.enemy_bullets = {}

        # ADD SCORE
        self.score = Score(self)
        self.start_game()

    def start_game(self) -> None:
        self.level = 5
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

        bullet = self.player.game_update(self.keys_pressed, len(self.bullets), self.level)
        if bullet:
            self.bullets.append(bullet)

        for bullet in self.bullets:
            if bullet.player_game_update():
                self.bullets.remove(bullet)
                break
            should_continue = False
            for enemy in self.enemies:
                if enemy.check_if_enemy_is_hit(bullet):
                    self.enemies.remove(enemy)
                    bullet.close()
                    self.bullets.remove(bullet)
                    self.score.print_results()
                    should_continue = True
            if should_continue:
                continue

            for shield in self.shields:
                if shield.check_if_shield_is_hit(bullet):
                    bullet.close()
                    self.bullets.remove(bullet)
                    should_continue = True

                if shield.check_if_shield_is_destroyed():
                    self.shields.remove(shield)
                if should_continue:
                    break

        keys_to_be_removed = []
        for key, value in self.enemy_bullets.items():
            enemy = self.enemies[key] if key < len(self.enemies) else None
            if value.enemy_game_update(enemy):
                keys_to_be_removed.append(key)

        for item in keys_to_be_removed:
            self.enemy_bullets.pop(item)

        for bullet in self.enemy_bullets.values():
            for shield in self.shields:
                shield.check_if_shield_is_hit(bullet)
                if shield.check_if_shield_is_destroyed():
                    self.shields.remove(shield)

            for life in self.lives:
                if self.player.check_if_player_is_hit(bullet):
                    if not self.player.life == 0:
                        life.close()
                        self.lives.remove(life)
                    else:
                        life.close()
                        self.lives.remove(life)
                        self.player.close()

    def move_enemy_update(self):
        for enemy in self.enemies:
            enemy.game_update()

    def enemy_game_update(self):
        # TODO leveling system:
        """ 1. Increment level when all enemies are cleared
            2. Dependent on a level choose a random number between zero and level number
            3. For range in random number choose another random number until

            randomNumber = choice([*range(0, currentLevel,1])
            for i in randomNumber:
                num = 0
                do:
                   num = choice([*range(0, len(self.enemies), 1)])
                while(num not in self.enemy_bullets)
                self.enemy_bullets[num] = Bullet(0, 0, self, True)
        """

        if not self.enemies:
            # TODO This is the next level logic
            print('GAME OVER, YOU WON')
            self.player_timer.stop()
            self.level += 1
            self.move_enemy.die()
            return

        if len(self.enemy_bullets) < self.level:
            random_bullet_number_to_be_spawned = choice([*range(0, self.level, 1)]) if self.level > 1 else 1
            for i in range(random_bullet_number_to_be_spawned):
                num = -1
                if len(self.enemy_bullets) == 0:
                    num = choice([*range(0, len(self.enemies), 1)])
                else:
                    while num in self.enemy_bullets.keys() or num == -1:
                        num = choice([*range(0, len(self.enemies), 1)])

                self.enemy_bullets[num] = Bullet(50, 50, self, True)

        self.move_enemy_update()

