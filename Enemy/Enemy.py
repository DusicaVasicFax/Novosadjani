from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from Constants import *


class Enemy(QGraphicsPixmapItem):
    def __init__(self, x, y, alien_type, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)

        if alien_type == '1':
            self.setPixmap(QPixmap("images/alien_1/alien_1_cycle_1_55x55.png"))
        elif alien_type == '2':
            self.setPixmap(QPixmap("images/alien_2/alien_2_cycle_1_55x55.png"))
        else:
            self.setPixmap(QPixmap("images/alien_3/alien_3_cycle_1_55x55.png"))
        self.setPos(self.calculate_start_position_x(x), self.calculate_start_position_y(y))
        self.moves = 0
        self.direction = 1
        self.health = 1

    def calculate_start_position_x(self, i) -> float:
        return (SCREEN_WIDTH - self.pixmap().width()) / 5 + i * 90

    def calculate_start_position_y(self, j) -> float:
        return ((j + 1) * self.pixmap().height()) + 20 * j

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
        self.setX(self.x() + PLAYER_SPEED)
        self.inc_moves()

    def move_left(self) -> None:
        self.setX(self.x() - PLAYER_SPEED)
        self.inc_moves()

    def move_down(self) -> None:
        self.setY(self.y() + self.pixmap().height())

    def change_direction(self, down=False) -> None:
        if down:
            self.direction = 2 if self.direction == -1 else 1
        else:
            self.direction *= -1

    def inc_moves(self) -> None:
        self.moves += 1

    def check_if_enemy_is_hit(self, bullet) -> bool:
        x_coordinate_in_range = (self.x() <= bullet.x() <= self.x() + self.pixmap().width() - 35) or \
                                (self.x() <= bullet.x() + 20 <= self.x() + self.pixmap().width() - 35)
        y_coordinate_in_range = (self.y() <= bullet.y() <= self.y() + self.pixmap().height() - 35) or \
                                (self.y() <= bullet.y() + bullet.pixmap().height() <=
                                 self.y() + self.pixmap().height() - 35)

        # TODO figure out the magic number for the bullet.y() since i guess bullet.pixmap().height is not accurate
        hit = x_coordinate_in_range and y_coordinate_in_range

        if hit:
            bullet.hit()
            self.health -= 1

        return self.health == 0


