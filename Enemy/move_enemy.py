from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import time


class MoveEnemy(QObject):
    move_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_done = False
        self.thread = QThread()
        self.speed = 0.50
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self) -> None:
        self.is_done = False
        self.thread.start()

    def die(self) -> None:
        self.is_done = True
        self.thread.quit()

    def increment_speed(self) -> None:
        if self.speed - 0.02 > 0:
            self.speed -= 0.02

    def reset_speed(self) -> None:
        self.speed = 0.50

    @pyqtSlot()
    def __work__(self) -> None:
        while not self.is_done:
            self.move_signal.emit()
            time.sleep(self.speed)
