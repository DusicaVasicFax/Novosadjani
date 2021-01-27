from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox

from random import choice
from Bullet.Bullets import Bullet
from Constants import *
from Enemy.Enemy import Enemy
from Enemy.move_enemy import MoveEnemy
from GameUpdate import GameUpdateThread, BulletUpdateThread, EnemyBulletUpdateThread
from Level.Level import Level
from Life.Life import Life
from Player.Player import Player
from Player.move_player import MovePlayer
from Score.Score import Score
from Shield.Shield import Shield
from DeusExMachina.DeusExMachine import DeusExMachine, DeusThread


class Game(QWidget):
    closeGame = pyqtSignal()

    def __init__(self, players_count, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setWindowTitle("Space invaders")
        self.players_count = players_count
        self.keys_pressed = set()

        self.game_update_thread = GameUpdateThread()
        self.game_update_thread.game_update_signal.connect(self.game_update)

        self.bullet_game_update_thread = BulletUpdateThread()
        self.bullet_game_update_thread.bullet_update_signal.connect(self.bullet_game_update)

        self.enemy_bullet_game_update_thread = EnemyBulletUpdateThread()
        self.enemy_bullet_game_update_thread.enemy_bullet_update_signal.connect(self.enemy_bullet_game_update)

        self.deus_thread = DeusThread()
        self.deus_thread.deus_signal.connect(self.init_deus)

        self.move_enemy = MoveEnemy()
        self.move_enemy.move_signal.connect(self.enemy_game_update)

        self.move_player = MovePlayer()
        self.move_player.key_pressed_signal.connect(self.player_move_update)

        self.random_number = -1
        self.hard_quit = False
        self.__init__ui()
        self.start_threads()

    def __init__ui(self):
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setStyleSheet("background-color: black;")
        self.deus_machine = {}
        self.shields = []
        self.enemies = []
        self.lives = []
        self.players = []
        self.player_bullets = []
        self.enemy_bullets = {}
        self.scores = []
        self.level = Level(self)

        for i in range(self.players_count):
            self.players.append(Player(self, i + 1, self.players_count))
            self.scores.append(Score(self, i + 1))
            self.player_bullets.append([])
            self.lives.append([])

        self.start_game()

    def start_threads(self) -> None:
        self.move_enemy.start()
        self.move_player.start()
        self.game_update_thread.start()
        self.bullet_game_update_thread.start()
        self.enemy_bullet_game_update_thread.start()
        self.deus_thread.start()

    def start_game(self) -> None:
        for i in range(4):
            self.shields.append(Shield(i, self))
        for j in range(5):
            for i in range(11):
                self.enemies.append(Enemy(i, j, self))
        for i in range(self.players_count):
            for j in range(3):
                self.lives[i].append(Life(j, self, i + 1))
        self.level.print_level()

    def keyPressEvent(self, event):
        if not self.move_player.is_done:
            self.move_player.add_key_pressed(event.key())

    def keyReleaseEvent(self, event):
        self.move_player.remove_key_pressed(event.key())

    def game_update(self):
        if len(self.enemies) == 0:
            self.level_up()
            return

        for i in range(self.players_count):
            if self.players[i].life == 0:
                self.you_lost(i + 1)
                return

        keys_to_be_removed = []
        for key, value in self.enemy_bullets.items():
            enemy = self.enemies[key] if key < len(self.enemies) else None
            if value.enemy_game_update(enemy):
                keys_to_be_removed.append(key)

        for item in keys_to_be_removed:
            self.enemy_bullets.pop(item)

    def enemy_bullet_game_update(self):
        for i in range(self.players_count):
            for bullet in self.enemy_bullets.values():
                for shield in self.shields:
                    shield.check_if_shield_is_hit(bullet)
                    if shield.check_if_shield_is_destroyed():
                        self.shields.remove(shield)

                for life in self.lives[i]:
                    if self.players[i].check_if_player_is_hit(bullet):
                        if not self.lives[i] == 0:
                            life.close()
                            self.lives[i].remove(life)
                        else:
                            life.close()
                            self.lives[i].remove(life)
                            self.players[i].close()

    def bullet_game_update(self):
        for i in range(self.players_count):
            for bullet in self.player_bullets[i]:
                if bullet.player_game_update():
                    self.player_bullets[i].remove(bullet)
                    continue
                should_continue = False
                for enemy in self.enemies:
                    if enemy.check_if_enemy_is_hit(bullet):
                        bullet.close()
                        self.player_bullets[i].remove(bullet)
                        self.scores[i].print_results(enemy.type)
                        should_continue = True
                        self.enemies.remove(enemy)
                if should_continue:
                    continue

                for shield in self.shields:
                    if shield.check_if_shield_is_hit(bullet):
                        bullet.close()
                        self.player_bullets[i].remove(bullet)
                        should_continue = True

                    if shield.check_if_shield_is_destroyed():
                        self.shields.remove(shield)
                    if should_continue:
                        continue

    def enemy_game_update(self):
        if not self.enemies:
            return
        elif len(self.enemies) == 1:
            if len(self.enemy_bullets) == 0:
                self.enemy_bullets[0] = Bullet(50, 50, self, True)
        elif self.level.level - len(self.enemy_bullets) > 0:
            bullets_missing = self.level.level - len(self.enemy_bullets)
            random_bullet_number_to_be_spawned = choice([*range(0, bullets_missing, 1)]) if bullets_missing > 1 else 1
            for i in range(random_bullet_number_to_be_spawned):
                num = -1
                if len(self.enemy_bullets) == 0:
                    num = choice([*range(0, len(self.enemies), 1)])
                    self.enemy_bullets[num] = Bullet(50, 50, self, True)
                elif len(self.enemies) == 1:
                    self.enemy_bullets[0] = Bullet(50, 50, self, True)
                else:
                    tries = 5
                    while (num in self.enemy_bullets.keys() or num == -1) and tries > 0:
                        num = choice([*range(0, len(self.enemies), 1)])
                        tries -= 1
                    if tries > 0:
                        self.enemy_bullets[num] = Bullet(50, 50, self, True)

        for enemy in self.enemies:
            if not self.shields:
                if enemy.game_update(self.players[0].y() - self.players[0].height()):
                    self.you_lost()
            else:
                if enemy.game_update(self.players[0].y() - self.players[0].height(),
                                     self.shields[0].y() - self.shields[0].height()):
                    self.you_lost()

    def player_move_update(self, key):
        for i in range(self.players_count):
            bullet = self.players[i].game_update(key, len(self.player_bullets[i]), self.level.level)
            if bullet:
                self.player_bullets[i].append(bullet)

    def init_deus(self, x):
        if self.level.level not in self.deus_machine.keys():
            if self.random_number == -1:
                self.random_number = choice([*range(0, 99, 1)])
            else:
                self.random_number -= 1
            if self.random_number == 0:
                self.deus_thread.should_generate = True
            if x != -1:
                self.deus_machine[self.level.level] = DeusExMachine(x, self)
        delete_deus_keys = []
        for key, deus in self.deus_machine.items():
            if deus is not None:
                for i in range(self.players_count):
                    if deus.is_hit(self.players[i]):
                        delete_deus_keys.append(key)
                        if self.players[i].life == 3:
                            self.scores[i].print_deluxe()
                        else:
                            self.lives[i].insert(0, Life(abs(len(self.lives[i]) - 2), self, i + 1))
                            self.players[i].life += 1
                        break
        for key in delete_deus_keys:
            self.deus_machine[key].close()
            self.deus_machine[key] = None

    def level_up(self):
        self.clear_screen()
        self.level.level_up()
        self.move_enemy.increment_speed()
        self.enemy_bullet_game_update_thread.increment_speed()
        self.start_game()

    def you_lost(self, player=None):
        self.clear_screen()
        self.pause_threads()
        close = QMessageBox()
        close.setWindowTitle("Game over")

        if player is None:
            message = "The enemies have won, you can try again!"
        else:
            message = "Player " + str(player) + " lost. The current score is:\n"
            for i in range(self.players_count):
                message += "Player  {}: {}, ".format(i + 1, self.scores[i].score)

        message += "\nDo you want to play a new game?"
        close.setText(message)
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        close.setDefaultButton(QMessageBox.Yes)
        close = close.exec()

        if close == QMessageBox.No:
            self.hard_quit = True
            self.close_game()
            self.close()
        else:
            self.reset_game()
            self.unpause_threads()
            self.start_game()

    def pause_threads(self):
        self.game_update_thread.game_pause = True

    def unpause_threads(self):
        self.game_update_thread.game_pause = False

    def reset_game(self):
        self.level.reset_level()
        for i in range(self.players_count):
            self.players[i].reset_lives()
            self.scores[i].reset_score()
        self.move_enemy.reset_speed()
        self.enemy_bullet_game_update_thread.reset_speed()

    def clear_screen(self):
        for bullet in self.enemy_bullets.values():
            bullet.close()
        self.enemy_bullets.clear()
        for i in range(self.players_count):
            for bullet in self.player_bullets[i]:
                bullet.close()
            self.player_bullets[i].clear()
            for life in self.lives[i]:
                life.close()
            self.lives[i].clear()

        for enemy in self.enemies:
            enemy.close()
        self.enemies.clear()
        for shield in self.shields:
            shield.close()
        self.shields.clear()
        delete_deus_keys = []
        for key, deus in self.deus_machine.items():
            if deus is not None:
                delete_deus_keys.append(key)
        for key in delete_deus_keys:
            self.deus_machine[key].close()
            self.deus_machine[key] = None

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
        self.bullet_game_update_thread.die()
        self.enemy_bullet_game_update_thread.die()
        self.game_update_thread.die()
        self.deus_thread.die()
        self.closeGame.emit()
