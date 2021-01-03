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
        new_game = QPushButton("New game", self)
        new_game.setStyleSheet(
            'QPushButton''{''background-color : black; color: orange}')
        new_game.setFont(QFont('Times', 14))
        new_game.setGeometry(570, 250, 220, 100)
        new_game.clicked.connect(self.on_new_game_clicked)

    def on_new_game_clicked(self):
        self.hide()
        self.game = Game()
        self.game.closeGame.connect(self.show)
        self.game.show()


def start():
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


start()
