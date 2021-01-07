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
        self.level = 1
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

        # ENEMY_BULLETS
        self.enemy_bullets = {}

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
            bullet.player_game_update(self.keys_pressed, self.player)
            for enemy in self.enemies:
                if enemy.check_if_enemy_is_hit(bullet):
                    self.enemies.remove(enemy)
                    self.score.print_results()

            for shield in self.shields:
                if shield.check_if_shield_is_destroyed(bullet):
                    self.shields.remove(shield)

        test_items = []
        for key in [key for (key, value) in self.enemy_bullets.items() if
                    value.enemy_game_update(self.enemies[key])]:
            try:
                # TODO check out this for some reason it is throwing index error
                del self.enemy_bullets[key]
            except IndexError:
                #Ovo smo mozda i resili sa ovim s obzirom da mi je stojao breakpoint na levelu 5 i nista se nije desilo
                test_items.append(key)
        for bullet in self.enemy_bullets.values():
            for shield in self.shields:
                if shield.check_if_shield_is_destroyed(bullet):
                    self.shields.remove(shield)

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

        # if not self.enemies:
        #     # TODO This is the next level logic
        #     print('GAME OVER, YOU WON')
        #     self.player_timer.stop()
        #     self.level += 1
        #     self.move_enemy.die()
        #     return

        if len(self.enemy_bullets) < self.level:
            random_bullet_number_to_be_spawned = choice([*range(0, self.level, 1)]) if self.level > 1 else 1
            for i in range(random_bullet_number_to_be_spawned):
                num = -1
                # Kada je 0 ne udje mi u while petlju uopste, samim tim mi ostaje num -1 a u pythonu ti to znaci 1 elemenat sa kraja niza znaci 50-ti enemy uvek puca pa mora sa ifom
                if not self.enemy_bullets.keys():
                    num = choice([*range(0, len(self.enemies), 1)])
                #Vrti se u while petlji da se ne bi desilo da jedan enemy puca dva puta (struktura nam ne dozvoljava po sebi(dictionary key))
                while num in self.enemy_bullets.keys():
                    num = choice([*range(0, len(self.enemies), 1)])
                self.enemy_bullets[num] = Bullet(50, 50, self, True)

        # Ovo sam ostavio tu
        # if not self.enemy_bullets:
        #     num = choice([*range(0, len(self.enemies), 1)])
        #     # self.enemies[num].bullet = Bullet(50, 50, self, True)
        #     self.enemy_bullets[num] = Bullet(50, 50, self, True)

        for enemy in self.enemies:
            enemy.game_update()
