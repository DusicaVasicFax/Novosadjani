from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from Constants import *


class Score(QLabel):
    def __init__(self, parent, player):
        QLabel.__init__(self, parent)
        self.score = 0
        self.setText("Score " + str(player) + ": 0")
        if player == 1:
            self.setGeometry(20, SCREEN_HEIGHT - 25, 120, 20)
        elif player == 2:
            self.setGeometry(SCREEN_WIDTH - 120, SCREEN_HEIGHT - 25, 120, 20)

        self.player = player
        self.setFont(QFont('Times', 12))
        self.setStyleSheet("color: orange")

    def print_results(self, i):
        self.score += i
        self.setText("Score " + str(self.player) + ":" + str(self.score)+"  ")

    def print_deluxe(self):
        self.score += 15
        self.setText("Score " + str(self.player) + ":" + str(self.score)+"  ")

    def reset_score(self):
        self.score = 0
        self.print_results(0)
