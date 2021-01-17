from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import time


class MoveEnemy(QObject):
    move_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_done = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self):
        self.is_done = False
        self.thread.start()

    def die(self):
        self.is_done = True
        self.thread.quit()

    @pyqtSlot()
    def __work__(self):
        while not self.is_done:
            self.move_signal.emit()
            time.sleep(0.50)
