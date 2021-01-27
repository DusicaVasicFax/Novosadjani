from random import randrange

from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from time import sleep
from Constants import *
from multiprocessing import Queue, Process


class DeusExMachine(QLabel):
    def __init__(self, x, parent):
        QLabel.__init__(self, parent)
        self.setPixmap(QPixmap("images/heart/heart.png"))
        self.setGeometry(x, SCREEN_HEIGHT - self.pixmap().height() - 25, self.pixmap().width(), self.pixmap().height())
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
    deus_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.run)
        self.is_done = False
        self.should_generate = False
        self.queue = Queue()
        self.process = Process(target=generate_position, args=(self.queue,))

    def start(self) -> None:
        self.is_done = False
        self.should_generate = False
        if not self.process.is_alive():
            self.process.start()
        self.thread.start()

    def die(self) -> None:
        self.is_done = True
        self.thread.quit()
        if self.process.is_alive():
            self.process.terminate()

    @pyqtSlot()
    def run(self):
        while not self.is_done:
            if not self.queue.empty() and self.should_generate:
                self.should_generate = False
                self.deus_signal.emit(self.queue.get())
            else:
                self.deus_signal.emit(-1)
            sleep(0.05)


def generate_position(queue):
    while True:
        if queue.empty():
            queue.put(randrange(0, SCREEN_WIDTH - 55))
        sleep(2)
