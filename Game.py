from PyQt5.QtCore import QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox

from random import choice
from Bullet.Bullets import Bullet
from Constants import *
from Enemy.Enemy import Enemy
from Enemy.move_enemy import MoveEnemy
from Life.Life import Life
from Player.Player import Player
from Player.move_player import MovePlayer
from Score.Score import Score
from Shield.Shield import Shield


class Game(QWidget):
    closeGame = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.keys_pressed = set()
        self.player_timer = QBasicTimer()
        self.move_enemy = MoveEnemy()
        self.move_player = MovePlayer()
        self.move_enemy.move_signal.connect(self.enemy_game_update)
        self.move_player.key_pressed_signal.connect(self.player_move_update)
        self.level = 0
        self.hard_quit = False
        self.__init__ui()

    def __init__ui(self):
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setStyleSheet("background-color: black;")

        self.player1 = Player(self, 1)
        self.player1_bullets = []

        self.player2 = Player(self, 2)
        self.player2_bullets = []

        self.shields = []

        self.enemies = []

        self.lives_player1 = []
        self.lives_player2 = []

        # ENEMY_BULLETS
        self.enemy_bullets = {}

        # ADD SCORE
        self.score = Score(self, 1)
        self.score2 = Score(self, 2)
        self.start_game()

    def start_game(self) -> None:
        for i in range(4):
            self.shields.append(Shield(i, self))
        for j in range(5):
            for i in range(11):
                self.enemies.append(Enemy(i, j, self))
        for i in range(3):
            self.lives_player1.append(Life(i, self, 1))
            self.lives_player2.append(Life(i, self, 2))

        self.level += 1

        self.player_timer.start(FRAME_TIME_PLAYER_MS, self)

        self.move_enemy.start()
        self.move_player.start()

    def keyPressEvent(self, event):
        if not self.move_player.is_done:
            self.move_player.add_key_pressed(event.key())

    def keyReleaseEvent(self, event):
        if not self.move_player.is_done:
            self.move_player.remove_key_pressed(event.key())

    def timerEvent(self, event):
        self.game_update()

    def game_update(self):
        if len(self.enemies) == 0:
            self.level_up()
            return
        if self.player1.life == 0:
            self.you_lost(1)
            return
        elif self.player2.life == 0:
            self.you_lost(2)
            return

        self.bullet_game_update(self.player1_bullets, self.score)
        self.bullet_game_update(self.player2_bullets, self.score2)

        keys_to_be_removed = []

        for key, value in self.enemy_bullets.items():
            enemy = self.enemies[key] if key < len(self.enemies) else None
            if value.enemy_game_update(enemy):
                keys_to_be_removed.append(key)

        for item in keys_to_be_removed:
            self.enemy_bullets.pop(item)

        self.enemy_bullet_game_update(self.player1, self.lives_player1)
        self.enemy_bullet_game_update(self.player2, self.lives_player2)

    def enemy_bullet_game_update(self, player, lives):
        for bullet in self.enemy_bullets.values():
            for shield in self.shields:
                shield.check_if_shield_is_hit(bullet)
                if shield.check_if_shield_is_destroyed():
                    self.shields.remove(shield)

            for life in lives:
                if player.check_if_player_is_hit(bullet):
                    if not lives == 0:
                        life.close()
                        lives.remove(life)
                    else:
                        life.close()
                        lives.remove(life)
                        player.close()

    def bullet_game_update(self, bullets, score):
        for bullet in bullets:
            if bullet.player_game_update():
                bullets.remove(bullet)
                break
            should_continue = False
            for enemy in self.enemies:
                if enemy.check_if_enemy_is_hit(bullet):
                    bullet.close()
                    bullets.remove(bullet)
                    score.print_results(enemy.type)
                    should_continue = True
                    self.enemies.remove(enemy)
            if should_continue:
                continue

            for shield in self.shields:
                if shield.check_if_shield_is_hit(bullet):
                    bullet.close()
                    bullets.remove(bullet)
                    should_continue = True

                if shield.check_if_shield_is_destroyed():
                    self.shields.remove(shield)
                if should_continue:
                    break

    def enemy_game_update(self):
        if not self.enemies:
            return
        elif len(self.enemies) == 1:
            if len(self.enemy_bullets) == 0:
                self.enemy_bullets[0] = Bullet(50, 50, self, True)
        elif len(self.enemy_bullets) - 1 < self.level:
            bullets_missing = self.level - len(self.enemy_bullets) - 1
            random_bullet_number_to_be_spawned = choice([*range(0, bullets_missing, 1)]) if bullets_missing > 1 else 1
            for i in range(random_bullet_number_to_be_spawned):
                num = -1
                if len(self.enemy_bullets) == 0:
                    num = choice([*range(0, len(self.enemies), 1)])
                elif len(self.enemies) == 1:
                    self.enemy_bullets[0] = Bullet(50, 50, self, True)
                else:
                    while num in self.enemy_bullets.keys() or num == -1:
                        num = choice([*range(0, len(self.enemies) + 1, 1)])
                self.enemy_bullets[num] = Bullet(50, 50, self, True)

        for enemy in self.enemies:
            enemy.game_update()

    def player_move_update(self, key):
        player1_bullet = self.player1.game_update(key, len(self.player1_bullets), self.level)
        player2_bullet = self.player2.game_update(key, len(self.player2_bullets), self.level)
        if player1_bullet:
            self.player1_bullets.append(player1_bullet)
        if player2_bullet:
            self.player2_bullets.append(player2_bullet)

    def level_up(self):
        self.clear_screen()
        self.move_enemy.die()
        self.player_timer.stop()
        self.move_player.die()
        self.move_enemy.increment_speed()
        self.start_game()

    def you_lost(self, player):
        self.clear_screen()
        self.move_enemy.die()
        self.move_player.die()
        self.player_timer.stop()

        close = QMessageBox()
        close.setWindowTitle("Game over")
        close.setText(
            "Player" + str(
                player) + " lost. The current score is Player1:{}, Player2:{}\nDo you want to play a new game?".format(
                self.score.score, self.score2.score))
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        close.setDefaultButton(QMessageBox.Yes)
        close = close.exec()

        if close == QMessageBox.No:
            self.hard_quit = True
            self.close_game()
            self.close()

        self.reset_game()
        self.start_game()

    def reset_game(self):
        self.level = 0
        self.player1.reset_lives()
        self.player2.reset_lives()
        self.move_enemy.reset_speed()
        self.score.reset_score()
        self.score2.reset_score()

    def clear_screen(self):
        for bullet in self.enemy_bullets.values():
            bullet.close()
        self.enemy_bullets.clear()
        for bullet in self.player1_bullets:
            bullet.close()
        self.player1_bullets.clear()
        for bullet in self.player2_bullets:
            bullet.close()
        self.player2_bullets.clear()

        for enemy in self.enemies:
            enemy.close()
        self.enemies.clear()
        for shield in self.shields:
            shield.close()
        self.shields.clear()
        for life in self.lives_player1:
            life.close()
        self.lives_player1.clear()
        for life in self.lives_player2:
            life.close()
        self.lives_player2.clear()

    def closeEvent(self, event):
        if self.hard_quit:
            self.close_game()
        else:
            close = QMessageBox()
            close.setWindowTitle("Are you sure you want to quit?")
            close.setText("Are you sure you want to quit")
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            close.setDefaultButton(QMessageBox.Yes)
            close = close.exec()

            if close == QMessageBox.Yes:
                self.close_game()
            else:
                event.ignore()

    def close_game(self):
        self.move_enemy.die()
        self.move_player.die()
        self.closeGame.emit()
