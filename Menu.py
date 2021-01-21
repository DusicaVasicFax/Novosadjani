from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, \
    QLabel
from PyQt5.QtCore import Qt
import sys
from Game import Game


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = None
        self.setWindowTitle("Space invaders")
        self.setGeometry(0, 0, 1400, 900)
        self.setStyleSheet("background-image:url(images/background/aaa.jpg);")
        self.ui_components()
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ui_components(self):
        head = QLabel("Space invaders", self)
        head.setGeometry(430, 10, 500, 60)
        head.setStyleSheet("color: gray")

        # font
        font = QFont('Times', 25)
        font.setBold(True)
        font.setUnderline(False)

        head.setFont(font)

        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)

        # setting button for 1 player
        player1_game = QPushButton("1 Player", self)
        player1_game.setStyleSheet(
            'QPushButton''{''background-color : black; color: orange}')
        player1_game.setFont(QFont('Times', 14))
        player1_game.setGeometry(570, 250, 220, 100)
        player1_game.clicked.connect(self.player1_game_clicked)

        # setting button for 2 players
        player2_game = QPushButton("2 Players", self)
        player2_game.setStyleSheet(
            'QPushButton''{''background-color : black; color: orange}')
        player2_game.setFont(QFont('Times', 14))
        player2_game.setGeometry(570, 400, 220, 100)
        player2_game.clicked.connect(self.player2_game_clicked)

        # setting button for exit
        exit_game = QPushButton("Exit", self)
        exit_game.setStyleSheet(
            'QPushButton''{''background-color : black; color: orange}')
        exit_game.setFont(QFont('Times', 14))
        exit_game.setGeometry(570, 550, 220, 100)
        exit_game.clicked.connect(self.close)

    def player1_game_clicked(self):
        self.hide()
        self.game = Game(1)
        self.game.closeGame.connect(self.show)
        self.game.show()

    def player2_game_clicked(self):
        self.hide()
        self.game = Game(2)
        self.game.closeGame.connect(self.show)
        self.game.show()


def start():
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


start()
