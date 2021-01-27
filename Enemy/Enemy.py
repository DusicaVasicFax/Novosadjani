from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Bullet.Bullets import Bullet
from Constants import *


class Enemy(QLabel):
    def __init__(self, i, j, parent):
        QLabel.__init__(self, parent)

        if j == 0:
            self.setPixmap(QPixmap("images/aliens/alien_1_1.png"))
            self.type = 1
            self.image = 1
        elif 0 < j <= 2:
            self.setPixmap(QPixmap("images/aliens/alien_2_1.png"))
            self.type = 2
            self.image = 1
        else:
            self.setPixmap(QPixmap("images/aliens/alien_3_1.png"))
            self.type = 3
            self.image = 1
        self.setGeometry(self.calculate_start_position_x(i), self.calculate_start_position_y(j), self.pixmap().width(),
                         self.pixmap().height())
        # self.setStyleSheet("border: 1px solid white;")
        self.moves = 0
        self.direction = 1
        self.health = 1
        self.show()

    def calculate_start_position_x(self, i) -> int:
        return (SCREEN_WIDTH - self.width()) / 5 + i * 90

    def calculate_start_position_y(self, j) -> int:
        return ((j + 1) * self.height() + 20) + 30 * j

    def game_update(self, player_y, shield_y=-1) -> bool:
        ret_value = False
        self.change_image()
        if self.moves == 18:
            self.change_direction()
            self.inc_moves()

        if self.direction < 0:
            ret_value = self.move_down(player_y, shield_y)
            self.change_direction(True)

        if self.moves > 42:
            self.moves = 0

        if self.direction == 1:
            self.move_right()
        else:
            self.move_left()
        return ret_value

    def change_image(self) -> None:
        if self.type == 1:
            if self.image == 1:
                self.setPixmap(QPixmap("images/aliens/alien_1_2.png"))
                self.setGeometry(self.x(), self.y(), self.pixmap().width(), self.pixmap().height())
                self.image = 2
            else:
                self.setPixmap(QPixmap("images/aliens/alien_1_1.png"))
                self.setGeometry(self.x(), self.y(), self.pixmap().width(), self.pixmap().height())
                self.image = 1
        elif self.type == 2:
            if self.image == 1:
                self.setPixmap(QPixmap("images/aliens/alien_2_2.png"))
                self.setGeometry(self.x(), self.y(), self.pixmap().width(), self.pixmap().height())
                self.image = 2
            else:
                self.setPixmap(QPixmap("images/aliens/alien_2_1.png"))
                self.setGeometry(self.x(), self.y(), self.pixmap().width(), self.pixmap().height())
                self.image = 1
        else:
            if self.image == 1:
                self.setPixmap(QPixmap("images/aliens/alien_3_2.png"))
                self.setGeometry(self.x(), self.y(), self.pixmap().width(), self.pixmap().height())
                self.image = 2
            else:
                self.setPixmap(QPixmap("images/aliens/alien_3_1.png"))
                self.setGeometry(self.x(), self.y(), self.pixmap().width(), self.pixmap().height())
                self.image = 1

    def move_right(self) -> None:
        self.setGeometry(self.x() + PLAYER_SPEED, self.y(), self.width(), self.height())
        self.inc_moves()

    def move_left(self) -> None:
        self.setGeometry(self.x() - PLAYER_SPEED, self.y(), self.width(), self.height())
        self.inc_moves()

    def move_down(self, player_y, shield_y) -> bool:
        if self.type == 1:
            self.setGeometry(self.x(), self.y() + self.height(), self.width(), self.height())
        elif self.type == 2:
            self.setGeometry(self.x(), self.y() + self.height() + 10, self.width(), self.height())
        else:
            self.setGeometry(self.x(), self.y() + self.height() - 5, self.width(), self.height())

        if shield_y != -1:
            if shield_y < self.y():
                return True
        elif player_y < self.y():
            return True
        return False

    def change_direction(self, down=False) -> None:
        if down:
            self.direction = 2 if self.direction == -1 else 1
        else:
            self.direction *= -1

    def inc_moves(self) -> None:
        self.moves += 1

    def check_if_enemy_is_hit(self, bullet) -> bool:
        x = self.x()
        x1 = self.x() + self.width()
        x_coordinate_in_range = (x <= bullet.x() <= x1) or \
                                (x <= bullet.x() + bullet.width() <= x1)
        y = self.y()
        y1 = self.y() + self.height()
        y_coordinate_in_range = (y <= bullet.y() <= y1) or \
                                (y <= bullet.y() + bullet.height() <= y1)

        hit = x_coordinate_in_range and y_coordinate_in_range

        if hit:
            bullet.hit()
            self.health -= 1

        if self.health == 0:
            self.close()
            return True
        return False
