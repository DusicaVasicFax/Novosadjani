from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, \
    QLabel
from PyQt5.QtCore import Qt
import sys
from Game import Game


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Space invaders")
        self.setGeometry(0, 0, 1400, 900)
        self.setStyleSheet("background-image:url(images/background/space_bg.jpg);")
        self.ui_components()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ui_components(self):
        head = QLabel("Space invaders", self)
        head.setGeometry(550, 300, 300, 60)

        # font
        font = QFont('Times', 14)
        font.setBold(True)
        font.setUnderline(True)

        head.setFont(font)

        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)
        self.new_game = QPushButton("New game", self)
        self.new_game.setStyleSheet("background-color: #ffffff; color: black; border: none")
        self.new_game.setGeometry(650, 360, 100, 50)
        self.new_game.clicked.connect(self.on_new_game_clicked)

    def on_new_game_clicked(self):
        Game()
        self.hide()


def start():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())


start()
