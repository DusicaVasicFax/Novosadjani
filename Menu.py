from PyQt5.QtGui import QFont, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLabel, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtCore import Qt, QBasicTimer
from Novosadjani.Enemy.Enemy import Enemy
from Novosadjani.Enemy.EnemyGenerator import EnemyGenerator
from Novosadjani.Enemy.EnemyGraphics import EnemyGraphics

import sys

from PyQt5.uic.properties import QtWidgets, QtCore, QtGui

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
FRAME_TIME_MS = 16


class Game(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1, -1, SCREEN_WIDTH + 2, SCREEN_HEIGHT + 2)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        for i in range(10):
            self.enemy = Enemy()
            self.enemy.setPos((SCREEN_WIDTH-self.enemy.pixmap().width())/5+i*90,
                              (SCREEN_HEIGHT-self.enemy.pixmap().height())/2)
            self.enemy.alien1()
            self.addItem(self.enemy)

        for j in range(2):
            for i in range(10):
                self.enemy = Enemy()
                self.enemy.setPos((SCREEN_WIDTH - self.enemy.pixmap().width()) / 5 + i * 90,
                                 (SCREEN_HEIGHT+200 - self.enemy.pixmap().height()) / 2+j*80)
                self.enemy.alien2()
                self.addItem(self.enemy)

        for j in range(2):
            for i in range(10):
                self.enemy = Enemy()
                self.enemy.setPos((SCREEN_WIDTH - self.enemy.pixmap().width()) / 5 + i * 90,
                                 (SCREEN_HEIGHT+500 - self.enemy.pixmap().height()) / 2+j*80)
                self.enemy.alien3()
                self.addItem(self.enemy)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setSceneRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


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
        self.new_game.setStyleSheet('QPushButton {background-color: #ffffff; color: black; border: none}')

        self.new_game.setGeometry(650, 360, 100, 50)

        self.new_game.clicked.connect(self.on_new_game_clicked)

    def on_new_game_clicked(self):
        # print("RADIIII")
        view = Game()
        self.hide()



def start():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())


start()
