from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from Constants import *


class Score(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.score = 0
        self.setText("Score: " + str(self.score))
        self.setGeometry(SCREEN_WIDTH - 100, 5, 100, 20)
        self.setFont(QFont('Times', 12))
        self.setStyleSheet("color: orange")

    def increment_results(self):
        self.score += 1
        self.setText("Score: " + str(self.score))
        return self.score
