from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QLabel
from Constants import *


class Enemy(QLabel):
    def __init__(self, i, j, parent):
        QLabel.__init__(self, parent)

        if j == 0:
            self.setPixmap(QPixmap("images/aliens/alien_1.png"))
        elif 0 < j <= 2:
            self.setPixmap(QPixmap("images/aliens/alien_2.png"))
        else:
            self.setPixmap(QPixmap("images/aliens/alien_3.png"))
        self.setGeometry(self.calculate_start_position_x(i), self.calculate_start_position_y(j), self.pixmap().width(),
                         self.pixmap().height())
        self.setStyleSheet("border: 1px solid white;")
        self.moves = 0
        self.direction = 1
        self.health = 1

    def calculate_start_position_x(self, i) -> float:
        return (SCREEN_WIDTH - self.width()) / 5 + i * 90

    def calculate_start_position_y(self, j) -> float:
        return ((j + 1) * self.height()) + 30 * j

    def game_update(self):
        if self.moves == 25:
            self.change_direction()
            self.inc_moves()

        if self.direction < 0:
            self.move_down()
            self.change_direction(True)

        if self.moves > 50:
            self.moves = 0

        if self.direction == 1:
            self.move_right()
        else:
            self.move_left()

    def move_right(self) -> None:
        self.setGeometry(self.x() + PLAYER_SPEED, self.y(), self.width(), self.height())
        self.inc_moves()

    def move_left(self) -> None:
        self.setGeometry(self.x() - PLAYER_SPEED, self.y(), self.width(), self.height())
        self.inc_moves()

    def move_down(self) -> None:
        self.setGeometry(self.x(), self.y() + self.height(), self.width(), self.height())

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

        return self.health == 0
