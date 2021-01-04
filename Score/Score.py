from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from Constants import *


class Score(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.score = 0
        self.setText("Score: 0")
        self.setGeometry(SCREEN_WIDTH - 100, 5, 100, 20)
        self.setFont(QFont('Times', 12))
        self.setStyleSheet("color: orange")

    def print_results(self):
        self.score += 1
        text = ('''<p>{}</p>'''.format(self.score))
        return text
