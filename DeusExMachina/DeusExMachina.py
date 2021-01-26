from random import randrange

from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel
from time import sleep
from Constants import *
from multiprocessing import Process, Queue


class DeusExMachina(QLabel):
    def __init__(self, x, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/heart/heart.png"))
        self.setGeometry(x, SCREEN_HEIGHT - 65, self.pixmap().width(), self.pixmap().height())
        self.show()

    def is_hit(self, player) -> bool:
        x = self.x()
        x1 = self.x() + self.width()

        x_coordinate_in_range = (x <= player.x() <= x1) or \
                                (x <= player.x() + player.width() <= x1)

        y = self.y()
        y1 = self.y() + self.height()

        y_coordinate_in_range = (y <= player.y() <= y1) or \
                                (y <= player.y() + player.height() <= y1)

        hit = x_coordinate_in_range and y_coordinate_in_range

        if hit:
            return True
        return False


class DeusThread(QObject):
    move = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.position = 0
        self.show_self = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.run)
        self.is_done = False

    def start(self) -> None:
        self.is_done = False
        self.thread.start()

    def die(self) -> None:
        self.is_done = True
        self.thread.quit()

    @pyqtSlot()
    def run(self):
        while not self.is_done:
            if self.show_self:
                self.move.emit(self.position)
            q = Queue()
            # self.thread.p = Process(target=calc, args=[q])
            # self.thread.p.start()
            # self.position = q.get()
            print(str(self.position))
            self.show_self = True
            sleep(0.05)


def calc(q):
    value = randrange(0, 1300)
    q.put(value)
